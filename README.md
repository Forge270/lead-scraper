# Lead Generation Scraper | Lead Toplama Aracı

[English](#english) | [Türkçe](#turkish)

---

<a name="english"></a>
## 🇬🇧 English

Automated lead generation tool that extracts contact information from websites.

### Features

- 📧 Email extraction
- 📞 Phone number detection
- 🔗 Social media links (Facebook, Twitter, LinkedIn, Instagram)
- 🏢 Company information scraping
- 📊 Excel/CSV export
- 🔍 Automatic contact page detection

### Tech Stack

- Python 3.10+
- BeautifulSoup4 (HTML parsing)
- Requests (HTTP client)
- Pandas (data export)
- Regex (pattern matching)

### Installation

```bash
pip install -r requirements.txt
```

### Configuration

Edit `config.py`:

```python
TARGET_WEBSITES = [
    'https://example.com/contact',
    'https://another-site.com/about',
]
```

### Usage

```bash
python main.py
```

The tool will:
1. Crawl specified websites
2. Extract contact information
3. Generate Excel report in `leads/` folder

### Sample Output

Excel file with columns:
- Company Name
- Email Addresses
- Phone Numbers
- Facebook URL
- LinkedIn URL
- Twitter URL
- Instagram URL
- Source URL

### Use Cases

- B2B sales teams building prospect lists
- Marketing agencies gathering client contacts
- Recruiters finding company information
- Business development lead generation

### Rate Limiting

Built-in delays prevent server overload and respect robots.txt.

### License

MIT

---

<a name="turkish"></a>
## 🇹🇷 Türkçe

Web sitelerinden iletişim bilgisi toplayan otomatik lead oluşturma aracı.

### Özellikler

- 📧 Email çıkarma
- 📞 Telefon numarası tespiti
- 🔗 Sosyal medya linkleri (Facebook, Twitter, LinkedIn, Instagram)
- 🏢 Şirket bilgisi toplama
- 📊 Excel/CSV dışa aktarma
- 🔍 Otomatik iletişim sayfası bulma

### Teknolojiler

- Python 3.10+
- BeautifulSoup4 (HTML işleme)
- Requests (HTTP istemci)
- Pandas (veri dışa aktarma)
- Regex (örüntü eşleştirme)

### Kurulum

```bash
pip install -r requirements.txt
```

### Yapılandırma

`config.py` dosyasını düzenleyin:

```python
TARGET_WEBSITES = [
    'https://ornek.com/iletisim',
    'https://baska-site.com/hakkimizda',
]
```

### Kullanım

```bash
python main.py
```

Araç şunları yapar:
1. Belirtilen web sitelerini tarar
2. İletişim bilgilerini çıkarır
3. `leads/` klasöründe Excel raporu oluşturur

### Örnek Çıktı

Excel dosyası sütunları:
- Şirket Adı
- Email Adresleri
- Telefon Numaraları
- Facebook URL
- LinkedIn URL
- Twitter URL
- Instagram URL
- Kaynak URL

### Kullanım Alanları

- B2B satış ekipleri potansiyel müşteri listeleri
- Pazarlama ajansları müşteri iletişim toplama
- İK uzmanları şirket bilgisi bulma
- İş geliştirme lead oluşturma

### Hız Sınırlama

Yerleşik gecikmeler sunucu yükünü önler ve robots.txt'ye saygı gösterir.

### Lisans

MIT

---

Built with ⚡ by [Forge270](https://github.com/Forge270)
