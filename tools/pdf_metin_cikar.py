import subprocess, re
from pathlib import Path
SRC = Path(r"C:\Users\cetin\Projects\tymm skill\sources\TEMEL ÖĞRETİM PROGRAMLARI")
OUT = Path(r"C:\ttx"); OUT.mkdir(exist_ok=True)
tags = {"türkçe 5. sınıf":"tur5","türkçe 6. sınıf":"tur6","türkçe 7. sınıf":"tur7",
 "sosyal bilgiler 5. sınıf":"sos5","sosyal bilgiler 6. sınıf":"sos6","sosyal bilgiler 7. sınıf":"sos7",
 "FEN BİLimleri 5. SINIF":"fen5","fen bilimleri 6. sınıf":"fen6","fen bilimleri 7. sınıf":"fen7"}
ok=fail=0
for d,tag in tags.items():
    for pdf in sorted((SRC/d).glob("*.pdf")):
        m = re.search(r"(\d+)\.\s*(TEMA|ÜNİTE|ÖĞRENME ALANI)", pdf.name)
        n = m.group(1) if m else "X"
        out = OUT / f"{tag}_{n}.txt"
        r = subprocess.run(["pdftotext","-layout","-enc","UTF-8",str(pdf),str(out)],capture_output=True)
        if r.returncode==0 and out.stat().st_size>500: ok+=1
        else: fail+=1; print("FAIL",tag,n)
print(f"ok={ok} fail={fail}")
