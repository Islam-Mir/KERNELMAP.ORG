import os

base_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

old_name = "kernel-map-index.html"
new_name = "index.html"

print("=" * 60)
print("RINOMINA kernel-map-index.html → index.html")
print("=" * 60 + "\n")

old_file = os.path.join(base_path, old_name)
new_file = os.path.join(base_path, new_name)

if os.path.exists(old_file):
    if os.path.exists(new_file):
        backup = os.path.join(base_path, "index_old_backup.html")
        os.rename(new_file, backup)
        print(f"⚠️  Backup creato: index_old_backup.html\n")
    
    os.rename(old_file, new_file)
    print(f"✅ Rinominato: {old_name} → {new_name}\n")
elif os.path.exists(new_file):
    print(f"✅ File index.html già esistente\n")
else:
    print(f"❌ Nessun file trovato!\n")

print("=" * 60)
print("AGGIORNAMENTO LINK IN TUTTI I FILE HTML")
print("=" * 60 + "\n")

html_files = [f for f in os.listdir(base_path) if f.endswith('.html')]

updated = 0

for html_file in html_files:
    file_path = os.path.join(base_path, html_file)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'kernel-map-index.html' in content:
            new_content = content.replace('kernel-map-index.html', 'index.html')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Aggiornato: {html_file}")
            updated += 1
    
    except Exception as e:
        print(f"❌ Errore: {html_file} - {str(e)}")

print(f"\n📊 Link aggiornati in {updated} file")
print("\n" + "=" * 60)
print("🎉 COMPLETATO!")
print("=" * 60)
print("\n✨ Modifiche:")
print("   ✅ kernel-map-index.html → index.html")
print("   ✅ Tutti i link aggiornati")
print("   ✅ Pulsante 'TORNA AL KERNEL MAP' ora punta a index.html")
