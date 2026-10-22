# -*- coding: utf-8 -*-
"""TYMM ünite sayfaları (HTML, tymm.meb.gov.tr) -> references/kazanimlar/<sınıf>-sinif-<ders>.md

2026-2027 üretim hattı (Ekim 2026). Eski hat (pdf_metin_cikar.py + kazanim_uret.py) 2025-2026 PDF'leri içindir.
Ünite listesi: MEB-KAYNAK/2026-2027/01-program/_KAYNAK.md (tymm-program-indir.mjs üretir).
Sayfalar önbelleğe indirilir (C:/ttx/html/<ders>-<sınıf>-<id>.html); --taze ile yeniden çekilir.

  python tools/kazanim_html_uret.py [--siniflar 5,6,7] [--out C:/ttx/out] [--taze]
Çıktıyı inceledikten sonra İKİ becerinin kazanimlar/ klasörüne kopyalayın (--kur ile otomatik).
"""
import argparse, html, re, subprocess, datetime
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--kaynak", default=r"C:\Users\cetin\Projects\MEB-KAYNAK\2026-2027\01-program\_KAYNAK.md")
ap.add_argument("--siniflar", default="5,6,7")
ap.add_argument("--cache", default=r"C:\ttx\html")
ap.add_argument("--out", default=r"C:\ttx\out")
ap.add_argument("--taze", action="store_true")
ap.add_argument("--kur", action="store_true", help="çıktıyı tymm-ders-planlama ve tymm-baglam-testi kazanimlar/ klasörlerine yaz")
a = ap.parse_args()
CACHE, OUT = Path(a.cache), Path(a.out); CACHE.mkdir(parents=True, exist_ok=True); OUT.mkdir(parents=True, exist_ok=True)
ROOT = Path(__file__).resolve().parent.parent
SINIFLAR = [int(x) for x in a.siniflar.split(",")]

DERS = {  # ders slug -> (başlık, kod öneki regex, birim adı)
    "turkce": ("Türkçe", r"T\.[DOKY]", "Tema"),
    "matematik": ("Matematik", r"MAT", "Tema"),
    "fen-bilimleri": ("Fen Bilimleri", r"FB", "Ünite"),
    "sosyal-bilgiler": ("Sosyal Bilgiler", r"SB", "Öğrenme Alanı"),
    "din-kulturu-ve-ahlak-bilgisi": ("Din Kültürü ve Ahlak Bilgisi", r"DKAB", "Ünite"),
    "ingilizce": ("İngilizce", r"ENG", "Theme"),
}
TR_ALAN = ["Dinleme/İzleme", "Okuma", "Konuşma", "Yazma"]

def liste():
    out = []
    for m in re.finditer(r"^\| (\d) \| ([a-z-]+) \| \[(\d+)\]\((https://tymm[^)]+)\) \| ([^|]+) \| ([^|]+) \|", Path(a.kaynak).read_text(encoding="utf-8"), re.M):
        g, d, uid, url, baslik, dosya = int(m[1]), m[2], m[3], m[4], m[5].strip(), m[6].strip()
        n = re.search(r"-unite-(\d+)-", dosya); out.append(dict(g=g, d=d, id=uid, url=url, baslik=baslik, n=int(n[1]) if n else 0, dosya=dosya))
    return out

def sayfa(u):
    p = CACHE / f"{u['d']}-{u['g']}-{u['id']}.html"
    if a.taze or not p.exists() or p.stat().st_size < 5000:
        subprocess.run(["curl", "-sL", "-m", "60", "--retry", "2", "-o", str(p), u["url"]], check=True)
    return p.read_text(encoding="utf-8")

def tr_upper(s): return s.replace("i", "İ").replace("ı", "I").upper()

def satirlar(h):
    """içerik HTML'ini mantıksal satırlara böl; aynı satırda birleşik kalmış bileşenleri (… b) … c) …) ayır"""
    h = re.sub(r"<(br|/p|/li|/td|/tr|/div|/h\d|p|li|td|div)[^>]*>", "\n", h, flags=re.I)
    h = html.unescape(re.sub(r"<[^>]+>", "", h)).replace("\xa0", " ")
    out = []
    for s in h.split("\n"):
        s = re.sub(r"\s+", " ", s).strip()
        if not s: continue
        out += [p.strip() for p in re.split(r"(?<=[.!?”\"])\s+(?=[a-zçğ]\)\s|(?:FB|MAT|SB|DKAB|ENG|T\.[DOKY])\.\d+\.\d)", s) if p.strip()]
    return out

def alanlar(t):
    r = {}
    for m in re.finditer(r'class="col-md-3 bg-light p-2 title">\s*(.*?)\s*</div>\s*<div class="col-md-9 p-2 content">(.*?)</div>\s*</div>', t, re.S):
        r[re.sub(r"\s+", " ", m[1]).strip()] = m[2]
    return r

def tek(h):
    return " ".join(satirlar(h)).strip(" -")

def ciktilar(h, pre, g):
    """-> [(alan|None, kod, ifade, [bileşen...])]"""
    # kod ile metin arasında boşluk olmayabilir ("FB.7.1.1.Uzay…", "ENG.5.2.S4.Students…")
    kod_re = re.compile(rf"^({pre}\.{g}\.\d+\.[A-Z]+\d+|{pre}\.{g}(?:\.\d+)+)\.?\s*([^\d\s.].*)$")
    L = satirlar(h); out = []; alan = None; i = 0; cur = None
    while i < len(L):
        s = L[i]
        if s in TR_ALAN:
            alan = s; cur = None; i += 1; continue
        m = kod_re.match(s)
        if m:
            cur = [alan, m[1].rstrip("."), m[2].strip(), []]; out.append(cur); i += 1; continue
        b = re.match(r"^([a-zçğı])\)\s*(.*)$", s)
        if b and cur is not None:
            metin = b[2]
            if not metin and i + 1 < len(L): i += 1; metin = L[i]
            cur[3].append(f"{b[1]}) {metin}"); i += 1; continue
        if cur is not None:  # devam satırı: bileşen yoksa ifadeye, varsa son bileşene eklenir
            if cur[3]: cur[3][-1] += " " + s
            else: cur[2] += " " + s
        i += 1
    for c in out: c[2] = re.sub(r"\s+", " ", c[2]).strip()
    return out

def anahtar(h):
    L = satirlar(h)
    if "Anahtar Kavramlar" in L:
        j = L.index("Anahtar Kavramlar") + 1; parca = []
        while j < len(L) and L[j] not in ("Sembol ve Gösterimler", "Genellemeler"): parca.append(L[j]); j += 1
        return " ".join(parca)
    if "Genellemeler" in L: return ""  # Türkçe: genellemeler metni, kavram listesi yok
    return " ".join(L)

def kisa(s, n=600): return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + " …"

def birim_basligi(u, h1):
    ad = re.sub(r"^\s*(\d+\.\s*)?(Ünite|Tema|Öğrenme Alanı|Theme\s*\d+)\s*:?\s*", "", h1, flags=re.I).strip()
    return tr_upper(ad) if u["d"] != "ingilizce" else ad

bugun = datetime.date.today().isoformat()
uniteler = [u for u in liste() if u["g"] in SINIFLAR and u["d"] in DERS]
for g in SINIFLAR:
    for d, (dad, pre, birim) in DERS.items():
        us = sorted([u for u in uniteler if u["g"] == g and u["d"] == d], key=lambda u: (u["n"], u["dosya"]))
        if not us: continue
        bloklar, tablo, toplam_c, toplam_s = [], [], 0, 0
        for u in us:
            t = sayfa(u); F = alanlar(t)
            h1 = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S); h1 = html.unescape(re.sub(r"<[^>]+>|\s+", " ", h1[1])).strip() if h1 else u["baslik"]
            if d == "ingilizce": h1 = h1.replace("ı", "i").replace("İ", "I")
            ad = birim_basligi(u, h1)
            cs = ciktilar(F.get("Öğrenme Çıktıları ve Süreç Bileşenleri", ""), pre, g)
            saat = tek(F.get("Ders Saati", "")); toplam_c += len(cs)
            try: toplam_s += int(re.search(r"\d+", saat)[0])
            except Exception: pass
            if d == "matematik":
                ek = re.search(r"\((\d)\)", h1); etiket = f"MAT.{g}.{u['n']}" + (f" ({ek[1]})" if ek else "")
            elif d == "sosyal-bilgiler": etiket = f"{u['n']}. ÖĞRENME ALANI"
            elif d == "ingilizce": etiket = f"THEME {u['n']}"
            else: etiket = f"{tr_upper(birim)} {u['n']}"
            tablo.append(f"| {etiket} | {ad} | {len(cs)} | {saat} |")
            B = [f"## {etiket} — {ad}", "", f"**Kaynak sayfa:** {u['url']}  ", f"**Ders saati:** {saat}  "]
            for k, lab in [("Alan Becerileri", "Alan becerileri"), ("Kavramsal Beceriler", "Kavramsal beceriler"), ("Eğilimler", "Eğilimler"),
                           ("Sosyal-Duygusal Öğrenme Becerileri", "SDB"), ("Değerler", "Değerler"), ("Okuryazarlık Becerileri", "Okuryazarlık"),
                           ("Disiplinler Arası İlişkiler", "Disiplinler arası"), ("Beceriler Arası İlişkiler", "Beceriler arası ilişkiler")]:
                if k in F: B.append(f"**{lab}:** {kisa(tek(F[k]), 900)}  ")
            if "İçerik Çerçevesi" in F:
                ic = satirlar(F["İçerik Çerçevesi"])
                B.append(f"**İçerik çerçevesi:** {kisa(' · '.join(ic), 1500 if d == 'ingilizce' else 900)}  ")
            if "Anahtar Kavramlar" in F:
                ak = anahtar(F["Anahtar Kavramlar"])
                if ak: B.append(f"**Anahtar kavramlar:** {kisa(ak, 900)}  ")
            B.append("")
            son_alan = None
            for alan, kod, ifade, bil in cs:
                if alan and alan != son_alan: B += [f"### {alan}", ""]; son_alan = alan
                if d == "turkce" and not bil:
                    B.append(f"- **{kod}.** {ifade}")
                else:
                    B.append(f"**{kod}.** {ifade}")
                    B += [f"- {b}" for b in bil]; B.append("")
            if d == "turkce": B.append("")
            bloklar += B
        notlar = {
            "turkce": "> **SÜREÇ BİLEŞENİ NOTU:** Türkçe resmî tema sayfaları çıktıları süreç bileşeni dökümü olmadan listeler; ifadeler çıktı düzeyinde birebirdir. Türkçe sarmal yapıdadır: aynı çıktı birden çok temada yeniden işlenir.",
            "ingilizce": "> **NOT:** İngilizce çıktıları tema içeriğine (\"current content on …\") bağlı uzun ifadelerdir ve süreç bileşenleri İngilizcedir; birebir aktarılmıştır. Kod deseni `ENG.<sınıf>.<tema>.<beceri><no>` (L dinleme, R okuma, S konuşma, W yazma, G dil bilgisi, V söz varlığı, P sesletim).",
        }
        H = [f"# {g}. Sınıf {dad} — TYMM Öğrenme Çıktısı Verisi (2026-2027)", "",
             f"**Kaynak (doğrulanmış):** MEB Türkiye Yüzyılı Maarif Modeli resmî ünite/tema sayfaları (tymm.meb.gov.tr), {bugun} tarihinde sayfa HTML'inden "
             "otomatik aktarıldı (`tools/kazanim_html_uret.py`). Öğrenme çıktıları ve süreç bileşenleri (a, b, c, ç…) **birebir**; asla yeniden yazılmaz.", "",
             f"> **KOD DESENİ (2026-2027):** `{pre.replace(chr(92), '')}.{g}.…` — kodlar sayfadaki gibidir. 2025-2026 verisindeki eski kodlar (ör. Fen'de 4 parçalı) geçersizdir.",
             "> Ortak yazılı sınavlarda geçerli kapsam, ÖDSGM konu-soru dağılım tablosudur (`tymm-acik-uclu-sinav/references/senaryolar/`).", ""]
        if d in notlar: H += [notlar[d], ""]
        H += [f"Toplam {birim.lower()}: {len(us)} · Öğrenme çıktısı: {toplam_c} · Ders saati (toplam): {toplam_s}", "",
              f"## {birim} tablosu", "", f"| Kod/No | Ad | Çıktı | Saat |", "|---|---|---|---|"] + tablo + [""]
        dst = OUT / f"{g}-sinif-{d}.md"
        dst.write_text("\n".join(H + bloklar).rstrip() + "\n", encoding="utf-8")
        print(f"{dst.name:42} {len(us)} birim · {toplam_c} çıktı · {toplam_s} saat")
        if a.kur:
            for beceri in ("tymm-ders-planlama", "tymm-baglam-testi"):
                (ROOT / "skills" / beceri / "references" / "kazanimlar" / dst.name).write_text(dst.read_text(encoding="utf-8"), encoding="utf-8")
