import os
import re

base_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

files_with_letture = [
    'detail-device-access-bus-drivers.html',
    'detail-driver-model.html',
    'detail-electronics.html',
    'detail-generic-hw-access.html',
    'detail-hi-hardware-interfaces.html',
    'detail-hi-subsystems.html',
    'detail-interfaces-core.html',
    'detail-logical-filesystems.html',
    'detail-memory.html',
    'detail-network-controllers.html',
    'detail-network-storage.html',
    'detail-security.html',
    'detail-user-peripherals.html'
]

pattern = r'<h2[^>]*>.*?📚\s*Letture Consigliate.*?</h2>\s*<ul[^>]*>.*?</ul>'

print("🗑️  Rimozione sezioni 'Letture Consigliate'...\n")

removed_count = 0

for html_file in files_with_letture:
    file_path = os.path.join(base_path, html_file)
    
    if not os.path.exists(file_path):
        print(f"⚠️  Non trovato: {html_file}")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Rimosso da: {html_file}")
            removed_count += 1
        else:
            print(f"⏭️  Nessuna sezione trovata in: {html_file}")
    
    except Exception as e:
        print(f"❌ Errore su {html_file}: {str(e)}")

print(f"\n🎉 Completato! Sezioni rimosse da {removed_count} file.")
