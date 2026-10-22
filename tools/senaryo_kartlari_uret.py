# -*- coding: utf-8 -*-
"""Her ders × sınıf × sınav × senaryo için SENARYO KARTI üretir ve kontrol eder (2026-2027, 5-6-7).

Kart satırı (senaryodaki her çıktı): kod · ifade (kazanım dosyasından) · soru sayısı · tema · konu · planda işlendiği haftalar ·
sınavdan önce işlendi mi · kitap yeri (cilt, tema aralığı, konunun bulunduğu sayfa) · Türkçe'de çıktının işlendiği metinler.
Kontroller: kod kazanımda var · tema adı tutuyor · sınavdan önce işleniyor · kitapta yer bulundu.
  python tools/senaryo_kartlari_uret.py → skills/tymm-acik-uclu-sinav/references/senaryo-kartlari/<s>-sinif-<ders>.md + evals/SENARYO-KONTROL.md
"""
import json, re, datetime, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "skills" / "tymm-acik-uclu-sinav" / "references"
KAZ = ROOT / "skills" / "tymm-ders-planlama" / "references" / "kazanimlar"
SEN = json.loads(Path(r"C:\Users\cetin\Projects\MEB-KAYNAK\2026-2027\07-ortak-sinav\senaryolar.json").read_text(encoding="utf-8"))
PLAN = {x["slug"]: x for x in json.loads(Path(r"C:\Users\cetin\Projects\lms\apps\web\src\data\yillik-plan-2026-2027.json").read_text(encoding="utf-8"))["dersler"]}
DIZIN = json.loads((REF / "kitap-dizini.json").read_text(encoding="utf-8"))
KITAP = Path(r"C:\Users\cetin\Projects\lms\content-gen\kaynak\kitap")
OUT = REF / "senaryo-kartlari"; OUT.mkdir(exist_ok=True)
BIRINCI = {"fen-bilimleri": (2026, 11, 3), "matematik": (2026, 11, 5), "sosyal-bilgiler": (2026, 11, 6), "turkce": (2026, 11, 10),
           "ingilizce": (2026, 11, 12), "din-kulturu-ve-ahlak-bilgisi": (2026, 11, 13)}
DERSLER = list(BIRINCI)

def n(s):
    s = unicodedata.normalize("NFKD", str(s).replace("&", " and ").replace("İ", "i").replace("I", "i").replace("ı", "i").replace("’", "'").lower())
    return re.sub(r"[^a-z0-9]+", "", "".join(c for c in s if not unicodedata.combining(c)))
def kod_ayir(c):
    h = re.sub(r"^([A-Z]+) (\d)", r"\1.\2", c.strip())
    m = re.match(r"^(E\d\.\d+\.[A-Z]+\d+|[A-Z]+(?:\.[A-Z]+)?(?:\.\d+)+(?:\.[A-Z]+\d+)?)\.?\s*(.*)$", h)
    return (m[1], m[2]) if m else (None, c)
def sinav_tarihi(d, g, ad):
    if ad.startswith("1. Dönem 1"):
        return datetime.date(2026, 11, 11) if (d == "matematik" and g == 6) else datetime.date(*BIRINCI[d])
    if d == "turkce" and g == 7: return datetime.date(2027, 1, 5)   # ülke geneli, resmî (ÖDSGM takvimi 10.09.2026)
    return datetime.date(2027, 1, 18)   # 2. yazılı takvimi yayımlanmadı (23.10.2026): dönem sonu haftası varsayıldı (kapsam ≤ 17. hafta)
def kitap_sayfalari(d, g):
    S = {}
    for f in sorted(KITAP.glob(f"{d}-{g}-[12].md")):
        c = int(f.stem[-1]); t = f.read_text(encoding="utf-8")
        for m in re.finditer(r"^--- s\.(\d+) ---$\n(.*?)(?=^--- s\.|\Z)", t, re.M | re.S):
            S[(c, int(m[1]))] = [n(x) for x in m[2].split("\n") if x.strip()]
    return S

ozet = ["# Senaryo kontrol özeti (2026-2027)", "", f"Üretim: {datetime.date.today().isoformat()} · `tools/senaryo_kartlari_uret.py`", "",
        "| Sınıf | Ders | Sınav | Senaryo | Soru | Çıktı | ✓ sınavdan önce | ⚠ sınav haftası/sonrası | kitap yeri bulundu | Not |", "|---|---|---|---|---|---|---|---|---|---|"]
uyarilar = []
for g in (5, 6, 7):
    for d in DERSLER:
        s = next((x for x in SEN if x["ders"] == d and x["sinif"] == g), None)
        kz = (KAZ / f"{g}-sinif-{d}.md").read_text(encoding="utf-8")
        K = {}; tema_of = {}; cur = None
        for line in kz.split("\n"):
            m = re.match(r"^## (.+?) — (.+)$", line)
            if m: cur = m[2]; continue
            m = re.match(r"^-? ?\*\*([A-Z][\w.]*?\d)\.\*\* (.+?)(?: \*\(.*\)\*)?$", line)
            if m and cur: K.setdefault(m[1], m[2]); tema_of.setdefault(m[1], cur)
        p = PLAN.get(f"{g}-sinif-{d}")
        hafta_of = {}
        for h in p["haftalar"]:
            for k in h.get("kodlar") or []: hafta_of.setdefault(k, []).append((h["h"], datetime.date.fromisoformat(h["pzt"]), h.get("konu") or ""))
        dizin = DIZIN.get(f"{g}-{d}", []); sayfa = kitap_sayfalari(d, g)
        L = [f"# Senaryo kartları — {g}. sınıf {d} (2026-2027, 1. dönem)", "",
             "Kaynaklar: ÖDSGM konu-soru dağılım tablosu · kazanım dosyası (çıktı ifadesi) · MEB 2026-27 çerçeve yıllık planı (hafta) · "
             "2026-27 ders kitabı (sayfa = PDF sayfası). ✓ = çıktının planda ilk işlendiği hafta sınav haftasından önce. "
             "⚠ = sınav haftasında ya da sonra başlıyor. Kitap sayfası konu başlığına göre bulunur; bulunamazsa tema aralığı verilir.", ""]
        if not s:
            L.append("Senaryo tablosu yok."); (OUT / f"{g}-sinif-{d}.md").write_text("\n".join(L), encoding="utf-8"); continue
        for e in s.get("senaryosuz_sinavlar", []): L += [f"> **ÜLKE GENELİ:** {e}", ""]
        for sv in s["sinavlar"]:
            ad = sv["sinav"]; t = sinav_tarihi(d, g, ad)
            L += [f"## {ad} — {t.strftime('%d.%m.%Y')}{' (varsayım)' if not ad.startswith('1. Dönem 1') else ''}", ""]
            for no in sv["senaryolar"]:
                satirlar = [(r, r["sayilar"].get(f"{ad}|{no}")) for r in s["satirlar"] if r["sayilar"].get(f"{ad}|{no}")]
                L += [f"### Senaryo {no} — {sv['toplam'][str(no)] if str(no) in sv['toplam'] else sv['toplam'].get(no)} soru", "",
                      "| Çıktı | Soru | Tema · konu | Planda | Sınavdan önce | Kitap |", "|---|---|---|---|---|---|"]
                ok = sonra = kbul = 0; notlar = []
                for r, sayi in satirlar:
                    kod, _ = kod_ayir(r["cikti"])
                    ifade = K.get(kod)
                    if not ifade: notlar.append(f"{kod} kazanımda YOK"); uyarilar.append(f"{g} {d} {ad} S{no}: {kod} kazanımda yok")
                    tema = tema_of.get(kod, r.get("unite", ""))
                    hf = hafta_of.get(kod, [])
                    # E7 kodları ve planda kodu olmayan çıktılar için: tema adının plandaki ilk haftası
                    if not hf:
                        hf = [(h["h"], datetime.date.fromisoformat(h["pzt"]), h.get("konu") or "") for h in p["haftalar"] if n(tema) and n(tema) in n(h.get("unite") or "")][:1]
                    ilk = hf[0] if hf else None
                    once = bool(ilk) and ilk[1] + datetime.timedelta(days=4) < t
                    if once: ok += 1
                    else:
                        sonra += 1; uyarilar.append(f"{g} {d} {ad} S{no}: {kod} planda {('hafta ' + str(ilk[0]) + ' (' + ilk[1].isoformat() + ')') if ilk else 'bulunamadı'} — sınav {t.isoformat()}")
                    haftalar = sorted({x[0] for x in hf})
                    hafta_txt = (f"h{haftalar[0]}" + (f"-{haftalar[-1]}" if len(haftalar) > 1 else "")) if haftalar else "—"
                    # kitap yeri: tema aralığı + konu başlığının geçtiği ilk sayfa
                    tz = next((x for x in dizin if n(x["tema"]) and (n(x["tema"]) in n(tema) or n(tema) in n(x["tema"]))), None)
                    if tz is None and d == "turkce" and ilk:   # Türkçe: çıktının işlendiği ilk haftanın teması
                        hu = next((h.get("unite") for h in p["haftalar"] if h["h"] == ilk[0]), "")
                        tz = next((x for x in dizin if n(x["tema"]) in n(hu)), None)
                    konu = r.get("konu") or (ilk[2] if ilk else "")
                    kitap = "—"
                    if tz:
                        kitap = f"{tz['cilt']}. kitap s.{tz['bas']}-{tz['son']}"; kbul += 1
                        kk = n(re.sub(r"\(.*?\)", "", konu.split(" / ")[0]))[:40]
                        if len(kk) > 8:
                            hit = next((sp for (c, sp), ls in sorted(sayfa.items()) if c == tz["cilt"] and tz["bas"] + 1 < sp <= tz["son"] and any(l.startswith(kk) or l == kk for l in ls)), None)
                            if hit: kitap += f" (konu s.{hit})"
                    L.append(f"| **{kod}** {ifade or r['cikti'][:80]} | {sayi} | {tema} · {konu[:70]} | {hafta_txt} | {'✓' if once else '⚠'} | {kitap} |")
                if d == "ingilizce" and g in (5, 6):
                    L.append(f"\nSöz varlığı: `references/ingilizce-sozcuk/{g}-sinif.md` (ilgili tema) dışına çıkılmaz.")
                L.append("")
                ozet.append(f"| {g} | {d} | {ad.replace(' Ortak Yazılı Sınav', '')} | {no} | {sum(x[1] for x in satirlar)} | {len(satirlar)} | {ok} | {sonra} | {kbul}/{len(satirlar)} | {'; '.join(notlar)} |")
        (OUT / f"{g}-sinif-{d}.md").write_text("\n".join(L), encoding="utf-8")
ozet += ["", "## Uyarılar", ""] + [f"- {u}" for u in uyarilar]
(ROOT / "evals" / "SENARYO-KONTROL.md").write_text("\n".join(ozet), encoding="utf-8")
print(f"kartlar: {len(list(OUT.glob('*.md')))} dosya · uyarı: {len(uyarilar)}")
for u in uyarilar: print(" ⚠", u)
