# -*- coding: utf-8 -*-
"""
TYMM çıktı denetimi — Katman 1 (deterministik).

Bir üretim paketini (klasör) alır, TYMM/yönetmelik kurallarının
MAKİNEYLE denetlenebilen kısmını koşar ve kural kural rapor verir.
Muhakeme gerektiren kontroller (işlevsellik testi, çeldirici geçerliliği,
bilimsel doğruluk, bağlam katmanlılığı) Katman 2'dedir — bkz. evals/DENETIM.md.

Kullanım:
    python tools/denetim.py <paket-klasörü> [<paket-klasörü> ...]
    python tools/denetim.py            # argümansız: ornekler/*/ taranır

Çıkış kodu: en az bir HATA bulunduysa 1, aksi hâlde 0.
"""
import sys, re
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
KAZ = ROOT / "skills" / "tymm-ders-planlama" / "references" / "kazanimlar"

KOD_RE = r"(?:FB\.\d\.\d+\.\d+\.\d+|MAT\.\d\.\d+\.\d+|SB\.\d\.\d+\.\d+|T\.[DOKY]\.\d\.\d+)"
IBARE = "Alıştırma, tarama ve deneme amaçlıdır"
YZ_BILDIRIM = "Yapay zekâ desteğiyle hazırlanmıştır"
IC_AD_SIZINTI = ["tymm-baglam-testi", "tymm-ders-planlama", "tymm-acik-uclu-sinav",
                 "tymm-ders-farklilastirma", "SKILL.md", "kilavuz-ilkeleri",
                 "rubrik-", "kazanimlar/"]
ANAHTAR_IZI = ['class="dogru"', "Örnek tam yanıt", "alt toplam",
               "Yanılgı Eşlemesi", "Çeldirici →", "Puanlama önerisi"]


def metin(html):
    t = re.sub(r"<style.*?</style>", " ", html, flags=re.S)
    t = re.sub(r"<script.*?</script>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&[a-z]+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()


class Rapor:
    def __init__(self):
        self.k = []  # (sev, kural, dosya, mesaj)
    def hata(self, kural, dosya, mesaj): self.k.append(("HATA", kural, dosya, mesaj))
    def uyari(self, kural, dosya, mesaj): self.k.append(("UYARI", kural, dosya, mesaj))
    def ok(self, kural, dosya, mesaj): self.k.append(("OK", kural, dosya, mesaj))


# ---------------------------------------------------------------- checks

def c_dipnot(dosyalar, R):
    """G01 dipnot standardı: yz bildirimi var; iç araç adı sızmamış."""
    for ad, (ham, txt) in dosyalar.items():
        if YZ_BILDIRIM not in txt:
            R.hata("G01-dipnot", ad, "Yapay zekâ bildirimi eksik")
        sizan = [w for w in IC_AD_SIZINTI if w in ham]
        if sizan:
            R.hata("G02-icad", ad, f"İç araç/beceri adı sızmış: {', '.join(sizan)}")
    if all(YZ_BILDIRIM in t for _, t in dosyalar.values()):
        R.ok("G01-dipnot", "*", "Tüm belgelerde yz bildirimi var")


def c_kod_varligi(dosyalar, R):
    """G03 veri sadakati: her çıktı kodu kazanım dosyasında var mı; desen doğru mu."""
    brans = {"FB": "fen-bilimleri", "MAT": "matematik", "SB": "sosyal-bilgiler", "T": "turkce"}
    kodlar = set()
    for _, (_, txt) in dosyalar.items():
        kodlar |= set(re.findall(KOD_RE, txt))
    if not kodlar:
        R.uyari("G03-veri", "*", "Belgede çıktı kodu bulunamadı (dipnot eksik olabilir)")
        return
    onbellek = {}
    for kod in sorted(kodlar):
        p = kod.split(".")
        pre = p[0]
        sinif = p[2] if pre == "T" else p[1]
        dosya = f"{sinif}-sinif-{brans[pre]}.md"
        yol = KAZ / dosya
        if yol not in onbellek:
            onbellek[yol] = yol.read_text(encoding="utf-8") if yol.exists() else None
        icerik = onbellek[yol]
        if icerik is None:
            R.uyari("G03-veri", "*", f"{kod}: kazanım dosyası yok ({dosya}) — doğrulanamadı")
        elif kod not in icerik:
            R.hata("G03-veri", "*", f"{kod}: {dosya} içinde YOK — uydurma/yanlış kod olabilir")
    if all((KAZ / f"{(k.split('.')[2] if k.split('.')[0]=='T' else k.split('.')[1])}-sinif-{brans[k.split('.')[0]]}.md").exists()
           and k in (KAZ / f"{(k.split('.')[2] if k.split('.')[0]=='T' else k.split('.')[1])}-sinif-{brans[k.split('.')[0]]}.md").read_text(encoding='utf-8')
           for k in kodlar):
        R.ok("G03-veri", "*", f"{len(kodlar)} çıktı kodunun tümü kazanım dosyalarında doğrulandı")


def _secenekler(ham):
    return re.findall(r"<li>\s*([A-D])\)\s*(.*?)</li>", ham, flags=re.S)


def c_test_paketi(dosyalar, R):
    testler = {a: v for a, v in dosyalar.items() if re.match(r"test-duzey-\d", a)}
    anahtar = {a: v for a, v in dosyalar.items() if "test-anahtari" in a}
    if not testler:
        return
    for ad, (ham, txt) in sorted(testler.items()):
        soru = len(re.findall(r'<span class="no">\d+\.</span>', ham))
        sec = _secenekler(ham)
        if soru and len(sec) != soru * 4:
            R.hata("T-secenek", ad, f"{soru} soru ama {len(sec)} seçenek (beklenen {soru*4})")
        else:
            R.ok("T-secenek", ad, f"{soru} soru × 4 seçenek")
        # hepsi/hiçbiri yasağı
        yasak = [f"{h}){m.strip()[:20]}" for h, m in sec
                 if re.match(r"\s*(Hepsi|Hiçbiri|Yukarıdakiler|[A-D] ve [A-D])\b", m.strip())]
        if yasak:
            R.hata("T-hepsihicbiri", ad, f"Yasak seçenek türü: {', '.join(yasak)}")
        else:
            R.ok("T-hepsihicbiri", ad, "Hepsi/Hiçbiri türü seçenek yok")
        # olumsuz kök
        buyuk = len(re.findall(r"DEĞİLDİR", ham))
        if buyuk > 2:
            R.hata("T-olumsuz", ad, f"Olumsuz kök {buyuk} > 2")
        elif buyuk:
            R.ok("T-olumsuz", ad, f"Olumsuz kök {buyuk} (vurgulu), sınır içinde")
        # ibare
        if IBARE not in txt:
            R.hata("T-ibare", ad, "'Alıştırma/deneme amaçlıdır' ibaresi eksik")
        # cevap sızıntısı
        sizan = [w for w in ANAHTAR_IZI if w in ham]
        if sizan:
            R.hata("T-sizinti", ad, f"Öğrenci testinde anahtar izi: {', '.join(sizan)}")
    # anahtar ayrı mı
    if not anahtar:
        R.hata("T-anahtar", "*", "test-anahtari.html yok (anahtar ayrı dosyada olmalı)")
        return
    R.ok("T-anahtar", "*", "Anahtar ayrı dosyada")
    # seçenek dengesi (anahtardan)
    aad, (aham, _) = next(iter(anahtar.items()))
    diz = re.findall(r'<td class="dogru">([A-D])</td>', aham)
    if diz and len(diz) % 10 == 0:
        for i in range(0, len(diz), 10):
            blok = diz[i:i+10]
            say = {h: blok.count(h) for h in "ABCD"}
            kotu = [h for h, n in say.items() if n > 4 or n < 1]
            duzey = i // 10 + 1
            if kotu:
                R.hata("T-denge", aad, f"Düzey {duzey} seçenek dengesi bozuk: {say}")
            else:
                R.ok("T-denge", aad, f"Düzey {duzey} dengesi uygun: {say}")


def c_calisma_kagidi(dosyalar, R):
    kagitlar = {a: v for a, v in dosyalar.items() if re.match(r"calisma-kagidi", a)}
    kanit = {a: v for a, v in dosyalar.items() if "ogrenme-kanitlari" in a or "puanlama-anahtari" in a}
    for ad, (ham, txt) in sorted(kagitlar.items()):
        puan = [int(x) for x in re.findall(r'class="puan">(\d+)\s*puan', ham)]
        bolum = [int(x) for x in re.findall(r'class="bp">(\d+)\s*puan', ham)]
        if puan and sum(puan) != 100:
            R.hata("K-puan", ad, f"Soru puanları toplamı {sum(puan)} ≠ 100")
        elif puan:
            R.ok("K-puan", ad, f"Soru puanları toplamı 100 ({len(puan)} soru)")
        if bolum and sum(bolum) != 100:
            R.hata("K-bolum", ad, f"Bölüm puanları toplamı {sum(bolum)} ≠ 100")
        if "Adı Soyadı" not in ham:
            R.uyari("K-ogrenci", ad, "Öğrenci ad/soyad satırı bulunamadı")
        sizan = [w for w in ANAHTAR_IZI if w in ham]
        if sizan:
            R.hata("K-sizinti", ad, f"Öğrenci kağıdında anahtar izi: {', '.join(sizan)}")
    if kagitlar and not kanit:
        R.hata("K-anahtar", "*", "Çalışma kağıdı var ama öğrenme-kanıtları/anahtar dosyası yok")
    elif kagitlar:
        R.ok("K-anahtar", "*", "Cevap anahtarı ayrı dosyada")


def c_acik_uclu(dosyalar, R):
    sinav = {a: v for a, v in dosyalar.items() if a == "sinav.html"}
    if not sinav:
        return
    ad, (ham, txt) = next(iter(sinav.items()))
    # çoktan seçmeli YOK (yönetmelik)
    sec = _secenekler(ham)
    ardisik = re.search(r"A\).{0,200}?B\).{0,200}?C\).{0,200}?D\)", metin(ham))
    if sec or ardisik:
        R.hata("A-format", ad, "Ortak yazılı sınavda çoktan seçmeli seçenek deseni bulundu — YÖNETMELİK İHLALİ")
    else:
        R.ok("A-format", ad, "Çoktan seçmeli seçenek yok (açık uçlu)")
    puan = [int(x) for x in re.findall(r'class="puan">(\d+)\s*puan', ham)]
    if puan and sum(puan) != 100:
        R.hata("A-puan", ad, f"Soru puanları toplamı {sum(puan)} ≠ 100")
    elif puan:
        R.ok("A-puan", ad, "Soru puanları toplamı 100")
    if not any("puanlama-anahtari" in a for a in dosyalar):
        R.hata("A-anahtar", ad, "puanlama-anahtari.html yok")


def c_konu_anlatimi(dosyalar, R):
    ka = {a: v for a, v in dosyalar.items() if a == "konu-anlatimi.html"}
    if not ka:
        return
    ad, (ham, txt) = next(iter(ka.items()))
    dis = re.findall(r'<img\b|<iframe\b|<script[^>]+\bsrc=|<link[^>]+\bhref=|https?://', ham)
    dis = [d for d in dis if "tymm.meb.gov.tr" not in d]  # metinsel atıf serbest
    if dis:
        R.hata("KA-diskaynak", ad, f"Dış kaynak çağrısı bulundu ({len(dis)} adet) — belge internetsiz açılmalı")
    else:
        R.ok("KA-diskaynak", ad, "Dış kaynak çağrısı yok (kendine yeten)")
    svg = ham.count("<svg")
    baslik = ham.count("<title")
    if svg and baslik < svg:
        R.uyari("KA-svgtitle", ad, f"{svg} SVG var ama {baslik} <title> — erişilebilirlik başlığı eksik olabilir")
    elif svg:
        R.ok("KA-svgtitle", ad, f"{svg} SVG, hepsinde başlık var")
    if "localStorage" in ham or "sessionStorage" in ham:
        R.uyari("KA-storage", ad, "localStorage/sessionStorage kullanımı (kural: kullanılmaz)")


CHECKS = [c_dipnot, c_kod_varligi, c_test_paketi, c_calisma_kagidi, c_acik_uclu, c_konu_anlatimi]


def denetle(klasor):
    klasor = Path(klasor)
    dosyalar = {}
    for f in sorted(klasor.glob("*.html")):
        ham = f.read_text(encoding="utf-8")
        dosyalar[f.name] = (ham, metin(ham))
    if not dosyalar:
        print(f"  (html dosyası yok: {klasor})")
        return 0
    R = Rapor()
    for chk in CHECKS:
        chk(dosyalar, R)
    # rapor
    hata = [x for x in R.k if x[0] == "HATA"]
    uyari = [x for x in R.k if x[0] == "UYARI"]
    ok = [x for x in R.k if x[0] == "OK"]
    print(f"\n{'='*70}\nPAKET: {klasor}  ({len(dosyalar)} belge)\n{'='*70}")
    for sev, sembol in [("HATA", "✗"), ("UYARI", "⚠"), ("OK", "✓")]:
        grup = {"HATA": hata, "UYARI": uyari, "OK": ok}[sev]
        for _, kural, dosya, mesaj in grup:
            print(f"  {sembol} [{kural:16s}] {dosya:26s} {mesaj}")
    print(f"\n  ÖZET: {len(ok)} geçti · {len(uyari)} uyarı · {len(hata)} HATA")
    return 1 if hata else 0


def main(argv):
    hedefler = argv[1:]
    if not hedefler:
        hedefler = [str(p) for p in sorted((ROOT / "ornekler").glob("*/")) if p.is_dir()]
        if not hedefler:
            print("Kullanım: python tools/denetim.py <paket-klasörü> ...")
            return 2
    kod = 0
    for h in hedefler:
        kod |= denetle(h)
    print(f"\n{'='*70}\nTOPLAM SONUÇ: {'HATA VAR (1)' if kod else 'TEMİZ (0)'}\n{'='*70}")
    return kod


if __name__ == "__main__":
    sys.exit(main(sys.argv))
