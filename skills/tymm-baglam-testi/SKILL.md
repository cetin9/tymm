---
name: tymm-baglam-testi
description: >
  TYMM'ye hizalı, bağlam temelli çoktan seçmeli test seti üretir: varsayılan
  olarak 10'ar soruluk, zorluk düzeyli 3 test (Düzey 1 Temel / Düzey 2
  Gelişen / Düzey 3 İleri) + ayrı cevap anahtarı; hepsi A4 baskıya hazır
  HTML. Bir öğretmen konu/çıktı için test, tarama testi, yaprak test, deneme
  bölümü veya çoktan seçmeli soru seti istediğinde kullan — sınıf veya konu
  henüz söylenmemiş olsa bile, netleştirme sorusundan ÖNCE yükle. Desteklenen
  branşlar: matematik, Türkçe, fen bilimleri, sosyal bilgiler. Ders planı,
  çalışma kağıdı veya konu anlatımı istekleri için YÜKLEME (tymm-ders-planlama
  becerisinin işi). Tek tek soru çözme, hazır bir testi puanlama veya soru
  tahlili için de YÜKLEME — bunları doğrudan yanıtla.
license: Apache-2.0 (kaynak: anthropics/k12-teacher-skills mimarisinin uyarlaması)
---

# TYMM Bağlam Testi

Tek turda dört belge üretir: `test-duzey-1.html`, `test-duzey-2.html`,
`test-duzey-3.html` ve `test-anahtari.html`. Sayı, düzey adedi veya soru
adedi öğretmence değiştirilebilir; varsayılan 3 × 10'dur.

"Öğretmen", konuştuğun kullanıcıdır. Teknik iç terimler kullanıcıya
görünmez; dipnot standardı `tymm-ders-planlama` ile aynıdır (çıktı kodu ·
sayfa · yapay zekâ bildirimi · varsa doğrulama uyarısı; beceri/sürüm adı
belgelere sızmaz).

---

## Adım 0 — Yönlendirme (sessiz)

0. **Müfredat ve sınav türü durumu.** `../tymm-ders-planlama/references/mufredat-durumu.md`
   dosyasını ŞİMDİ oku. Sınıf düzeyinin hangi müfredata tabi olduğunu ve
   sınav türü kurallarını bu dosya belirler.

   **KRİTİK:** Ortak yazılı sınavlarda çoktan seçmeli soru kullanılamaz
   (MEB Ölçme ve Değerlendirme Yönetmeliği). Bu beceri çoktan seçmeli
   üretir; dolayısıyla:
   - Üretilen her test dosyasına ve öğretmene verilen nota **"alıştırma /
     tarama / deneme amaçlıdır; ortak yazılı sınavda kullanılamaz"** ibaresi
     ZORUNLU olarak eklenir.
   - Öğretmen açıkça **ortak yazılı sınav** için soru isterse, çoktan seçmeli
     ÜRETME. Bu iş `tymm-acik-uclu-sinav` becerisinindir: o beceriyi kullan
     (kuruluysa) veya kural gereği açık uçlu / kısa cevaplı sınav + konu
     soru dağılım tablosu üret. Öğretmene kuralı bir cümleyle açıkla.

1. `references/kilavuz-ilkeleri.md` dosyasını ŞİMDİ oku — resmî TYMM
   Bağlam Temelli Çoktan Seçmeli Soru Yazım Kılavuzu'ndan türetilmiş ortak
   yazım ilkeleri, hata listesi ve yayın öncesi kontrol listesi oradadır.
   Branş dosyasıyla çelişme hâlinde o dosya esastır.
2. Branşı belirle ve branş referansını ŞİMDİ oku — okumadan soru yazmak
   kritik hatadır:
   - **matematik** → `references/test-matematik.md`
   - **türkçe / fen-bilimleri / sosyal-bilgiler** → `references/test-diger-branslar.md`
     (dosya içinde ilgili branş bölümüne git)
3. `references/kazanimlar/` altında sınıf-branş dosyası var mı bak
   (ders-planlama becerisiyle paylaşılan veri). Varsa çıktı eşlemesi
   oradan yapılır ve ifade birebir aktarılır; yoksa en iyi bilgiyle
   ilerlenir ve anahtara doğrulama dipnotu eklenir.

## Adım 1 — Netleştirme (en fazla bir tur, en fazla üç soru)

Öncelik: (1) sınıf düzeyi, (2) konu/çıktı, (3) kapsam tek çıktı mı tema
geneli mi. Varsayılanlar: 3 test × 10 soru, 4 seçenek (A-D), süre önerisi
test başına 20 dk, tek çıktı odağı.

Dönem/yıl tarama testi veya "şu ana kadar işlenenler" kapsamı istenirse
`../tymm-ders-planlama/references/tema-sirasi.md` dosyasından işleniş
sırasına bak — kapsam tema numarasına göre değil bu sıraya göre seçilir.

## Adım 2 — Düzey mimarisi

Her düzey kendi **bağlam ailesinden** beslenir (ör. Düzey 1: market/kantin,
Düzey 2: okul etkinliği, Düzey 3: üretim/planlama problemi) — üç test aynı
senaryonun kopyası olmaz. Düzey içi kademe dağılımı:

| Düzey | KB1 | KB2 | KB3 | Karakter |
|-------|-----|-----|-----|----------|
| 1 — Temel | 6 | 3 | 1 | Kuralı tanıma ve tek adımlı uygulama |
| 2 — Gelişen | 3 | 5 | 2 | İlişkilendirme, iki adımlı bağlam problemleri |
| 3 — İleri | 1 | 4 | 5 | Muhakeme, karşı örnek, kural sınırları |

Aynı kavram üç düzeyde de yoklanır; değişen şey bağlamın soyutluğu ve adım
sayısıdır. Düzeyler etiketiyle basılır; öğrenciye "kolay/zor" değil
"Temel/Gelişen/İleri" dili kullanılır.

**Bağlam zenginliği düzeye göre ölçeklenir** (ayrıntı: `kilavuz-ilkeleri.md`
§5). Temel'de tek veri, en kısa bağlam. Gelişen'de en az iki veri
birleştirilir. **İleri'de katmanlı bağlam zorunludur:** öğrencinin
ayıklaması gereken, işe yaramayan/çeldirici veri de içeren zengin bağlam
kurulur — MEB örnek soruları bu yüzden uzundur ve bu doğrudur. İleri düzey
soruları fazla kısa/tek adımlı kalıyorsa yeniden yazılır. Uzunluk düzey
etiketiyle değil, ölçülen düşünme adımıyla artar. Gerektiğinde **bağlam
seti** kullan: tek zengin bağlamdan 2-3 bağımsız soru (ipucu zinciri
yasağıyla).

## Adım 3 — Soru yazım kuralları

Ayrıntısı `references/kilavuz-ilkeleri.md` dosyasındadır; aşağıdakiler
üretim sırasında sürekli açık tutulan çekirdektir.

- **İşlevsellik testi (her soru için):** "Öğrenci bağlamı incelemeden,
  yalnızca ön bilgisiyle veya seçeneklerden giderek bu soruyu
  cevaplayabilir mi?" Cevap evetse bağlam ve/veya soru yeniden kurgulanır.
  Ters yönü de hatadır: çözüm için gereken **her bilgi bağlamda açıkça
  verilirse** soru okuduğunu anlamayı ölçer.
- **Soru bir çıktıya değil, çıktının bir süreç bileşenine yazılır**
  (a, b, c, ç…); hedef bileşen anahtarda belirtilir.
- **Kökte konu anlatımı, kural hatırlatması veya öznel kalıp
  ("sizce") yok;** çift olumsuzluk yok.
- **İpucu zinciri yok:** aynı bağlamdan yazılan sorular birbirinden
  bağımsız çözülebilmelidir ("Bir önceki soruda bulduğunuz…" yasak).
- **Seçenekler homojen:** kelime sayısı, uzunluk, dil yapısı ve sayı
  biçimi benzer; doğru seçenek uzun/detaylı olamaz. Bağlamdaki bir ifade
  seçeneğe birebir kopyalanmaz, anlamca karşılığı yazılır.
- **Görsel metni tekrar etmez, yeni veri sunar;** grafikler iki boyutlu,
  sade ve net etiketli olur. Bağlam ile ona bağlı sorular aynı sayfada
  durur.
- **Erişilebilir ve tarafsız bağlam:** dar erişimli alanlar (borsa, golf,
  marka, gelir varsayan senaryolar) ve kültür/cinsiyet/bölge/din/ideoloji
  bakımından taraflı kurgular kullanılmaz.
- **Her soru bağlama bağlıdır:** kök, gerçek yaşam durumundan gelir; "Salt
  işlem: 738 ÷ 6 = ?" tarzı bağlamsız kök yazılamaz. Bağlam işlevseldir —
  bir cümlelik süs bağlam ("Ali'nin 738 kurabiyesi var") KB1'de kabul,
  KB2-3'te karar/yorum gerektiren bağlam zorunludur.
- **Kavram izlenebilirliği:** soruda adlandırılan kavramlar, hedef çıktının
  ifadesi + branş dosyasında tanımlı dolgu kavram listesiyle sınırlıdır;
  liste dışı kavram kullanan soru yeniden yazılır.
- **Çeldiriciler yanılgıdan türetilir:** her sorunun en az iki çeldiricisi,
  branş dosyasındaki yanılgı envanterinden gelir ve anahtar belgesinde
  hangi yanılgıyı yakaladığı etiketlenir. Rastgele-yanlış çeldirici en çok
  bir tanedir.
- **Tek doğru cevap; "hepsi/hiçbiri" seçeneği yasak;** olumsuz kök
  ("hangisi DEĞİLDİR") test başına en çok 2 ve büyük harfle vurgulu.
- **Seçenek dengesi:** 10 soruluk testte hiçbir harf 4'ten fazla veya
  1'den az doğru olamaz; sayısal seçenekler artan sırada dizilir. Anahtar
  yazıldıktan sonra dağılımı say ve gerekirse seçenek yerlerini değiştir.

## Adım 4 — Çıktı üretimi

A4 şablon kuralları geçerlidir (`tymm-ders-planlama` ile aynı şablon
ailesi): soru blokları sayfa sonunda bölünmez, her test kendi dosyasında,
üstte sınıf/çıktı/süre bilgisi ve öğrenci ad satırı. Her test dosyasının
dipnotunda "Alıştırma ve deneme amaçlıdır; ortak yazılı sınavda çoktan
seçmeli soru kullanılamaz." ibaresi bulunur. Öğrenci test
dosyalarına anahtar belgesine ait hiçbir parça — içerik, tablo VEYA stil
tanımı — kopyalanmaz; her dosya yalnızca kendi kullandığı stilleri taşır.
**Anahtar daima ayrı dosyadadır** ve şunları içerir: düzey × soru × doğru harf tablosu; soru
başına hedef çıktı + **süreç bileşeni harfi** ve kademe (KB) etiketi; soru
başına bağlam adı; çeldirici → yanılgı eşleme tablosu; seçenek dağılım
sayımı; gerçek veri kullanıldıysa kaynak satırı; puanlama önerisi (soru
başına 10 puan).

Belgeleri teslim etmeden önce `kilavuz-ilkeleri.md` §6 kontrol listesini
tüm sorulara uygula; karşılanmayan madde varsa soruyu yeniden yaz.

## Kapsam dışı

Açık uçlu yazılı soruları, ders planı/çalışma kağıdı (tymm-ders-planlama),
mevcut testin tahlili veya puanlaması.
