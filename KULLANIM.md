# KULLANIM — Öğretmenler için istem rehberi

Bu belge, TYMM öğretim becerilerini (ders paketi, bağlam testi, ortak
yazılı, farklılaştırma) kurmuş bir öğretmenin Claude'a **nasıl istek
yazacağını** örneklerle gösterir.
Kurulum için `README.md`'ye bakın.

Buradaki örnek istemler aynı zamanda becerilerin tetikleme testlerinin
(doğru beceri doğru anda devreye giriyor mu?) veri setidir; makine
tarafından okunan kopyası `evals/tetikleme/tetikleme-seti.csv`
dosyasındadır. **İki liste birlikte güncellenir.**

---

## 1. Hızlı başlangıç

En kısa iyi istem iki bilgi taşır: **sınıf + konu.**

> *"6. sınıf, bölünebilme kuralları — ders planı hazırlar mısın?"*

Gerisi sorulmadan makul varsayılanlarla doldurulur ve varsayımlar belgede
görünür yazılır:

| Bilgi | Söylemezseniz varsayılan |
|---|---|
| Süre | 2 ders saati (2 × 40 dk) |
| Çalışma kağıdı sayısı | 1 (100 puanlık, kademeli) |
| Konu anlatımı belgesi | Üretilmez (isterseniz eklenir) |
| Test yapısı | 3 düzey × 10 soru, 4 seçenek |
| Sınıf profili | Tam sınıf erişimi, kitap bağımsız |

Eksik bilgi çoksa Claude **tek mesajda en fazla üç soru** sorar, sonra
üretime geçer — soru yağmuruna tutulmazsınız.

---

## 2. Ders paketi istemek (`tymm-ders-planlama`)

Çıktısı: öğretmene dönük **ders planı** + öğrenciye dönük **çalışma
kağıdı** + **öğrenme kanıtları** (cevap anahtarı ve gözlem odakları).
Üçü de A4 baskıya hazır ayrı belgelerdir.

### Açık istekler — doğrudan söylersiniz

| # | Örnek istem |
|---|---|
| DP01 | 6. sınıf matematikte bölünebilme kuralları için ders planı hazırlar mısın? |
| DP02 | Yarınki derse günlük plan lazım: 6. sınıf Türkçe, hikâye unsurları, 2 ders saati. |
| DP03 | Güneş sistemi konusunda etkinlik planı ve çalışma kağıdı istiyorum, 6. sınıf fen. |
| DP04 | 5. sınıf çarpma işlemi: plan + 2 çalışma kağıdı olsun, ikincisi eve ödev. |
| DP05 | Bölünebilme planına akıllı tahtada açacağım bir konu anlatımı da ekler misin? |

### Örtük istekler — plan demeseniz de anlaşılır

Öğretmen niyeti yeterlidir; "plan" kelimesi geçmese de ders paketi
hazırlanır:

| # | Örnek istem |
|---|---|
| DP06 | Yarın 6'larda çarpanlar ve katları işleyeceğim. |
| DP07 | Pazartesi ışığın yansımasını anlatacağım, elimde hiçbir materyal yok. |
| DP08 | Sosyal bilgilerde İslam medeniyeti konusuna giriyorum, sınıfa ne götürsem? |
| DP09 | Kesirlerde sıralamayı bir türlü kavratamadım, haftaya baştan alacağım. |

### İsteğe bağlı seçenekler

- **2-3 çalışma kağıdı:** kopya değil, amaç ayrışması — ders içi / ev
  pekiştirmesi / karışık tekrar.
- **Konu anlatımı belgesi:** ekran/akıllı tahta için etkileşimli sayfa;
  gömülü görseller ve anında dönütlü alıştırmalar içerir, video linki
  içermez (video köşesine kendi linkinizi yapıştırırsınız).
- **Farklılaştırma zaten içindedir:** destekleme ve zenginleştirme her
  planın standart bölümüdür, ayrıca istemeniz gerekmez.

---

## 3. Test istemek (`tymm-baglam-testi`)

Çıktısı: **Temel / Gelişen / İleri** üç düzeyde 10'ar soruluk bağlam
temelli çoktan seçmeli testler + **ayrı** cevap anahtarı (yanılgı
etiketleri ve puanlamayla). Düzey adedi ve soru sayısı değiştirilebilir.

### Açık istekler

| # | Örnek istem |
|---|---|
| T01 | Bölünebilme kurallarından üç düzeyli test seti hazırla, 6. sınıf. |
| T02 | Kesirler konusundan 10 soruluk çoktan seçmeli tarama testi. |
| T03 | Işık ünitesinden yaprak test istiyorum. |
| T04 | 6. sınıf sosyalden deneme bölümü gibi 10 soru, cevap anahtarı ayrı olsun. |

### Örtük istekler

| # | Örnek istem |
|---|---|
| T05 | Konuyu bitirdik, çocukları bir yoklamak istiyorum — soru seti hazırlar mısın? |
| T06 | Öğrencilerimin bölünebilmede hangi düzeyde olduğunu görmek istiyorum. |

### ⚠️ Ortak yazılı sınav kuralı

MEB yönetmeliğine göre **ortak yazılı sınavlarda çoktan seçmeli soru
kullanılamaz.** Bu yüzden ürettiğimiz her test *"alıştırma/tarama/deneme
amaçlıdır"* ibaresi taşır; ortak yazılı için aşağıdaki ayrı beceri devreye
girer.

## 3b. Ortak yazılı istemek (`tymm-acik-uclu-sinav`)

Çıktısı: **konu soru dağılım tablosu** (sınavdan önce öğrenciyle
paylaşılır) + **açık uçlu/kısa cevaplı sınav kağıdı** + **dereceli
puanlama anahtarı** (örnek yanıtlar ve kısmi puan basamaklarıyla).

| # | Örnek istem |
|---|---|
| A01 | 6. sınıf matematik 1. dönem 2. ortak yazılısını hazırla; kapsam ilk 9 hafta. |
| A02 | Fen 5 için Ü1-Ü2'den açık uçlu yazılı + puanlama anahtarı istiyorum. |

## 3c. Farklılaştırma istemek (`tymm-ders-farklilastirma`)

Mevcut bir dersi/kağıdı veya konuyu resmî yaklaşımla iki yönde açar:
**Destekleme** (somut örnek, materyal, akran desteğiyle aynı hedefe
ulaştırma) ve **Zenginleştirme** (içerik çerçevesi içinde derinleştirme).
Çıktı, resmî Farklılaştırma Etkinlikleri Kılavuz Kitabı desenindedir
(etkinlik künyesi + Ek 1 öğrenci sayfası + Ek 2 değerlendirme).

| # | Örnek istem |
|---|---|
| F01 | Bu çalışma kağıdını sınıfımdaki seviye farkına göre farklılaştırır mısın? |
| F02 | Bölünebilme konusunda hızlı bitirenlere zenginleştirme etkinliği lazım. |
| F03 | Kesirlerde zorlanan öğrencilerim için destekleme etkinliği hazırla. |

Not: "Üç düzeye ayır" derseniz resmî yapı korunur — destekleme sürümü +
ana materyal + zenginleştirme sürümü üçlüsü sunulur; "kolay/orta/zor"
etiketi kullanılmaz.

---

## 4. Bilmeniz gereken sınır durumları

| # | Durum | Ne olur |
|---|---|---|
| S01 | *"Ortak yazılı için matematikten 10 çoktan seçmeli soru hazırla."* | Çoktan seçmeli üretilmez; kural bir cümleyle açıklanır ve `tymm-acik-uclu-sinav` ile açık uçlu paket üretilir. |
| S02 | *"8. sınıf üslü ifadelerden test."* | 8. sınıf eski programdadır: "öğrenme çıktısı" değil **kazanım** dili kullanılır, belgeye teyit notu düşülür. |
| S03 | *"7. sınıf Türkçe temasından süreç bileşenlerine bağlı ölçme."* | Türkçe'nin resmî tema sayfaları süreç bileşeni dökümü yayımlamaz; çıktı düzeyinde üretilir, süreç bileşeni gerekiyorsa belgeye doğrulama notu düşülür. |
| S04 | *"İngilizce 5. sınıf için ders planı."* | Desteklenmeyen branş (matematik, Türkçe, fen, sosyal dışı): açıkça söylenir, beceri dışında elden gelen yardım yapılır. |
| S05 | *"Test istiyorum."* (sınıf/konu yok) | Beceri yine devreye girer; tek mesajda en fazla üç netleştirme sorusu sorulur. |
| S06 | Ders paketi hazırlanırken *"bir de test olsun"* derseniz | İki iş ayrı becerilerle sırayla yapılır; ikisini tek istemde de isteyebilirsiniz. |

## 5. Kapsam dışı istekler

Bunlarda beceriler devreye **girmez** — Claude yine yardım eder ama
normal sohbet olarak:

| # | Örnek istem | Neden kapsam dışı |
|---|---|---|
| K01 | MAT.6.1.2'nin süreç bileşenleri neler? | Salt çıktı sorgusu; doğrudan yanıtlanır. |
| K02 | Şu soruyu çözer misin: 738 sayısı 4'e bölünür mü? | Tek soru çözümü. |
| K03 | Elimdeki 10 soruluk testi analiz et, hangi sorular zayıf? | Hazır testin tahlili/puanlaması. |
| K04 | Sınav puanlarından dönem sonu ortalamalarını hesaplar mısın? | Not verme/hesaplama; doğrudan yanıtlanır. |
| K05 | Sınıfım için yıllık plan çıkarır mısın? | Yıllık plan/zümre evrakı beceri kapsamında değil. |
| K06 | Veli toplantısı daveti yazar mısın? | Evrak işi. |

---

## 6. Daha iyi sonuç için ipuçları

- **Çıktı kodunu biliyorsanız yazın** (`MAT.6.1.2` gibi) — eşleme
  netleşir. Bilmiyorsanız konu adı yeter; kod programdan bulunur.
- **Amacı söyleyin:** "ders içi mi, ödev mi, dönem tekrarı mı" — kağıt ve
  soru kurgusu buna göre değişir.
- **Sınıfınıza özgü durumu ekleyin:** "işlem hızı düşük bir grubum var",
  "bu konuya 1 saat ayırabildim" gibi notlar plana yansır.
- Her belgenin dipnotunda *"Yapay zekâ desteğiyle hazırlanmıştır;
  uygulamadan önce öğretmen incelemesi gerekir."* yazar — basmadan önce
  gözden geçirmek her zaman sizin adımınızdır.
