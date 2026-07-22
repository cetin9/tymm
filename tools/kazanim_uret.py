# -*- coding: utf-8 -*-
"""TYMM tema sayfası -> kazanım .md üretici (türkçe/sosyal/fen 5-7)."""
import re, sys
from pathlib import Path

TXT = Path(r"C:\ttx")
OUT = Path(r"C:\ttx\out"); OUT.mkdir(exist_ok=True)

MARKERS = ["Ders Saati","Alan Becerileri","Kavramsal Beceriler","Eğilimler",
    "Programlar Arası Bileşenler","Sosyal-Duygusal Öğrenme Becerileri","Değerler",
    "Okuryazarlık Becerileri","Disiplinler Arası İlişkiler","Beceriler Arası İlişkiler",
    "Öğrenme Çıktıları ve Süreç Bileşenleri","İçerik Çerçevesi","Anahtar Kavramlar",
    "Öğrenme Kanıtları (Ölçme ve Değerlendirme)"]

def clean(path):
    out=[]
    for ln in Path(path).read_text(encoding="utf-8").splitlines():
        s=re.sub("[-​ ﻿]"," ",ln)
        s=re.sub(r"\s+"," ",s).strip()
        if re.match(r"^\d{2}\.\d{2}\.\d{4}",s): continue
        if "tymm.meb.gov.tr" in s: continue
        out.append(s)
    return out

def sections(lines):
    sec={}; cur=None
    for s in lines:
        if s in MARKERS:
            cur=s; sec[cur]=[]
            continue
        if cur: sec[cur].append(s)
    return sec

def joined(sec,key):
    parts=[x for x in sec.get(key,[]) if x]
    t=" ".join(parts)
    t=re.sub(r"\s+"," ",t).replace(" ,",",").strip()
    return t

def title_of(lines):
    for s in lines[:6]:
        m=re.match(r"^\d+\.\s*(TEMA|ÜNİTE|ÖĞRENME ALANI):\s*(.+)$",s)
        if m: return m.group(2).strip()
    return "?"

def hours_of(sec):
    for s in sec.get("Ders Saati",[]):
        m=re.match(r"^(\d+)$",s)
        if m: return int(m.group(1))
    return None

def parse_outcomes(sec_lines, code_re, bolum=False):
    """returns list of ('bolum',no,title) / ('out',code,title,[components])"""
    items=[]; mode=None
    for s in sec_lines:
        if not s: continue
        mb=re.match(r"^(\d+)\.\s*Bölüm:\s*(.+)$",s) if bolum else None
        mc=re.match(code_re,s)
        mk=re.match(r"^([a-hçğ])\)\s*(.*)$",s)
        if mb:
            items.append(["bolum",mb.group(1),mb.group(2).strip()]); mode=None
        elif mc:
            items.append(["out",mc.group(1),mc.group(2).strip(),[]]); mode="title"
        elif mk and items and items[-1][0]=="out":
            items[-1][3].append([mk.group(1),mk.group(2).strip()]); mode="comp"
        else:
            if not items: continue
            last=items[-1]
            if mode=="comp" and last[0]=="out" and last[3]:
                last[3][-1][1]=(last[3][-1][1]+" "+s).strip()
            elif mode=="title" and last[0]=="out":
                last[2]=(last[2]+" "+s).strip()
            elif last[0]=="bolum":
                last[2]=(last[2]+" "+s).strip()
    # normalize whitespace
    for it in items:
        if it[0]=="out":
            it[1]=it[1].replace(" ",".")
            it[2]=re.sub(r"\s+"," ",it[2])
            for c in it[3]: c[1]=re.sub(r"\s+"," ",c[1])
        else: it[2]=re.sub(r"\s+"," ",it[2])
    return items

def parse_turkce_outcomes(sec_lines):
    """alan-> list of (code,title)"""
    alans={"Dinleme/İzleme":[],"Okuma":[],"Konuşma":[],"Yazma":[]}
    cur=None; last=None
    for s in sec_lines:
        if not s: continue
        if s in alans: cur=s; last=None; continue
        m=re.match(r"^(T\.[DOKY]\.\d\.\d+)\.?\s*(.*)$",s)
        if m and cur:
            alans[cur].append([m.group(1),m.group(2).strip()]); last=alans[cur][-1]
        elif last is not None:
            last[1]=(last[1]+" "+s).strip()
    for v in alans.values():
        for it in v: it[1]=re.sub(r"\s+"," ",it[1])
    return alans

def meta_block(sec):
    rows=[]
    def add(label,key):
        v=joined(sec,key)
        if v and v!="-": rows.append(f"**{label}:** {v}  ")
    add("Alan becerileri","Alan Becerileri")
    add("Kavramsal beceriler","Kavramsal Beceriler")
    add("Eğilimler","Eğilimler")
    add("SDB","Sosyal-Duygusal Öğrenme Becerileri")
    add("Değerler","Değerler")
    add("Okuryazarlık","Okuryazarlık Becerileri")
    add("Disiplinler arası","Disiplinler Arası İlişkiler")
    add("Beceriler arası ilişkiler","Beceriler Arası İlişkiler")
    ic=[x for x in sec.get("İçerik Çerçevesi",[]) if x]
    if ic: rows.append("**İçerik çerçevesi:** "+" · ".join(ic)+"  ")
    add("Anahtar kavramlar","Anahtar Kavramlar")
    return rows

# ---------- builders ----------

def build_fen(grade):
    themes=[]
    for n in range(1,8):
        lines=clean(TXT/f"fen{grade}_{n}.txt"); sec=sections(lines)
        items=parse_outcomes(sec.get("Öğrenme Çıktıları ve Süreç Bileşenleri",[]),
                             rf"^(FB\.{grade}\.\d+\.\d+\.\d+)\.?\s*(.*)$", bolum=True)
        themes.append(dict(no=n,title=title_of(lines),hours=hours_of(sec),sec=sec,items=items))
    total=sum(1 for t in themes for i in t["items"] if i[0]=="out")
    hsum=sum(t["hours"] or 0 for t in themes)
    L=[f"# {grade}. Sınıf Fen Bilimleri — TYMM Öğrenme Çıktısı Verisi","",
       "**Kaynak (doğrulanmış):** MEB Türkiye Yüzyılı Maarif Modeli — Fen Bilimleri",
       "Dersi Öğretim Programı, resmî ünite sayfaları (tymm.meb.gov.tr). Öğrenme",
       "çıktıları ve süreç bileşenleri (a, b, c, ç…) birebir aktarılmıştır.","",
       "> **KOD DESENİ:** `FB.<sınıf>.<ünite>.<bölüm>.<çıktı no>` — dört parçalı.",
       "> Her çıktının altında **süreç bileşenleri** a) b) c) ç)… listelenir; TYMM'de",
       "> ölçmenin konusu çıktı + süreç bileşenleridir; bileşenler bu dosyadan aynen",
       "> alınır, asla yeniden yazılmaz.","",
       f"Toplam ünite: 7 · Öğrenme çıktısı: {total} · Ders saati (üniteler toplamı): {hsum}","",
       "## Ünite tablosu","","| Ünite | Ad | Çıktı | Saat |","|-------|----|-------|------|"]
    for t in themes:
        c=sum(1 for i in t["items"] if i[0]=="out")
        L.append(f"| {t['no']} | {t['title']} | {c} | {t['hours']} |")
    for t in themes:
        L+=["",f"## ÜNİTE {t['no']} — {t['title']}","",f"**Ders saati:** {t['hours']}  "]
        L+=meta_block(t["sec"]); L.append("")
        for i in t["items"]:
            if i[0]=="bolum": L+=[f"### {i[1]}. Bölüm: {i[2]}",""]
            else:
                L.append(f"**{i[1]}.** {i[2]}")
                for c in i[3]: L.append(f"- {c[0]}) {c[1]}")
                L.append("")
    return "\n".join(L).rstrip()+"\n", total, hsum

def build_sosyal(grade):
    themes=[]
    for n in range(1,7):
        lines=clean(TXT/f"sos{grade}_{n}.txt"); sec=sections(lines)
        items=parse_outcomes(sec.get("Öğrenme Çıktıları ve Süreç Bileşenleri",[]),
                             rf"^(SB[. ]{grade}\.\d+\.\d+)\.?\s*(.*)$", bolum=False)
        themes.append(dict(no=n,title=title_of(lines),hours=hours_of(sec),sec=sec,items=items))
    total=sum(1 for t in themes for i in t["items"] if i[0]=="out")
    hsum=sum(t["hours"] or 0 for t in themes)
    L=[f"# {grade}. Sınıf Sosyal Bilgiler — TYMM Öğrenme Çıktısı Verisi","",
       "**Kaynak (doğrulanmış):** MEB Türkiye Yüzyılı Maarif Modeli — Sosyal Bilgiler",
       "Dersi Öğretim Programı, resmî öğrenme alanı sayfaları (tymm.meb.gov.tr).",
       "Öğrenme çıktıları ve süreç bileşenleri (a, b, c, ç…) birebir aktarılmıştır.","",
       "> **KOD DESENİ:** `SB.<sınıf>.<öğrenme alanı>.<çıktı no>` — üç parçalı.",
       "> Her çıktının altında **süreç bileşenleri** a) b) c) ç)… listelenir; TYMM'de",
       "> ölçmenin konusu çıktı + süreç bileşenleridir; bileşenler bu dosyadan aynen",
       "> alınır, asla yeniden yazılmaz.","",
       f"Toplam öğrenme alanı: 6 · Öğrenme çıktısı: {total} · Ders saati (alanlar toplamı): {hsum}","",
       "## Öğrenme alanı tablosu","","| Alan | Ad | Çıktı | Saat |","|------|----|-------|------|"]
    for t in themes:
        c=sum(1 for i in t["items"] if i[0]=="out")
        L.append(f"| {t['no']} | {t['title']} | {c} | {t['hours']} |")
    for t in themes:
        L+=["",f"## {t['no']}. ÖĞRENME ALANI — {t['title']}","",f"**Ders saati:** {t['hours']}  "]
        L+=meta_block(t["sec"]); L.append("")
        for i in t["items"]:
            L.append(f"**{i[1]}.** {i[2]}")
            for c in i[3]: L.append(f"- {c[0]}) {c[1]}")
            L.append("")
    return "\n".join(L).rstrip()+"\n", total, hsum

def build_turkce(grade):
    themes=[]
    for n in range(1,7):
        lines=clean(TXT/f"tur{grade}_{n}.txt"); sec=sections(lines)
        alans=parse_turkce_outcomes(sec.get("Öğrenme Çıktıları ve Süreç Bileşenleri",[]))
        themes.append(dict(no=n,title=title_of(lines),hours=hours_of(sec),sec=sec,alans=alans))
    allcodes=set()
    for t in themes:
        for v in t["alans"].values():
            for code,_ in v: allcodes.add(code)
    hsum=sum(t["hours"] or 0 for t in themes)
    L=[f"# {grade}. Sınıf Türkçe — TYMM Öğrenme Çıktısı Verisi","",
       "**Kaynak (doğrulanmış):** MEB Türkiye Yüzyılı Maarif Modeli — Ortaokul Türkçe",
       "Dersi Öğretim Programı, resmî tema sayfaları (tymm.meb.gov.tr). Çıktı kodları",
       "ve ifadeleri birebir aktarılmıştır.","",
       "> **KOD DESENİ:** `T.<alan>.<sınıf>.<çıktı no>` — alan: D (Dinleme/İzleme),",
       "> O (Okuma), K (Konuşma), Y (Yazma). Türkçe sarmal yapıdadır: aynı çıktı",
       "> birden çok temada yeniden işlenir; tema, çıktının hangi metin/bağlam",
       "> evreninde çalışılacağını belirler.","",
       "> **SÜREÇ BİLEŞENİ NOTU:** Türkçe resmî tema sayfaları çıktıları süreç",
       "> bileşeni (a, b, c…) dökümü olmadan listeler. Bu dosyadaki ifadeler çıktı",
       "> düzeyinde birebirdir; süreç bileşeni gerektiğinde resmî program PDF'inden",
       "> teyit edilmeli, belgeye doğrulama notu düşülmelidir.","",
       f"Toplam tema: 6 · Tekil çıktı kodu: {len(allcodes)} · Ders saati (temalar toplamı): {hsum}","",
       "## Tema tablosu","","| Sıra | Tema | Saat |","|------|------|------|"]
    for t in themes:
        L.append(f"| {t['no']} | {t['title']} | {t['hours']} |")
    for t in themes:
        L+=["",f"## TEMA {t['no']} — {t['title']}","",f"**Ders saati:** {t['hours']}  "]
        L+=meta_block(t["sec"]); L.append("")
        for alan in ["Dinleme/İzleme","Okuma","Konuşma","Yazma"]:
            v=t["alans"][alan]
            if not v: continue
            L.append(f"### {alan}")
            for code,ti in v: L.append(f"- **{code}.** {ti}")
            L.append("")
    return "\n".join(L).rstrip()+"\n", len(allcodes), hsum

for g in (5,6,7):
    for name,fn in [(f"{g}-sinif-fen-bilimleri.md",build_fen),
                    (f"{g}-sinif-sosyal-bilgiler.md",build_sosyal),
                    (f"{g}-sinif-turkce.md",build_turkce)]:
        text,total,hsum=fn(g)
        (OUT/name).write_text(text,encoding="utf-8")
        print(f"{name}: outcomes={total} hours={hsum} bytes={len(text)}")
