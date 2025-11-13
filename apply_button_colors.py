import os
import glob
import subprocess

root_dir = r"c:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

fix_quiz_file = os.path.join(root_dir, "fix_quiz_button.py")

with open(fix_quiz_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Cambia la box-shadow da arancione a verde
content = content.replace(
    'box-shadow: 0 4px 8px rgba(245, 124, 0, 0.3);',
    'box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3);'
)

with open(fix_quiz_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Aggiornato fix_quiz_button.py con box-shadow verde")

# Esegui il fix_quiz_button.py
subprocess.run(['python', fix_quiz_file], encoding='utf-8')
