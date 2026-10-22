# -*- coding: utf-8 -*-
"""Ders kitaplarında her temanın başladığı PDF sayfasını bulur → tema → sayfa aralığı dizini (6-7. sınıf, 6 ders).

Yöntem: tema adları ve sırası 2026-27 resmî yıllık plandan (lms/apps/web/src/data/yillik-plan-2026-2027.json) alınır. Her tema adının kitapta
BAŞLIK SATIRI olarak (satırın tamamı ya da satır başı) ilk geçtiği sayfa = tema başlangıcı. İçindekiler sayfaları (≥3 tema adı geçen) atlanır.
Bulunan başlangıçlar plan sırasıyla artmıyorsa ⚠ yazılır (kitap sırası = plan sırası, 23.10.2026'da numaralı başlıklarla doğrulandı).
  python tools/kitap_dizini_uret.py → skills/tymm-acik-uclu-sinav/references/kitap-dizini-6-7.md (5. sınıf: elle yazılmış kitap-dizini.md)
"""
import json, re, unicodedata
from pathlib import Path

KITAP = Path(r"C:\Users\cetin\Projects\lms\content-gen\kaynak\kitap")
PLAN = Path(r"C:\Users\cetin\Projects\lms\apps\web\src\data\yillik-plan-2026-2027.json")
OUT = Path(__file__).resolve().parent.parent / "skills" / "tymm-acik-uclu-sinav" / "references" / "kitap-dizini-6-7.md"
JSON_OUT = OUT.with_name("kitap-dizini.json")
DIZIN = {}
DERS = {"turkce": "Türkçe", "matematik": "Matematik", "fen-bilimleri": "Fen Bilimleri", "sosyal-bilgiler": "Sosyal Bilgiler",
        "din-kulturu-ve-ahlak-bilgisi": "Din Kültürü ve Ahlak Bilgisi", "ingilizce": "İngilizce"}
ALIAS = {"KÜLTÜRÜMÜZDE DİNİ MOTİFLER": "KÜLTÜRÜMÜZDEKİ DİNÎ MOTİFLER"}   # plan adı ≠ kitap adı
def n(s):
    s = ALIAS.get(s.strip(), s).replace("&", " and ")
    s = unicodedata.normalize("NFKD", s.replace("İ", "i").replace("I", "i").replace("ı", "i").replace("’", "'").lower())
    return re.sub(r"[^a-z0-9]+", "", "".join(c for c in s if not unicodedata.combining(c)))

plan = {x["slug"]: x for x in json.loads(PLAN.read_text(encoding="utf-8"))["dersler"]}
L = ["# 6. ve 7. sınıf ders kitabı dizini (MEB, 2026-2027) — otomatik", "",
     "Üretim: `tools/kitap_dizini_uret.py`. Tema adı/sırası resmî yıllık plandan; başlangıç sayfası, adın kitapta başlık satırı olarak ilk geçtiği "
     "sayfa. Sayfa = PDF sayfası (`--- s.N ---`); basılı numara genellikle 1-2 eksiktir. Kitap içi tema numarası program kodundan farklı olabilir "
     "(ör. Matematik); eşleme ADLA yapılır. 5. sınıf: `kitap-dizini.md`.", ""]
for g in (5, 6, 7):
    for d, ad in DERS.items():
        p = plan.get(f"{g}-sinif-{d}"); ciltler = sorted(KITAP.glob(f"{d}-{g}-[12].md"))
        if not p or not ciltler: continue
        temalar = []
        for h in p["haftalar"]:
            u = h.get("unite") or ""
            if "→" in u or re.search(r"OKUL TEMELL|SOSYAL ETK|LABORATUVAR|ORIENTATION|REVISION", u, re.I): continue
            u = re.sub(r"^\s*(\d+\.?\s*(ÜNİTE|TEMA)?\s*:?\s*|THEME \d+:\s*|\d+\s+)", "", u.strip(), flags=re.I).strip()
            if u and n(u) not in {n(x) for x in temalar}: temalar.append(u)   # "ve"/"VE" yazım farkı aynı tema
        temalar = [t for t in temalar if not any(o != t and n(o) in n(t) for o in temalar)]   # geçiş satırı birleşimlerini at
        satir, sayfa_metni, son, sayfa_ham = [], {}, {}, {}
        for f in ciltler:
            c = int(f.stem[-1]); s = 0
            for line in f.read_text(encoding="utf-8").split("\n"):
                m = re.match(r"^--- s\.(\d+) ---", line)
                if m: s = int(m[1]); son[c] = s; continue
                if s > 10 and line.strip():
                    satir.append((c, s, n(line))); sayfa_metni.setdefault((c, s), "")
                    sayfa_metni[(c, s)] += n(line); sayfa_ham[(c, s)] = sayfa_ham.get((c, s), "") + line + "\n"
        keys = [n(t) for t in temalar]
        toc = {k for k, tx in sayfa_metni.items() if sum(1 for x in keys if x and x in tx) >= 3}
        # Yöntem 1: numaralı ünite/tema başlıkları ("2. ÜNİTE", "3.TEMA", "THEME 4", "UNIT 5"); k. başlık = plandaki k. tema
        hepsi = {}   # numara → tüm geçtiği (cilt, sayfa)'lar; içindekiler sayfaları hariç
        for (cc, s) in sorted(sayfa_metni):
            if (cc, s) in toc: continue
            for rx in (r"(\d{1,2})\s*\.\s*(?:ÜNİTE|Ünite|TEMA|Tema)\b", r"\bTHEME\s*(\d)\b", r"\bUNIT\s*(\d{1,2})\b"):
                for m in re.finditer(rx, sayfa_ham.get((cc, s), "")):
                    no = int(m[1])
                    if 0 < no <= len(temalar) and (cc, s) not in hepsi.setdefault(no, []): hepsi[no].append((cc, s))
        # açgözlü seçim: her numara için, bir önceki temanın başlangıcından SONRAKİ ilk görünüş (önceki ciltteki atıflar elenir)
        sira, onceki = [], (0, 0)
        for i in range(1, len(temalar) + 1):
            sec = next((x for x in sorted(hepsi.get(i, [])) if x > onceki), None)
            sira.append(sec)
            if sec: onceki = sec
        if all(sira) and sira == sorted(sira):
            bas = list(zip(temalar, sira)); yontem = "numaralı başlık"
        else:
            # Yöntem 2: tema adının sayfa üst başlığı olarak tekrarlandığı ilk küme (8 sayfada ≥3 kez)
            bas = []
            for t, k in zip(temalar, keys):
                hits = sorted(x for x, tx in sayfa_metni.items() if x not in toc and k and k in tx)
                st = next((h for h in hits if sum(1 for x in hits if x[0] == h[0] and h[1] <= x[1] < h[1] + 8) >= 3), hits[0] if hits else None)
                bas.append((t, st))
            yontem = "sayfa üst başlığı"
        if g == 5: L_5 = True
        if g != 5: L += [f"## {ad} {g}", "", f"Yöntem: {yontem}.", "", "| Sıra | Tema/Ünite (plan) | Cilt | PDF sayfaları |", "|---|---|---|---|"]
        bulunan = [b for b in bas if b[1]]
        for i, (t, hit) in enumerate(bas):
            if not hit: L.append(f"| {i + 1} | {t} | ? | başlık bulunamadı |"); continue
            c, s = hit
            sonraki = next((b[1] for b in bas[i + 1:] if b[1] and b[1][0] == c), None)
            bit = sonraki[1] - 1 if sonraki else son[c]
            DIZIN.setdefault(f"{g}-{d}", []).append({"sira": i + 1, "tema": t, "cilt": c, "bas": s, "son": bit})
            if g != 5: L.append(f"| {i + 1} | {t} | {c} | {s}-{bit} |")
        if [b[1] for b in bulunan] != sorted(b[1] for b in bulunan): L.append("\n> ⚠ başlangıçlar plan sırasıyla artmıyor — elle teyit edilmeli.")
        L.append("")
OUT.write_text("\n".join(L), encoding="utf-8"); print("yazıldı", OUT)
JSON_OUT.write_text(json.dumps(DIZIN, ensure_ascii=False, indent=1), encoding="utf-8"); print("yazıldı", JSON_OUT)
