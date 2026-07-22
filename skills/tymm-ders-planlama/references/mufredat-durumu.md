# Müfredat Geçiş Durumu ve Sınav Türü Kuralları

**Her iki beceri de (ders-planlama, bağlam-testi) plan/test üretmeden önce
bu dosyayı okumak zorundadır.** Sınıf düzeyi, hangi müfredatın ve hangi
terminolojinin kullanılacağını belirler.

---

## 1. TYMM kademeli geçiş — hangi sınıf hangi müfredatta?

TYMM ortaokula kademeli olarak uygulanmaktadır. **2026-2027 öğretim yılı
durumu (öğretmen tarafından teyit edilmiştir):**

| Sınıf | Müfredat | Terminoloji | Kod deseni |
|-------|----------|-------------|------------|
| 5 | **TYMM** | Öğrenme çıktısı + süreç bileşenleri | `FB.5.1.1.1` (4 parçalı) |
| 6 | **TYMM** | Öğrenme çıktısı + süreç bileşenleri | `FB.6.1.1.1` (4 parçalı) |
| 7 | **TYMM** (2026-27'de geçti) | Öğrenme çıktısı + süreç bileşenleri | `FB.7.1.1.1` (4 parçalı) |
| 8 | **Eski program** | Kazanım | `F.8.1.1.1` (nokta öncesi tek harf) |

> **NOTLAR:**
> - `kazanimlar/` klasöründe 5-6-7. sınıf **dört branşın** (matematik,
>   Türkçe, fen, sosyal) verisi resmî tema/ünite sayfalarından birebir
>   mevcuttur. Türkçe dosyalarında süreç bileşeni dökümü yoktur (resmî
>   tema sayfaları yayımlamaz); Türkçe'de süreç bileşeni gerektiğinde
>   doğrulama notu düşülür.
> - 8. sınıf eski programdadır: "öğrenme çıktısı" değil **"kazanım"** denir,
>   süreç bileşeni katmanı zorlanmaz, LGS hazırlık bağlamı geçerli olabilir.
> - 2027-2028'de 8. sınıfın da geçmesi beklenir; o yıl bu tablo yeniden
>   teyit edilmelidir (son teyit: Temmuz 2026).

### Beceri davranışı sınıfa göre
- **5-6. sınıf:** Tam TYMM üretimi — öğrenme çıktısı + süreç bileşenleri +
  alan becerisi/KB/eğilim/SDB/değer/okuryazarlık katmanları.
- **7-8. sınıf (eski programdaysa):** "Öğrenme çıktısı" değil **"kazanım"**
  denir; süreç bileşeni katmanı ZORLANMAZ (eski programda yoktur). Beceri
  temelli katmanlar (KB, eğilim, SDB) plana eklenebilir ama TYMM koduyla
  etiketlenmez. Plana şu not düşülür: *"Bu sınıf düzeyi [tarih] itibarıyla
  eski öğretim programına tabidir; güncel durumu teyit ediniz."*
- Farklı sınıf düzeylerinden iki müfredatı **karıştırmak kritik hatadır.**

---

## 2. Sınav türü kuralı — ÇOK ÖNEMLİ

MEB Ölçme ve Değerlendirme Yönetmeliği ve konu soru dağılım tablolarının
resmî açıklamasına göre, **okul genelinde uygulanan ortak yazılı sınavlar**:

> Açık uçlu veya açık uçlu + kısa cevaplı sorulardan oluşacak şekilde
> yapılır. **Çoktan seçmeli, eşleştirme, doğru/yanlış gibi diğer soru türleri
> kesinlikle kullanılmaz.**

Ayrıca ortak yazılı sınav soruları, zümrenin seçtiği bir **konu soru dağılım
tablosu senaryosuna** göre hazırlanır (hangi çıktıdan kaç soru sorulacağı
önceden öğrenciyle paylaşılır).

### Bunun becerilere yansıması
- `tymm-baglam-testi` çoktan seçmeli üretir → çıktısı **ortak yazılı sınav
  olarak kullanılamaz.** Beceri, ürettiği test setinin üstüne ve öğretmene
  verdiği notta şunu belirtmek zorundadır: *"Bu testler alıştırma, tarama ve
  deneme amaçlıdır; ortak yazılı sınavlarda çoktan seçmeli soru
  kullanılamaz."*
- Öğretmen **ortak yazılı sınav** için soru isterse: çoktan seçmeli
  üretilmez; bu iş `tymm-acik-uclu-sinav` becerisinindir (konu soru
  dağılım tablosu + açık uçlu sınav + dereceli puanlama anahtarı). Beceri
  kurulu değilse aynı kurallarla açık uçlu / kısa cevaplı sınav üretilir.
- Ders planlarındaki değerlendirme önerileri de bu ayrımı gözetir: sınıf içi
  ölçme araçları (çalışma kâğıdı, grid, tanılayıcı dallanmış ağaç, kontrol
  listesi, dereceli puanlama anahtarı) serbesttir; **ortak yazılı** söz
  konusuysa açık uçlu/kısa cevaplı kuralı hatırlatılır.

---

## 3. Süreç bileşeni yapısı (TYMM sınıfları)

Öğrenme çıktısının altındaki a) b) c) ç) d) maddeleri **süreç bileşenidir**
ve resmî programda tanımlıdır — beceri bunları uydurmaz, kazanım
dosyasından birebir alır. Dosyada yoksa, en yakın ifadeyle ilerler ve
doğrulama uyarısı düşer.

Ölçme ve gözlem odakları daima bu bileşenlere bağlanır; çıkış kartı,
gözlem formu ve dereceli puanlama anahtarı ölçütleri bileşenlerden türetilir.
