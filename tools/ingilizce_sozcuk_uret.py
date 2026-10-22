# -*- coding: utf-8 -*-
"""İngilizce 5-6 için tema başına GÜVENLİ SÖZCÜK listesi: program hedef sözcükleri ∩ ders kitabının o temanın sayfaları.

Ölçüm (23.10.2026): kitabın tema sayfaları programın hedef sözcüklerinin yalnız %44-71'ini kullanıyor. Sınav sorusunda öğrencinin
kitapta görmediği sözcük kullanılmasın diye skill bu listeyle sınırlanır.
  python tools/ingilizce_sozcuk_uret.py   → skills/tymm-acik-uclu-sinav/references/ingilizce-sozcuk/<sınıf>-sinif.md
"""
import re, glob
from pathlib import Path

KAYNAK = Path(r"C:\Users\cetin\Projects\lms\content-gen\kaynak")
OUT = Path(__file__).resolve().parent.parent / "skills" / "tymm-acik-uclu-sinav" / "references" / "ingilizce-sozcuk"
OUT.mkdir(parents=True, exist_ok=True)
DUR = {"nouns", "verbs", "adjectives", "adverbs", "vocabulary", "target", "with", "revisional", "phrases", "prepositions", "expressions",
       "pronouns", "numbers", "other", "use", "and", "the", "for", "about", "from", "into", "that", "this", "their", "your", "sub", "themes"}

def sayfalar(f):
    t = f.read_text(encoding="utf-8"); p = re.split(r"^--- s\.(\d+) ---$", t, flags=re.M)
    return {int(p[i]): p[i + 1] for i in range(1, len(p), 2)}

for g in (5, 6):
    bk = sayfalar(KAYNAK / "kitap" / f"ingilizce-{g}-1.md")
    calisma = KAYNAK / "kitap" / f"ingilizce-{g}-calisma.md"
    ck = " ".join(sayfalar(calisma).values()).lower() if calisma.exists() else ""
    bas = {}
    for s, t in sorted(bk.items()):
        if s < 12: continue
        for m in re.finditer(r"theme\s*(\d)", t.lower()): bas.setdefault(int(m.group(1)), s)
    sirali = sorted(bas.items())
    aralik = {k: (v, sirali[i + 1][1] - 1 if i + 1 < len(sirali) else max(bk)) for i, (k, v) in enumerate(sirali)}
    L = [f"# {g}. sınıf İngilizce — tema başına güvenli sözcük listesi", "",
         "Program hedef sözcükleri (`Target Vocabulary in Use`) ∩ ders kitabının o temaya ait sayfaları (çalışma kitabı dahil). "
         "Sınav sorularında **yalnız bu sözcükler** (ve temel işlev sözcükleri: a, the, is, are, have, can…) kullanılır. "
         "Listede olmayan program sözcüğü kitapta bu temada geçmiyor demektir; öğrenci görmemiş olabilir.", ""]
    for f in sorted(glob.glob(str(KAYNAK / "program" / f"ingilizce-{g}-sinif" / "*.md"))):
        no = int(re.search(r"unite-(\d)", f)[1]); t = open(f, encoding="utf-8").read()
        ad = re.search(r"unite-\d-(.+)\.md", f)[1].replace("-", " ").title()
        i = t.find("Target Vocabulary"); j = t.find("Anahtar Kavramlar", i) if i > 0 else -1
        blok = t[i:j if j > 0 else i + 4000] if i > 0 else ""
        kelime = sorted(set(w.lower() for w in re.findall(r"\b[A-Za-z][a-z]{2,}\b", blok)) - DUR)
        if no not in aralik: continue
        a, b = aralik[no]
        metin = " ".join(bk[s] for s in range(a, b + 1) if s in bk).lower() + " " + ck
        guvenli = [w for w in kelime if re.search(r"\b" + re.escape(w), metin)]
        disarida = [w for w in kelime if w not in guvenli]
        L += [f"## Tema {no} — {ad} (kitap PDF s. {a}-{b})", "",
              f"**Güvenli ({len(guvenli)}/{len(kelime)}):** " + ", ".join(guvenli), "",
              f"**Programda var, kitabın bu temasında YOK ({len(disarida)}) — kullanma:** " + ", ".join(disarida), ""]
    (OUT / f"{g}-sinif.md").write_text("\n".join(L), encoding="utf-8")
    print(f"İngilizce {g}: {OUT / f'{g}-sinif.md'}")
