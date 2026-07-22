# Konu Anlatımı Belgesi — etkileşimli HTML kuralları

`tymm-ders-planlama` becerisi, öğretmen konu anlatımı belgesi istediğinde
bu dosyayı yükler. Bu belge bir **ekran belgesidir** (akıllı tahta, tablet,
ev bilgisayarı); A4 baskı şablonu ve kuralları burada GEÇERSİZDİR.

## Teknik zemin

- Tek, kendine yeten HTML dosyası: tüm CSS, JS ve görseller gömülü; dış
  kütüphane, CDN, font veya resim çağrısı YOK. Belge internetsiz açılır.
- `localStorage`/`sessionStorage` kullanılmaz; durum sayfa içi JS
  değişkenlerinde tutulur (sayfa yenilenince sıfırlanması sorun değildir).
- Dokunmatik uyum esastır: sürükle-bırak yerine tıkla-seç; tıklanabilir
  hedefler en az 44 px; hover'a bağlı hiçbir bilgi yoktur.
- Yazı ekran için boyutlanır (taban 16-18 px); ders planındaki renk
  paletiyle (vurgu #0f4c81 ailesi) tutarlı kalınır.

## Görseller

- Tüm görseller **özgün, belge içine gömülü SVG** olarak çizilir: bağlam
  sahnesi (ör. kermes tezgâhı, okul bahçesi), şemalar, sayı doğruları.
  Basit geometrik stil yeterlidir; amaç süs değil bağlamı görünür kılmak.
- Hazır fotoğraf, stok görsel, tanınabilir karakter/marka/logo, başka bir
  eserin kopyası KULLANILMAZ. Gerçek kişi çizilmez; figürler nötr ve
  temsilîdir.
- Her SVG'ye kısa bir erişilebilirlik başlığı (`<title>`) eklenir.

## Video köşesi

- Beceri hiçbir dış video linki üretmez, gömmez veya önermez — var olmayan
  ya da eskiyecek bir bağlantı uydurmak kritik hatadır.
- Belgeye standart bir **"Video köşesi"** kutusu konur: konu başlığına uygun
  bir açıklama satırı + öğretmenin kendi linkini (EBA, okul hesabı vb.)
  yapıştıracağı görünür alan ve "buraya bağlantınızı ekleyin" yönergesi.
- Sohbet ortamında web araması açıksa öğretmene gerçek bir video birlikte
  aranabilir; bu, belgenin dışında yürütülen ayrı bir yardımdır.

## İçerik yapısı (bölüm sırası)

1. **Bağlam sahnesi:** Ders planındaki senaryonun SVG çizimi + iki-üç
   cümlelik açılış; çözülmemiş soru ekranda asılı kalır.
2. **Keşif alanı:** Ders planındaki keşif etkinliğinin ekran hâli —
   ör. tıklanınca ✓/✗ durumu ve tek satırlık gerekçesi açılan sayı
   tablosu. Önce tahmin, sonra tıklayıp görme akışı korunur.
3. **Kural kartları:** Her kural bir aç-kapa karttır: ön yüz kuralın adı ve
   kriteri, arka yüz bir örnek + bir karşı örnek. Kartlar ders planındaki
   Kavramsallaştırma sırasını izler.
4. **Anında dönütlü mini alıştırmalar:** 4-6 kısa soru; öğrenci cevabı
   seçer/yazar, "Kontrol et" düğmesiyle dönüt alır. Dönüt yalnızca
   doğru/yanlış demez, yanılgıya özgü tek cümlelik açıklama verir
   (çeldirici dönütleri ders planındaki yanılgı tablosundan türetilir).
   PUAN YOKTUR — bu belge ölçme aracı değildir; ölçme çalışma kağıdının
   ve testlerin işidir.
5. **Video köşesi** (yukarıdaki kurallarla).
6. **Özet şeması:** Tek ekranlık görsel özet (ör. kural → neye bakar
   eşleme şeması) + "kendini dene" yönlendirmesi ile çalışma kağıdına köprü.

## Tutarlılık kuralları

- Kavram izlenebilirliği burada da geçerlidir: belgede adlandırılan her
  kavram ders planı akışında kurulmuş olmalıdır; konu anlatımı plana yeni
  kavram SOKAMAZ.
- Senaryo, sayılar ve kural dili ders planı/çalışma kağıdıyla aynı evrenden
  gelir; belge kendi başına farklı bir bağlam uydurmaz.
- Dipnot standardı geçerlidir (SKILL.md Adım 4); ek olarak "bu belge ekran
  kullanımı içindir, baskı düzeni garanti edilmez" notu düşülür.
