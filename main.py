from lead_scraper import LeadScraper
from export_leads import LeadExporter
import config

def main():
    print("="*60)
    print("📇 LEAD GENERATION TOOL")
    print("="*60)
    print(f"\n🎯 Hedef: {len(config.TARGET_WEBSITES)} website")
    print(f"📁 Çıktı: {config.OUTPUT_FOLDER}/{config.OUTPUT_FORMAT}")
    
    # Kullanıcı onayı
    print("\n" + "="*60)
    print("Scrape edilecek siteler:")
    for i, site in enumerate(config.TARGET_WEBSITES, 1):
        print(f"{i}. {site}")
    print("="*60)
    
    response = input("\nBaşlamak için ENTER'a bas (İptal için 'q'): ")
    if response.lower() == 'q':
        print("❌ İşlem iptal edildi")
        return
    
    # Scraping başlat
    scraper = LeadScraper()
    leads = scraper.scrape_all()
    
    # Export
    if leads:
        exporter = LeadExporter()
        exporter.create_statistics_report(leads)
        filename = exporter.export_leads(leads)
        
        print(f"\n✅ İşlem tamamlandı!")
        print(f"📂 Rapor: {filename}")
    else:
        print("\n⚠️ Hiç lead bulunamadı")
        print("💡 İpucu: config.py'deki TARGET_WEBSITES listesini kontrol et")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Program kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Beklenmeyen hata: {e}")
        import traceback
        traceback.print_exc()