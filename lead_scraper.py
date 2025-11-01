import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin, urlparse
import config
from tqdm import tqdm

class LeadScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': config.USER_AGENT})
        self.visited_urls = set()
        self.leads = []
    
    def extract_emails(self, text):
        """Email adreslerini çıkar"""
        emails = re.findall(config.EMAIL_PATTERN, text)
        # Yaygın olmayan uzantıları filtrele
        valid_emails = [email for email in emails if not any(ext in email.lower() for ext in ['.png', '.jpg', '.jpeg', '.gif'])]
        return list(set(valid_emails))
    
    def extract_phones(self, text):
        """Telefon numaralarını çıkar"""
        phones = []
        for pattern in config.PHONE_PATTERNS:
            found = re.findall(pattern, text)
            phones.extend(found)
        
        # Temizle ve normalize et
        cleaned_phones = []
        for phone in phones:
            # Sadece rakamları al
            digits = re.sub(r'\D', '', phone)
            if len(digits) >= 10:  # En az 10 haneli olmalı
                cleaned_phones.append(phone)
        
        return list(set(cleaned_phones))
    
    def extract_social_media(self, soup):
        """Sosyal medya linklerini çıkar"""
        social_links = {
            'facebook': None,
            'twitter': None,
            'linkedin': None,
            'instagram': None
        }
        
        all_links = soup.find_all('a', href=True)
        
        for link in all_links:
            href = link['href'].lower()
            if 'facebook.com' in href:
                social_links['facebook'] = link['href']
            elif 'twitter.com' in href or 'x.com' in href:
                social_links['twitter'] = link['href']
            elif 'linkedin.com' in href:
                social_links['linkedin'] = link['href']
            elif 'instagram.com' in href:
                social_links['instagram'] = link['href']
        
        return social_links
    
    def extract_company_info(self, soup, url):
        """Şirket bilgilerini çıkar"""
        # Başlıktan şirket adını al
        title = soup.find('title')
        company_name = title.get_text(strip=True) if title else urlparse(url).netloc
        
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc['content'] if meta_desc else ''
        
        return {
            'company_name': company_name,
            'description': description,
            'website': url
        }
    
    def scrape_page(self, url):
        """Tek bir sayfadan lead bilgisi topla"""
        if url in self.visited_urls:
            return None
        
        try:
            print(f"🔍 Scraping: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            self.visited_urls.add(url)
            
            soup = BeautifulSoup(response.text, 'lxml')
            text_content = soup.get_text()
            
            # Bilgileri çıkar
            emails = self.extract_emails(text_content)
            phones = self.extract_phones(text_content)
            social = self.extract_social_media(soup)
            company = self.extract_company_info(soup, url)
            
            if emails or phones:
                lead = {
                    'source_url': url,
                    'company_name': company['company_name'],
                    'description': company['description'][:200] if company['description'] else '',
                    'emails': ', '.join(emails),
                    'phones': ', '.join(phones),
                    'facebook': social['facebook'] or '',
                    'twitter': social['twitter'] or '',
                    'linkedin': social['linkedin'] or '',
                    'instagram': social['instagram'] or '',
                }
                
                print(f"✅ Lead bulundu: {len(emails)} email, {len(phones)} telefon")
                return lead
            else:
                print(f"⚠️ Lead bulunamadı")
                return None
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Hata: {e}")
            return None
        except Exception as e:
            print(f"❌ Parse hatası: {e}")
            return None
    
    def find_contact_pages(self, base_url):
        """İletişim sayfalarını bul"""
        contact_keywords = [
            'contact', 'iletisim', 'about', 'hakkimizda', 
            'team', 'ekip', 'info', 'support'
        ]
        
        potential_urls = [base_url]
        
        try:
            response = self.session.get(base_url, timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            
            links = soup.find_all('a', href=True)
            
            for link in links:
                href = link['href'].lower()
                full_url = urljoin(base_url, link['href'])
                
                # İletişim sayfası gibi görünüyorsa ekle
                if any(keyword in href for keyword in contact_keywords):
                    if urlparse(full_url).netloc == urlparse(base_url).netloc:
                        potential_urls.append(full_url)
            
            return list(set(potential_urls[:config.MAX_PAGES_PER_SITE]))
            
        except Exception as e:
            print(f"⚠️ İletişim sayfaları bulunamadı: {e}")
            return [base_url]
    
    def scrape_website(self, base_url):
        """Bir web sitesinden lead topla"""
        print(f"\n{'='*60}")
        print(f"🌐 Website: {base_url}")
        print(f"{'='*60}")
        
        # İletişim sayfalarını bul
        urls_to_check = self.find_contact_pages(base_url)
        print(f"📄 {len(urls_to_check)} sayfa kontrol edilecek")
        
        for url in tqdm(urls_to_check, desc="Sayfalar"):
            lead = self.scrape_page(url)
            if lead:
                self.leads.append(lead)
            
            time.sleep(config.REQUEST_DELAY)
    
    def scrape_all(self):
        """Tüm hedef sitelerden lead topla"""
        print("\n" + "="*60)
        print("🚀 LEAD SCRAPING BAŞLIYOR")
        print("="*60)
        
        for website in config.TARGET_WEBSITES:
            self.scrape_website(website)
        
        print(f"\n{'='*60}")
        print(f"✅ Toplam {len(self.leads)} lead toplandı")
        print(f"{'='*60}")
        
        return self.leads

if __name__ == '__main__':
    scraper = LeadScraper()
    leads = scraper.scrape_all()
    
    if leads:
        print("\n📊 Bulunan Lead'ler:")
        for i, lead in enumerate(leads, 1):
            print(f"\n{i}. {lead['company_name']}")
            print(f"   Email: {lead['emails']}")
            print(f"   Telefon: {lead['phones']}")
    else:
        print("\n⚠️ Hiç lead bulunamadı")