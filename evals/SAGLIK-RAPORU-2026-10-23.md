# Veri sağlık raporu: kazanım · tema · senaryo · kitap · plan (23 Ekim 2026, son durum)

Kapsam: 5-6-7. sınıf; Türkçe, Matematik, Fen, Sosyal, Din Kültürü, İngilizce.

## 1. Karşılaştırma sonuçları

| # | Karşılaştırma | Araç | Sonuç | Durum |
|---|---|---|---|---|
| 1 | Kazanım ↔ ÖDSGM senaryo (kod, TAM cümle, tema) | `kazanim_capraz_dogrula.py` | **0 hata.** 251 satırın 245'i birebir; 5'i MEB tablosundaki yazım hatası (kazanım doğru); 1'i onaylı fark (T.Y.5.2) | ✅ |
| 2 | Kazanım ↔ tam program PDF'i (kod listesi) | noktasız/boşluklu yazımları da tanıyan tarama | Türkçe, Mat, Fen, Sosyal, İngilizce 5-6: PDF'teki **her kod** kazanımda var. Bu tarama sırasında 2 hata bulunup düzeltildi (aşağıda) | ✅ |
| 3 | Kazanım ↔ yıllık plan (kodlar) | aynı araç | Plandaki bütün kodlar kazanımda var | ✅ |
| 4 | Kitap ↔ plan (tema sırası) | numaralı ünite başlıkları | 18/18 aynı | ✅ |
| 5 | Kitap ↔ plan (Türkçe metin sırası) | metin başlıkları + içindekiler sayfası | 5-6-7 aynı; bulunamayanlar yalnız dinleme/izleme metinleri (kitapta basılı değil) | ✅ |
| 6 | Kitap ↔ kazanım (çıktı cümleleri) | `kitap_kazanim_karsilastir.py` | Din 5-6 18/18; Fen 6-7 ve Sosyal 6-7 çoğu birebir. Bilinen farklar onaylandı (§2) | ✅ (onaylı) |
| 7 | Kitap ↔ program (İngilizce söz varlığı) | `ingilizce_sozcuk_uret.py` | Kitabın tema sayfaları program hedef sözcüklerinin %44-71'ini kullanıyor → tema başına "güvenli sözcük" listesi üretildi | ✅ (önlem alındı) |
| 8 | Her senaryo: çıktılar sınavdan önce işleniyor mu, kitapta yeri var mı | `senaryo_kartlari_uret.py` | 180 senaryo, 932 satır; 930 ✓, 2 ⚠ (Din 6, DKAB.6.2.1); kitap aralığı 932/932 | ✅ (1 bilinen uyarı) |
| 9 | Kitap dizini otomatik ↔ elle (5. sınıf) | `kitap_dizini_uret.py` | 6/6 ders aynı (±2 sayfa kapak farkı) | ✅ |

## 2. Bu turda bulunup düzeltilen hatalar

| Hata | Nasıl bulundu | Düzeltme |
|---|---|---|
| 5. sınıf İngilizce **7. tema (Life in Nature) tümüyle eksikti**: sitede kodlar "ENG5.7.L1" diye noktasız | Plan verisi tamamlanınca çapraz doğrulama "plan kodu kazanımda yok" dedi | Ayrıştırıcı noktasız kodu tanıyor; 23 çıktı eklendi |
| ENG.5.7.R3 ve ENG.5.8.R4 eksikti: sitede "ENG.5.7. R 3." gibi boşluklu yazım | PDF ile kod kod karşılaştırma | Kod içi boşluklar birleştiriliyor; 184/184 |
| Doğrulama aracı ifadenin yalnız ilk 60 karakterine bakıyordu | Kitap karşılaştırmasında fiil farkı fark edildi | Tam cümle karşılaştırması |
| LMS plan verisi: "SB 7.1.1" okunmuyordu, Sosyal'de konu sütunu boştu, İngilizce 7-8 kodları yoktu, bazı satırlar sütun kaymıştı | Senaryo ↔ plan kontrolü | `lms/apps/web/scripts/yillik-plan-tamamla.py` (yalnız boş hücreler, resmî xlsx'ten) |
| Din 6, 5. ünite adı planda farklı | Kitap ↔ plan | Kitaptaki ad esas: "Kültürümüzdeki Dinî Motifler" |

## 3. Onaylanan kararlar (öğretmen, 23.10.2026)

- **T.Y.5.2:** program ifadesi ("…teknik seçimlerini…").
- **Sosyal 5 ve Fen 5'teki kitap–program ifade farkları:** sınavda program ifadesi, içerik kitaptan.
- **DKAB.6.2.1:** sınav haftasında başlıyor; zümre Senaryo 1 ve 4'ü seçerken bilmeli.
- **DKAB kaynağı:** DÖGM planı.
- **Okul zümre planı:** MEB çerçeve planıyla aynı kabul edilir.
- **İl:** İstanbul.
- **İngilizce 7 kitabı:** EBA'dan indirilen dosya elimizdekiyle bayt bayt aynı; resmî.

## 4. Açık kalanlar

| Konu | Durum | Ne yapılacak |
|---|---|---|
| 2. yazılı takvimi | Yayımlanmadı | 18 Ocak 2027 haftası varsayıldı (7. sınıf Türkçe resmî: 5 Ocak). Takvim çıkınca tarih girilip araçlar yeniden çalıştırılır |
| Ülke geneli konu-soru tabloları (6 Mat 1. yazılı, 7 Türkçe 2. yazılı) | Yayımlanmadı | Kılavuzla gelince eklenir |
| MEBİ "Yazılıya Hazırlanıyorum" serisi | Yalnız Din 5 eklendi (kullanıcı indirdi) | Diğer derslerin PDF'leri MEBİ'den indirilirse aynı yere eklenir |

## 5. Eklenen kaynaklar (23.10.2026, akşam)

- TYMM Kılavuzlar menüsündeki 10 belgenin hepsi indirildi: Program Okuryazarlığı 1-6. Modül (5. Modül iki parça) ve veli/öğrenci kılavuzları (`MEB-KAYNAK/2026-2027/04-cerceve/kilavuzlar/`).
- 5. Modül'ün açık uçlu soru, puanlama ve dereceli puanlama hükümleri skill'e işlendi (`references/olcme-ilkeleri.md`). Bağlamda "gereksiz ayrıntı olmamalı" kuralı, çoktan seçmeli kılavuzun "katmanlı bağlam" kuralının önüne alındı.
- Performans Gelişim Çerçevesi: bağlantı sitede yorum satırında, yani gizli; belge yayımlanmamış. Listeden çıkarıldı.
