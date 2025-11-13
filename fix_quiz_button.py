import os
import glob

root_dir = r"c:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

old_button = '''<button onclick="startQuiz()" style="background: linear-gradient(135deg, #0277bd, #01579b); color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 1em; font-weight: bold; cursor: pointer; box-shadow: 0 4px 8px rgba(2, 119, 189, 0.3);">
                    🔄 Riprova il Quiz
                </button>'''

new_button = '''<button onclick="window.scrollTo({top: 0, behavior: 'smooth'});" style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 1em; font-weight: bold; cursor: pointer; box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3);">
                    ⬆️ Torna all'Inizio della Pagina
                </button>'''

html_files = glob.glob(os.path.join(root_dir, "detail-*.html"))

count = 0
for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_button in content:
            new_content = content.replace(old_button, new_button)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Aggiornato: {os.path.basename(file_path)}")
            count += 1
    except Exception as e:
        print(f"✗ Errore in {os.path.basename(file_path)}: {str(e)}")

print(f"\nFatto! {count} file modificati.")
