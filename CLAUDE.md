# CLAUDE.md — TYMM Öğretim Becerileri Proje Anayasası

Bu depo, Anthropic'in açık kaynak **k12-teacher-skills** mimarisinin (Apache 2.0)
Türkiye Yüzyılı Maarif Modeli'ne (TYMM) uyarlamasıdır. Geliştiren: Çetin
GÜLTEKİN (İstanbul); hedef kitle TYMM ile çalışan ortaokul öğretmenleridir.
Tüm çıktılar ve iletişim Türkçedir.

## Beceriler

- `skills/tymm-ders-planlama/` — ders planı + çalışma kağıdı/kağıtları +
  öğrenme kanıtları + isteğe bağlı etkileşimli konu anlatımı (A4/ekran HTML)
- `skills/tymm-baglam-testi/` — düzeyli (Temel/Gelişen/İleri) bağlam temelli
  çoktan seçmeli test setleri + ayrı cevap anahtarı
- `skills/tymm-acik-uclu-sinav/` — yönetmeliğe uygun ortak yazılı: konu soru
  dağılım tablosu + açık uçlu/kısa cevaplı sınav + dereceli puanlama anahtarı
- `skills/tymm-ders-farklilastirma/` — mevcut ders/kağıt/konu için resmî
  desende Destekleme + Zenginleştirme etkinlik paketleri (Ek 1 / Ek 2)

## Değiştirilemez mimari kararlar

1. **Branş = referans dosyası; iskelet ortak.** Ders başına ayrı beceri YOK;
   beceriyi iş türü belirler.
2. **Kazanım verisi statik dosyalardan okunur** (`references/kazanimlar/`).
   Çıktı ifadeleri ve süreç bileşenleri (a, b, c, ç…) resmî programdan
   **birebir** aktarılır, ASLA uydurulmaz veya yeniden yazılmaz. Veri yoksa
   belgeye doğrulama uyarısı eklenerek ilerlenir.
3. **Beceri kodu kaydı:** `references/beceri-cercevesi.md` içindeki listede
   olmayan hiçbir KB/E/MAB/TAB/FBAB/SBAB/SDB/D/OB kodu kullanılamaz. Kod +
   resmî ad birlikte yazılır.
4. **Kavram izlenebilirliği:** kağıtta adlandırılan her kavram plan akışında
   kurulmuş olmalı; dolgu kavramlar "Varsayımlar" satırında bildirilir.
5. **Dipnot standardı:** çıktı kodu · sayfa · "Yapay zekâ desteğiyle
   hazırlanmıştır…" · doğrulama uyarısı. Araç/sürüm adı belgelere sızmaz.
6. **Çalışma kağıdı:** senaryo + KB1/KB2/KB3 kademeli bölümler + tam 100 puan;
   cevap anahtarı daima ayrı belge.
7. **Test:** KB dağılımı Temel 6-3-1 / Gelişen 3-5-2 / İleri 1-4-5;
   çeldiriciler yanılgı envanterinden; seçenek dengesi (10 soruda hiçbir
   harf >4 veya <1).
8. **Soru yazım ilkeleri resmî kılavuzdan gelir.**
   `skills/tymm-baglam-testi/references/kilavuz-ilkeleri.md` (MEB TYMM
   Bağlam Temelli Çoktan Seçmeli Soru Yazım Kılavuzu, Mart 2026) test
   üretiminde zorunlu ilk okumadır ve branş dosyalarıyla çelişme hâlinde
   esas alınır. Soru, çıktıya değil çıktının **süreç bileşenine** yazılır;
   her soru bağlam işlevsellik testini geçer.

## Kritik resmî kurallar

- **Ortak yazılı sınavlarda çoktan seçmeli KULLANILAMAZ** (MEB yönetmeliği;
  açık uçlu/kısa cevaplı zorunlu). Test becerisi çıktıları "alıştırma/deneme
  amaçlıdır" ibaresi taşır; ortak yazılı istenirse açık uçlu üretilir.
- **Kod desenleri:** Fen 4 parçalı `FB.<sınıf>.<ünite>.<bölüm>.<çıktı>`;
  matematik/Türkçe/sosyal 3 parçalı (`MAT.6.1.1` / `T.6.1.1` / `SB.6.1.1`).
- **Müfredat durumu (2026-27, öğretmen teyitli):** 5-6-7 → TYMM; 8 → eski
  program (kazanım terminolojisi). `references/mufredat-durumu.md` her
  üretimde zorunlu ilk okumadır.

## Veri durumu (2026-2027, 22 Ekim 2026'da yenilendi)

| Veri | Durum |
|------|-------|
| kazanimlar/ 5/6/7 · Türkçe, Mat, Fen, Sosyal, İngilizce 5-6 | ✅ tymm.meb.gov.tr ünite sayfaları HTML'inden birebir (`tools/kazanim_html_uret.py`); tam program PDF'leriyle kod kod karşılaştırıldı (Mat/Fen/Sosyal birebir). Türkçe 5 T.O.5.14 sitede eksik → tam programdan eklendi. Türkçe'de süreç bileşeni yayımlanmıyor. |
| kazanimlar/ Din Kültürü 5/6/7 | ✅ DÖGM 2026-27 çerçeve planından (`tools/kazanim_ozel_uret.py`). TYMM sitesindeki DKAB sayfaları kitap + plan + ÖDSGM senaryosuyla çelişiyor; site kullanılmaz. |
| kazanimlar/ İngilizce 7 | ✅ ESKİ program (E7.x.y, 10 ünite), MEB 2026-27 planından. 7. sınıf İngilizce okulda eski programda ve OYSS dışında. |
| Çapraz doğrulama | ✅ `tools/kazanim_capraz_dogrula.py`: 18 ders-sınıf senaryo tablosunun tüm satırları kod+ifade+tema ile tutuyor (tek fark T.Y.5.2 ifade varyantı; program ifadesi esas). Eski↔yeni fark: `evals/KAZANIM-FARK-2026-2027.md`. |
| tema-sirasi.md | ✅ 2026-27 resmî planlardan 5-7 × 6 ders, 1. yazılı sınırı işaretli (`tools/tema_sirasi_uret.py`) |
| beceri-cercevesi.md | ✅ birincil kaynaklardan; yalnız D2/D12 ad eşleşmesi alfabetik çıkarım (dosyada işaretli) |
| Yenileme sırası | `kazanim_html_uret.py` → `kazanim_ozel_uret.py` → `kazanim_capraz_dogrula.py` (0 HATA olmalı) → `kazanim_fark.py` → `--kur` / kopyala → `tema_sirasi_uret.py` → `acik_uclu_kaynak_uret.py` |
| Açık uçlu: senaryolar 5/6/7 | ✅ ÖDSGM 2026-2027 1. dönem konu-soru dağılım tabloları, 6 ders (`tymm-acik-uclu-sinav/references/senaryolar/`) |
| Açık uçlu: program + kitap 5 | ✅ 2026-2027 ünite programları + MEB ders kitabı metinleri, 6 ders; `kitap-dizini.md` tema→sayfa (`tymm-acik-uclu-sinav/references/program/`, `kitap/`). 6-7. sınıfta kitap yok. |

## Kaynaklar

**2026-2027 kaynakları tek merkezde:** `C:\Users\cetin\Projects\MEB-KAYNAK\2026-2027\`
(program, kitap, farklılaştırma, çerçeve, yıllık plan, `07-ortak-sinav` senaryo
tabloları; bkz. oradaki README ve `_KAYNAK.md` dosyaları). Metin çıkarımı LMS
deposunda yapılır (`lms/content-gen/kaynak/`). Açık uçlu becerinin verisi
`python tools/acik_uclu_kaynak_uret.py` ile oradan yeniden üretilir.
`sources/` klasörü 2025-2026 arşividir.

Resmî PDF'ler kullanıcının "TYMM" Google Drive klasöründedir; Claude Code'da
klasör yerel olarak `sources/` altına indirilmiş kabul edilir. Beklenen yapı:
`sources/TEMEL ÖĞRETİM PROGRAMLARI/<branş> <sınıf>. sınıf/...` (tema başına
PDF), kökte çerçeve PDF'leri, `sources/DERS KİTAPLARI/`,
`sources/farklılaştırma etkinlik kitapları/`, `sources/TASLAK YILLIK PLANLAR/`.
PDF → metin: `pdftotext -layout -enc UTF-8`. Türkçe/fen/sosyal kazanım
üretim hattı **depodadır**: `tools/pdf_metin_cikar.py` +
`tools/kazanim_uret.py` (notlar: `tools/README.md` — MAX_PATH, görünmez
U+E000-F8FF karakterleri, `SB 7.1.1.` dizgi toleransı). Matematik için
sohbet geçmişindeki `parse_tema.py` / `gen_mat.py` yaklaşımı: bileşen
imleçleri `a b c ç d e f g ğ h` (ğ dahil!), hece kopmalarını derlem
tabanlı onar ("ya da" gibi meşru ikilileri birleştirme).

## Çalışma döngüsü

Üret → **üç denetim** → bulguyu beceri dosyasına geri yaz:
1. Tetikleme (`evals/tetikleme/tetikleme-seti.csv`);
2. **Katman 1 otomatik:** `python tools/denetim.py <paket>` (mekanik kurallar —
   kod varlığı, puan, hepsi/hiçbiri, denge, sızıntı, yönetmelik ibaresi);
3. **Katman 2 muhakeme:** rubrikle (planlama 14, test 16, açık uçlu 10,
   farklılaştırma 10) işlevsellik/çeldirici/bilimsel doğruluk/katmanlılık.

Ayrıntı ve kural→rubrik eşlemesi: `evals/DENETIM.md`. Sınıfta yakalanan
gerçek hatalar (soğan-kloroplast, "hiçbiri" kayması, katmansız İleri düzey)
Katman 2'den çıkar — otomatik denetim onları göremez. Beceri metnine kural
eklemeden önce kuralın hangi üretim hatasından doğduğunu not et; denetimden
geçmiş referans paketler `ornekler/` altındadır (2025-26 paketleri `ornekler-arsiv-2025-2026/`, kodları eski).

## Yol haritası

1. ~~`test-matematik.md` kurallarını Çoktan Seçmeli Soru Yazım
   Kılavuzu'ndan yeniden yaz~~ ✅ v0.7.1 (`kilavuz-ilkeleri.md` +
   yeniden yazılmış `test-matematik.md`; rubrik T11-T15).
2. ~~`KULLANIM.md` — öğretmenler için örnek promptlar~~ ✅ v0.7.2
   (27 istem: açık/örtük/sınır/kapsam dışı; makine okunur eşi
   `evals/tetikleme/tetikleme-seti.csv` — iki liste birlikte güncellenir).
3. ~~Türkçe → Sosyal kazanım dosyaları (5-6-7), sonra fen tamamlama~~
   ✅ v0.7.3 (57 resmî tema/ünite/alan sayfası ayrıştırıldı; 9 dosya —
   Türkçe süreç bileşenleri hariç, kaynak yayımlamıyor).
4. ~~Tema işleniş sırasını taslak yıllık plan xlsx'lerinden ekle~~
   ✅ v0.7.4 (`references/tema-sirasi.md` — 5-6. sınıf dört branş; 7. sınıf
   sırası kaynakta yok, resmî numara sırası + teyit notu varsayılır).
5. ~~Açık uçlu ortak yazılı sınav becerisi~~ ✅ v0.8.0;
   ~~`tymm-ders-farklilastirma`~~ ✅ v0.8.1 (resmî kılavuz kitap deseni:
   Destekleme + Zenginleştirme, künye + Ek 1/Ek 2);
   ~~2. dönem~~ ✅ v0.7.3 (tüm üniteler);
   **gerçek sınıf denemesi** → öğretmenin adımı: bir paketi sınıfta
   uygula, bulguları rubrikle puanla, beceri dosyasına geri yaz.
