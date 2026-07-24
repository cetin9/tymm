# Araçlar

- `pdf_metin_cikar.py` + `kazanim_uret.py` — kazanım verisi üretim hattı
- `denetim.py` — üretim çıktılarının otomatik (deterministik) denetimi

## denetim.py — çıktı denetimi (Katman 1)

Bir üretim paketini (klasör) alıp TYMM/yönetmelik kurallarının makineyle
denetlenebilen kısmını koşar; kural kural ✓/⚠/✗ raporu verir.

```bash
python tools/denetim.py <paket-klasörü> ...   # belirli paket(ler)
python tools/denetim.py                        # argümansız: ornekler/*/
```
Çıkış kodu HATA varsa 1. Kural listesi ve muhakeme katmanı (Katman 2) için
`evals/DENETIM.md`. Yeni kural eklerken hem temiz hem kasıtlı bozuk paketle
sına (araç bozuğu yakalamıyorsa işe yaramaz).

---

## Kazanım üretim hattı

Resmî tema/ünite PDF'lerinden `references/kazanimlar/` dosyalarını üreten
betikler. Program güncellenirse (veya 8. sınıf TYMM'ye geçince) bu hat
yeniden koşulur.

## Kullanım

```bash
# 1) PDF → UTF-8 metin (kısa yola yazar: C:\ttx — Windows MAX_PATH 260
#    sınırı yüzünden; uzun scratchpad yollarında pdftotext I/O hatası verir)
python tools/pdf_metin_cikar.py

# 2) metin → kazanım .md (C:\ttx\out\ altına üretir)
python tools/kazanim_uret.py

# 3) çıktı dosyalarını İKİ becerinin kazanimlar/ klasörüne kopyala
```

Gereksinimler: `pdftotext` (poppler, `-layout -enc UTF-8`), Python 3.

## Ayrıştırma notları (yeniden koşarken bil)

- **Görünmez karakterler:** tymm.meb.gov.tr sayfa PDF'lerinde U+E000-F8FF
  özel kullanım karakterleri (web ikonları) satır başlarına sızar; bölüm
  başlığı eşleşmesini bozar. `kazanim_uret.py` bunları temizler.
- **Dizgi hatası toleransı:** kaynakta `SB 7.1.1.` (nokta yerine boşluk)
  görüldü; sosyal kod regex'i `SB[. ]` kabul eder ve kodu normalleştirir.
- **Türkçe süreç bileşenleri:** Türkçe tema sayfaları çıktıları bileşen
  dökümü OLMADAN listeler — bu veri eksikliği değil, kaynağın biçimidir;
  üretilen dosyaya sınır notu yazılır.
- **Bölüm yapısı:** fen 4 parçalı kod + "N. Bölüm:" başlıkları; sosyal 3
  parçalı; matematik için ayrı hat (bkz. CLAUDE.md geçmiş notu).
- **Yıllık plan xlsx'leri:** tema-sirasi.md elle bu betiklerin dışında,
  openpyxl ile üretildi; birleşik hücrelerde tema adı yalnız çapa satırda
  durur (taşıma/carry-forward gerekir), hafta deseni `N. Hafta`.
