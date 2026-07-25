# TYMM Çıktı Denetim Yapısı

Bir üretim (ders paketi, test seti, açık uçlu sınav, farklılaştırma paketi)
teslim edilmeden önce **üç tür denetimden** geçer. Bu belge her birinin ne
denetlediğini, nasıl koşulacağını ve hangi rubrik kriterine karşılık
geldiğini tanımlar.

```
Üretim  ─►  ① Tetikleme denetimi   (doğru beceri doğru anda tetiklendi mi)
            ② Katman 1 — otomatik   (tools/denetim.py — mekanik kurallar)
            ③ Katman 2 — muhakeme   (rubrik + LLM-yargıç/insan — anlam)
        ─►  bulguyu beceri dosyasına geri yaz
```

Neden iki katman? Kuralların bir kısmı regex/parser'la **kesin** denetlenir
(kod var mı, puan 100 mü, hepsi/hiçbiri yok mu). Bir kısmı ise **anlamayı**
gerektirir (bağlam işlevsel mi, çeldirici yanılgıyı yakalıyor mu, bilim
doğru mu). Birincisi otomatiktir ve her seferinde koşmalı; ikincisi
rubrikle, gerekiyorsa bir yargıç turuyla yapılır. Sınıf denemesinde
yakalanan gerçek hatalar (soğan-kloroplast, "hiçbiri" kayması, katmansız
İleri düzey) hep **Katman 2**'den çıktı — otomatik denetim onları göremez.

---

## ① Tetikleme denetimi

**Ne:** Bir öğretmen istemi geldiğinde doğru beceri (ya da hiçbiri) devreye
giriyor mu; netleştirme öncesi yükleniyor mu; kapsam dışı istekler doğru
reddediliyor mu.

**Veri:** `evals/tetikleme/tetikleme-seti.csv` — 33 istem
(`id · kategori · istem · beklenen_beceri · beklenen_davranis`).
Kategoriler: açık · örtük · sınır · kapsam-dışı.

**Nasıl:** Her istemi temiz bir oturuma verip hangi becerinin tetiklendiğini
gözle ya da bir yargıç turuyla `beklenen_beceri` ile karşılaştır. Bu liste
`KULLANIM.md` ile **birlikte** güncellenir (biri değişince diğeri de).

---

## ② Katman 1 — Otomatik denetim (`tools/denetim.py`)

**Çalıştırma:**
```bash
python tools/denetim.py <paket-klasörü> [<paket-klasörü> ...]
python tools/denetim.py            # argümansız: ornekler/*/ taranır
```
Çıkış kodu: en az bir **HATA** varsa `1`, aksi hâlde `0` (CI'a bağlanabilir).
Çıktı: kural kural `✓ geçti / ⚠ uyarı / ✗ HATA` + özet.

**Denetlediği kurallar:**

| Kural | Ne denetler | Rubrik |
|---|---|---|
| `G01-dipnot` | Her belgede yapay zekâ bildirimi var | T09 · M dipnot |
| `G02-icad` | Beceri/dosya/sürüm adı belgeye sızmamış | dil |
| `G03-veri` | Her çıktı kodu `kazanimlar/`'da **gerçekten var** (uydurma kod yok) | T01 · M hizalama |
| `T-secenek` | Her testte soru × 4 seçenek | T07 |
| `T-hepsihicbiri` | "Hepsi/Hiçbiri/A ve B" türü seçenek yok | T07 |
| `T-olumsuz` | Olumsuz kök test başına ≤2 (DEĞİLDİR, vurgulu) | T07 |
| `T-ibare` | "Alıştırma/deneme amaçlıdır" ibaresi var | yönetmelik |
| `T-sizinti` | Öğrenci testinde anahtar izi yok | T09 |
| `T-anahtar` | Anahtar ayrı dosyada | T09 |
| `T-denge` | 10 soruda hiçbir harf >4/<1 (anahtardan) | T08 |
| `K-puan` / `K-bolum` | Çalışma kağıdı soru/bölüm toplamı = 100 | çalışma kağıdı |
| `K-ogrenci` | Öğrenci ad/soyad satırı var | çalışma kağıdı |
| `K-sizinti` / `K-anahtar` | Kağıtta cevap yok; anahtar ayrı dosyada | M sızıntı |
| `A-format` | **Ortak yazılıda çoktan seçmeli YOK** (yönetmelik) | Y01 |
| `A-puan` / `A-anahtar` | Sınav 100 puan; puanlama anahtarı ayrı | Y07 |
| `KA-diskaynak` | Konu anlatımı dış kaynak çağırmıyor (internetsiz açılır) | konu-anlatimi |
| `KA-svgtitle` / `KA-storage` | SVG'lerde başlık; storage kullanılmıyor | konu-anlatimi |

**Sınırı:** Bu araç metnin **biçimini** denetler, **anlamını** değil.
"Kod var" der ama "doğru çıktıya mı yazılmış" diyemez; "hepsi/hiçbiri yok"
der ama "çeldirici yanılgıyı yakalıyor mu" diyemez. Onlar Katman 2'dedir.

**Aracı doğrulama:** `denetim.py` hem temiz paketleri geçirdiği hem de kasıtlı
bozuk paketteki 11 hatayı (uydurma kod, hiçbiri, olumsuz kök >2, ibare
eksik, sızıntı, çoktan seçmeli ihlali, puan≠100…) yakaladığı test edilerek
kurulmuştur. Yeni kural eklerken bozuk örnekle de sınayın.

---

## ③ Katman 2 — Muhakeme denetimi (rubrik + yargıç)

Otomatik denetimden geçen paket, rubriğin **anlam gerektiren** kriterlerine
karşı okunur. Rubrikler: `evals/<beceri>/rubrik-matematik.csv`
(planlama 14 · test 16 · açık uçlu 10 · farklılaştırma 10 kriter).

**Bu katmanın kapsadığı (araç göremeyen) kriterler:**

| Boyut | Ne sorulur | Rubrik |
|---|---|---|
| **Bilimsel doğruluk** | Olgu doğru mu? *(soğan-kloroplast burada yakalandı)* | — (kritik) |
| **Tek/benzersiz cevap** | Doğru cevap gerçekten tek mi? İkinci savunulabilir cevap yok mu? | — (kritik) |
| **İşlevsellik testi** | Bağlam okunmadan çözülüyor mu? Tersi: her bilgi hazır mı? | T05 · T11 |
| **Çeldirici geçerliliği** | Yanılgıyı teşhis ediyor mu, rastgele yanlış mı? | T06 |
| **İpucu zinciri** | Aynı bağlamdan sorular bağımsız çözülüyor mu? | T12 |
| **Seçenek homojenliği** | Doğru seçenek uzun/detaylı değil; birebir alıntı yok | T13 |
| **Erişilebilir/tarafsız bağlam** | Marka/gelir/dar alan yok; tarafsız | T14 |
| **Bağlam katmanlılığı** | İleri düzey soruları ayıklanacak veri içeriyor mu? | T16 |
| **Kavram izlenebilirliği** | Soruda geçen kavram çıktı+dolgu listesinde mi? | T02 |
| **Kısmi puan bağı (açık uçlu)** | Basamaklar süreç bileşenine bağlı; toplam = soru puanı | Y07 |

**Skill içine gömülü hâli:** Katman 2'nin en yüksek değerli dört kontrolü,
her SKILL.md'nin sonundaki **"Teslimden önce denetim (zorunlu)"** adımına
işaret olarak konmuştur (kural kopyalanmaz, `kilavuz-ilkeleri.md` §6'ya
yönlendirilir). Böylece skill tek başına claude.ai'a yüklendiğinde bile
üretimden hemen önce öz-denetim tetiklenir. Not: bu öz-denetim, çıktıyı
üreten aynı model tarafından yapıldığından **insan incelemesinin ve bu
belgedeki tam protokolün yerini tutmaz** — otomatik Katman 1 ve elle Katman 2
depo tarafında çalışmaya devam eder.

**Protokol (adım adım):**
1. Katman 1'i koştur; HATA varsa önce onları gider (muhakeme turunu boşa
   harcama).
2. Her soruyu **çöz** ve anahtarla karşılaştır — cevap doğru ve tek mi?
3. Her soruya **işlevsellik testini** uygula: "bağlamı silsem çözülür mü?"
4. Her çeldiriciyi branş **yanılgı envanteriyle** eşle; eşleşmeyen çeldirici
   ya yanılgıya bağlanır ya "rastgele yanlış" sayılır (soru başına ≤1).
5. İleri düzey/muhakeme sorularında **katmanlılık** (T16) ve **bilimsel
   doğruluk** ayrı ayrı denetlenir.
6. Bulguları "soru → sorun → öneri" olarak yaz; düzeltmeyi uygula;
   **kuralın hangi üretim hatasından doğduğunu** ilgili beceri dosyasına
   (`kilavuz-ilkeleri.md`, yanılgı envanteri, SKILL) geri yaz.

**Ölçekleme (isteğe bağlı):** Çok sayıda soru veya yüksek güven gerektiğinde
Katman 2, çok-ajanlı bir yargıç turuyla koşulabilir — her çeldiriciyi
çürütmeye çalışan **adversarial doğrulama**, bilimsel doğruluk için ayrı bir
"olgu denetçisi" ajanı. Bu, tek geçişin kaçırdığı kuyruğu yakalar. Küçük
paketlerde tek dikkatli okuma yeterlidir.

---

## Çalışma döngüsüne bağlanışı

`CLAUDE.md` → "Çalışma döngüsü": üret → **① tetikleme + ② Katman 1 + ③
Katman 2** → bulguyu beceri dosyasına geri yaz. Beceri metnine kural
eklemeden önce kuralın hangi üretim hatasından doğduğu not edilir; bu
belgedeki kural→rubrik eşlemesi o izlenebilirliği taşır.

Denetimden geçmiş referans paketler `ornekler/` altındadır ve "iyi çıktı
neye benzer"in sürüm kontrollü örneğidir.
