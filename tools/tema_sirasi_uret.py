# -*- coding: utf-8 -*-
"""references/tema-sirasi.md üretir: 2026-2027 resmî çerçeve yıllık planlarından (TEGM 03.09.2026, DÖGM 31.08.2026) hafta → tema/ünite.

Veri: lms/apps/web/src/data/yillik-plan-2026-2027.json (MEB-KAYNAK/2026-2027/05-yillik-plan xlsx'lerinden üretilir).
  python tools/tema_sirasi_uret.py [--plan ...json] [--out skills/tymm-ders-planlama/references/tema-sirasi.md]
"""
import argparse, json, re, datetime
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--plan", default=r"C:\Users\cetin\Projects\lms\apps\web\src\data\yillik-plan-2026-2027.json")
ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "skills" / "tymm-ders-planlama" / "references" / "tema-sirasi.md"))
a = ap.parse_args()
veri = json.loads(Path(a.plan).read_text(encoding="utf-8"))
AD = {"turkce": "Türkçe", "matematik": "Matematik", "fen-bilimleri": "Fen Bilimleri", "sosyal-bilgiler": "Sosyal Bilgiler",
      "din-kulturu-ve-ahlak-bilgisi": "Din Kültürü ve Ahlak Bilgisi", "ingilizce": "İngilizce"}
BIRINCI = {"fen-bilimleri": "03.11", "matematik": "05.11", "sosyal-bilgiler": "06.11", "turkce": "10.11", "ingilizce": "12.11", "din-kulturu-ve-ahlak-bilgisi": "13.11"}

L = ["# Tema İşleniş Sırası — 2026-2027 resmî çerçeve yıllık planları", "",
     f"**Kaynak:** MEB 2026-2027 taslak çerçeve yıllık planları (TEGM zip'i 03.09.2026; Din Kültürü DÖGM 31.08.2026), "
     f"`MEB-KAYNAK/2026-2027/05-yillik-plan/`. Üretim: `tools/tema_sirasi_uret.py` ({datetime.date.today().isoformat()}).", "",
     "**Neden önemli:** İşleniş sırası tema/ünite numarasını izlemez (ör. 5. sınıf Matematik yıla MAT.5.3 Geometrik Şekiller ile başlar). "
     "Ortak yazılı senaryoları, \"bu hafta hangi konudayız\" ve karışık tekrar kapsamı bu sıraya göre belirlenir, tema numarasına göre değil.", "",
     "**Kullanım kuralları:**",
     "- 1. hafta = 14-18 Eylül 2026; 37 öğretim haftası. Ara tatiller hafta numarası almaz (1. ara tatil 16-20 Kasım).",
     "- Bu sıra çerçeve plandır; okulun zümre planı farklıysa öğretmenin söylediği geçerlidir.",
     "- \"A → B\" satırı, haftanın iki temaya bölündüğünü gösterir.",
     "- ▶ 1. yazılı: 2026-2027 OYSS takvimi (20.10.2026). Sınav haftası ve sonrası o sınavın kapsamına girmez.",
     "- 7. sınıf İngilizce okulda **eski programla** (10 ünite) okutulur; 8. sınıf bu dosyada yoktur.", ""]
for g in (5, 6, 7):
    for d, ad in AD.items():
        k = next((x for x in veri["dersler"] if x["slug"] == f"{g}-sinif-{d}"), None)
        if not k: continue
        L += [f"## {ad} {g}", "", "| Hafta | Ünite/Tema | Konular |", "|---|---|---|"]
        t1 = datetime.date(2026, 11, 11 if (d == "matematik" and g == 6) else int(BIRINCI[d][:2]))
        etiket = "ÜLKE GENELİ, 11.11" if (d == "matematik" and g == 6) else BIRINCI[d]
        if g == 7 and d == "ingilizce": etiket += "; OYSS dışı"
        SINAV = dict(u="▶", bas=0, son=0, k=[])
        gruplar = []; yazildi = False
        for h in k["haftalar"]:
            # sınavın düştüğü hafta (pazartesi..cuma) ve sonrası sınav kapsamı dışında: işaret o haftanın ÖNÜNE konur
            if not yazildi and datetime.date.fromisoformat(h["pzt"]) + datetime.timedelta(days=4) >= t1:
                gruplar.append(SINAV); yazildi = True
            u = re.sub(r"\s+", " ", h.get("unite") or "").strip().replace("iŞ", "İŞ").replace(" ve ", " VE ") or "—"
            konu = re.sub(r"\s+", " ", h.get("konu") or "").strip()
            if gruplar and gruplar[-1] is not SINAV and gruplar[-1]["u"] == u:
                gruplar[-1]["son"] = h["h"]
                if konu and konu not in gruplar[-1]["k"]: gruplar[-1]["k"].append(konu)
            else:
                gruplar.append(dict(u=u, bas=h["h"], son=h["h"], k=[konu] if konu else []))
        for gr in gruplar:
            if gr is SINAV:
                L.append(f"| ▶ | **1. dönem 1. yazılı ({etiket}) — kapsam bu satırın üstü** | |"); continue
            hafta = f"{gr['bas']}" if gr["bas"] == gr["son"] else f"{gr['bas']}-{gr['son']}"
            L.append(f"| {hafta} | {gr['u']} | {' · '.join(gr['k'])[:300]} |")
        L.append("")
Path(a.out).write_text("\n".join(L), encoding="utf-8")
print("yazıldı:", a.out, len(L), "satır")
