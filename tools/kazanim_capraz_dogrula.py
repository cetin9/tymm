# -*- coding: utf-8 -*-
"""Kazanım dosyalarını resmî kaynaklarla çapraz doğrular (2026-2027).

  A) ÖDSGM senaryo tabloları  → her kod kazanım dosyasında var mı, ifade aynı mı, ünite/tema adı tutuyor mu
  B) MEB yıllık plan (lms/apps/web/src/data/yillik-plan-2026-2027.json) → plan kodları kazanımda var mı; tema adları
  C) Bileşensiz çıktı (Türkçe hariç) ve yinelenen kod
  D) Ders kitabı (lms/content-gen/kaynak/kitap) → her tema/ünite adı kitapta geçiyor mu

  python tools/kazanim_capraz_dogrula.py [--kaz C:/ttx/out] [--siniflar 5,6,7]
Çıkış kodu: HATA varsa 1.
"""
import argparse, json, re, sys
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

ap = argparse.ArgumentParser()
ap.add_argument("--kaz", default=r"C:\ttx\out")
ap.add_argument("--senaryo", default=r"C:\Users\cetin\Projects\MEB-KAYNAK\2026-2027\07-ortak-sinav\senaryolar.json")
ap.add_argument("--plan", default=r"C:\Users\cetin\Projects\lms\apps\web\src\data\yillik-plan-2026-2027.json")
ap.add_argument("--kitap", default=r"C:\Users\cetin\Projects\lms\content-gen\kaynak\kitap")
ap.add_argument("--siniflar", default="5,6,7")
a = ap.parse_args()
SIN = [int(x) for x in a.siniflar.split(",")]
DERSLER = ["turkce", "matematik", "fen-bilimleri", "sosyal-bilgiler", "din-kulturu-ve-ahlak-bilgisi", "ingilizce"]
import unicodedata, html as _html
TR = str.maketrans({"İ": "i", "I": "i", "ı": "i", "Â": "a", "â": "a", "Î": "i", "î": "i", "Û": "u", "û": "u", "’": "'", "‘": "'"})
def n(s):
    s = unicodedata.normalize("NFKD", _html.unescape(s).replace("&", " and ").translate(TR))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9' ]+", " ", s).split()
def nj(s): return " ".join(n(s))
# Öğretmen onaylı bilinen farklar (23.10.2026): senaryo ifadesi kazanımdan farklı ama kazanım (program) ifadesi esas
ONAYLI = {"T.Y.5.2": "tam program + TYMM sitesi 'teknik seçimlerini' der; senaryo varyantı"}
hata = uyari = 0
def H(m):
    global hata; hata += 1; print("  ✗", m)
def U(m):
    global uyari; uyari += 1; print("  ⚠", m)

def kaz_oku(g, d):
    p = Path(a.kaz) / f"{g}-sinif-{d}.md"
    if not p.exists(): return None
    t = p.read_text(encoding="utf-8"); kod = {}; birim = {}; cur_b = None; sayac = {}
    for line in t.split("\n"):
        m = re.match(r"^## (.+?) — (.+)$", line)
        if m: cur_b = m[2].strip(); birim[cur_b] = []; continue
        m = re.match(r"^-? ?\*\*([A-Z][\w.]*?)\.\*\* (.+)$", line)
        if m and cur_b:
            k = m[1]; sayac[k] = sayac.get(k, 0) + 1
            kod.setdefault(k, {"ifade": m[2].strip(), "birimler": [], "bilesen": 0})
            kod[k]["birimler"].append(cur_b); birim[cur_b].append(k); son = k; continue
        if re.match(r"^- [a-zçğ]\) ", line) and cur_b and kod:
            kod[son]["bilesen"] += 1
    return dict(kod=kod, birim=birim, sayac=sayac)

sen = json.loads(Path(a.senaryo).read_text(encoding="utf-8"))
plan = {x["slug"]: x for x in json.loads(Path(a.plan).read_text(encoding="utf-8"))["dersler"]} if Path(a.plan).exists() else {}
for g in SIN:
    for d in DERSLER:
        K = kaz_oku(g, d)
        print(f"\n== {g}. sınıf {d}")
        if not K: H("kazanım dosyası yok"); continue
        # C) iç tutarlılık
        for k, v in K["kod"].items():
            if d not in ("turkce",) and v["bilesen"] == 0 and not k.startswith("E7."): U(f"{k}: süreç bileşeni yok")
            if d != "turkce" and K["sayac"][k] > 1: U(f"{k}: {K['sayac'][k]} kez geçiyor")
        # A) senaryo
        s = next((x for x in sen if x["ders"] == d and x["sinif"] == g), None)
        if s:
            ok = 0
            for r in s["satirlar"]:
                ham = re.sub(r"^([A-Z]+) (\d)", r"\1.\2", r["cikti"].strip())      # "SB 7.1.1." -> "SB.7.1.1."
                m = re.match(r"^(E\d\.\d+\.[A-Z]+\d+|[A-Z]+(?:\.[A-Z]+)?(?:\.\d+)+(?:\.[A-Z]+\d+)?)\.?\s*([^\d\s.].*)$", ham)  # boşluksuz "SB.5.2.3.Yaşadığı" da
                if not m: U(f"senaryo satırı çözümlenemedi: {r['cikti'][:60]}"); continue
                k, ifade = m[1], m[2]
                if k not in K["kod"]: H(f"SENARYO kodu kazanımda YOK: {k} — {ifade[:70]}"); continue
                # TAM cümle karşılaştırılır (önek karşılaştırması cümle sonundaki fiil farkını kaçırıyordu).
                # Boşluk farkı (PDF hece kopması "farkın dalık") yok sayılır; çok küçük fark MEB tablosundaki yazım hatası sayılır.
                a1, a2 = nj(ifade).replace(" ", ""), nj(K["kod"][k]["ifade"]).replace(" ", "")
                if a1 != a2:
                    import difflib
                    oran = difflib.SequenceMatcher(None, a1, a2).ratio()
                    kaz_basi = a1.startswith(a2) and len(a1) > len(a2) + 20   # senaryo hücresine bileşen yapışmış
                    if oran >= 0.985 or kaz_basi:
                        U(f"{k} senaryo tablosunda yazım farkı (MEB tablosu hatası olabilir; kazanım ifadesi esas): {ifade[:120]}")
                    elif k in ONAYLI:
                        U(f"{k} onaylı fark ({ONAYLI[k]}): senaryo '{ifade[:90]}'")
                    else:
                        H(f"{k} ifade farklı:\n      senaryo : {ifade[:200]}\n      kazanım : {K['kod'][k]['ifade'][:200]}")
                        continue
                if r.get("unite") and d not in ("turkce",):
                    su = nj(re.sub(r"^\d+\.\s*ÜNİTE:\s*", "", r["unite"], flags=re.I))
                    if not any(su == nj(b) or su in nj(b) or nj(b) in su for b in K["kod"][k]["birimler"]):
                        H(f"{k} ünite/tema adı tutmuyor: senaryo '{r['unite']}' ↔ kazanım {K['kod'][k]['birimler']}")
                        continue
                ok += 1
            print(f"  senaryo: {ok}/{len(s['satirlar'])} satır kod+ifade+tema ile doğrulandı")
        else:
            print("  senaryo tablosu yok")
        # B) yıllık plan
        p = plan.get(f"{g}-sinif-{d}")
        if p:
            pk = {k for h in p["haftalar"] for k in (h.get("kodlar") or [])}
            eksik = sorted(k for k in pk if k not in K["kod"])
            if eksik: H(f"plan kodları kazanımda yok: {eksik[:12]}{' …' if len(eksik) > 12 else ''}")
            pu = list(dict.fromkeys(h.get("unite", "") for h in p["haftalar"] if h.get("unite")))
            bn = [nj(b) for b in K["birim"]]
            for u in pu:
                for parca in re.split(r"\s*→\s*", u):
                    pj = nj(re.sub(r"^\d+\.\s*(ÜNİTE|TEMA|ÖĞRENME ALANI)?:?\s*", "", parca, flags=re.I))
                    if pj and not any(pj in b or b in pj for b in bn): U(f"plan teması kazanımda bulunamadı: '{parca}'")
            print(f"  plan: {len(pk)} kod, {len(pu)} ünite/tema satırı kontrol edildi")
        else:
            print("  yıllık plan verisi yok (LMS JSON'da bu sınıf yok)")
        # D) kitap
        kt = ""
        for f in sorted(Path(a.kitap).glob(f"{d}-{g}-*.md")): kt += f.read_text(encoding="utf-8")
        if kt:
            ktn = nj(kt)
            for b in K["birim"]:
                if nj(b) not in ktn: U(f"tema/ünite adı kitapta geçmiyor: '{b}'")
            print(f"  kitap: {len(K['birim'])} tema/ünite adı arandı")
        else:
            print("  kitap metni yok")
print(f"\nSONUÇ: {hata} HATA · {uyari} uyarı")
sys.exit(1 if hata else 0)
