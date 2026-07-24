# Örnekler — denetimden geçmiş referans paketler

Bu klasör, becerilerle üretilip **sınıfta denenen**, ardından rubrikle
(planlama M01-M14, test T01-T16) içerik denetiminden geçirilip düzeltilen
örnek çıktıları tutar. Amaç: "iyi çıktı neye benzer" sorusunun kalıcı,
sürüm kontrollü cevabı olmak ve ileride tetikleme/kalite evallerine tohum
sağlamak.

`ciktilar/` klasöründen farkı: orası günlük, atılabilir üretim alanıdır ve
`.gitignore`'dadır; burası **incelenmiş ve onaylanmış** sürümdür, depoda kalır.

## Paketler

### `fen5-u3-canlilarin-yapisi/` — 9 belge
5. sınıf Fen, **3. Ünite: Canlıların Yapısına Yolculuk**
(çıktılar FB.5.3.1.1 · FB.5.3.1.2 · FB.5.3.2.1 · FB.5.3.2.2).
- `konu-anlatimi.html` — etkileşimli ekran belgesi (gömülü SVG, anında dönütlü alıştırma)
- `calisma-kagidi-1/2/3.html` — ders içi / ev pekiştirme / karışık tekrar (her biri 100 puan)
- `ogrenme-kanitlari.html` — üç kâğıdın anahtarı + yanılgı→müdahale + gözlem odakları
- `test-duzey-1/2/3.html` — Temel/Gelişen/İleri 10'ar soru
- `test-anahtari.html` — cevap + çeldirici→yanılgı eşlemesi + KB/denge denetimi

**Denetim düzeltmeleri (bu paket):**
1. Soğan zarına kloroplast atfeden bilimsel hata giderildi — bitki hücresi
   örneği, kloroplast iddia edilen her yerde **yaprak (yeşil yaprak)** ile
   değiştirildi (soğan yumru zarı ışık görmez, kloroplast içermez). Soğan
   yalnızca hücre duvarı/zar bağlamında (doğru olduğu yerde) korundu.
2. Bir çoktan seçmeli soruda oluşan "Hiçbiri ortak değildir" seçeneği,
   soruyu veriden çıkarım yaptırmaya çevirerek giderildi.
3. İleri düzey iki soru (D3-3, D3-4) **katmanlı bağlamla** zenginleştirildi:
   öğrenci çok satırlı veri tablosundan ilgili olanı ayıklar.

### `fen5-yazili-u1-4/` — 3 belge
5. sınıf Fen, **1-4. Ünite** yönetmeliğe uygun **açık uçlu ortak yazılı**
(FB.5.1.2.1 · FB.5.2.1.1 · FB.5.2.3.1 · FB.5.3.1.1 · FB.5.3.1.2 · FB.5.4.2.1).
- `konu-soru-dagilimi.html` — sınav öncesi öğrenciyle paylaşılan tablo
- `sinav.html` — 6 açık uçlu soru, 100 puan
- `puanlama-anahtari.html` — örnek yanıt + süreç bileşenine bağlı kısmi puan + yaygın hata

Denetimde içerik hatası bulunmadı; anahtar tam doğru. Referans olarak eklendi.

### `fen5-u3-acik-uclu/` — 3 belge
5. sınıf Fen, **3. Ünite** (Canlıların Yapısına Yolculuk) için yönetmeliğe
uygun **açık uçlu ortak yazılı** — düzey testleri/kâğıtlarla aynı konu
(FB.5.3.1.1 · FB.5.3.1.2 · FB.5.3.2.1 · FB.5.3.2.2). 6 soru, 100 puan; her
çıktı tam 25 puan.
- `konu-soru-dagilimi.html` · `sinav.html` · `puanlama-anahtari.html`

**Denetim düzeltmeleri (Katman 2 muhakeme):**
1. Soru 1-b: hücreler "yaprak/yanak" diye adlandırılınca "hangi canlıya
   ait?" sorusu tabloyu okumadan (ad → bitki) cevaplanabiliyordu →
   hücreler anonimleştirildi (1./2. hücre); sınıflandırma verilerden yapılır.
2. Soru 2-b: kavram adları düzeyi ele veriyordu ("kalp kası **hücresi**",
   "kas **dokusu**") → b) yalnız "kalp"(organ) ve "insan"(organizma)
   basamaklarına ve bunların nasıl oluştuğuna odaklandı.
Her iki düzeltmenin kök ilkesi — *sınıflandırma sorusunda adlandırma
cevabı sızdırır* — `kilavuz-ilkeleri.md` §2'ye üretim uyarısı olarak
işlendi.
