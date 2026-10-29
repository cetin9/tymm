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
license: "Apache-2.0 (kaynak: anthropics/k12-teacher-skills mimarisinin uyarlaması)"
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

### Yaşamla bağ ilkesi: "Bu ne işimize yarayacak?" (öğretmen isteği, 29.10.2026)

Öğrencilerin yıllardır sorduğu "Öğretmenim, bu ne işimize yarayacak, nerede
kullanacağız?" sorusuna sorunun kendisi cevap verir. Soru, öğrencinin bilgiyi
gerçek hayatta karşılaşabileceği bir durumda **kullanıp kullanamadığını** ölçer.
Dayanak: Maarif Modeli'nin bağlam ve beceri temelli ölçme anlayışı (5. Modül
§5.4.17) ve bağlam temelli soru yazım kılavuzu. Bu ilke bağlam kurallarının
yerine geçmez, onları yönlendirir.

1. **Önce yaşam haritası.** Soru yazmadan önce konunun kısa bir yaşam
   haritasını çıkar: bu bilgi ya da beceri 10-13 yaşındaki bir öğrencinin
   hayatında nerede karşısına çıkar? Örnek alanlar: ev ve mutfak, okul,
   oyun ve spor, alışveriş ve para, yolculuk ve trafik, doğa ve hava,
   sağlık ve güvenlik, teknoloji, aile işleri. En az üç gerçek durum yaz.
   Her biri için şunu cevapla: "Bu bilgiyi bilmeyen kişi o durumda neyi
   yapamaz ya da neyi yanlış yapar?" Cevabı güçlü olan durumlar soruya dönüşür.
2. **Bağlam bilgiyi kullandırır, süslemez.** Öğrenci durumda bir karar
   verir, bir sorunu çözer, bir öneriyi ya da iddiayı değerlendirir, bir
   hatayı fark eder ya da bir sonucu tahmin eder. Bağlam çıkarılınca soru
   anlamsızlaşmalı, bilgi çıkarılınca da çözülememelidir (işlevsellik
   testi). "Ali'nin 3/7 pizzası var" gibi süs bağlam bu ilkeyi karşılamaz.
3. **Gerçekçilik.** İnsanların gerçekten yaptığı işi kur: telefonun şarj
   göstergesini okumak, tarifteki ölçüyü ayarlamak, kaygan zeminde önlem
   almak, iki seçenekten daha uygununu seçmek. Sayılar, ölçüler, süreler ve
   fiyatlar makul olur. Durum öğrencinin tanıdığı bir çevrededir: ev, okul,
   mahalle, park, market, otobüs. Dar erişimli ya da gelir varsayan
   durumlar kullanılmaz (bağlam erişilebilirlik kuralı).
4. **Cevap durumdaki kişiye işe yarar.** Sorunun sonucu, o kişiye bir şey
   kazandırır: doğru seçimi yapar, kazayı önler, israfı azaltır, zamanı
   doğru planlar. Öğrenci cevabı bulunca "Demek bunun için öğreniyormuşuz."
   diyebilmelidir.
5. **Zorlama yok.** Konunun doğal bir yaşam karşılığı yoksa ya da bağlam
   yalnız süs olacaksa yaşam durumu uydurulmaz. O soru şu iki yoldan biriyle
   yazılır: (a) bilginin bilimdeki ya da matematikteki iç kullanımını
   gösteren bir problem durumu (deney, model, örüntü, gözlem); (b) sade ve
   net bir soru. Anahtarda "Yaşamla bağ: yok (gerekçe)" yazılır.
   Zorlanmış bir yaşam bağlamı, bağlamsız sorudan daha kötüdür.
6. **Kitapla uyum.** Kitabın konuyu bağladığı yaşam durumlarını izle (kitap
   sayfasını anahtara yaz), ama kitabın örneğini kopyalama. Kişi, sayı ve
   durum değiştirilir. Kavramlar kitabın adlandırmasıyla sınırlıdır.
7. **Kayıt.** Anahtarda her soru için tek cümlelik bir "Yaşamla bağ:"
   satırı bulunur. Bu satır durumu ve bilginin o durumda ne işe yaradığını
   söyler (ör. "Yaşamla bağ: Kaygan zeminde ayakkabı tabanının
   desenine bakmak; sürtünmeyi artıran taban kaymayı önler."). Öğretmen bu
   satırı sınıfta "Ne işe yarar?" sorusuna cevap olarak kullanabilir.
8. **Denetimde yeri.** Teslimden önce her soruya iki soru sorulur: "Bu
   durum gerçekte olur mu, öğrenci tanır mı?" ve "Bilgiyi bilmek bu durumda
   gerçekten fark yaratıyor mu?" İkisinden birinin cevabı hayırsa soru
   yeniden kurgulanır ya da 5. maddeye göre yaşam bağlamsız yazılır.
9. **Pilot dersleri (29.10.2026, kör incelemeden).** (a) Karar soran sorularda doğru şık biçimce ayrışmaz: sonuçlar ("binebilir/binemez", "alır/almaz") seçeneklere ikişer dağıtılır, bir çeldirici "sonuç doğru, gerekçe yanlış" olur. (b) Çeldiricinin kapsamı da denetlenir: yanlış şık bile kapsam dışı bir hesaba (ör. 5. sınıfta bir sayının yüzdesini bulma) dayanamaz. (c) Aynı bilgi ya da fikir (ör. "ıslaklık sürtünmeyi azaltır") bir testte en çok iki soruda kullanılır. (d) Mevcut sorularla tekrar sözcük düzeyinde değil, bağlam düzeyinde aranır (aynı ıslak basamak, aynı fren). (e) Kök ile doğru şık çelişmez (kök "kaydırarak" diyorsa doğru cevap tekerlek olamaz). (f) Uydurma ölçümler fiziksel olarak gerçekçidir (okul dinamometresi 0-10 N; hafif cisimler). (g) Gündelik dille yazılan ölçüt cümleleri ("en büyük kısmı") iki anlama gelebilir; ölçüt açık yazılır ("kaçta kaçı").

**Düzeylere göre:** Düzey 1 (Temel) de yaşam durumundan gelir, ama tek adımlıdır ve kısadır. Düzey 2 iki bilgiyi birleştirip bir seçim yaptırır. Düzey 3 karar, tahmin ya da iddia değerlendirmesi ister. Çeldiriciler, o yaşam durumunda insanların gerçekten yaptığı hatalardan da türetilebilir (ör. "Islak zeminde düz tabanlı ayakkabı daha az kaydırır" yanılgısı). Platformdaki dereceli konu testlerinde (Çok kolay → Çok zor) aynı ölçek uygulanır.

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
başına bağlam adı ve "Yaşamla bağ:" satırı; çeldirici → yanılgı eşleme tablosu; seçenek dağılım
sayımı; gerçek veri kullanıldıysa kaynak satırı; puanlama önerisi (soru
başına 10 puan).

## Adım 5 — Teslimden önce denetim (zorunlu)

Belgeleri teslim etmeden ÖNCE her soruyu şu dört muhakeme kontrolünden
geçir (ayrıntılı liste: `references/kilavuz-ilkeleri.md` §6):

1. **İşlevsellik + adlandırma sızıntısı:** Soru bağlam/tablo okunmadan
   çözülebiliyor mu? Sınıflandırma sorusunda örneği ADIYLA verip cevabı
   sızdırdın mı? (Bkz. §2 üretim uyarısı — "yaprak hücresi → bitki" tuzağı;
   örneği anonimleştir: 1./2. hücre.)
2. **Bilimsel doğruluk + tek cevap:** Her sorunun cevabı olgusal doğru ve
   tek mi? İkinci savunulabilir cevap kaldı mı?
3. **Çeldirici + biçim:** Çeldiriciler yanılgıdan mı türetilmiş; hepsi/hiçbiri
   yok, olumsuz kök ≤2, seçenek dengesi tutuyor, "alıştırma/deneme" ibaresi
   var mı?
4. **İzlenebilirlik:** Her soru çıktının süreç bileşenine mi yazılmış; çıktı
   kodu/ifadesi birebir mi?

Karşılanmayan madde varsa soruyu yeniden yaz. **Bu öz-denetim, öğretmenin
kendi incelemesinin yerini tutmaz** — her belge "uygulamadan önce öğretmen
incelemesi gerekir" dipnotu taşır.

## Kapsam dışı

Açık uçlu yazılı soruları, ders planı/çalışma kağıdı (tymm-ders-planlama),
mevcut testin tahlili veya puanlaması.
