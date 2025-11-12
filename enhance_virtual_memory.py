import os

file_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG\detail-virtual-memory.html"

enhanced_content = '''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Memory - Linux Kernel</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #e0f4ff 0%, #b3e5fc 100%);
            padding: 20px;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        h1 {
            color: #0288d1;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-align: center;
            border-bottom: 4px solid #0288d1;
            padding-bottom: 15px;
        }

        h2 {
            color: #01579b;
            font-size: 1.8em;
            margin-top: 30px;
            margin-bottom: 15px;
            border-left: 5px solid #0288d1;
            padding-left: 15px;
        }

        h3 {
            color: #0277bd;
            font-size: 1.4em;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        p {
            margin-bottom: 15px;
            color: #333;
            text-align: justify;
        }

        .highlight-box {
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }

        .code-box {
            background: #263238;
            color: #aed581;
            padding: 20px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
            margin: 20px 0;
        }

        .quiz-container {
            background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
            padding: 30px;
            border-radius: 15px;
            margin: 30px 0;
            border: 3px solid #ff9800;
        }

        .quiz-question {
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border: 2px solid #ff9800;
        }

        .quiz-options {
            margin-top: 15px;
        }

        .quiz-option {
            background: #f5f5f5;
            padding: 12px;
            margin: 8px 0;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
            border: 2px solid transparent;
        }

        .quiz-option:hover {
            background: #e3f2fd;
            border-color: #2196f3;
        }

        .quiz-option.correct {
            background: #c8e6c9;
            border-color: #4caf50;
        }

        .quiz-option.wrong {
            background: #ffcdd2;
            border-color: #f44336;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        .info-card {
            background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #4caf50;
        }

        .back-button-fixed {
            position: fixed;
            top: 20px;
            left: 20px;
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            z-index: 1001;
        }

        .back-button-fixed:hover {
            background: linear-gradient(135deg, #45a049 0%, #388e3c 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        ul, ol {
            margin-left: 30px;
            margin-bottom: 15px;
        }

        li {
            margin-bottom: 8px;
        }

        .diagram {
            background: white;
            border: 2px solid #0288d1;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            text-align: center;
        }

        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }

            h1 {
                font-size: 1.8em;
            }

            h2 {
                font-size: 1.4em;
            }

            .info-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <button class="back-button-fixed" onclick="window.location.href='index.html'">← TORNA AL KERNEL MAP</button>

    <div class="container">
        <h1>🧠 Virtual Memory Management</h1>

        <div class="highlight-box">
            <h3>📌 Cos'è la Virtual Memory?</h3>
            <p>
                La <strong>Virtual Memory</strong> è un meccanismo fondamentale del kernel Linux che permette ai processi 
                di utilizzare uno spazio di indirizzamento virtuale molto più grande della memoria fisica disponibile. 
                Ogni processo vede uno spazio di indirizzamento privato e contiguo, mentre il kernel gestisce la mappatura 
                tra indirizzi virtuali e fisici.
            </p>
        </div>

        <h2>🔧 Componenti Principali</h2>

        <div class="info-grid">
            <div class="info-card">
                <h3>📍 Page Tables</h3>
                <p>Strutture dati gerarchiche che mappano indirizzi virtuali a indirizzi fisici. Su x86-64 si usano 4 livelli di page tables.</p>
            </div>

            <div class="info-card">
                <h3>🔄 TLB (Translation Lookaside Buffer)</h3>
                <p>Cache hardware che memorizza le traduzioni più recenti da indirizzi virtuali a fisici per velocizzare l'accesso.</p>
            </div>

            <div class="info-card">
                <h3>📄 Page Fault Handler</h3>
                <p>Gestisce le eccezioni quando un processo accede a una pagina non presente in memoria fisica.</p>
            </div>

            <div class="info-card">
                <h3>💾 Memory Mapping</h3>
                <p>Permette di mappare file o dispositivi direttamente nello spazio di indirizzamento del processo.</p>
            </div>
        </div>

        <h2>🏗️ Architettura della Virtual Memory</h2>

        <div class="diagram">
            <pre style="text-align: left; font-family: monospace;">
┌─────────────────────────────────────┐
│   User Space (0x0000 - 0x7FFF...)   │
├─────────────────────────────────────┤
│   • Stack (cresce verso il basso)   │
│   • Memory Mapped Region            │
│   • Heap (cresce verso l'alto)      │
│   • BSS (dati non inizializzati)    │
│   • Data (dati inizializzati)       │
│   • Text (codice eseguibile)        │
└─────────────────────────────────────┘
┌─────────────────────────────────────┐
│   Kernel Space (0x8000... - 0xFFFF) │
├─────────────────────────────────────┤
│   • Kernel Code & Data              │
│   • Page Tables                     │
│   • Device Mappings                 │
└─────────────────────────────────────┘
            </pre>
        </div>

        <h2>⚙️ Funzioni Chiave</h2>

        <h3>1. Allocazione Memoria Virtuale</h3>
        <div class="code-box">
struct vm_area_struct *find_vma(struct mm_struct *mm, unsigned long addr);
int do_mmap(struct file *file, unsigned long addr, unsigned long len);
void *vmalloc(unsigned long size);
        </div>

        <h3>2. Page Fault Handling</h3>
        <div class="code-box">
static int __handle_mm_fault(struct vm_area_struct *vma, 
                             unsigned long address, 
                             unsigned int flags);
        </div>

        <h3>3. Memory Protection</h3>
        <div class="code-box">
int mprotect(void *addr, size_t len, int prot);
// prot: PROT_READ, PROT_WRITE, PROT_EXEC, PROT_NONE
        </div>

        <h2>🔍 Strutture Dati Fondamentali</h2>

        <div class="highlight-box">
            <h3>struct mm_struct</h3>
            <p>Rappresenta lo spazio di indirizzamento di un processo:</p>
            <div class="code-box">
struct mm_struct {
    struct vm_area_struct *mmap;     // Lista delle VMA
    struct rb_root mm_rb;            // Red-black tree delle VMA
    pgd_t *pgd;                      // Page Global Directory
    atomic_t mm_users;               // Numero di utenti
    atomic_t mm_count;               // Reference count
    unsigned long start_code;        // Inizio codice
    unsigned long end_code;          // Fine codice
    unsigned long start_data;        // Inizio dati
    unsigned long end_data;          // Fine dati
    unsigned long start_brk;         // Inizio heap
    unsigned long brk;               // Fine heap
    unsigned long start_stack;       // Inizio stack
};
            </div>
        </div>

        <div class="highlight-box">
            <h3>struct vm_area_struct (VMA)</h3>
            <p>Rappresenta una regione contigua di memoria virtuale:</p>
            <div class="code-box">
struct vm_area_struct {
    unsigned long vm_start;          // Indirizzo iniziale
    unsigned long vm_end;            // Indirizzo finale
    struct vm_area_struct *vm_next;  // VMA successiva
    pgprot_t vm_page_prot;          // Protezioni di accesso
    unsigned long vm_flags;          // Flag (VM_READ, VM_WRITE, VM_EXEC)
    struct file *vm_file;            // File mappato (se presente)
    const struct vm_operations_struct *vm_ops;
};
            </div>
        </div>

        <h2>🎯 Meccanismi Avanzati</h2>

        <h3>Copy-on-Write (COW)</h3>
        <p>
            Quando un processo fa fork(), le pagine di memoria vengono condivise tra padre e figlio 
            e marcate come read-only. Solo quando uno dei due tenta di scrivere, viene creata una copia privata.
        </p>

        <h3>Demand Paging</h3>
        <p>
            Le pagine vengono caricate in memoria fisica solo quando effettivamente accedute, 
            non al momento dell'allocazione. Questo riduce l'uso di memoria e velocizza l'avvio dei processi.
        </p>

        <h3>Memory Overcommit</h3>
        <p>
            Il kernel può allocare più memoria virtuale di quella fisicamente disponibile, 
            assumendo che non tutti i processi useranno tutta la memoria allocata contemporaneamente.
        </p>

        <h2>📊 Gestione delle Page Tables</h2>

        <div class="info-grid">
            <div class="info-card">
                <h3>PGD (Page Global Directory)</h3>
                <p>Livello 1 - Punta alle PUD</p>
            </div>

            <div class="info-card">
                <h3>PUD (Page Upper Directory)</h3>
                <p>Livello 2 - Punta alle PMD</p>
            </div>

            <div class="info-card">
                <h3>PMD (Page Middle Directory)</h3>
                <p>Livello 3 - Punta alle PTE</p>
            </div>

            <div class="info-card">
                <h3>PTE (Page Table Entry)</h3>
                <p>Livello 4 - Contiene l'indirizzo fisico</p>
            </div>
        </div>

        <h2>🚀 Ottimizzazioni</h2>

        <ul>
            <li><strong>Huge Pages:</strong> Pagine di dimensioni maggiori (2MB o 1GB) per ridurre il numero di TLB miss</li>
            <li><strong>Transparent Huge Pages (THP):</strong> Gestione automatica delle huge pages</li>
            <li><strong>NUMA Awareness:</strong> Allocazione preferenziale su nodi NUMA vicini al processo</li>
            <li><strong>KSM (Kernel Samepage Merging):</strong> Unione di pagine identiche per risparmiare memoria</li>
        </ul>

        <h2>🎓 Quiz Interattivo</h2>

        <div class="quiz-container">
            <h3 style="text-align: center; color: #e65100; margin-bottom: 20px;">🧪 Testa le tue conoscenze!</h3>

            <div class="quiz-question">
                <p><strong>Domanda 1:</strong> Qual è la dimensione standard di una pagina su architettura x86-64?</p>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, false)">A) 2 KB</div>
                    <div class="quiz-option" onclick="checkAnswer(this, true)">B) 4 KB</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">C) 8 KB</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">D) 16 KB</div>
                </div>
            </div>

            <div class="quiz-question">
                <p><strong>Domanda 2:</strong> Cosa succede durante un Copy-on-Write?</p>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, false)">A) La pagina viene immediatamente copiata</div>
                    <div class="quiz-option" onclick="checkAnswer(this, true)">B) La pagina viene copiata solo quando modificata</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">C) La pagina viene eliminata</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">D) La pagina viene condivisa permanentemente</div>
                </div>
            </div>

            <div class="quiz-question">
                <p><strong>Domanda 3:</strong> Quanti livelli di page tables usa x86-64?</p>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, false)">A) 2 livelli</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">B) 3 livelli</div>
                    <div class="quiz-option" onclick="checkAnswer(this, true)">C) 4 livelli</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">D) 5 livelli</div>
                </div>
            </div>

            <div class="quiz-question">
                <p><strong>Domanda 4:</strong> Cosa rappresenta una VMA (vm_area_struct)?</p>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, false)">A) Una singola pagina fisica</div>
                    <div class="quiz-option" onclick="checkAnswer(this, true)">B) Una regione contigua di memoria virtuale</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">C) Un processo in esecuzione</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">D) Un file system virtuale</div>
                </div>
            </div>

            <div class="quiz-question">
                <p><strong>Domanda 5:</strong> Qual è il vantaggio principale del Demand Paging?</p>
                <div class="quiz-options">
                    <div class="quiz-option" onclick="checkAnswer(this, false)">A) Aumenta la velocità della CPU</div>
                    <div class="quiz-option" onclick="checkAnswer(this, true)">B) Carica le pagine solo quando necessario</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">C) Elimina i page fault</div>
                    <div class="quiz-option" onclick="checkAnswer(this, false)">D) Raddoppia la memoria disponibile</div>
                </div>
            </div>
        </div>

        <h2>🔗 Interazione con Altri Sottosistemi</h2>

        <ul>
            <li><strong>Page Allocator:</strong> Fornisce le pagine fisiche per le mappature virtuali</li>
            <li><strong>Swap:</strong> Gestisce lo spostamento di pagine su disco quando la RAM è piena</li>
            <li><strong>VFS:</strong> Permette il memory mapping di file (mmap)</li>
            <li><strong>Scheduler:</strong> Considera l'uso di memoria nei criteri di scheduling</li>
            <li><strong>Device Drivers:</strong> Possono mappare memoria di dispositivi nello spazio virtuale</li>
        </ul>

        <h2>📈 Monitoraggio e Debug</h2>

        <div class="code-box">
# Visualizza le VMA di un processo
cat /proc/[PID]/maps

# Statistiche memoria virtuale
cat /proc/meminfo | grep -i virtual

# Page fault statistics
cat /proc/vmstat | grep pgfault

# Huge pages info
cat /proc/meminfo | grep -i huge
        </div>

        <div class="highlight-box">
            <h3>⚠️ Problemi Comuni</h3>
            <ul>
                <li><strong>Memory Fragmentation:</strong> Difficoltà nell'allocare regioni contigue grandi</li>
                <li><strong>TLB Thrashing:</strong> Troppi TLB miss degradano le performance</li>
                <li><strong>OOM (Out of Memory):</strong> Il kernel deve terminare processi quando la memoria è esaurita</li>
                <li><strong>Page Table Overhead:</strong> Le page tables stesse consumano memoria</li>
            </ul>
        </div>

    </div>

    <script>
        function checkAnswer(element, isCorrect) {
            const options = element.parentElement.querySelectorAll('.quiz-option');
            options.forEach(opt => {
                opt.style.pointerEvents = 'none';
            });

            if (isCorrect) {
                element.classList.add('correct');
                element.innerHTML += ' ✅ Corretto!';
            } else {
                element.classList.add('wrong');
                element.innerHTML += ' ❌ Sbagliato!';
                
                options.forEach(opt => {
                    if (opt !== element && !opt.classList.contains('wrong')) {
                        opt.classList.add('correct');
                        opt.innerHTML += ' ✅ Risposta corretta';
                    }
                });
            }
        }
    </script>
</body>
</html>'''

print("📝 Creazione contenuto dettagliato per detail-virtual-memory.html...\n")

try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(enhanced_content)
    
    print("✅ File aggiornato con successo!")
    print("\n📊 Contenuto aggiunto:")
    print("   • Spiegazione completa della Virtual Memory")
    print("   • Componenti principali (Page Tables, TLB, etc.)")
    print("   • Strutture dati (mm_struct, vm_area_struct)")
    print("   • Meccanismi avanzati (COW, Demand Paging)")
    print("   • 5 domande quiz interattive")
    print("   • Diagrammi e codice di esempio")
    print("   • Sezione debug e monitoraggio")
    
except Exception as e:
    print(f"❌ Errore: {str(e)}")
