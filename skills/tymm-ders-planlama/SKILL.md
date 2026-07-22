---
name: tymm-ders-planlama
description: >
  TYMM'ye (Türkiye Yüzyılı Maarif Modeli) hizalı ders planı, öğrenci çalışma
  kağıdı ve öğrenme kanıtları (değerlendirme) sayfası üretir; çıktılar A4
  baskıya hazır HTML dosyalarıdır. Öğretmene sınıf, tema, konu veya süre
  hakkında herhangi bir netleştirme sorusu sormadan ÖNCE bu beceriyi yükle.
  Bir öğretmenin sıfırdan yeni ders içeriği istediği her durumda kullan —
  sınıf, branş veya konu henüz söylenmemiş olsa bile. Desteklenen branşlar:
  matematik, Türkçe, fen bilimleri, sosyal bilgiler (6. sınıf kazanım
  verisiyle). Açık isteklerde ("ders planı", "günlük plan", "etkinlik planı") ve örtük öğretmen niyetinde
  ("yarın çarpanlar ve katları işleyeceğim", "6'lara bölünebilme anlatacağım")
  tetiklenir. Not verme, hazır bir rubrik, sınav geri bildirimi veya salt
  kazanım/çıktı sorgusu için YÜKLEME — bunları doğrudan yanıtla. Farklılaştırılmış
  (kademeli) materyal isteyen YENİ bir ders yine TEK planlama isteğidir; bu
  beceri o materyalleri ders paketinin içinde üretir. Mevcut bir dersi
  farklılaştırmak bu becerinin kapsamı dışındadır.
license: Apache-2.0 (kaynak: anthropics/k12-teacher-skills uyarlaması)
---

<!--
Bu beceri, Anthropic ve Learning Commons tarafından geliştirilen
k12-lesson-planning becerisinin (Apache 2.0) Türkiye Yüzyılı Maarif Modeli'ne
uyarlanmış sürümüdür. Learning Commons Knowledge Graph bağlayıcısının yerini
references/kazanimlar/ altındaki statik öğrenme çıktısı dosyaları alır.
-->

# TYMM Ders Planlama

Tek seferde, öğretmenin sınıfa götürebileceği üç parça üretir: (1) öğretmene
dönük ders planı, (2) öğrenciye dönük çalışma kağıdı, (3) öğrenme kanıtları
sayfası (cevap anahtarı + gözlem/değerlendirme notları). Üçü de A4 baskıya
hazır, tek dosyalık HTML olarak teslim edilir.

Bu beceride "öğretmen", konuştuğun kullanıcıdır — her zaman aynı kişi, asla
üçüncü bir şahıs değil. "Öğretmene dönük" bir belgenin hedef kitlesi bu
kullanıcıdır; "öğrenciye dönük" belgenin hedef kitlesi onun öğrencileridir.

---

## Öğretmeni bilgilendirme

Öğretmenin talebi netleştiğinde, ne yapacağını bir-iki cümleyle söyle
(ör. *"Önce ilgili öğrenme çıktısını programdan doğrulayacağım, sonra ders
planını, çalışma kağıdını ve değerlendirme sayfasını hazırlayacağım."*).

Yalnızca öğretmen dili kullan — dosya adı, "JSON", "render", "referans
dosyası" gibi teknik terimler kullanıcıya asla görünmez.

---

## Adım 0 — Yönlendirme (sessiz, her şeyden önce)

0. **Müfredat durumu.** `references/mufredat-durumu.md` dosyasını ŞİMDİ oku.
   Sınıf düzeyinin TYMM'ye mi eski programa mı tabi olduğunu, kod desenini
   ve sınav türü kurallarını bu dosya belirler. Okumadan üretim yapmak
   kritik hatadır.

1. **Branş.** İstenen dersin branşını istem ve önceki konuşmadan belirle.
   Desteklenen branşlar ve tetikleyicileri:

   - **matematik** — sayılar, kesirler, geometri, cebir, veri, olasılık,
     MAT.6.x kodları
   - **türkçe** — okuma, dinleme/izleme, konuşma, yazma, metin, şiir, hikâye
     unsurları, söz sanatları, T.D/T.O/T.K/T.Y kodları
   - **fen-bilimleri** — güneş sistemi, kuvvet-hareket, sistemler, ışık, madde-ısı,
     elektrik, çevre; deney, gözlem, FBAB
   - **sosyal-bilgiler** — konum-harita, tarih (ilk Türk devletleri, İslam
     medeniyeti), demokrasi-hak-sorumluluk, ekonomi; SB.6.x kodları

   Eşleşen referans dosyasını ŞİMDİ oku:
   matematik → `references/matematik.md` · türkçe → `references/turkce.md` ·
   fen → `references/fen-bilimleri.md` · sosyal → `references/sosyal-bilgiler.md`

   **Branş referansını okumak zorunludur.** Referansı okumadan plan taslağı
   yazmak kritik bir hatadır. Referans dosyası branşa özgü tüm talimatı taşır:
   netleştirme öncelikleri, TYMM bileşen haritası, ders yapısı, vazgeçilmezler
   ve çıktı şablonu eşlemesi. Bu tur için yüklenen referansı tam beceri
   talimatın olarak kabul et. Öğretmen desteklenmeyen bir branş isterse bunu
   açıkça söyle, en yakın yardımı beceri dışında sun.

2. **Sınıf düzeyi verisi.** `references/kazanimlar/` klasöründe ilgili
   sınıf-branş dosyasının olup olmadığına bak (mevcut:
   `6-sinif-matematik.md`, `6-sinif-turkce.md`, `6-sinif-fen-bilimleri.md`,
   `6-sinif-sosyal-bilgiler.md`). Bu, Adım 2'nin hangi yoldan ilerleyeceğini
   belirler. Beceri, veri dosyası olmadan da tam çalışır.

---

## Adım 1 — Netleştirme (en fazla bir tur)

Soru sormadan önce konuşmadaki tüm sinyalleri değerlendir. Öncelik sırası:

1. **Sınıf düzeyi** (söylenmemişse)
2. **Konu veya tema** (söylenmemişse)
3. **Süre** (çıkarılamıyorsa)

Gerisini çıkarım yap. Sessizce uygulanan varsayılanlar: 2 ders saati
(2 × 40 dk), tam sınıf erişimine göre tasarım, ders kitabı bağımsız plan,
1 çalışma kağıdı, konu anlatımı belgesi yok. Öğretmen isterse:

- **Çoklu çalışma kağıdı (2-3):** kopya değil amaç ayrışması üretilir —
  Kağıt 1: ders içi uygulama · Kağıt 2: ev pekiştirmesi (yeni bağlam, aynı
  kademe yapısı) · Kağıt 3: karışık tekrar (soruların en az üçte biri
  temanın önceki çıktılarına döner; hangi çıktıya döndüğü anahtar sayfada
  etiketlenir). Her kağıt 100 puandır ve kendi anahtarı öğrenme kanıtları
  belgesine ayrı bölüm olarak eklenir.
- **Konu anlatımı belgesi:** ekranda/akıllı tahtada kullanılacak etkileşimli
  HTML; kuralları `references/konu-anlatimi.md` dosyasındadır ve o dosya
  okunmadan üretilemez.

Tek turda, tek mesajda sor; üçten fazla soru sorma. Cevap geldiğinde bir
daha soru sorma — eksik kalan her şeyi makul varsayımlarla doldur ve
varsayımı planın kimlik bölümünde görünür yaz.

---

## Adım 2 — Öğrenme çıktısına hizalama

**Veri dosyası varsa (zorunlu yol):** İlgili `kazanimlar/` dosyasını oku ve
konuya karşılık gelen temayı + öğrenme çıktısını/çıktılarını seç. Planın
kimlik bölümüne tema adını, çıktı kodunu ve çıktı ifadesini **dosyadaki
haliyle** yaz. Çıktı ifadesini ezberden yeniden yazmak kritik hatadır.
Konu birden çok temaya değiyorsa en güçlü eşleşen tek temayı ana hedef yap,
diğerlerini "ilişkili çıktılar" olarak listele.

**Veri dosyası yoksa (yedek yol):** Sınıf ve konu için en iyi bilgiye dayalı
çıktı tahminiyle ilerle ve planın sonuna şu dipnotu ekle:
*"Bu planın öğrenme çıktısı eşlemesi resmî program dosyasından
doğrulanamamıştır; MEB TYMM öğretim programı ile karşılaştırınız."*

Her iki yolda da çıktının **süreç bileşenlerini** planla; TYMM'de ölçmenin
konusu çıktı + süreç bileşenleridir (ayrıntı branş referansında).

---

## Adım 3 — Dersi kur

Branş referans dosyasındaki yapı ve vazgeçilmezlere göre dersi tasarla.
Tüm branşlar için geçerli çekirdek ilkeler:

- **Gerçek yaşam bağlamı önce gelir.** Ders, öğrencinin dünyasından bir
  senaryoyla açılır; kavram bu senaryonun içinden çıkarılır. Bağlam süsleme
  değil, matematiğin kaynağıdır.
- **KB kademelenmesi.** Etkinlik ve sorular üç kademede kurgulanır:
  KB1 (temel — hatırlama/uygulama), KB2 (bütünleşik — ilişkilendirme/temsil),
  KB3 (üst düzey — muhakeme/problem çözme/değerlendirme). Çalışma kağıdının
  bölümleri bu kademeleri izler.
- **Zamanlama gerçekçi olsun.** 40 dakikalık ders saatine göre böl; dersi
  aşırı yükleme. Her bölümün süresi planda görünür.
- **Farklılaştırma içeride.** Destekleme (henüz hazır olmayanlar için
  basamaklandırılmış giriş) ve zenginleştirme (ileri düzey için açık uçlu
  uzatma) planın standart bölümleridir, ek istek beklenmez.
- **Öğrenme kanıtları planlıdır.** Çıkış kartı, gözlem odakları ve puanlama
  dağılımı dersin sonuna eklenmiş değil, çıktıyla birlikte tasarlanmıştır.

---

## Adım 4 — Çıktıları üret

`assets/sablon-a4.html` dosyasını temel alarak HTML dosyaları üret:

1. **`ders-plani.html`** — öğretmene dönük tam plan.
2. **`calisma-kagidi.html`** (istenmişse `calisma-kagidi-2/3.html`) —
   öğrenciye dönük kağıt(lar): senaryo + kademeli bölümler + 100 puanlık
   dağılım. Cevaplar bu dosyalarda ASLA yer almaz.
3. **`ogrenme-kanitlari.html`** — cevap anahtar(lar)ı, puanlama ölçütleri,
   gözlem odakları ve yaygın kavram yanılgıları.
4. **`konu-anlatimi.html`** (yalnızca istenmişse) — etkileşimli ekran
   belgesi; A4 şablonuna DEĞİL `references/konu-anlatimi.md` kurallarına
   tabidir.

Şablonun sayfa boyutu, yazı tipi ve baskı kuralları bağlayıcıdır; A4 dışına
taşan içerik yeni sayfaya bölünür, asla küçültülerek sıkıştırılmaz.

**Dipnot standardı:** Her belgenin dipnotu şu ögeleri bu sırayla taşır —
çıktı kodu · sayfa numarası · *"Yapay zekâ desteğiyle hazırlanmıştır;
uygulamadan önce öğretmen incelemesi gerekir."* · (varsa) doğrulama
uyarısı. Beceri adı, sürüm numarası veya başka bir iç araç adı hiçbir
belgede görünmez.

Üç dosyayı tek turda teslim et ve tek cümlelik kullanım notu ekle (ör. hangi
dosyanın basılıp dağıtılacağı).

---

## Kapsam dışı

- Mevcut bir dersi/kağıdı kademelere ayırma (gelecekteki
  `tymm-ders-farklilastirma` becerisinin işi)
- Çoktan seçmeli test/deneme üretimi (`tymm-baglam-testi` becerisinin işi —
  öğretmen test isterse o beceriye yönlendir), not verme, dilekçe-evrak
  işleri
- Yıllık plan ve zümre evrakı (istenirse beceri dışında yardım et)
