# Skill Dizini Kartı — TYMM Öğretim Becerileri

Bu dosya, projeyi bir skill dizinine (skills.sh, awesomeclaude.ai, SkillsMP
vb.) veya sosyal medyada/tanıtımda listelerken kopyala-yapıştır
kullanabileceğiniz hazır metinleri içerir.

---

## Kısa tanım (tek satır)

**TR:** TYMM (Türkiye Yüzyılı Maarif Modeli) müfredatına hizalı, Türk
ortaokul öğretmenleri için Claude öğretim becerileri.

**EN:** Claude Agent Skills for Turkish middle-school teachers, aligned to
the Türkiye Yüzyılı Maarif Modeli (TYMM) national curriculum. (Turkish-only
output.)

## Etiketler

`education` · `teaching` · `k12` · `turkish` · `türkçe` · `curriculum` ·
`lesson-planning` · `assessment` · `differentiation` · `turkey` · `meb` ·
`tymm`

---

## Açıklama (dizin gövde metni)

Türkiye Yüzyılı Maarif Modeli (TYMM) ile çalışan 5-8. sınıf öğretmenleri
için dört öğretim becerisi. Anthropic + Learning Commons'ın açık kaynak
[k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills)
mimarisinin Türk müfredatına uyarlaması (Apache 2.0).

Öğretmen doğal dille ister ("6. sınıf bölünebilmeyi işleyeceğim, plan lazım"),
beceri A4 baskıya hazır belgeler üretir:

- **tymm-ders-planlama** — ders planı + çalışma kâğıdı/kâğıtları + öğrenme
  kanıtları + isteğe bağlı etkileşimli konu anlatımı
- **tymm-baglam-testi** — düzeyli (Temel/Gelişen/İleri) bağlam temelli
  çoktan seçmeli test setleri + ayrı cevap anahtarı
- **tymm-acik-uclu-sinav** — yönetmeliğe uygun açık uçlu ortak yazılı:
  konu soru dağılım tablosu + sınav + dereceli puanlama anahtarı
- **tymm-ders-farklilastirma** — Destekleme + Zenginleştirme etkinlik
  paketleri (resmî kılavuz deseni)

**Öne çıkanlar:**
- 📚 **Veriye dayalı:** çıktı kodları ve ifadeler modelin ezberinden değil,
  resmî MEB programlarından aktarılmış statik kazanım dosyalarından okunur
  (4 branş × 5-6-7. sınıf: matematik, Türkçe, fen, sosyal).
- 📏 **Yönetmelik-uyumlu:** ortak yazılıda çoktan seçmeli üretmez; resmî
  Soru Yazım Kılavuzu ilkelerini uygular.
- ✅ **Kendini denetler:** her beceri teslimden önce işlevsellik, bilimsel
  doğruluk, süreç bileşeni hedefleme ve denge kontrollerinden geçer
  (yine de öğretmen incelemesi şarttır).

## Kimler için

TYMM ile çalışan Türk ortaokul (5-8) öğretmenleri. Çıktı ve arayüz Türkçedir.

## Kurulum

- **claude.ai:** İlgili `skills/<beceri>/` klasörünü zip'leyin (SKILL.md
  kökte olacak şekilde) → Settings → Capabilities → Skills → Upload skill.
- **Claude Code:** `skills/` altındaki klasörleri `~/.claude/skills/`
  içine kopyalayın.

Repo: `<GITHUB-URL-BURAYA>`

## Uyarılar

- Yapay zekâ desteğiyle üretilir; **son onay öğretmenindir.**
- MEB ile **resmî bağlantısı yoktur;** telifli MEB kaynakları depoya dahil
  değildir. Kazanım verisi kamuya açık resmî programlardan aktarılmıştır.

## Lisans / Geliştiren

Apache 2.0 · Çetin GÜLTEKİN — MEB Çayırbaşı Fatma Seher Hanım Ortaokulu,
İstanbul · cetin@sile.k12.tr
