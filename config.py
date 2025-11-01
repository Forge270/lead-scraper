import os

# Arama ayarları - Türkiye'den gerçek siteler
TARGET_WEBSITES = [
    'https://www.digitalage.com.tr/iletisim/',
    'https://www.brandingturkiye.com/iletisim/',
    'https://www.pazarlamasyon.com/iletisim/',
    'https://www.webtures.com.tr/iletisim',
    'https://www.socialmatik.com/iletisim/',
    'https://www.inomera.com/iletisim',
    'https://www.istanbulreklam.com/iletisim',
    'https://www.dijitalajanslar.com/iletisim/',
]

# Google arama (opsiyonel - manuel URL yerine)
GOOGLE_SEARCH_QUERIES = [
    'istanbul dijital pazarlama ajansı iletişim',
    'ankara yazılım şirketi contact',
]

# Çıktı ayarları
OUTPUT_FOLDER = 'leads'
OUTPUT_FORMAT = 'excel'  # 'excel' veya 'csv'

# Email/telefon regex patterns
EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
PHONE_PATTERNS = [
    r'\+90\s?\d{3}\s?\d{3}\s?\d{2}\s?\d{2}',  # +90 XXX XXX XX XX
    r'0\d{3}\s?\d{3}\s?\d{2}\s?\d{2}',        # 0XXX XXX XX XX
    r'\(\d{3}\)\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}',  # (XXX) XXX XX XX
]

# User agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Rate limiting (saniye)
REQUEST_DELAY = 2

# Maksimum sayfa sayısı
MAX_PAGES_PER_SITE = 10