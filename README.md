# TYMM Öğretim Becerileri

Türkiye Yüzyılı Maarif Modeli'ne (TYMM) hizalı, Claude için öğretim
becerileri. Anthropic + Learning Commons'ın açık kaynak
[k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills)
mimarisinin (Apache 2.0) Türk müfredatına uyarlamasıdır.

Temel fark: Learning Commons Knowledge Graph bağlayıcısının yerini,
`references/kazanimlar/` altındaki **statik öğrenme çıktısı dosyaları** alır.
Beceri, plan üretmeden önce bu dosyaları okumak zorundadır; böylece plan
modelin ezberinden değil, doğrulanmış program verisinden üretilir. Veri
dosyası bulunmayan sınıf/branşlar için beceri yine çalışır ve plana bir
doğrulama uyarısı ekler.

## Kapsam (v0.6)

- İki beceri: **tymm-ders-planlama** ve **tymm-baglam-testi**
- Dört branş: **matematik, Türkçe, fen bilimleri, sosyal bilgiler**
- Kapsam hedefi: **5-8 ortaokul** (5-6-7 TYMM; 8 eski program)
- Doğrulanmış veri: **dört branş × 5-6-7. sınıf** — resmî tema/ünite
  sayfalarından birebir (Türkçe'de süreç bileşeni dökümü kaynakta yok)
- Çıktı: A4 baskıya hazır 3 HTML — ders planı, çalışma kağıdı (100 puanlık,
  KB1/KB2/KB3 kademeli), öğrenme kanıtları (cevap anahtarı + gözlem odakları)

## Klasör yapısı

```
skills/tymm-ders-planlama/
  SKILL.md                     Becerinin tetikleme ve adım talimatları
  references/<brans>.md        Branş pedagojisi (matematik/turkce/fen-bilimleri/sosyal-bilgiler)
  references/konu-anlatimi.md  Etkileşimli konu anlatımı HTML kuralları
  references/mufredat-durumu.md ⚠️ ZORUNLU İLK OKUMA — sınıf/müfredat durumu + sınav türü kuralları
  references/kazanimlar/       Sınıf-branş öğrenme çıktısı verisi (4 branş × 6. sınıf)
  assets/sablon-a4.html        Baskı çıktılarının ortak A4 şablonu
skills/tymm-baglam-testi/
  SKILL.md                     Düzeyli bağlam testi becerisi (3 × 10 soru)
  references/kilavuz-ilkeleri.md    ⚠️ ZORUNLU İLK OKUMA — resmî soru yazım kılavuzu ilkeleri
  references/test-matematik.md      Matematik yanılgı envanteri + bağlam aileleri
  references/test-diger-branslar.md Türkçe/fen/sosyal yanılgı envanteri + bağlam aileleri
KULLANIM.md                    Öğretmenler için istem rehberi (açık/örtük/kapsam dışı örnekler)
evals/
  tymm-ders-planlama/rubrik-matematik.csv   (14 kriter)
  tymm-baglam-testi/rubrik-matematik.csv    (15 kriter)
  tetikleme/tetikleme-seti.csv              (27 istem — KULLANIM.md ile aynı set)
```

## Kurulum (claude.ai)

1. `skills/tymm-ders-planlama/` klasörünü zip'leyin (SKILL.md kökte olacak
   şekilde).
2. claude.ai → Settings → Capabilities → Skills → **Upload skill**.
3. Yeni sohbette deneyin: *"Yarın 6. sınıfta bölünebilme kurallarını
   işleyeceğim, plan hazırlar mısın?"*

Claude Code kullanıyorsanız klasörü `~/.claude/skills/` altına
kopyalamanız yeterlidir.

## Yeni sınıf/branş ekleme

1. `references/kazanimlar/<sinif>-sinif-<brans>.md` dosyasını, mevcut
   dosyanın sonundaki şablona göre oluşturun (tema tablosu + kodlu çıktılar).
2. Yeni branşsa `references/<brans>.md` pedagoji dosyasını yazın ve
   SKILL.md'nin Adım 0 branş listesine ekleyin.
3. `evals/` altına branş rubriğini ekleyin.

## Sürüm notları

- **v0.7.3 — Veri katmanı tamamlandı: dört branş × 5-6-7. sınıf.** 57 resmî
  tema/ünite/öğrenme alanı sayfası (tymm.meb.gov.tr PDF'leri) ayrıştırılarak
  9 kazanım dosyası üretildi/yeniden kuruldu:
  - **Fen 5/6/7:** tüm üniteler, süreç bileşenleriyle (28/36/36 çıktı) —
    önceki kısmi dosyaların (5: Ü1-3, 6: Ü1-4) yerini tam sürüm aldı.
  - **Sosyal 5/6/7:** tüm öğrenme alanları, süreç bileşenleriyle
    (19/18/17 çıktı) — doğrulanmamış 6. sınıf dosyası değiştirildi.
  - **Türkçe 5/6/7:** tema bazlı çıktı listeleri birebir (100/100/102 tekil
    kod). Resmî tema sayfaları süreç bileşeni dökümü yayımlamadığından
    dosyalara bu sınırı belirten not eklendi; beceriler Türkçe'de süreç
    bileşeni katmanını zorlamaz.
  - Her tema/ünite başlığında ders saati, alan/kavramsal beceriler,
    eğilimler, SDB, değerler, okuryazarlık, disiplinler arası ilişkiler,
    içerik çerçevesi ve anahtar kavramlar da resmî sayfadan aktarıldı.
  - Kaynaktaki bir dizgi hatası ayrıştırıcıda tolere edildi
    (`SB 7.1.1.` → `SB.7.1.1.`); 2. dönem üniteleri dahil olduğundan yol
    haritasındaki "2. dönem çıktı verileri" maddesi de kapandı.

- **v0.7.2 — KULLANIM.md ve tetikleme eval tohumu.** Öğretmenler için istem
  rehberi eklendi: açık/örtük/sınır/kapsam dışı 27 örnek istem, varsayılanlar
  tablosu, ortak yazılı kuralı ve ipuçları. Aynı set makine okunur biçimde
  `evals/tetikleme/tetikleme-seti.csv` dosyasına yazıldı (id · kategori ·
  istem · beklenen beceri · beklenen davranış); iki liste birlikte
  güncellenir.

- **v0.7.1 — Test becerisinin resmî kılavuza hizalanması.** `tymm-baglam-testi`
  soru yazım kuralları, MEB'in *TYMM Bağlam Temelli Çoktan Seçmeli Soru
  Yazım Kılavuzu*'ndan (Mart 2026) yeniden yazıldı:
  1. Yeni ortak dosya `references/kilavuz-ilkeleri.md` — kılavuzun 2.
     bölümündeki yazım akışı, bağlam kurgulama, soru kökü/seçenek/çeldirici
     kuralları, bilişsel yük ilkeleri, sık yapılan hatalar tablosu, yayın
     öncesi kontrol listesi ve soru yazım formunun anahtar belgesine
     eşlenmesi. Branş dosyalarıyla çelişme hâlinde bu dosya esastır.
  2. **Bağlam işlevsellik testi zorunlu:** bağlam okunmadan çözülebilen soru
     yeniden kurgulanır; tersi de hata — çözüm için gereken her bilgi
     bağlamda verilirse soru okuduğunu anlamayı ölçer.
  3. Yeni yasaklar: ipucu zinciri ("bir önceki soruda bulduğunuz…"), çift
     olumsuzluk, öznel kök, bağlamdan birebir alıntı seçenek, seçenek
     uzunluk/biçim farkı, dar erişimli veya taraflı bağlam, metni tekrar
     eden dekoratif görsel.
  4. Soru artık çıktıya değil **çıktının süreç bileşenine** yazılıyor;
     anahtar belgesi süreç bileşeni harfi, bağlam adı ve (varsa) gerçek veri
     kaynağını kaydediyor.
  5. `test-matematik.md` bu ilkelerin matematiğe özgü uygulaması olarak
     yeniden yazıldı (hatalı/doğru kurgu tablosu, yasaklı bağlamlar, sayı
     gerçekçiliği, sayısal seçenek biçimi, grafik kuralları); yanılgı
     envanterine oran-orantı/ölçek ve birim fiyat yanılgıları eklendi.
  6. Test rubriği 10 → 15 kritere çıkarıldı (T11-T15: kılavuz uyumu ve
     izlenebilirlik).

- **v0.7 — Veri katmanının genişlemesi.** Matematik 5/6/7 öğrenme çıktıları
  resmî tema sayfalarından birebir kuruldu (süreç bileşenleri dahil);
  `beceri-cercevesi.md` birincil kaynaklardan doğrulandı. Ayrıntılı veri
  durumu için `CLAUDE.md`.

- **v0.6 — Resmî kaynak doğrulaması (kritik düzeltmeler).** Öğretmenin
  sağladığı resmî TYMM kaynaklarıyla veri katmanı yeniden kuruldu:
  1. **Kod deseni düzeltildi:** Fen çıktıları dört parçalıdır
     (`FB.5.2.3.1`), üç parçalı değil. Önceki dosyalardaki kod deseni hatalıydı.
  2. **Süreç bileşenleri eklendi:** Her çıktının a) b) c) ç) maddeleri
     resmî programdan birebir alındı; artık uydurulmuyor.
  3. **5. sınıf fen verisi oluşturuldu** (Ü1 tam + Ü2-3 çıktılar);
     **6. sınıf fen verisi doğrulanmış hâliyle yeniden yazıldı** (Ü1-4).
  4. **Müfredat geçiş durumu belgelendi** (`mufredat-durumu.md`): 5-6. sınıf
     TYMM, 7-8. sınıf (2025-26 itibarıyla) eski program. Beceriler artık
     sınıfa göre doğru terminolojiyi kullanıyor.
  5. **SINAV TÜRÜ KURALI:** MEB yönetmeliğine göre ortak yazılı sınavlarda
     çoktan seçmeli soru kullanılamaz. `tymm-baglam-testi` çıktılarına
     "alıştırma/deneme amaçlıdır" ibaresi zorunlu hâle getirildi; öğretmen
     ortak yazılı isterse beceri açık uçlu sınav üretiyor.

- **v0.5** — Çok branşlı genişleme: ders-planlama ve bağlam-testi becerilerine
  Türkçe, fen bilimleri ve sosyal bilgiler eklendi. Her branşın kendi pedagoji
  dosyası (TAB/FBAB/SBAB bileşen haritaları) ve 6. sınıf öğrenme çıktısı verisi
  var. Ders ders ayrı beceri YAPILMADI — branş bir referans dosyasıdır, iskelet
  ortaktır; iş türü (planlama vs test) beceriyi belirler. Ayrıca v0.4.1: öğrenci
  test dosyalarına anahtar stillerinin sızmaması kuralı.

- **v0.4** — Zenginleştirme sürümü: (1) çoklu çalışma kağıdı seçeneği
  (amaç ayrışmalı: ders içi / ev pekiştirme / karışık tekrar), (2) yeni
  beceri `tymm-baglam-testi` — düzeyli 3 × 10 bağlam temelli test, yanılgı
  envanterinden türetilen çeldiriciler ve seçenek dengesi kuralı, (3)
  isteğe bağlı etkileşimli `konu-anlatimi.html` çıktısı (özgün gömülü SVG
  görseller, anında dönütlü alıştırmalar, öğretmenin link yapıştıracağı
  Video köşesi — beceri hiçbir dış video linki üretmez ve gömmez).
- **v0.3** — İlk rubrik puanlamasının (11/14 tam, 3 kısmen) düzeltmeleri:
  dipnot standardı (nötr yapay zekâ bildirimi; beceri/sürüm adı belgelere
  sızamaz) ve kapsam-gerekçe kuralı (çıktı başına ortalama saatin belirgin
  altındaki planlar Varsayımlar satırında gerekçelendirilir) eklendi.
- **v0.2** — Kavram izlenebilirliği kuralı eklendi: çalışma kağıdında
  adlandırılan her kavram, ders planı akışında inşa edilmiş olmalı; çıktı
  metninden gelmeyen kavramsal dolgu, planın Varsayımlar satırında bildirilir.
  Rubriğe M14 kriteri eklendi. (İlk simülasyon testinin bulgusu.)
- **v0.1** — İlk pilot: tymm-ders-planlama becerisi + 6. sınıf matematik
  verisi + A4 şablon + 13 kriterli rubrik.

## Yol haritası

- [x] Pilotu gerçek bir istekle simüle etme (bölünebilme kuralları paketi)
- [x] Simülasyon paketini rubrikle puanlama (11/14 tam → v0.3 düzeltmeleri)
- [ ] Gerçek sınıf denemesi
- [x] `tymm-baglam-testi` becerisi (düzeyli bağlam testleri)
- [ ] `tymm-ders-farklilastirma` becerisi (mevcut dersi kademelendirme)
- [x] Test soru yazım kurallarını resmî kılavuzdan yeniden yazma (v0.7.1)
- [x] KULLANIM.md — öğretmen istem rehberi + tetikleme eval tohumu (v0.7.2)
- [ ] Konu anlatımı ve test çıktılarının ilk rubrik puanlaması
- [x] Diğer branşlar: Türkçe, Fen Bilimleri, Sosyal Bilgiler (6. sınıf)
- [x] 5. sınıf fen verisi (1. dönem) — resmî kaynaktan doğrulandı
- [x] 5-6-7. sınıf: dört branşın verisi resmî kaynaktan kuruldu (v0.7.3)
- [x] 2. dönem ünitelerinin çıktı verileri (v0.7.3 — tüm üniteler dahil)
- [ ] Açık uçlu ortak yazılı sınav becerisi (yönetmeliğe uygun)
- [ ] 7-8. sınıf: güncel müfredat durumuna göre karar
- [ ] Diğer sınıf düzeyleri (5-8)

## Lisans ve kaynaklar

- **Mimari:** anthropics/k12-teacher-skills (Apache 2.0)
- **Öğrenme çıktısı verisi (doğrulanmış):**
  - tymm.meb.gov.tr — resmî ünite sayfaları ve öğretim programları
  - MEB Konu Soru Dağılım Tabloları (Ekim 2025) — çıktı + süreç bileşenleri
  - mufredat.meb.gov.tr — eski program kazanımları (7-8. sınıf)
- **Ölçme kuralları:** MEB Ölçme ve Değerlendirme Yönetmeliği; TYMM Çoktan
  Seçmeli Soru Yazım Kılavuzu
- **Doğrulama durumu her kazanım dosyasının başında belirtilmiştir.**
  ✅ doğrulanmış / ⚠️ kısmi / ❌ veri yok
