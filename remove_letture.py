import os
import re

base_paths = [
    r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0",
    r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"
]

patterns_to_remove = [
    r'<div[^>]*>[\s\S]*?📚\s*Letture Consigliate[\s\S]*?</div>',
    r'<section[^>]*>[\s\S]*?📚\s*Letture Consigliate[\s\S]*?</section>',
    r'<h[23][^>]*>[\s\S]*?📚\s*Letture Consigliate[\s\S]*?</h[23]>[\s\S]*?(?=<h[23]|<div class="back-button|</body>)',
    r'📚\s*Letture Consigliate[\s\S]*?(?=<div class="back-button|</body>|<script)',
]

print("🔍 Ricerca sezioni 'Letture Consigliate'...\n")

total_removed = 0

for base_path in base_paths:
    if not os.path.exists(base_path):
        print(f"⚠️  Cartella non trovata: {base_path}")
        continue
    
    print(f"📁 Controllo: {os.path.basename(base_path)}\n")
    
    html_files = [f for f in os.listdir(base_path) if f.endswith('.html')]
    
    for html_file in html_files:
        file_path = os.path.join(base_path, html_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            if '📚' not in original_content and 'Letture Consigliate' not in original_content:
                continue
            
            content = original_content
            
            for pattern in patterns_to_remove:
                content = re.sub(pattern, '', content, flags=re.IGNORECASE)
            
            content = re.sub(r'📚[^\n]*\n', '', content)
            content = re.sub(r'📖[^\n]*\n', '', content)
            content = re.sub(r'🌐[^\n]*\n', '', content)
            
            lines = content.split('\n')
            cleaned_lines = []
            skip_next = False
            
            for i, line in enumerate(lines):
                if 'Letture Consigliate' in line or '📚' in line or '📖' in line or '🌐' in line:
                    skip_next = True
                    continue
                
                if skip_next and line.strip() == '':
                    continue
                
                if skip_next and '<' in line:
                    skip_next = False
                
                if not skip_next:
                    cleaned_lines.append(line)
            
            content = '\n'.join(cleaned_lines)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Rimosso da: {html_file}")
                total_removed += 1
        
        except Exception as e:
            print(f"❌ Errore su {html_file}: {str(e)}")

print(f"\n🎉 Completato! Sezioni rimosse da {total_removed} file.")
