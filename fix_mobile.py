import os
import re

base_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

mobile_css_for_details = '''
        @media (max-width: 768px) {
            .back-button-fixed {
                top: 10px;
                left: 10px;
                padding: 10px 16px;
                font-size: 12px;
                z-index: 1001;
            }
            
            .nav-buttons-right {
                position: fixed;
                top: 60px;
                left: 10px;
                right: auto;
                flex-direction: column;
                gap: 8px;
                z-index: 1000;
                width: calc(100% - 20px);
            }
            
            .nav-button {
                width: 100%;
                padding: 10px 16px;
                font-size: 12px;
                text-align: center;
            }
            
            body {
                padding-top: 140px;
            }
        }
'''

mobile_css_for_index = '''
        @media (max-width: 768px) {
            .kernel-map-container {
                padding: 10px;
                overflow-x: auto;
            }
            
            .section {
                min-width: 120px;
                padding: 8px;
            }
            
            .section-title {
                font-size: 11px;
                word-wrap: break-word;
                overflow-wrap: break-word;
                hyphens: auto;
            }
            
            .subsection {
                font-size: 10px;
                padding: 6px;
                min-height: 40px;
            }
            
            .header h1 {
                font-size: 20px;
            }
            
            .header p {
                font-size: 12px;
            }
        }
        
        @media (max-width: 480px) {
            .section {
                min-width: 100px;
                padding: 6px;
            }
            
            .section-title {
                font-size: 9px;
            }
            
            .subsection {
                font-size: 8px;
                padding: 4px;
                min-height: 35px;
            }
        }
'''

print("🚀 Inizio ottimizzazione mobile...\n")

html_files = [f for f in os.listdir(base_path) if f.endswith('.html')]

detail_count = 0
index_updated = False

for html_file in html_files:
    file_path = os.path.join(base_path, html_file)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '@media (max-width: 768px)' in content:
            print(f"⏭️  Già ottimizzato: {html_file}")
            continue
        
        if html_file == 'index.html':
            if '<meta name="viewport"' not in content:
                content = content.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
            
            if '</style>' in content:
                content = content.replace('</style>', mobile_css_for_index + '\n    </style>', 1)
                index_updated = True
                print(f"✅ Ottimizzato mobile: {html_file}")
        
        elif html_file.startswith('detail-'):
            if '<meta name="viewport"' not in content:
                content = content.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
            
            if '</style>' in content:
                content = content.replace('</style>', mobile_css_for_details + '\n    </style>', 1)
                detail_count += 1
                print(f"✅ Ottimizzato mobile: {html_file}")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    except Exception as e:
        print(f"❌ Errore su {html_file}: {str(e)}")

print(f"\n🎉 Completato!")
print(f"📱 Pagine detail ottimizzate: {detail_count}")
print(f"📱 Index.html ottimizzato: {'Sì' if index_updated else 'No'}")
print(f"\n✨ Modifiche applicate:")
print(f"   - Pulsanti non si sovrappongono più su mobile")
print(f"   - Testo celle index.html si adatta allo schermo")
print(f"   - Viewport meta tag aggiunto dove mancante")
