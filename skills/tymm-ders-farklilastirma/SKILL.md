---
name: tymm-ders-farklilastirma
description: >
  MEVCUT bir dersi, çalışma kağıdını veya konuyu TYMM farklılaştırma
  yaklaşımıyla iki yönde açar: DESTEKLEME (somut örnek, materyal,
  görselleştirme, akran desteğiyle hedefe ulaştırma) ve ZENGİNLEŞTİRME
  (içerik çerçevesinden uzaklaşmadan derinleştirme). Çıktı, resmî
  Farklılaştırma Etkinlikleri Öğretmen Kılavuz Kitabı desenindedir:
  etkinlik künyesi + öğretmen yönergesi + Ek 1 öğrenci sayfası + Ek 2
  değerlendirme; A4 baskıya hazır HTML. Öğretmen "farklılaştır",
  "kademelendir", "seviyelere ayır", "sınıfta seviye farkı var", "hızlı
  bitirenlere ek etkinlik", "zorlananlar için basitleştir" dediğinde
  kullan. SIFIRDAN yeni ders isteniyorsa YÜKLEME — o tymm-ders-planlama
  işidir (farklılaştırma zaten her planın standart bölümüdür).
license: Apache-2.0 (kaynak: anthropics/k12-teacher-skills mimarisinin uyarlaması)
---

# TYMM Ders Farklılaştırma

Tek turda iki etkinlik paketi üretir: `destekleme.html` ve
`zenginlestirme.html`. Her paket, MEB **Farklılaştırma Etkinlikleri
Öğretmen Kılavuz Kitabı**'nın etkinlik desenini izler (aşağıda).
Öğretmen yalnız birini isterse yalnız o üretilir.

"Öğretmen", konuştuğun kullanıcıdır. Dipnot standardı diğer becerilerle
aynıdır; beceri/sürüm adı belgelere sızmaz.

---

## Adım 0 — Yönlendirme (sessiz)

0. `../tymm-ders-planlama/references/mufredat-durumu.md` dosyasını oku
   (terminoloji ve kod deseni).
1. Branş pedagoji dosyasını oku:
   `../tymm-ders-planlama/references/<brans>.md`.
2. `../tymm-ders-planlama/references/kazanimlar/` altından sınıf-branş
   dosyasını oku; hedef çıktının ifadesi ve süreç bileşenleri birebir
   alınır.
3. Yanılgı envanterini oku (destekleme etkinliğinin hata-önleyici
   kurgusu için): matematik →
   `../tymm-baglam-testi/references/test-matematik.md`; diğer branşlar →
   `../tymm-baglam-testi/references/test-diger-branslar.md`.

## Adım 1 — Girdiyi belirle (en fazla bir tur soru)

İki meşru girdi vardır:

- **Mevcut materyal:** Öğretmen bir plan/kağıt/etkinlik yapıştırdıysa veya
  bu sohbette üretildiyse, farklılaştırma ONA bağlanır: aynı çıktı, aynı
  bağlam evreni, aynı kavram seti. Materyaldeki kavramların dışına çıkılmaz.
- **Yalnız konu adı:** Materyal yoksa hedef çıktı kazanım dosyasından
  seçilir ve bağımsız etkinlik paketi üretilir (resmî kitap da böyle
  yapar).

Eksikse sor (tek mesaj, en çok üç soru): sınıf, konu/materyal, hangi yön
(destekleme / zenginleştirme / ikisi — varsayılan ikisi).

## Adım 2 — Resmî farklılaştırma yaklaşımı (bağlayıcı tanımlar)

- **Destekleme:** programın hedeflediği bilgi ve becerilere ulaşmada daha
  fazla **somut örnek, günlük hayat bağlamı, somut materyal ve
  görselleştirmeye** ihtiyaç duyan öğrenciler içindir. Araç gereç ve
  teknoloji kullanımı, **akran öğrenmesi** (grup çalışması) ve öğretmenin
  süreçteki rolü vurgulanır; uygun yerde **dijital platform** önerisi
  eklenir. Destekleme, hedefi DÜŞÜRMEZ — aynı çıktıya daha basamaklı ve
  somut bir yoldan ulaştırır.
- **Zenginleştirme:** karmaşık ve soyut bilgiyi hızlı çözümleyen
  öğrenciler içindir. **İçerik çerçevesinden uzaklaşmadan** tema/ünite
  içindeki bilgiyi derinleştirir; üst düzey düşünme (muhakeme, karşı
  örnek, genelleme, disiplinler arası ilişkilendirme, gerçek yaşam
  uygulaması) hedefler. Sonraki sınıfın konusuna GEÇMEZ.
- Etkinlikler örnek niteliğindedir; öğretmenin seçip uyarlayabileceği
  esneklikte yazılır (bu not öğretmen yönergesine eklenir).

**Düzey isteği çevirisi:** Öğretmen "üç düzeye ayır" derse resmî yapı
açıklanır ve üçlü şöyle kurulur: destekleme sürümü · mevcut/ana materyal ·
zenginleştirme sürümü. "Kolay/orta/zor" etiketi kullanılmaz.

## Adım 3 — Etkinlik deseni (resmî kılavuz kitap şablonu)

Her etkinlik paketi bu künyeyle açılır:

| Alan | İçerik |
|------|--------|
| Tema/Ünite No ve Adı | kazanım dosyasındaki adıyla |
| Etkinlik Adı | özgün, içeriği yansıtan ad |
| Etkinliğin Amacı | hedef çıktı + süreç bileşen(ler)ine bağlı tek cümle |
| Destekleme/Zenginleştirme Uygulaması | yaklaşımın bu konudaki somut önerisi (1-2 cümle) |
| Araç Gereç | madde madde; "Ek 1 ve Ek 2'nin çıktısı (öğrenci sayısı kadar)" kalıbı |
| Yönerge | öğretmene, madde işaretli uygulama basamakları ("…dağıtınız", "…isteyiniz", "…sağlayınız") |

Künyeden sonra:

- **Ek 1 — öğrenci sayfası:** etkinliğin kendisi. Desteklemede: çözümlü
  örnek + basamaklandırılmış görev + görsel/model alanı; zenginleştirmede:
  açık uçlu derinleştirme görevi, gerekçelendirme ve üretim istemi.
- **Ek 2 — değerlendirme:** desteklemede kontrol listesi veya öz
  değerlendirme; zenginleştirmede öz değerlendirme + paylaşım/yansıtma
  yönergesi. Ölçütler süreç bileşenlerinden türetilir.

Kurallar:
- Hedef çıktı kodu + ifadesi her pakette birebir görünür.
- Kavram izlenebilirliği: mevcut materyal verildiyse onun kavram seti,
  verilmediyse çıktı + branş dolgu listesi sınırdır.
- Desteklemede yanılgı envanterinden en az bir yaygın hata, etkinliğin
  içinde açıkça önlenir (ör. karşı örnekle gösterilir).
- İki paket aynı senaryonun kopyası olmaz; destekleme somut/tanıdık,
  zenginleştirme açık uçlu/derin bağlam kullanır.

## Adım 4 — Çıktı üretimi

A4 şablon kuralları geçerlidir (`../tymm-ders-planlama/assets/sablon-a4.html`
temel alınır). Her paket kendi dosyasında; Ek 1 ve Ek 2 sayfa başında
başlar. Cevap/ölçüt içeriği öğrenci sayfasına sızmaz (Ek 2 değerlendirme
öğrencinin kendisi içinse sızıntı sayılmaz). Dipnot standardı uygulanır.
Teslim notunda etkinliklerin örnek olduğu ve sınıfa göre uyarlanabileceği
bir cümleyle belirtilir.

## Adım 5 — Teslimden önce denetim (zorunlu)

Paketleri teslim etmeden ÖNCE şu dört kontrolü yap:

1. **Hedef korunumu:** Destekleme hedefi düşürmüyor (aynı çıktı);
   zenginleştirme içerik çerçevesinin dışına (sonraki sınıf konusuna)
   çıkmıyor mu?
2. **Kavram seti + adlandırma:** Mevcut materyal verildiyse kavram seti
   korunmuş mu? Sınıflandırma etkinliğinde örneği ADIYLA verip cevabı
   sızdırdın mı?
3. **Yanılgı + bilim:** Desteklemede en az bir yaygın hata etkinlik içinde
   önleniyor; olgular doğru mu?
4. **İzlenebilirlik + sızıntı:** Hedef çıktı kodu/ifadesi birebir; Ek 2
   değerlendirme ölçütleri öğrenci etkinlik sayfasına sızmamış mı?

Karşılanmayan madde varsa düzelt. **Bu öz-denetim öğretmen incelemesinin
yerini tutmaz.**

## Kapsam dışı

Sıfırdan ders paketi (`tymm-ders-planlama`), test üretimi
(`tymm-baglam-testi`), ortak yazılı (`tymm-acik-uclu-sinav`), BEP/RAM
resmî evrakı (istenirse beceri dışında yardım edilir).
