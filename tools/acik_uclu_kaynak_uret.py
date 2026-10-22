"""tymm-acik-uclu-sinav için 2026-2027 kaynak verisini üretir (yeniden çalıştırılabilir).

Girdi:
  MEB-KAYNAK/2026-2027/07-ortak-sinav/<ders>/<sınıf>/*-ortak-sinav-senaryolari.md   (ÖDSGM senaryo tabloları)
  lms/content-gen/kaynak/program/<ders>-<sınıf>-sinif/*.md                          (TYMM ünite programları, sayfa işaretli metin)
  lms/content-gen/kaynak/kitap/<ders>-<sınıf>-<cilt|calisma>.md                     (MEB ders kitapları, sayfa işaretli metin)
Çıktı (skills/tymm-acik-uclu-sinav/references/):
  senaryolar/<sınıf>-sinif-<ders>.md
  program/<sınıf>-sinif-<ders>.md        (yalnız --program-siniflar; varsayılan 5)
  kitap/<sınıf>-sinif-<ders>-<cilt>.md   (yalnız --kitap-siniflar; varsayılan 5; boş sayfalar atılır, "--- s.N ---" işaretleri korunur)

  python tools/acik_uclu_kaynak_uret.py [--meb C:/.../MEB-KAYNAK/2026-2027] [--lms-kaynak C:/.../lms/content-gen/kaynak]
"""
import argparse, re, shutil
from pathlib import Path

DERSLER = ["turkce", "matematik", "fen-bilimleri", "sosyal-bilgiler", "din-kulturu-ve-ahlak-bilgisi", "ingilizce"]
ap = argparse.ArgumentParser()
ap.add_argument("--meb", default=r"C:\Users\cetin\Projects\MEB-KAYNAK\2026-2027")
ap.add_argument("--lms-kaynak", default=r"C:\Users\cetin\Projects\lms\content-gen\kaynak")
ap.add_argument("--senaryo-siniflar", default="5,6,7")
ap.add_argument("--program-siniflar", default="5")
ap.add_argument("--kitap-siniflar", default="5")
a = ap.parse_args()
MEB, LMS = Path(a.meb), Path(a.lms_kaynak)
OUT = Path(__file__).resolve().parent.parent / "skills" / "tymm-acik-uclu-sinav" / "references"
siniflar = lambda s: [int(x) for x in s.split(",") if x]

# 1) senaryolar
for g in siniflar(a.senaryo_siniflar):
    for d in DERSLER:
        src = MEB / "07-ortak-sinav" / d / str(g) / f"{d}-{g}-ortak-sinav-senaryolari.md"
        if not src.exists():
            print(f"senaryo yok: {d} {g}"); continue
        dst = OUT / "senaryolar" / f"{g}-sinif-{d}.md"; dst.parent.mkdir(parents=True, exist_ok=True)
        t = src.read_text(encoding="utf-8").replace("(ham dosya: `../../_ham/", "(ÖDSGM dosyası: `")
        dst.write_text(t, encoding="utf-8"); print("senaryo", dst.name)

# 2) program (ünite dosyalarını tek dosyada birleştir; sayfa işaretlerini ve yazdırma artıklarını at)
ARTIK = [r"^--- s\.\d+ ---$", r"^# .*\.pdf$", r"^Kaynak: ", r"^Sayfa: \d+$", r"^\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}$",
         r"Türkiye Yüzyılı Maarif Modeli$", r"^https://tymm\.meb\.gov\.tr", r"^\d+/\d+$"]
def unite_no(p):
    m = re.search(r"-unite-(\d+)-", p.name); return int(m.group(1)) if m else 99
for g in siniflar(a.program_siniflar):
    for d in DERSLER:
        klasor = LMS / "program" / f"{d}-{g}-sinif"
        if not klasor.exists():
            print(f"program yok: {d} {g}"); continue
        L = [f"# {g}. sınıf {d} — TYMM öğretim programı (2026-2027)", ""]
        if d == "din-kulturu-ve-ahlak-bilgisi":
            L += [f"> **UYARI:** Bu dosya TYMM sitesindeki DKAB sayfalarından alındı; bazı çıktı ifadeleri ve süreç bileşenleri 2026-2027 ders kitabı, "
                  f"DÖGM yıllık planı ve ÖDSGM senaryo tablosuyla ÇELİŞİR. Çıktı ifadesi ve bileşenler için "
                  f"`../../tymm-ders-planlama/references/kazanimlar/{g}-sinif-{d}.md` esastır; bu dosya yalnız içerik çerçevesi, kapsam sınırları "
                  f"ve öğrenme-öğretme uygulamaları için okunur.", ""]
        L += [
             "Kaynak: tymm.meb.gov.tr ünite sayfaları (18.10.2026 yazdırması). Öğrenme çıktısı + süreç bileşenleri + içerik çerçevesi + "
             "anahtar kavramlar + öğrenme kanıtları + öğrenme-öğretme uygulamaları (kapsam sınırları) BİREBİR; yeniden yazılmaz.", ""]
        for f in sorted(klasor.glob("*.md"), key=unite_no):
            satir = [s for s in f.read_text(encoding="utf-8").split("\n") if not any(re.search(r, s.strip()) for r in ARTIK)]
            metin = re.sub(r"\n{3,}", "\n\n", "\n".join(satir)).strip()
            L += [f"## Ünite/Tema {unite_no(f)} — {f.stem}", "", metin, ""]
        dst = OUT / "program" / f"{g}-sinif-{d}.md"; dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text("\n".join(L), encoding="utf-8"); print("program", dst.name, f"{dst.stat().st_size // 1024} KB")

# 4) yıllık plan (hafta → tema/konu/kod) — sınav tarihine kadar işlenen kapsam için
import json, datetime
PLAN = LMS.parent.parent / "apps" / "web" / "src" / "data" / "yillik-plan-2026-2027.json"
# 1. yazılı tarihleri: ÖDSGM "Okul Geneli Ortak Yazılı Sınav Uygulama Takvimi" (20.10.2026) — derse göre farklı.
# 2. yazılı takvimi henüz yayımlanmadı (22.10.2026): 5 Ocak 2027 yer tutucudur (7. sınıf Türkçe ülke geneli tarihi).
BIRINCI = {"turkce": (2026, 11, 10), "matematik": (2026, 11, 5), "fen-bilimleri": (2026, 11, 3), "sosyal-bilgiler": (2026, 11, 6),
           "din-kulturu-ve-ahlak-bilgisi": (2026, 11, 13), "ingilizce": (2026, 11, 12)}
def sinavlar(d, g):
    t1 = datetime.date(*BIRINCI[d]); ek = ""
    if d == "matematik" and g == 6: t1, ek = datetime.date(2026, 11, 11), " — ÜLKE GENELİ"
    return [(f"1. dönem 1. ortak yazılı ({t1.strftime('%d.%m.%Y')}{ek})", t1),
            ("1. dönem 2. ortak yazılı (tarih henüz yayımlanmadı; ~5 Ocak 2027 varsayıldı)", datetime.date(2027, 1, 5))]
if PLAN.exists():
    veri = json.loads(PLAN.read_text(encoding="utf-8"))["dersler"]
    for g in siniflar(a.program_siniflar):
        L = [f"# {g}. sınıf yıllık plan — hafta hafta işleniş (MEB 2026-2027 çerçeve planı)", "",
             "Kaynak: MEB taslak çerçeve yıllık planları (TEGM 03.09.2026, DÖGM 31.08.2026). 1. hafta = 14 Eylül 2026. "
             "Sınav satırları (▶) sınav haftasını gösterir; sınav o haftaya kadar **işlenmiş** konuları kapsar. "
             "Okulun zümre planı farklıysa öğretmenin söylediği geçerlidir.", ""]
        for d in DERSLER:
            k = next((x for x in veri if x["slug"] == f"{g}-sinif-{d}"), None)
            if not k: continue
            L += [f"## {d}", "", "| Hafta | Pazartesi | Ünite/Tema | Konu | Kod |", "|---|---|---|---|---|"]
            kalan = sinavlar(d, g)
            for h in k["haftalar"]:
                pzt = datetime.date.fromisoformat(h["pzt"])
                # sınav, içine düştüğü haftanın satırından ÖNCE yazılır: o hafta (ve sonrası) sınava girmez
                while kalan and pzt + datetime.timedelta(days=4) >= kalan[0][1]:
                    L.append(f"| ▶ | {kalan[0][1].isoformat()} | **{kalan[0][0]}** | | |"); kalan.pop(0)
                L.append(f"| {h['h']} | {h['pzt']} | {h.get('unite','')} | {h.get('konu','')} | {', '.join(h.get('kodlar') or [])} |")
            L.append("")
        dst = OUT / f"plan-{g}-sinif.md"
        dst.write_text("\n".join(L), encoding="utf-8"); print("plan", dst.name, f"{dst.stat().st_size // 1024} KB")
else:
    print("yıllık plan verisi yok:", PLAN)

# 5) resmî örnek sorular (MEB-KAYNAK/2026-2027/08-ornek-sorular): 5. sınıf 2024-25 TYMM kitapçıkları + 6. sınıf ülke geneli kitapçıkları
ORN = MEB / "08-ornek-sorular"
if ORN.exists():
    for f in sorted(ORN.glob("*/*/*.md")):
        d, g = f.parent.parent.name, f.parent.name
        if g == "5" or (g == "6" and "ulke-geneli" in f.name and "mazeret" not in f.name):
            dst = OUT / "ornek-sorular" / f"{g}-{d}-{f.name}"; dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(f"<!-- Kaynak: MEB-KAYNAK/2026-2027/08-ornek-sorular/{d}/{g}/{f.name} (resmî ÖDSGM yayını; PyMuPDF ham metni, şekil/tablo düzeni bozuk olabilir) -->\n\n"
                           + f.read_text(encoding="utf-8"), encoding="utf-8")
            print("örnek", dst.name)

# 3) kitaplar
for g in siniflar(a.kitap_siniflar):
    for d in DERSLER:
        for f in sorted((LMS / "kitap").glob(f"{d}-{g}-*.md")):
            cilt = f.stem.rsplit("-", 1)[1]
            t = f.read_text(encoding="utf-8")
            parca = re.split(r"^(--- s\.\d+ ---)$", t, flags=re.M)
            bas = parca[0].strip().split("\n")
            L = [f"# {g}. sınıf {d} ders kitabı — {'çalışma kitabı' if cilt == 'calisma' else cilt + '. kitap'} (MEB, 2026-2027)", "",
                 f"Kaynak PDF: {next((s for s in bas if s.startswith('Kaynak:')), '?').replace('Kaynak: ', '')}",
                 "Sayfa işareti `--- s.N ---` = PDF sayfa numarası (kitabın basılı numarası değil). Boş sayfalar atıldı.", ""]
            for i in range(1, len(parca), 2):
                govde = parca[i + 1].strip()
                if len(govde) < 20: continue
                L += [parca[i], "", govde, ""]
            dst = OUT / "kitap" / f"{g}-sinif-{d}-{cilt}.md"; dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text("\n".join(L), encoding="utf-8"); print("kitap", dst.name, f"{dst.stat().st_size // 1024} KB")
