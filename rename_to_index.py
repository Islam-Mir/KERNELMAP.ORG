import os
import shutil

base_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0"

old_name = "kernel-map-index.html"
new_name = "index.html"

old_file_path = os.path.join(base_path, old_name)
new_file_path = os.path.join(base_path, new_name)

print("🚀 Inizio rinominazione e aggiornamento link...\n")

if os.path.exists(new_file_path):
    backup_path = os.path.join(base_path, "index_backup.html")
    print(f"⚠️  index.html esiste già. Creazione backup: index_backup.html")
    shutil.copy2(new_file_path, backup_path)
    os.remove(new_file_path)

if os.path.exists(old_file_path):
    os.rename(old_file_path, new_file_path)
    print(f"✅ Rinominato: {old_name} → {new_name}\n")
else:
    print(f"❌ File {old_name} non trovato!\n")

print("📝 Aggiornamento link in tutti i file HTML...\n")

html_files = [f for f in os.listdir(base_path) if f.endswith('.html')]

updated_count = 0
for html_file in html_files:
    file_path = os.path.join(base_path, html_file)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'kernel-map-index.html' in content:
            content = content.replace('kernel-map-index.html', 'index.html')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Aggiornato: {html_file}")
            updated_count += 1
    
    except Exception as e:
        print(f"❌ Errore su {html_file}: {str(e)}")

print(f"\n🎉 Completato! {updated_count} file aggiornati.")
print(f"📄 La pagina principale è ora: index.html")
