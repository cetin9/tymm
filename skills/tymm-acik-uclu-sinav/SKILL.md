---
name: tymm-acik-uclu-sinav
description: >
  MEB yönetmeliğine uygun, açık uçlu / kısa cevaplı ORTAK YAZILI SINAV paketi
  üretir: konu soru dağılım tablosu + sınav kağıdı + dereceli puanlama
  anahtarı (ayrı belge); hepsi A4 baskıya hazır HTML. Bir öğretmen "ortak
  yazılı", "yazılı sınav", "klasik sınav", "açık uçlu sınav" veya "yazılı
  sorusu" istediğinde kullan — sınıf veya konu henüz söylenmemiş olsa bile,
  netleştirme sorusundan ÖNCE yükle. Ortak yazılılarda çoktan seçmeli
  KULLANILAMAZ; öğretmen çoktan seçmeli test/tarama/deneme isterse bu beceri
  DEĞİL tymm-baglam-testi kullanılır. Desteklenen branşlar: matematik,
  Türkçe, fen bilimleri, sosyal bilgiler.
license: Apache-2.0 (kaynak: anthropics/k12-teacher-skills mimarisinin uyarlaması)
---

# TYMM Açık Uçlu Ortak Yazılı Sınav

Tek turda üç belge üretir: `konu-soru-dagilimi.html` (sınav öncesi
öğrenciyle paylaşılan tablo), `sinav.html` (öğrenci kağıdı),
`puanlama-anahtari.html` (dereceli puanlama anahtarı + örnek yanıtlar).

"Öğretmen", konuştuğun kullanıcıdır. Dipnot standardı diğer becerilerle
aynıdır (çıktı kodu · sayfa · yapay zekâ bildirimi · varsa doğrulama
uyarısı; beceri/sürüm adı belgelere sızmaz). Teknik iç terimler kullanıcıya
görünmez.

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
2. Branş yanılgı envanterini oku (kısmi puanlama ve "yaygın hata"
   satırları için): matematik →
   `../tymm-baglam-testi/references/test-matematik.md`; diğerleri →
   `../tymm-baglam-testi/references/test-diger-branslar.md`.
3. `../tymm-ders-planlama/references/kazanimlar/` altından sınıf-branş
   dosyasını oku; çıktı ifadeleri ve süreç bileşenleri oradan birebir
   alınır. Dosya yoksa doğrulama uyarısıyla ilerlenir.

## Adım 1 — Netleştirme (en fazla bir tur, en fazla üç soru)

Öncelik: (1) sınıf düzeyi, (2) kapsam — hangi çıktılar/temalar? ("dönem
başından bu yana" denirse `../tymm-ders-planlama/references/tema-sirasi.md`
işleniş sırasından belirle), (3) sınav yapısı.

Varsayılanlar: 1 ders saati (40 dk), 10 soru (açık uçlu ağırlıklı, en çok
3 kısa cevaplı), 100 puan, tek ortak yazılı.

## Adım 2 — Konu soru dağılım tablosu

Ortak yazılı soruları, zümrenin seçtiği bir **konu soru dağılım tablosu**
senaryosuna göre hazırlanır ve tablo sınavdan önce öğrenciyle paylaşılır.
Bu yüzden ilk belge budur:

- Satır: hedef çıktı (kod + ifade birebir) · hedeflenen süreç bileşen(ler)i
  · soru numarası/numaraları · soru türü (açık uçlu / kısa cevaplı) · puan.
- Puanlar çıktıların ders saati ağırlığıyla orantılı dağıtılır; toplam 100.
- Kapsamdaki her çıktıya en az bir soru düşer; tek çıktıya 25 puandan
  fazla yüklenmez.

## Adım 3 — Soru yazım kuralları

- **Format:** yalnızca açık uçlu ve kısa cevaplı. Kısmen bile çoktan
  seçmeli/eşleştirme/doğru-yanlış içeren soru yazılamaz.
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
- **Bağlam zenginliği kademeye göre ölçeklenir** (`kilavuz-ilkeleri.md` §5):
  temel sorularda tek veri; muhakeme/gerekçelendirme sorularında **katmanlı
  bağlam** — öğrencinin ayıklaması gereken, işe yaramayan veri de içeren
  zengin durum. Kılavuz üst düzey için "pürüzsüz, hazır sunulmuş ortam"
  yasaktır der. MEB örnek sorularının uzunluğu bu katmanlılıktan gelir;
  uzunluk dekoratif değil işlevsel olduğu sürece kısaltılmaz.
- **Alt basamaklı sorular:** bir soru a-b-c alt maddelerine bölünebilir;
  alt maddeler bağımsız puanlanır ve ipucu zinciri kurmaz (a'yı yapamayan
  b'yi yapabilmelidir).
- **Kavram izlenebilirliği:** sorularda kullanılan kavramlar çıktı
  ifadeleri + branş dosyasındaki dolgu kavram listesiyle sınırlıdır.
- Yönerge net olur: istenen ürün (işlem, açıklama, çizim, tablo) ve puan
  her sorunun yanında görünür.

## Adım 4 — Dereceli puanlama anahtarı

`puanlama-anahtari.html` ayrı belgedir ve şunları içerir:

- Soru başına **örnek tam yanıt** (birden çok geçerli çözüm varsa en yaygın
  ikisi).
- **Kısmi puan basamakları:** süreç bileşenlerine bağlanmış ölçütler
  (ör. "modeli doğru kurdu: 4p · işlemi doğru yürüttü: 4p · sonucu
  yorumladı: 2p"). Basamak toplamları soru puanına eşittir.
- **Yaygın hata satırı:** yanılgı envanterinden, o soruda beklenen hatalar
  ve bunlara puan verilip verilmeyeceği.
- Toplam puan sayımı (100 kontrolü) ve sınıf içi uygulama notu.

## Adım 5 — Çıktı üretimi

A4 şablon kuralları geçerlidir (`../tymm-ders-planlama/assets/sablon-a4.html`
temel alınır): soru blokları sayfa sonunda bölünmez, üstte okul/ders/sınıf/
süre başlık alanı ve öğrenci ad satırı, cevaplar için yeterli boş alan
bırakılır. Öğrenci kağıdına anahtar içeriği veya stili sızmaz. Üç belge tek
turda teslim edilir; teslim notunda konu soru dağılım tablosunun sınavdan
önce öğrencilerle paylaşılması gerektiği hatırlatılır.

## Adım 6 — Teslimden önce denetim (zorunlu)

Teslimden ÖNCE her soruyu şu dört kontrolden geçir (ayrıntı:
`../tymm-baglam-testi/references/kilavuz-ilkeleri.md` §6):

1. **İşlevsellik + adlandırma sızıntısı:** Soru bağlam/veri okunmadan
   çözülüyor mu? Sınıflandırma sorusunda örneği ADIYLA verip cevabı
   sızdırdın mı? (§2 üretim uyarısı; örneği anonimleştir.)
2. **Bilimsel doğruluk + örnek yanıt:** Olgu doğru mu; her sorunun örnek tam
   yanıtı tutarlı ve tek mi?
3. **Yönetmelik + puanlama:** Yalnız açık uçlu/kısa cevaplı (çoktan seçmeli
   YOK); kısmi puan basamaklarının toplamı soru puanına, sorular 100'e
   kapanıyor mu?
4. **İzlenebilirlik:** Her soru süreç bileşenine yazılmış; hiçbir çıktı 25
   puanı aşmıyor; kod/ifade birebir mi?

Karşılanmayan madde varsa soruyu yeniden yaz. **Bu öz-denetim öğretmen
incelemesinin yerini tutmaz.**

## Kapsam dışı

Çoktan seçmeli test/tarama/deneme (`tymm-baglam-testi`), ders planı ve
çalışma kağıdı (`tymm-ders-planlama`), hazır sınavın puanlanması veya
tahlili, not hesaplama ve e-Okul işlemleri.
