import os
import re
import glob

root_dir = r"c:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

new_show_results = '''function showResults() {
        const container = document.getElementById('quizContent');
        const percentage = Math.round((score / 5) * 100);
        let correctAnswers = score;

        let message, color, buttonHTML;

        if (correctAnswers >= 4) {
            const nextPageLink = Array.from(document.querySelectorAll('a')).find(link => 
                link.textContent.includes('SUCCESSIVA') || link.textContent.includes('Pagina successiva') || link.textContent.includes('PAGINA')
            );

            if (nextPageLink && nextPageLink.href) {
                buttonHTML = `<button onclick="window.location.href='\${nextPageLink.href}'" style="background: linear-gradient(135deg, #0277bd, #01579b); color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 1em; font-weight: bold; cursor: pointer; box-shadow: 0 4px 8px rgba(2, 119, 189, 0.3);">
                    ⬜ Vai alla Pagina Successiva
                </button>`;
                message = "Eccellente! Puoi passare al capitolo successivo! 🎉";
            } else {
                buttonHTML = `<button onclick="window.location.href='index.html'" style="background: linear-gradient(135deg, #27ae60, #229954); color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 1em; font-weight: bold; cursor: pointer; box-shadow: 0 4px 8px rgba(39, 174, 96, 0.3);">
                    🏠 Torna alla Home
                </button>`;
                message = "Eccellente! Hai completato tutti i capitoli! Torna alla home! 🎉";
            }
            color = "#2e7d32";
        } else {
            buttonHTML = `<button onclick="window.scrollTo({top: 0, behavior: 'smooth'}); startQuiz();" style="background: linear-gradient(135deg, #f57c00, #e65100); color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 1em; font-weight: bold; cursor: pointer; box-shadow: 0 4px 8px rgba(245, 124, 0, 0.3);">
                📚 Torna all'Inizio della Pagina
            </button>`;
            message = "Devi ripassare meglio! Torna all'inizio della pagina e ristudia il contenuto 📚";
            color = "#d32f2f";
        }

        container.innerHTML = `
            <div style="background: white; padding: 25px; border-radius: 8px; border: 3px solid \${color}; text-align: center;">
                <h3 style="color: \${color}; margin-bottom: 15px;">Quiz Completato!</h3>
                <div style="font-size: 3em; margin: 20px 0; color: \${color};">\${score}/5</div>
                <div style="font-size: 1.2em; margin-bottom: 15px; color: \${color};">\${percentage}% di risposte corrette</div>
                <p style="font-size: 1.1em; color: #333; margin-bottom: 20px;">\${message}</p>
                \${buttonHTML}
            </div>
        `;
    }'''

html_files = glob.glob(os.path.join(root_dir, "detail-*.html"))

pattern = r'function showResults\(\)\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}'

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'function showResults' in content:
            new_content = re.sub(pattern, new_show_results, content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Aggiornato: {os.path.basename(file_path)}")
        else:
            print(f"- Saltato (nessun quiz): {os.path.basename(file_path)}")
    except Exception as e:
        print(f"✗ Errore in {os.path.basename(file_path)}: {str(e)}")

print("\nFatto!")
