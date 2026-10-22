# -*- coding: utf-8 -*-
"""Kazanım ifadelerini 2026-2027 ders kitabı metninde arar (kitaplarda kod basılmaz; çıktılar ünite açılışlarında cümle olarak geçer).

Her çıktı için kitapta en benzer satır penceresi bulunur:
  BİREBİR (≥0.92) · YAKIN (0.80-0.92, ifade farkı olabilir → elle bakılmalı) · YOK (<0.80, kitap çıktıyı yazmıyor ya da farklı yazıyor)
  python tools/kitap_kazanim_karsilastir.py [--kaz skills/tymm-ders-planlama/references/kazanimlar] [--kitap .../lms/content-gen/kaynak/kitap] [--rapor ...md]
"""
import argparse, re, difflib, unicodedata
from pathlib import Path

ap = argparse.ArgumentParser()
ROOT = Path(__file__).resolve().parent.parent
ap.add_argument("--kaz", default=str(ROOT / "skills" / "tymm-ders-planlama" / "references" / "kazanimlar"))
ap.add_argument("--kitap", default=r"C:\Users\cetin\Projects\lms\content-gen\kaynak\kitap")
ap.add_argument("--rapor", default=str(ROOT / "evals" / "KITAP-KAZANIM-2026-2027.md"))
a = ap.parse_args()
TR = str.maketrans({"İ": "i", "I": "i", "ı": "i", "’": "'", "‘": "'"})
def n(s):
    s = unicodedata.normalize("NFKD", s.translate(TR).lower()); s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", " ", s).split()

R = ["# Kitap ↔ kazanım ifade karşılaştırması (2026-2027)", "",
     "Kitaplarda çıktı kodu basılmaz; çıktı cümleleri ünite/tema açılışlarında (\"Bu ünitede…\") geçer. Her kazanım ifadesi kitap metninde bulanık arandı.",
     "**BİREBİR** ≥0.92 · **YAKIN** 0.80-0.92 (ifade farkı olabilir, elle bakılmalı) · **YOK** <0.80 (kitap o cümleyi yazmıyor; tek başına hata değildir).", "",
     "| Sınıf | Ders | Çıktı | Birebir | Yakın | Yok |", "|---|---|---|---|---|---|"]
D = []
for kf in sorted(Path(a.kaz).glob("*-sinif-*.md")):
    m = re.match(r"(\d)-sinif-(.+)\.md", kf.name); g, d = m[1], m[2]
    kit = sorted(Path(a.kitap).glob(f"{d}-{g}-*.md"))
    if not kit: R.append(f"| {g} | {d} | — | kitap metni yok | | |"); continue
    satir = []
    for f in kit:
        for line in f.read_text(encoding="utf-8").split("\n"):
            w = n(line)
            if w: satir.append(w)
    # 1-3 satırlık pencereler (çıktı cümlesi kitapta satır kırılmalı olabilir)
    pencere = [sum(satir[i:i + k], []) for i in range(len(satir)) for k in (1, 2, 3)]
    ciktilar = re.findall(r"^-? ?\*\*([A-Z][\w.]*?\d)\.\*\* (.+?)(?: \*\(.*\)\*)?$", kf.read_text(encoding="utf-8"), re.M)
    seen = set(); b = y = yok = 0; yakinlar = []
    for kod, ifade in ciktilar:
        if kod in seen: continue
        seen.add(kod); hedef = n(ifade)
        if len(hedef) < 3: continue
        anahtar = set(x for x in hedef if len(x) > 4)
        best, bw = 0.0, None
        for w in pencere:
            if len(anahtar & set(w)) < max(2, len(anahtar) // 2): continue
            r = difflib.SequenceMatcher(None, " ".join(hedef), " ".join(w[:len(hedef) + 4])).ratio()
            if r > best: best, bw = r, w
        if best >= 0.92: b += 1
        elif best >= 0.80: y += 1; yakinlar.append((kod, ifade, " ".join(bw[:len(hedef) + 4]), best))
        else: yok += 1
    R.append(f"| {g} | {d} | {len(seen)} | {b} | {y} | {yok} |")
    if yakinlar:
        D += [f"## {g}. sınıf {d}: YAKIN eşleşmeler (ifade farkı olabilir)", ""]
        for kod, ifade, kitap, r in yakinlar:
            D += [f"- **{kod}** ({r:.2f})", f"  - kazanım: {ifade}", f"  - kitap: {kitap}"]
        D.append("")
Path(a.rapor).write_text("\n".join(R + [""] + D), encoding="utf-8")
print("\n".join(R[5:]))
