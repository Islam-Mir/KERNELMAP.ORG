import re
import glob
import os

root_dir = r"c:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

# Colori di "TORNA AL KERNEL MAP"
km_normal = "linear-gradient(135deg, #4CAF50 0%, #45a049 100%)"
km_hover = "linear-gradient(135deg, #45a049 0%, #388e3c 100%)"

# 1. Aggiorna add_navigation.py
nav_file = os.path.join(root_dir, "add_navigation.py")
with open(nav_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'background: linear-gradient\(135deg, #FF9800 0%, #F57C00 100%\)',
    f'background: {km_normal}',
    content
)
content = re.sub(
    r'background: linear-gradient\(135deg, #FB8C00 0%, #E65100 100%\)',
    f'background: {km_hover}',
    content
)

with open(nav_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("✓ Aggiornato add_navigation.py")

# 2. Aggiorna fix_quiz_button.py
quiz_file = os.path.join(root_dir, "fix_quiz_button.py")
with open(quiz_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'background: linear-gradient\(135deg, #f57c00, #e65100\)',
    f'background: {km_normal}',
    content
)

with open(quiz_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("✓ Aggiornato fix_quiz_button.py")

# 3. Aggiorna tutti i file detail-*.html che contengono i button del quiz
html_files = glob.glob(os.path.join(root_dir, "detail-*.html"))
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Torna all\'Inizio della Pagina' in content or 'Torna all\'Inizio' in content:
        content = re.sub(
            r'background: linear-gradient\(135deg, #f57c00, #e65100\)',
            f'background: {km_normal}',
            content
        )
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Aggiornato {os.path.basename(file_path)}")

print("\n✅ Tutti i button ora hanno i colori di TORNA AL KERNEL MAP!")
