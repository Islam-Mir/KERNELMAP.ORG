import os
import glob
import re

root_dir = r"c:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

scripts = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GW3S1CKY7Q"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-GW3S1CKY7Q');
</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4240610713346131"
     crossorigin="anonymous"></script>
'''

html_files = glob.glob(os.path.join(root_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<head>' in content and scripts not in content:
        content = content.replace('<head>', '<head>\n' + scripts + '\n')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Aggiornato: {os.path.basename(file_path)}")
    elif scripts in content:
        print(f"- Già presente: {os.path.basename(file_path)}")
    else:
        print(f"✗ <head> non trovato: {os.path.basename(file_path)}")

print("\n✅ Fatto!")
