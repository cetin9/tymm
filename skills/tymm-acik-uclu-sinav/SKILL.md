---
name: tymm-acik-uclu-sinav
description: >
  MEB yönetmeliğine uygun, açık uçlu / kısa cevaplı ORTAK YAZILI SINAV paketi
  üretir: konu soru dağılım tablosu + sınav kağıdı + dereceli puanlama
  anahtarı (ayrı belge); hepsi A4 baskıya hazır HTML. Bir öğretmen "ortak
  yazılı", "yazılı sınav", "klasik sınav", "açık uçlu sınav", "yazılı
  sorusu" veya "N. senaryoya göre sınav" istediğinde kullan — sınıf veya
  konu henüz söylenmemiş olsa bile, netleştirme sorusundan ÖNCE yükle.
  2026-2027 ÖDSGM konu-soru dağılım tablolarındaki senaryo numarasıyla
  çalışır; sorular 2026-2027 MEB ders kitabına dayanır (5. sınıf: tüm
  ortak sınav dersleri). Ortak yazılılarda çoktan seçmeli KULLANILAMAZ;
  öğretmen çoktan seçmeli test/tarama/deneme isterse bu beceri DEĞİL
  tymm-baglam-testi kullanılır. Branşlar: Türkçe, matematik, fen bilimleri,
  sosyal bilgiler, din kültürü ve ahlak bilgisi, İngilizce.
license: "Apache-2.0 (kaynak: anthropics/k12-teacher-skills mimarisinin uyarlaması)"
---

# TYMM Açık Uçlu Ortak Yazılı Sınav

Tek turda üç belge üretir: `konu-soru-dagilimi.html` (sınav öncesi
öğrenciyle paylaşılan tablo), `sinav.html` (öğrenci kağıdı),
`puanlama-anahtari.html` (dereceli puanlama anahtarı + örnek yanıtlar).

"Öğretmen", konuştuğun kullanıcıdır. Teknik iç terimler kullanıcıya
görünmez.

**Dipnot standardı (üç belgenin altında):** sınav adı ve senaryo · kapsanan
çıktı kodları · "Yapay zekâ desteğiyle hazırlanmıştır; öğretmen tarafından
incelenmelidir." · varsa doğrulama uyarısı. Beceri, dosya ya da sürüm adı
belgelere sızmaz. Kitap sayfası yalnız puanlama anahtarında verilir ve
kitabın **basılı** sayfa numarasıyla yazılır (ör. "Türkçe 5, 1. kitap,
s. 13"). Basılı numara sayfa metninin başında ya da sonunda yazan sayıdır;
bulunamazsa "PDF s. 14" yazılır.

---

## Adım 0 — Yönlendirme (sessiz)

0. `../tymm-ders-planlama/references/mufredat-durumu.md` dosyasını ŞİMDİ
   oku. Sınıf düzeyi, terminolojiyi (öğrenme çıktısı / kazanım) ve kod
   desenini belirler. **Bu becerinin varlık sebebi oradaki sınav türü
   kuralıdır:** ortak yazılılar açık uçlu veya açık uçlu + kısa cevaplı
   olur; çoktan seçmeli, doğru/yanlış, eşleştirme **kesinlikle kullanılmaz.**
1. `../tymm-baglam-testi/references/kilavuz-ilkeleri.md` dosyasını oku.
   Bağlam temelli soru yazımı bir tasarım yaklaşımıdır, format değil —
   bağlam kurgulama, işlevsellik testi, soru kökü kuralları, bilişsel yük
   ve etik/tarafsızlık ilkeleri açık uçlu sorularda da aynen geçerlidir.
   (Seçenek/çeldirici bölümleri bu beceride uygulanmaz.)
1b. `references/olcme-ilkeleri.md` dosyasını oku. Bu dosya MEB TYMM
   Program Okuryazarlığı 5. Modülü'nün açık uçlu ve kısa cevaplı soru
   yazımı, puanlama ve dereceli puanlama anahtarı hükümlerini özetler.
   Açık uçlu soruya doğrudan ilişkin resmî kaynak olduğu için, çoktan
   seçmeli soru yazım kılavuzuyla çeliştiği yerde **bu dosya önceliklidir**.
2. Branş yanılgı envanterini oku (kısmi puanlama ve "yaygın hata"
   satırları için): matematik →
   `../tymm-baglam-testi/references/test-matematik.md`; diğerleri →
   `../tymm-baglam-testi/references/test-diger-branslar.md`. Bu dosyalardan
   **yalnız yanılgı ve hata bilgisi** alınır. Oradaki kod ve çıktı
   eşlemeleri ile "kazanimlar/ tek veri kaynağıdır" ifadesi 2025-2026
   verisine aittir. Bir kod iki dosyada farklı anlama geliyorsa senaryo ve
   program dosyasındaki anlam geçerlidir (ör. T.Y.5.16 = yazım ve
   noktalama).
3. **Senaryo tablosu (2026-2027):** `references/senaryolar/<sınıf>-sinif-<ders>.md`
   (ders: `turkce`, `matematik`, `fen-bilimleri`, `sosyal-bilgiler`,
   `din-kulturu-ve-ahlak-bilgisi`, `ingilizce`; sınıf 5-6-7). ÖDSGM'nin
   resmî tablosudur. Her sınavda (1. dönem 1. / 2. ortak yazılı) her
   senaryo için hangi çıktıdan **kaç soru** sorulacağını verir. Bu beceride
   kapsam ve soru sayısı **buradan** gelir, uydurulmaz.
3b. **Senaryo kartı (ÖNCE BUNU OKU):** `references/senaryo-kartlari/<sınıf>-sinif-<ders>.md`
   dosyasında ilgili sınavın `### Senaryo K` bölümü. Her çıktı için tek satırda şunları verir:
   - kazanım ifadesi ve soru sayısı,
   - tema · konu,
   - planda işlendiği haftalar,
   - sınavdan önce işlenip işlenmediği (✓ / ⚠),
   - kitap yeri (cilt, tema sayfa aralığı, varsa konu sayfası).

   Kartlar 180 senaryonun hepsi için önceden üretildi ve kontrol edildi.
   Bu bölüm okunduktan sonra yalnız gereken kitap sayfalarına gidilir.
   ⚠ işaretli çıktı varsa (2026-27'de yalnız Din 6, DKAB.6.2.1, 1. yazılı
   Senaryo 1 ve 4), teslim notunda öğretmene "bu çıktı sınav haftasında
   işlenmeye başlıyor" diye yazılır.
4. **Çıktı + süreç bileşenleri:** `../tymm-ders-planlama/references/kazanimlar/<sınıf>-sinif-<ders>.md`
   dosyası (2026-2027, 5-7. sınıf, 6 ders). Bu dosya senaryo tablolarıyla
   kod, ifade ve tema düzeyinde çapraz doğrulandı. Çıktı ifadesi ve süreç
   bileşenleri **buradan birebir** alınır.
   **Kapsam sınırları için** ayrıca
   `references/program/<sınıf>-sinif-<ders>.md` dosyasına (5-6-7) bakılır.
   7. sınıf İngilizce program dosyası TYMM'dir ve okulda **uygulanmaz**;
   7. sınıf İngilizce için yalnız kazanım dosyası (eski program) ile kitap
   kullanılır. İlgili
   çıktının bölümünü Grep ile bul, dosyanın tamamını okuma. Burada
   "öğrenme-öğretme uygulamaları" altındaki kapsam sınırları ("değinilir",
   "verilmez", "girilmez") bulunur; bu sınırlar soruyu bağlar. İki dosya
   çıktı ifadesinde ayrışırsa kazanım dosyası geçerlidir. Örneğin Din
   Kültürü'nde program dosyası eski TYMM sayfalarından gelir; doğru ifade
   kitap ve senaryoyla aynı olan kazanım dosyasındaki ifadedir.
   Kod senaryo tablosunda geçip kazanım dosyasında yoksa üretim durur ve
   öğretmene bildirilir; kod uydurulmaz.
   **Türkçe ve İngilizce 7 (eski program):** süreç bileşeni (a, b, c)
   yoktur. İngilizce 5-6'da bileşenler vardır ve kullanılır. Bileşen
   olmayan derslerde "süreç bileşeni" yerine **ölçülen odak** yazılır. Odak,
   programın o çıktı için verdiği öğrenme-öğretme uygulamalarından ve
   kitabın bilgi kutusundan alınır (ör. "metinde geçen bir kelimenin
   anlamını bağlamdan tahmin etme"). Harf kodu uydurulmaz. Alt maddeler
   aynı çıktının farklı odaklarını ölçer.
4b. **Kapsam (hangi konular işlendi):** `references/plan-<sınıf>-sinif.md`
   dosyasında dersin bölümüne bak. ▶ satırı sınav haftasıdır; sınav, o
   satırın **üstündeki tüm haftaları** kapsar. Bir tema sınav haftasından
   önce başladıysa kısmen işlenmiştir; o temanın yalnız işlenmiş konuları
   kapsama girer. Senaryo tablosunda tema sütunu olmayan derslerde
   (Türkçe, kısmen İngilizce) hangi temaların kitap ve kavram kaynağı
   olacağı **buradan** belirlenir. Örneğin 5. sınıf Türkçe 1. yazılı =
   Oyun Dünyası + Atatürk'ü Tanımak'ın ilk haftaları (Mustafa, Oğlu
   Hüseyin'den Emine Ana'ya Mektuplar). Öğretmen aksini söylemedikçe okulun
   zümre planı **MEB çerçeve planıyla aynı** kabul edilir.
5. **Ders kitabı (2026-2027, 5-6-7. sınıf):** kitap yeri senaryo kartında
   hazırdır. Kartta yoksa dizin dosyasına bakılır: 5. sınıf için
   `references/kitap-dizini.md`, 6-7. sınıf için
   `references/kitap-dizini-6-7.md`. İlgili sayfalar
   `references/kitap/<sınıf>-sinif-<ders>-<cilt>.md` içinden **yalnız o
   aralıkta** okunur (Grep → `--- s.N ---` işareti → Read offset/limit).
   Kitap ile yıllık plan tema sırası 18 ders-sınıfın hepsinde aynıdır
   (doğrulandı). Türkçe kitaplarındaki metin sırası da planla aynıdır.
   Türkçe'de konu adı yoktur: işlenen temaların aralığında çıktının
   anahtar kavramı aranır (ör. "anahtar kelime", "nokta", "yüzey anlam").
   Kitaptan alınacaklar: kavramların kitaptaki adı ve tanımı, kitabın
   işlediği örnek ve bağlam türleri, birim/sayı yazımı, konunun kitapta
   nereye kadar işlendiği.
   **Kitap ifadesi ile program ifadesi ayrışırsa** (onaylı karar,
   23.10.2026): sınav belgelerinde çıktı ifadesi **program/kazanım**
   ifadesidir; konu içeriği, kavram adları ve örnek türleri kitaptan
   alınır. Bilinen durumlar:
   - Sosyal 5: SB.5.2.1, 5.2.3 ve 5.6.2'de kitap eski ifadeyi kullanır.
   - Fen 5: FB.5.3.2, 5.6.2 ve 5.2.4'te fiiller farklıdır.
   - Türkçe 5: T.Y.5.2'de senaryo tablosunda bir varyant var.

### OYSS gerçeği (2026-2027, ÖDSGM kılavuzu 20.10.2026)

Okul geneli ortak yazılılar 2026-2027'den itibaren **Ortak Yazılı Sınav
Sistemi (OYSS)** üzerinden yapılır: 5-6-7. sınıf Türkçe, Matematik, Fen,
Sosyal, Din Kültürü, İngilizce (7. sınıf İngilizce **hariç**).
- Zümre senaryoyu seçer. Soruların çoğu Yeni EBA'daki **kapalı soru
  havuzundan** gelir; havuz yalnız öğretmenlere, sınavdan 4 gün önce
  açılır.
- Zümre, seçilen senaryodaki **iki öğrenme çıktısı için iki açık uçlu soru
  ve puanlama anahtarı** yazar. Havuzdan gelen en çok 2 soruyu gerekçeyle
  değiştirebilir.
- Sorular kolay/orta/zor güçlük düzeylidir; puanları zümre belirler.
  Kâğıt en çok 4 sayfa, süre 40 dakika, toplam 100 puandır.
- Bu yüzden bu beceri iki iş yapar: (a) öğrenciyi hazırlamak için
  senaryonun tamamını kapsayan **deneme sınavı**, (b) zümrenin OYSS'ye
  gireceği **iki açık uçlu soru + puanlama anahtarı**. Gerçek sınav
  kâğıdını tahmin ettiğini ya da havuzdaki soruları bildiğini asla ima
  etme.

**1. yazılı tarihleri (resmî takvim):** Fen 3 Kasım · Matematik 5 Kasım ·
Sosyal 6 Kasım · Türkçe 10 Kasım · İngilizce 12 Kasım · Din Kültürü 13
Kasım 2026. 6. sınıf Matematik 1. yazılı **ülke geneli**, 11 Kasım. 2.
yazılı takvimi henüz yayımlanmadı. Dönem sonu haftası (18 Ocak 2027)
varsayılır; 7. sınıf Türkçe 2. yazılı ise resmî olarak 5 Ocak'ta, ülke
geneli yapılır. Kapsam bu tarihlere göre `references/plan-<sınıf>-sinif.md`
dosyasından okunur.

**Resmî örnek sorular (stil kaynağı):** `references/ornek-sorular/`
klasöründe şunlar var:
- 5. sınıf, 6 ders: ÖDSGM 2024-2025 örnek kitapçıkları (TYMM, öğrenme
  çıktısı etiketli).
- 6. sınıf Türkçe ve Matematik: 2025-2026 ülke geneli sınav kitapçıkları
  (8 açık uçlu soru, puanlamalı).
- **5-6. sınıf, 6 ders, 4 sınav: MEBİ "Yazılıya Hazırlanıyorum"
  (2025-2026, TYMM; 41 dosya, ad deseni `…mebi-yaziliya-hazirlaniyorum_<1d1y|1d2y|2d1y|2d2y>_<ders><sınıf>.md`).**
  Senaryo moduna **en yakın resmî örnekler** bunlardır, çünkü her sorunun
  üstünde çıktı kodu yazar. Soru yazmadan önce ilgili ders, sınıf ve
  sınavın dosyasına bakılır. Kodları 2026-27 kazanımlarıyla 216/223
  uyuşur. Uyuşmayan 7 kod 5. sınıf Türkçe'dedir (T.Y.5.18, 5.19, 5.21,
  T.O.5.23): bu kodlar 2026-27'de kaldırıldı. Bu dosyalardaki kod
  numaraları kullanılmaz; kod her zaman kazanım dosyasından alınır.
Soru yazmadan önce ilgili dersin dosyasına bak: soru kökü uzunluğu,
bağlam türü, görsel kullanımı ve puanlama dili bu örneklere benzemelidir.
Örnek sorular **kopyalanmaz**; yalnız biçim ve düzey ölçütüdür. Metin PDF'ten
ham çıkarılmıştır, şekil düzeni bozuk olabilir.

## Adım 1 — Netleştirme (en fazla bir tur, en fazla üç soru)

**Senaryo modu** (kullanıcı senaryo numarası verdiğinde ya da "ortak
yazılı" + sınıf + ders söylediğinde; 2026-2027'de varsayılan budur).
Gerekenler: sınıf · ders · hangi sınav (1. dönem **1.** mi **2.** ortak
yazılı mı) · senaryo no · **iş türü**: deneme sınavının tamamı mı, OYSS
için iki soru mu? İş türü söylenmemişse deneme sınavı üretilir; teslim
notunda OYSS için iki soru da istenebileceği belirtilir.
- Sınav belirtilmemişse tarihe göre seç: dersin 1. yazılı tarihi
  geçmediyse 1. yazılı, geçtiyse 2. yazılı. Seçimi teslim notunda söyle.
- **OYSS iki soru modu:** zümre hangi iki çıktıyı seçeceğini söylemediyse
  senaryodaki çıktılardan iki öneri sun. Öneride en az biri havuzun zor
  ölçeceği muhakeme/üretim çıktısı olsun. Her soru için güçlük düzeyi
  (kolay/orta/zor) ve önerilen puan yazılır. Çıktı yine üç belgedir, ama
  sınav kâğıdında yalnız iki soru bulunur. Konu soru dağılım tablosunda
  seçilen senaryonun tamamı gösterilir ve bu iki sorunun yeri işaretlenir.
- Senaryo no verilmemişse sor. Soruda, o sınavın senaryolarını soru sayısı
  ve kapsadığı temalarla tek satırda listele (senaryo dosyasının sonundaki
  özet satırları).
- İstenen senaryo o sınavda yoksa (ör. Fen 1. yazılıda 4 senaryo var,
  "6. senaryo" istendi) bunu söyle ve mevcut senaryoları listele.
- **Ülke geneli sınav:** senaryo dosyasında "Senaryo yok — ÜLKE GENELİ"
  notu varsa (2026-2027: 6. sınıf Matematik 1. yazılı, 7. sınıf Türkçe 2.
  yazılı), resmî tablo henüz yoktur. Öğretmene bunu bildir ve iki seçenek
  sun: program kapsamından deneme sınavı ya da kılavuz yayımlanınca
  üretim.
- "Tüm dersler" istenirse her ders için ayrı paket üretilir (aynı sınav ve
  senaryo no; o derste bu numara yoksa ders için en yakın numara seçilir ve
  bu not edilir).
- **7. sınıf İngilizce** OYSS dışındadır ve eski programla okutulur
  (`E7.x.y` kazanımları). Senaryo tablosu yine geçerlidir. Terminolojide
  "kazanım" kullanılır, süreç bileşeni katmanı uygulanmaz.
- **Deneme sınavı biçimi:** her sorunun yanında güçlük düzeyi (kolay /
  orta / zor) belirtilir. Sınav kâğıdı **en çok 4 sayfa** ve 40 dakikalık
  olur.

**Serbest mod** (senaryo dışı kapsam: "şu iki çıktıdan yazılı" ya da
2. dönem): öncelik (1) sınıf düzeyi, (2) kapsam ("dönem başından bu yana"
denirse `../tymm-ders-planlama/references/tema-sirasi.md`), (3) sınav
yapısı. Varsayılanlar: 1 ders saati (40 dk), 10 soru (açık uçlu ağırlıklı,
en çok 3 kısa cevaplı), 100 puan.

## Adım 2 — Konu soru dağılım tablosu

Ortak yazılı soruları, zümrenin seçtiği **konu soru dağılım tablosu**
senaryosuna göre hazırlanır. Tablo sınavdan önce öğrenciyle paylaşılır.
Bu yüzden ilk belge budur.

**Senaryo modunda:**
- Satırlar senaryo tablosundan **birebir** alınır: ünite/tema · konu
  (içerik çerçevesi) · çıktı kodu + ifadesi · **soru sayısı** (yalnız o
  senaryoda sayısı olan çıktılar). Soru sayısı ve toplam değiştirilmez.
- Her soru tek bir çıktıya yazılır. Alt maddeler (a, b, c) aynı çıktının
  farklı süreç bileşenlerini ölçebilir; tek soru sayılır. Tabloya ek
  sütunlar konur: hedeflenen süreç bileşen(ler)i · soru no · soru türü ·
  puan.
- Puan: MEB tabloları puan vermez. Toplam 100 olur. Taban eşit
  dağıtımdır; gerekçelendirme veya muhakeme isteyen sorular tabanın 5 puan
  üstüne, tek adımlı sorular 5 puan altına çıkabilir. Örneğin 7 soru →
  10-10-15-15-15-15-20, 6 soru → 15-15-15-15-20-20. Puanlar 5'in katıdır.
  Öğretmen değiştirebilir. Senaryo modunda "tek çıktı 25 puanı aşmaz"
  kuralı **uygulanmaz**: bir çıktıya iki soru düşmesi resmî tablonun
  kararıdır.
- Tek soru alan çıktının birden çok süreç bileşeni varsa, alt maddelerle
  en az ikisi ölçülür. Hangi bileşenin ölçüldüğü tabloda yazar.
- Başlıkta şunlar yazar: "2026-2027 · 1. Dönem N. Ortak Yazılı · Senaryo
  K (ÖDSGM konu-soru dağılım tablosu)".

**Serbest modda:** satır = hedef çıktı · süreç bileşen(ler)i · soru no ·
tür · puan. Puanlar çıktıların ders saati ağırlığıyla orantılıdır, toplam
100 eder. Her çıktıya en az bir soru düşer; tek çıktı 25 puanı aşmaz.

## Adım 3 — Soru yazım kuralları

- **Format:** yalnızca açık uçlu ve kısa cevaplı. Kısmen bile çoktan
  seçmeli/eşleştirme/doğru-yanlış içeren soru yazılamaz. Program
  dosyasının "öğrenme kanıtları" bölümü bazen çoktan seçmeli ya da
  doğru-yanlış önerir. Bu öneri sınıf içi değerlendirme içindir; ortak
  yazılıda **yönetmelik önceliklidir**. Sınır durumları şöyle çözülür:
  - "Tabloyu doldurun": öğrenci değeri kendisi üretiyorsa açık uçludur.
  - "Uyumlu mu / doğru mu?": yalnız gerekçeyle birlikte sorulur. Evet/hayır
    kısmına puan verilmez ya da en çok soru puanının beşte biri verilir;
    puanın kalanı gerekçeye aittir.
- **Bağlam temelli:** her soru gerçek yaşam durumu, veri, metin veya
  görselden hareket eder; işlevsellik testi uygulanır (bağlam okunmadan
  cevaplanabilen soru yeniden kurgulanır). Kılavuzun bağlam erişilebilirlik
  ve tarafsızlık kuralları geçerlidir.
- **Süreç bileşeni hedefleme:** her soru, çıktının belirli süreç
  bileşen(ler)ine yazılır; hangi bileşeni ölçtüğü anahtarda belirtilir.
  (8. sınıfta kazanım dili kullanılır, bileşen katmanı zorlanmaz.)
- **Kademelendirme:** soruların yaklaşık yarısı tek bileşenli uygulama
  (temel), kalanı ilişkilendirme ve muhakeme/gerekçelendirme ister; en az
  2 soru "neden/nasıl/gerekçelendir" tipindedir.
- **Bağlam (5. Modül §5.4.17 öncelikli):** bağlam gerçekçi verilere
  dayanır, **gereksiz ayrıntı içermez**, problem durumu örtüktür ve soru
  tek adımda çözülmez. Kolay ve orta sorularda bağlam yalnız gerekli
  bilgiyi verir. **Zor** düzeyde, çıktının muhakeme bileşeni gerektiriyorsa,
  öğrencinin ayıklaması gereken en çok bir-iki öğe eklenebilir
  (`kilavuz-ilkeleri.md` §5). Uzunluk işlevsel olmalıdır, süs değil.
- **Alt basamaklı sorular:** bir soru a-b-c alt maddelerine bölünebilir;
  alt maddeler bağımsız puanlanır ve ipucu zinciri kurmaz (a'yı yapamayan
  b'yi yapabilmelidir).
- **Kavram izlenebilirliği:** sorularda kullanılan kavramlar çıktı
  ifadeleri + program dosyasındaki anahtar kavramlar + **kitabın o temada
  işlediği kavramlarla** sınırlıdır. Kitapta geçmeyen terim kullanılmaz;
  kitabın adlandırması esas alınır.
- **Kitaba dayanma, kopyalamama:** soru, kitabın işlediği bağlam türünü ve
  etkinlik mantığını izler. Kitaptaki etkinlik, örnek veya soru ise
  **aynen** sınava konmaz; sayılar, kişiler ve durum değiştirilir. Böylece
  ezber değil çıktı ölçülür. Puanlama anahtarında her soru için dayanılan
  kitap sayfası yazılır (ör. "Kitap: 1. kitap, PDF s. 73-77").

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

### Branşa özgü kurallar
- **Türkçe:** Okuma çıktıları (T.O.5.x) bir metin üzerinden sorulur. Sınav
  için **özgün** metin yazılır (bilgilendirici/öyküleyici/şiir; 5. sınıf
  düzeyine uygun, 120-250 sözcük). Kitaptaki metin kullanılmaz, çünkü
  öğrenci onu işlemiştir; metin türü ve tema kitaptaki temalarla uyumlu
  olur. Bir metne 2-4 soru bağlanabilir. Görsel okuma (T.O.5.7) için
  görsel HTML/SVG ya da tarif edilmiş tablo/afiş olarak verilir. Yazma
  çıktıları (T.Y.5.x) kısa üretim görevidir (2-5 cümle, ölçütleri
  yönergede yazılı). T.Y.5.16'da yazım/noktalama hatası içeren cümle
  düzelttirilir; hatalar TDK yazım kurallarına göre seçilir.
- **Matematik:** sayılar kitabın yazımıyla verilir (5+ basamakta binlik
  **boşluk**: 125 400). Çizim/ölçme çıktıları (MAT.5.3.x) için kareli
  zemin, açıölçer görseli veya nokta kağıdı SVG ile konur. "Araç ve
  teknolojiden yararlanma" çıktıları kâğıt üzerinde araç kullanımını
  betimleyen ya da ölçüm sonucunu yorumlatan soruyla ölçülür.
- **Fen:** kavramlar kitaptaki tanımla kullanılır (ör. kütle-ağırlık).
  Model/deney çıktılarında düzenek görseli veya veri tablosu verilir.
  Sayılar kitaptaki gibi binlik **nokta** ve ondalık virgülle yazılır
  (384.400 km, 29,5 gün). Bilinen yanılgılar puanlama anahtarının "yaygın
  hata" satırına yazılır; örneğin Ay: "evreler Dünya'nın gölgesiyle
  oluşur", "Ay kendi ekseninde dönmez", "dolanma süresi ile evre
  döngüsünü (29,5 gün) karıştırmak".
- **Sosyal Bilgiler:** sayılar kitabın yazımıyla verilir (binlik
  **nokta**: 85.000). "Yaşadığı il" çıktılarında il **İstanbul**'dur
  (öğretmen teyidi, 23.10.2026); başka il söylenirse o kullanılır.
  İstanbul'a ilişkin veriler (konum, komşu iller, afet riski, ortak miras
  ögeleri) doğrulanabilir genel bilgiyle sınırlı tutulur; uydurma sayı
  verilmez. Harita gerektiren sorularda basit SVG kroki kullanılır.
- **Din Kültürü ve Ahlak Bilgisi:** saygı ifadeleri (cc), (sav), (as)
  kitaptaki gibi yazılır. Sure ve dua metinleri kitaptaki okunuşla
  birebir verilir. Sorular bilgiyi ve yorumu ölçer; öğrencinin kendi
  ibadet pratiğini veya inancını puanlayan soru yazılmaz.
- **İngilizce:** sorular ve metinler İngilizcedir. Yönerge kısa İngilizce
  olur, gerekirse yanına Türkçe açıklama eklenir. Okuma çıktıları (R)
  özgün kısa metinle, kelime (V) ve dil yapısı (G) çıktıları **seçeneksiz**
  boşluk doldurma ya da kısa yanıtla, yazma çıktıları (W) yönlendirmeli
  kısa yazma ile ölçülür. **Söz varlığı:** 5-6. sınıfta
  `references/ingilizce-sozcuk/<sınıf>-sinif.md` dosyasındaki temanın
  "Güvenli" listesiyle sınırlıdır. Bu liste, program hedef sözcükleri ile
  kitabın o tema sayfalarının kesişimidir; kitap program sözcüklerinin
  ancak %44-71'ini kullanır. "Kullanma" listesindeki sözcük soruya
  girmez. 7. sınıfta (eski program) kitabın ünite sayfalarındaki sözcükler
  kullanılır. Kelime havuzundan seçtirme yapılmaz, çünkü bu eşleştirmeye
  kayar.
- Yönerge net olur: istenen ürün (işlem, açıklama, çizim, tablo) ve puan
  her sorunun yanında görünür.

### Anlaşılırlık kuralları (öğretmen geri bildirimi, 29.10.2026)
Soruyu yazan, cevabı bildiği için kendi sorusunu hep anlaşılır bulur. Bu
yüzden aşağıdaki kurallar, bilimsel doğruluktan ayrı olarak uygulanır:
- **Ders içinde başka anlamı olan sözcük, işaret olarak kullanılmaz.** Ay
  ünitesinde tişörte/topa "yıldız" konmaz (gökteki yıldızla karışır);
  "gülen yüz resmi", "kırmızı nokta" gibi nötr işaret seçilir.
- **Tablo başlığı tam bir soru ya da açık bir ad olur.** "Ece'nin gördüğü
  yan" gibi kısaltılmış, ne yazılacağı belli olmayan başlık yazılmaz;
  "Ece resmi görür mü?" + "Her kutuya Görür ya da Görmez yazınız." gibi
  kutuya yazılacak değer kökte söylenir.
- **Zihinsel döndürme yükü sınırlanır (5-6. sınıf).** Üstten görünüşte
  sağ/sol yan, başkasının gözünden görünüş, yön çevirme isteniyorsa
  bunlar ölçülen çıktının kendisi değilse sorudan çıkarılır; daha basit bir
  gözlem (görür/görmez, aydınlık/karanlık) sorulur. Anahtar sağ/sol için
  ayrı puan vermez.
- **Şekildeki simge, öğrencinin çizmesi istenen cevapla karıştırılamaz.**
  Ay evresi düzeneklerinde yukarıdan görünüşle çizilmiş yarım koyu toplar
  "öğrencinin gördüğü şekil" sanılıp kopyalanır. Cevabı istenen konumlar
  boş "?" daire olur; şekle "toplar yukarıdan görünüyor" notu eklenir;
  önce evrenin adı, sonra çizim istenir.
- **Kökte geçen her nesne şekilde de vardır** (ör. "sınıfın kapısı"),
  şekildeki her etiket metinde de aynı adla geçer.
- **Yön, sayma, karşılaştırma isteklerinde ölçüt kökte verilir**
  ("saatin dönme yönüyle aynı / tersine yazınız"), öğrenci tahmin etmez.
- **Sezgiye ters cevaplı maddelere 5. sınıf düzeyinde ipucu konur**
  ("Mert'in yüzü tur boyunca sırayla hangi duvarlara bakar?").
- **Kök, öğrenciyi yanlış terime itmez** (kökte "kendi çevresinde dönüyor"
  deyip anahtarda "dolanma" beklenmez).
- **Bir cümleye bir iş:** çok işli uzun kökler bölünür; "değerlendiriniz"
  gibi soyut fiiller yerine somut soru sorulur ("… doğru mu? Neden?").
- **Şekil yazıları baskıda okunur** (en az ~8 punto); bilgi yalnız renkle
  verilmez.

## Adım 4 — Dereceli puanlama anahtarı

`puanlama-anahtari.html` ayrı belgedir ve şunları içerir:

- Soru başına **örnek tam yanıt** (birden çok geçerli çözüm varsa en yaygın
  ikisi).
- **Kısmi puan basamakları (analitik anahtar, 5. Modül §5.4.15):**
  süreç bileşenlerine bağlanmış ölçütler (ör. "modeli doğru kurdu: 4p ·
  işlemi doğru yürüttü: 4p · sonucu yorumladı: 2p"). Basamak toplamları
  soru puanına eşittir. Her soruda 2-4 ölçüt bulunur ve ölçüt adları
  gözlenebilir davranışı anlatır; "iyi", "güzel" gibi değer yargısı
  kullanılmaz. Türkçe dışı derslerde yazım ve dil bilgisine en çok soru
  puanının %10'u verilir.
- **Yaygın hata satırı:** yanılgı envanterinden, o soruda beklenen hatalar
  ve bunlara puan verilip verilmeyeceği.
- Toplam puan sayımı (100 kontrolü) ve sınıf içi uygulama notu.

## Adım 5 — Çıktı üretimi

HTML biçim sözleşmesi (mekanik denetim buna göre okur):
- Soru puanı: `<span class="puan">15 puan</span>` (her soru başlığında bir
  kez; alt madde puanları farklı bir sınıfla yazılır).
- Alt maddeler **küçük harfle** yazılır: a) b) c). Büyük harf A) B) C) D)
  dizisi çoktan seçmeli sayılır ve denetimden kalır.
- Sayfa numarası ("Sayfa 1/N") yazılacaksa N, baskı sonrası gerçek sayfa
  sayısıyla eşleşmelidir. Emin değilsen sayfa numarası yazma.

A4 şablon kuralları geçerlidir (`../tymm-ders-planlama/assets/sablon-a4.html`
temel alınır): soru blokları sayfa sonunda bölünmez, üstte okul/ders/sınıf/
süre başlık alanı ve öğrenci ad satırı, cevaplar için yeterli boş alan
bırakılır. Öğrenci kağıdına anahtar içeriği veya stili sızmaz. Üç belge tek
turda teslim edilir. Teslim notunda şunlar yazar: hangi sınav ve senaryo
kullanıldı, konu soru dağılım tablosu sınavdan önce öğrencilerle
paylaşılmalı, kitaba dayanılan sayfalar anahtarda gösterildi.

Dosya adı (senaryo modu): `<sınıf>-<ders>-<1|2>yazili-senaryo<K>/`
klasörü altında üç belge. "Tüm dersler" isteğinde ders başına bir klasör
oluşturulur.

## Adım 6 — Teslimden önce denetim (zorunlu)

Teslimden ÖNCE her soruyu şu altı kontrolden geçir (ayrıntı:
`../tymm-baglam-testi/references/kilavuz-ilkeleri.md` §6):

1. **İşlevsellik + adlandırma sızıntısı:** Soru bağlam/veri okunmadan
   çözülüyor mu? Sınıflandırma sorusunda örneği ADIYLA verip cevabı
   sızdırdın mı? (§2 üretim uyarısı; örneği anonimleştir.)
2. **Bilimsel doğruluk + örnek yanıt:** Olgu doğru mu; her sorunun örnek tam
   yanıtı tutarlı ve tek mi?
3. **Yönetmelik + puanlama:** Yalnız açık uçlu/kısa cevaplı (çoktan seçmeli
   YOK); kısmi puan basamaklarının toplamı soru puanına, sorular 100'e
   kapanıyor mu?
4. **İzlenebilirlik:** Her soru süreç bileşenine yazılmış mı, kod ve ifade
   birebir mi? Senaryo modunda: her çıktının soru sayısı tablodaki sayıya,
   toplam soru sayısı senaryo toplamına eşit mi; senaryoda olmayan çıktıdan
   soru var mı? Serbest modda: hiçbir çıktı 25 puanı aşmıyor mu?
5. **Kitap ve kapsam uyumu:** Soru, plan dosyasına göre sınava kadar
   işlenmiş konular içinde mi? Kullanılan her kavram kitabın o temasında
   geçiyor mu?
   Kitaptaki bir etkinlik birebir kopyalanmış mı? Program/kitap kapsam
   sınırı ("verilmez") aşılmış mı?
6. **Öğrenci gözüyle anlaşılırlık (ayrı göz, anahtarı görmeden):** Kâğıt
   PDF'e basılır; görsel ve şekiller görüntü olarak incelenir. Anahtarı
   görmemiş biri her soruyu ortalama bir öğrenci (5. sınıf: 10-11 yaş)
   gibi okur ve şunu sorar: ne istendiğini ilk okumada anlıyor mu, tabloya
   ne yazacağını biliyor mu, şekildeki her simge ve etiket metinle aynı mı,
   iki anlamlı sözcük var mı, kök onu başka bir cevaba itiyor mu? Yukarıdaki
   "Anlaşılırlık kuralları" listesi bu kontrolün ölçütüdür. Bilimsel/sayısal
   doğruluk incelemesi bu kontrolün yerini tutmaz: soru doğru olup yine de
   anlaşılmaz olabilir.

Paket bir klasöre yazıldıysa `python tools/denetim.py <klasör>` mekanik
kontrolü çalıştırılır (depo içindeyken).

Karşılanmayan madde varsa soruyu yeniden yaz. **Bu öz-denetim öğretmen
incelemesinin yerini tutmaz.**

## Kapsam dışı

Çoktan seçmeli test/tarama/deneme (`tymm-baglam-testi`), ders planı ve
çalışma kağıdı (`tymm-ders-planlama`), hazır sınavın puanlanması veya
tahlili, not hesaplama ve e-Okul işlemleri.
