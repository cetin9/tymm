# -*- coding: utf-8 -*-
"""Eski ve yeni kazanım dosyaları arasındaki farkı raporlar (kod eklendi/kalktı, ifade değişti, süreç bileşeni değişti).

  python tools/kazanim_fark.py --eski skills/tymm-ders-planlama/references/kazanimlar --yeni C:/ttx/out --rapor KAZANIM-FARK-2026-2027.md
Fen'de 2025-26 dört parçalı kod (FB.5.1.2.1) → 2026-27 üç parçalı (FB.5.1.2) eşlemesi ifade benzerliğiyle yapılır.
"""
import argparse, re, difflib
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--eski", required=True); ap.add_argument("--yeni", required=True); ap.add_argument("--rapor", required=True)
a = ap.parse_args()

def oku(p):
    if not p.exists(): return None
    K = {}; son = None
    for line in p.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^-? ?\*\*([A-Z][\w.]*?\d)\.\*\* (.+?)(?: \*\(.*\)\*)?$", line)
        if m:
            son = m[1]
            if son not in K: K[son] = [m[2].strip(), []]
            continue
        b = re.match(r"^- ([a-zçğ])\) (.+)$", line)
        if b and son and (b[1], b[2].strip()) not in K[son][1]: K[son][1].append((b[1], b[2].strip()))
    return K

def n(s): return re.sub(r"\s+", " ", s.replace("’", "'")).strip().rstrip(".").lower()
DERSLER = ["turkce", "matematik", "fen-bilimleri", "sosyal-bilgiler", "din-kulturu-ve-ahlak-bilgisi", "ingilizce"]
R = ["# Kazanım verisi değişiklik raporu: 2025-2026 → 2026-2027", "",
     "Eski: Temmuz 2026 kazanım dosyaları (2025-2026 programı). Yeni: tymm.meb.gov.tr ünite sayfaları (22.10.2026) + DKAB için DÖGM 2026-27 planı + İngilizce 7 için MEB 2026-27 planı (eski program).",
     "Sayılar: **+** yeni kod · **−** kalkan kod · **ifade** çıktı cümlesi değişti · **bileşen** süreç bileşenleri değişti.", ""]
ozet = ["| Sınıf | Ders | Eski kod | Yeni kod | + | − | ifade | bileşen |", "|---|---|---|---|---|---|---|---|"]
detay = []
for g in (5, 6, 7):
    for d in DERSLER:
        E = oku(Path(a.eski) / f"{g}-sinif-{d}.md") or {}
        Y = oku(Path(a.yeni) / f"{g}-sinif-{d}.md") or {}
        if d == "matematik": E = {k: v for k, v in E.items() if k.count(".") >= 3}   # eski dosyadaki tema düzeyi kodları (MAT.5.1) çıktı değil
        esle = {}
        if d == "fen-bilimleri":   # 4 parçalı → 3 parçalı: ifade benzerliğiyle eşle
            for ek, (ei, _) in E.items():
                best = max(Y, key=lambda yk: difflib.SequenceMatcher(None, n(ei), n(Y[yk][0])).ratio(), default=None)
                if best and difflib.SequenceMatcher(None, n(ei), n(Y[best][0])).ratio() > 0.6: esle[ek] = best
        else:
            esle = {k: k for k in E if k in Y}
        eslesen_yeni = set(esle.values())
        eklenen = [k for k in Y if k not in eslesen_yeni]; kalkan = [k for k in E if k not in esle]
        ifade = [(ek, yk) for ek, yk in esle.items() if n(E[ek][0]) != n(Y[yk][0])]
        bilesen = [(ek, yk) for ek, yk in esle.items() if [n(x[1]) for x in E[ek][1]] != [n(x[1]) for x in Y[yk][1]]]
        ozet.append(f"| {g} | {d} | {len(E)} | {len(Y)} | {len(eklenen)} | {len(kalkan)} | {len(ifade)} | {len(bilesen)} |")
        if not (eklenen or kalkan or ifade or bilesen): continue
        detay += [f"## {g}. sınıf {d}", ""]
        if d == "fen-bilimleri" and esle: detay += [f"Kod şeması değişti: {len(esle)} çıktı ifade benzerliğiyle eşlendi (ör. {next(iter(esle))} → {esle[next(iter(esle))]}).", ""]
        if eklenen: detay += ["**Yeni çıktılar:**", ""] + [f"- {k} — {Y[k][0][:160]}" for k in eklenen] + [""]
        if kalkan: detay += ["**Kalkan çıktılar:**", ""] + [f"- {k} — {E[k][0][:160]}" for k in kalkan] + [""]
        if ifade:
            detay += ["**İfadesi değişen çıktılar:**", ""]
            for ek, yk in ifade: detay += [f"- {yk}{' (eski ' + ek + ')' if ek != yk else ''}", f"  - eski: {E[ek][0][:200]}", f"  - yeni: {Y[yk][0][:200]}"]
            detay.append("")
        if bilesen:
            detay += ["**Süreç bileşenleri değişen çıktılar:**", ""]
            for ek, yk in bilesen[:40]:
                detay.append(f"- {yk}: {len(E[ek][1])} → {len(Y[yk][1])} bileşen")
            if len(bilesen) > 40: detay.append(f"- … ve {len(bilesen) - 40} çıktı daha")
            detay.append("")
Path(a.rapor).write_text("\n".join(R + ["## Özet", ""] + ozet + [""] + detay), encoding="utf-8")
print("\n".join(ozet))
