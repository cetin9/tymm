# -*- coding: utf-8 -*-
"""Her beceriyi KENDİ İÇİNDE TAM (self-contained) paket olarak dist/ altına çıkarır ve zip'ler.

Depoda beceriler birbirinin dosyasına göreli yolla erişir ("../tymm-ders-planlama/references/…").
claude.ai'ye her beceri ayrı zip olarak yüklendiği için bu yollar orada çözülmeyebilir. Bu araç:
  1) skills/<beceri>/ → dist/<beceri>/ kopyalar,
  2) .md dosyalarında geçen her "../tymm-X/<yol>" hedefini (dosya / klasör / <yer tutucu>) pakete kopyalar,
  3) yolları paket içi yola çevirir ("../tymm-X/references/a.md" → "references/a.md"),
  4) dist/<beceri>.zip üretir (SKILL.md zip kökünde).
Depodaki kaynak dosyalar DEĞİŞMEZ. Kitap metinleri (references/kitap/, .gitignore'da) varsa pakete girer.

  python tools/paketle.py [--claude-code]   # --claude-code: ayrıca ~/.claude/skills/ altına kurar
"""
import argparse, re, shutil, sys, zipfile
import yaml
from pathlib import Path

ap = argparse.ArgumentParser(); ap.add_argument("--claude-code", action="store_true"); a = ap.parse_args()
ROOT = Path(__file__).resolve().parent.parent; SK = ROOT / "skills"; DIST = ROOT / "dist"
if DIST.exists(): shutil.rmtree(DIST)
REF = re.compile(r"(?:\.\./)+(tymm-[a-z-]+)/([A-Za-z0-9_./<>-]*)")

def hedefleri_kopyala(paket, beceri):
    """paket içindeki md'lerde geçen başka-beceri yollarını pakete kopyala; yolları yeniden yaz"""
    for md in list(paket.rglob("*.md")):
        t = md.read_text(encoding="utf-8"); yeni = t
        for m in set(REF.finditer(t)):
            diger, yol = m[1], m[2]
            if diger == beceri: continue
            kaynak_yol = re.sub(r"<[^>]*>.*$", "", yol)            # "<brans>.md" → klasörün tamamı
            kaynak = SK / diger / kaynak_yol
            if kaynak.is_file():
                hedef = paket / kaynak_yol; hedef.parent.mkdir(parents=True, exist_ok=True)
                if not hedef.exists(): shutil.copy2(kaynak, hedef)
            elif kaynak.is_dir() or (kaynak.parent.is_dir() and not kaynak_yol.endswith("/")):
                d = kaynak if kaynak.is_dir() else kaynak.parent
                for f in d.rglob("*"):
                    if f.is_file():
                        h = paket / f.relative_to(SK / diger); h.parent.mkdir(parents=True, exist_ok=True)
                        if not h.exists(): shutil.copy2(f, h)
            else:
                print(f"  ! hedef yok: {m[0]} ({md.relative_to(paket)})"); continue
        # yolu paket köküne göre yeniden yaz: md'nin derinliğine göre "../" öneki
        derinlik = len(md.relative_to(paket).parts) - 1
        onek = "../" * derinlik
        yeni = REF.sub(lambda m: m[0] if m[1] == beceri else onek + m[2], yeni)
        if yeni != t: md.write_text(yeni, encoding="utf-8")

for b in sorted(p.name for p in SK.iterdir() if (p / "SKILL.md").exists()):
    paket = DIST / b; shutil.copytree(SK / b, paket)
    for _ in range(2): hedefleri_kopyala(paket, b)   # kopyalanan dosyaların kendi atıfları için ikinci tur
    kalan = [str(md.relative_to(paket)) for md in paket.rglob("*.md") if REF.search(md.read_text(encoding="utf-8"))]
    # SKILL.md: satır sonlarını LF yap ve başlığı claude.ai yükleyicisinin kurallarıyla denetle
    sk = paket / "SKILL.md"; metin = sk.read_text(encoding="utf-8").replace("\r\n", "\n"); sk.write_text(metin, encoding="utf-8", newline="\n")
    m = re.match(r"^---\n(.*?)\n---\n", metin, re.S)
    if not m: sys.exit(f"HATA {b}: SKILL.md YAML başlığıyla (---) başlamıyor")
    try: fm = yaml.safe_load(m[1])
    except yaml.YAMLError as e: sys.exit(f"HATA {b}: SKILL.md başlığı geçersiz YAML — {' '.join(str(e).split())[:200]}")
    if not isinstance(fm, dict) or not fm.get("name") or not fm.get("description"): sys.exit(f"HATA {b}: name/description eksik")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", fm["name"]): sys.exit(f"HATA {b}: name yalnız küçük harf/rakam/tire, ≤64")
    if len(fm["description"]) > 1024: sys.exit(f"HATA {b}: description {len(fm['description'])} karakter (>1024)")
    z = DIST / f"{b}.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(paket.rglob("*")):
            if f.is_file(): zf.write(f, f.relative_to(paket))
    print(f"{b:28} {sum(1 for f in paket.rglob('*') if f.is_file()):4} dosya · zip {z.stat().st_size / 1048576:.1f} MB"
          + (f" · ÇÖZÜLMEMİŞ ATIF: {kalan}" if kalan else ""))
    if a.claude_code:
        hedef = Path.home() / ".claude" / "skills" / b
        if hedef.exists(): shutil.rmtree(hedef)
        shutil.copytree(paket, hedef); print(f"  → {hedef}")
