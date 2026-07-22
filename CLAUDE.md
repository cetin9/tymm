# CLAUDE.md — TYMM Öğretim Becerileri Proje Anayasası

Bu depo, Anthropic'in açık kaynak **k12-teacher-skills** mimarisinin (Apache 2.0)
Türkiye Yüzyılı Maarif Modeli'ne (TYMM) uyarlamasıdır. Kullanıcı (Çetin)
İstanbul'da bir eğitimci; hedef kitle TYMM ile çalışan ortaokul öğretmenleridir.
Tüm çıktılar ve iletişim Türkçedir.

## Beceriler

- `skills/tymm-ders-planlama/` — ders planı + çalışma kağıdı/kağıtları +
  öğrenme kanıtları + isteğe bağlı etkileşimli konu anlatımı (A4/ekran HTML)
- `skills/tymm-baglam-testi/` — düzeyli (Temel/Gelişen/İleri) bağlam temelli
  çoktan seçmeli test setleri + ayrı cevap anahtarı

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

## Veri durumu (v0.7.1)

| Veri | Durum |
|------|-------|
| Matematik 5/6/7 | ✅ resmî tema sayfalarından birebir (23/24/30 çıktı; süreç bileşenleri dahil; sınıf başına 172 tema-saat + 8 okul temelli = 180) |
| Fen 5 (Ü1-3), Fen 6 (Ü1-4) | ✅ doğrulandı (1. dönem); kalan üniteler eksik |
| Türkçe 6, Sosyal 6 | ⚠️ doğrulanmamış — resmî temalardan yeniden kurulacak |
| Türkçe/Sosyal 5 ve 7 | ❌ yok |
| beceri-cercevesi.md | ✅ birincil kaynaklardan; yalnız D2/D12 ad eşleşmesi alfabetik çıkarım (dosyada işaretli) |

## Kaynaklar

Resmî PDF'ler kullanıcının "TYMM" Google Drive klasöründedir; Claude Code'da
klasör yerel olarak `sources/` altına indirilmiş kabul edilir. Beklenen yapı:
`sources/TEMEL ÖĞRETİM PROGRAMLARI/<branş> <sınıf>. sınıf/...` (tema başına
PDF), kökte çerçeve PDF'leri, `sources/DERS KİTAPLARI/`,
`sources/farklılaştırma etkinlik kitapları/`, `sources/TASLAK YILLIK PLANLAR/`.
PDF → metin: `pdftotext -layout`. Matematik tema ayrıştırıcısı örneği için
sohbet geçmişindeki `parse_tema.py` / `gen_mat.py` yaklaşımı esas alınabilir:
sayfa üstbilgilerini temizle, "Öğrenme Çıktıları ve Süreç Bileşenleri" →
"İçerik Çerçevesi" arasını al, `MAT.x.y.z` üzerinden böl, bileşen imleçleri
`a b c ç d e f g ğ h` (ğ dahil!), hece kopmalarını derlem tabanlı onar
("ya da" gibi meşru ikilileri birleştirme).

## Çalışma döngüsü

Üret → `evals/` altındaki rubrikle puanla (planlama M01-M14, test T01-T10) →
bulguyu beceri dosyasına geri yaz. Beceri metnine kural eklemeden önce kuralın
hangi üretim hatasından doğduğunu not et.

## Yol haritası

1. ~~`test-matematik.md` kurallarını Çoktan Seçmeli Soru Yazım
   Kılavuzu'ndan yeniden yaz~~ ✅ v0.7.1 (`kilavuz-ilkeleri.md` +
   yeniden yazılmış `test-matematik.md`; rubrik T11-T15).
2. ~~`KULLANIM.md` — öğretmenler için örnek promptlar~~ ✅ v0.7.2
   (27 istem: açık/örtük/sınır/kapsam dışı; makine okunur eşi
   `evals/tetikleme/tetikleme-seti.csv` — iki liste birlikte güncellenir).
3. Türkçe → Sosyal kazanım dosyaları (5-6-7), sonra fen tamamlama.
4. Tema işleniş sırasını taslak yıllık plan xlsx'lerinden ekle.
5. Açık uçlu ortak yazılı sınav becerisi; `tymm-ders-farklilastirma`
   (resmî farklılaştırma etkinlik kitaplarından); 2. dönem; gerçek sınıf
   denemesi.
