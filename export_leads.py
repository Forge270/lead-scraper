import pandas as pd
from datetime import datetime
import os
import config

class LeadExporter:
    def __init__(self):
        if not os.path.exists(config.OUTPUT_FOLDER):
            os.makedirs(config.OUTPUT_FOLDER)
    
    def export_to_excel(self, leads):
        """Lead'leri Excel'e aktar"""
        if not leads:
            print("Export edilecek lead yok")
            return None
        
        df = pd.DataFrame(leads)
        
        # Sıralama
        df = df[[
            'company_name', 'emails', 'phones', 
            'facebook', 'twitter', 'linkedin', 'instagram',
            'description', 'source_url'
        ]]
        
        # Dosya adı
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{config.OUTPUT_FOLDER}/leads_{timestamp}.xlsx"
        
        # Excel oluştur
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Leads', index=False)
            
            # Ozet sayfa
            summary = {
                'Metric': [
                    'Toplam Lead',
                    'Email Bulunan',
                    'Telefon Bulunan',
                    'Facebook Bulunan',
                    'LinkedIn Bulunan'
                ],
                'Count': [
                    len(df),
                    len(df[df['emails'] != '']),
                    len(df[df['phones'] != '']),
                    len(df[df['facebook'] != '']),
                    len(df[df['linkedin'] != ''])
                ]
            }
            pd.DataFrame(summary).to_excel(writer, sheet_name='Summary', index=False)
        
        print(f"Excel raporu olusturuldu: {filename}")
        return filename
    
    def export_to_csv(self, leads):
        """Lead'leri CSV'ye aktar"""
        if not leads:
            print("Export edilecek lead yok")
            return None
        
        df = pd.DataFrame(leads)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{config.OUTPUT_FOLDER}/leads_{timestamp}.csv"
        
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        
        print(f"CSV raporu olusturuldu: {filename}")
        return filename
    
    def export_leads(self, leads):
        """Lead'leri belirlenen formatta export et"""
        if config.OUTPUT_FORMAT == 'excel':
            return self.export_to_excel(leads)
        elif config.OUTPUT_FORMAT == 'csv':
            return self.export_to_csv(leads)
        else:
            print(f"Gecersiz format: {config.OUTPUT_FORMAT}")
            return None
    
    def create_statistics_report(self, leads):
        """Istatistik raporu olustur"""
        if not leads:
            return
        
        df = pd.DataFrame(leads)
        
        print("\n" + "="*60)
        print("ISTATISTIKLER")
        print("="*60)
        print(f"Toplam Lead: {len(df)}")
        print(f"Email Bulunan: {len(df[df['emails'] != ''])}")
        print(f"Telefon Bulunan: {len(df[df['phones'] != ''])}")
        print(f"Facebook: {len(df[df['facebook'] != ''])}")
        print(f"Twitter: {len(df[df['twitter'] != ''])}")
        print(f"LinkedIn: {len(df[df['linkedin'] != ''])}")
        print(f"Instagram: {len(df[df['instagram'] != ''])}")
        print("="*60)

if __name__ == '__main__':
    # Test
    test_leads = [
        {
            'company_name': 'Test Company',
            'emails': 'info@test.com',
            'phones': '0212 123 45 67',
            'facebook': 'https://facebook.com/test',
            'twitter': '',
            'linkedin': 'https://linkedin.com/company/test',
            'instagram': '',
            'description': 'Test company description',
            'source_url': 'https://test.com'
        }
    ]
    
    exporter = LeadExporter()
    exporter.export_leads(test_leads)
    exporter.create_statistics_report(test_leads)