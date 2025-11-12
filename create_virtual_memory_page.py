import os

file_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG\detail-virtual-memory.html"

content = '''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Memory - Dettagli</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #e0f4ff 0%, #b3e5fc 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            padding: 15px;
        }

        .header {
            background: linear-gradient(135deg, #0288d1 0%, #01579b 100%);
            padding: 8px;
            border-radius: 8px;
            margin-bottom: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            color: white;
            text-align: center;
        }

        .header h1 {
            font-size: 1.8em;
            margin-bottom: 8px;
            letter-spacing: 1px;
            font-weight: bold;
            text-transform: uppercase;
        }

        .header .subtitle {
            font-size: 1.1em;
            opacity: 0.95;
            font-weight: 500;
        }

        .content {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }

        .info-box {
            background: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .info-box h3 {
            color: #0288d1;
            font-size: 1em;
            margin-bottom: 10px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .info-box p {
            font-size: 0.85em;
            line-height: 1.6;
            color: #555;
            margin-bottom: 6px;
        }

        .info-box ul {
            font-size: 0.85em;
            line-height: 1.6;
            color: #555;
            margin-left: 18px;
        }

        .info-box li {
            margin-bottom: 6px;
        }

        .content h2 {
            font-size: 1.3em;
            color: #0288d1;
            margin: 18px 0 10px 0;
            border-bottom: 3px solid #0288d1;
            padding-bottom: 8px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .content h3 {
            font-size: 1.05em;
            color: #01579b;
            margin: 14px 0 8px 0;
            font-weight: 600;
        }

        .content p {
            font-size: 0.9em;
            line-height: 1.7;
            color: #444;
            margin-bottom: 10px;
        }

        .content ul, .content ol {
            margin-left: 20px;
            margin-bottom: 14px;
        }

        .content li {
            font-size: 0.9em;
            line-height: 1.6;
            color: #555;
            margin-bottom: 7px;
        }

        .back-button {
            position: fixed;
            top: 15px;
            left: 15px;
            z-index: 1000;
            padding: 8px 14px;
            background: linear-gradient(135deg, #0288d1 0%, #01579b 100%);
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 0.8em;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            text-align: center;
            font-weight: 600;
            box-shadow: 0 2px 8px rgba(2, 136, 209, 0.3);
        }

        .back-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(2, 136, 209, 0.5);
        }
        
        .back-button-fixed {
            display: inline-block;
            margin: 0;
        }

        .badge {
            display: inline-block;
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.8em;
            margin-bottom: 12px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }

        @media (max-width: 1000px) {
            .container {
                flex-direction: column;
                gap: 10px;
            }
            .right-panel {
                width: 100%;
                flex-direction: row;
            }
            .info-box {
                flex: 1;
            }
            .header h1 {
                font-size: 1.6em;
            }
        }

        footer {
            text-align: center;
            padding: 3px;
            border-top: 1px solid #ddd;
            font-size: 0.4em;
            color: #999;
            background: white;
            border-radius: 8px;
            margin-top: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
    
        .nav-buttons-right {
            position: fixed;
            top: 20px;
            right: 20px;
            display: flex;
            gap: 10px;
            z-index: 1000;
        }

        .nav-button {
            background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            box-sizing: border-box;
        }

        .nav-button:hover {
            background: linear-gradient(135deg, #FB8C00 0%, #E65100 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        .nav-button:disabled {
            background: linear-gradient(135deg, #BDBDBD 0%, #9E9E9E 100%);
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        @media (max-width: 768px) {
            * {
                box-sizing: border-box;
            }
            
            body {
                padding: 10px;
                margin: 0;
                overflow-x: hidden;
            }
            
            .back-button-fixed {
                position: fixed;
                top: 10px;
                left: 10px;
                padding: 8px 12px;
                font-size: 11px;
                z-index: 1001;
                max-width: calc(100vw - 20px);
                white-space: nowrap;
            }
            
            .nav-buttons-right {
                position: fixed;
                top: 55px;
                left: 10px;
                right: 10px;
                flex-direction: column;
                gap: 6px;
                z-index: 1000;
                width: auto;
            }
            
            .nav-button {
                width: 100%;
                padding: 10px 12px;
                font-size: 11px;
                text-align: center;
                white-space: nowrap;
            }
            
            .content, .container, main, article {
                padding-top: 130px !important;
                max-width: 100vw;
                overflow-x: hidden;
            }
            
            h1 {
                font-size: 1.5em !important;
            }
            
            h2 {
                font-size: 1.3em !important;
            }
            
            p, li, div {
                font-size: 14px !important;
                word-wrap: break-word;
            }
        }

        @media (max-width: 480px) {
            .back-button-fixed {
                font-size: 10px;
                padding: 6px 10px;
            }
            
            .nav-button {
                font-size: 10px;
                padding: 8px 10px;
            }
            
            .content, .container, main, article {
                padding-top: 120px !important;
            }
        }

    </style>
</head>
<body>
    <button class="back-button back-button-fixed" onclick="window.location.href='index.html'">
        ← Torna alla Kernel Map
    </button>
    
    <div class="header">
        <h1>VIRTUAL MEMORY</h1>
        <p class="subtitle">Gestione della memoria virtuale</p>
    </div>

    <div class="content">
        <span class="badge">🧠 Virtual Memory</span>
        <h2>DESCRIZIONE:</h2>
        <p><strong>La Virtual Memory è un meccanismo fondamentale del kernel Linux che permette ai processi di utilizzare uno spazio di indirizzamento virtuale molto più grande della memoria fisica disponibile. Ogni processo vede uno spazio di indirizzamento privato e contiguo, mentre il kernel gestisce la mappatura tra indirizzi virtuali e fisici attraverso le page tables.</strong></p>
        
        <h2>CONFRONTO:</h2>
        <p>Immagina la Virtual Memory come un sistema di archiviazione intelligente: ogni processo ha il proprio "magazzino virtuale" (spazio di indirizzamento) che sembra infinito, ma il kernel è il magazziniere che gestisce lo spazio fisico reale, spostando "scatole" (pagine) tra scaffali (RAM) e deposito esterno (swap) secondo necessità.</p>
        
        <h2>🔍 Descrizione Tecnica</h2>
        <p><strong>La Virtual Memory nel kernel Linux gestisce la traduzione da indirizzi virtuali a fisici, l'isolamento tra processi, il demand paging, il copy-on-write e lo swapping. Fornisce astrazione, protezione e condivisione efficiente della memoria fisica.</strong></p>
        <p>• <strong>Address Translation</strong> - Traduzione indirizzi virtuali → fisici via page tables</p>
        <p>• <strong>Memory Isolation</strong> - Ogni processo ha spazio indirizzamento privato</p>
        <p>• <strong>Demand Paging</strong> - Caricamento pagine solo quando necessario</p>
        <p><em>• Interfaccia principale tra processi e memoria fisica del sistema</em></p>

<h2>⚙️ Operazioni Principali della Virtual Memory</h2>
<p><strong>La Virtual Memory nel kernel Linux gestisce diverse categorie critiche di operazioni per la gestione della memoria:</strong></p>

<h3>⚙️ Page Table Management</h3>
<p>• <strong>pgd_alloc()</strong> - Alloca Page Global Directory</p>
<p>• <strong>pte_alloc()</strong> - Alloca Page Table Entry</p>

<h3>⚙️ Page Fault Handling</h3>
<p>• <strong>do_page_fault()</strong> - Gestisce page fault</p>
<p>• <strong>handle_mm_fault()</strong> - Risolve fault memoria</p>

<h3>⚙️ Memory Mapping</h3>
<p>• <strong>do_mmap()</strong> - Crea nuova mappatura memoria</p>
<p>• <strong>do_munmap()</strong> - Rimuove mappatura esistente</p>

<h2>📋 Esempi Pratici della Virtual Memory</h2>
<p><strong>La Virtual Memory è coinvolta in ogni accesso alla memoria da parte dei processi, dalla semplice lettura di variabili alla gestione complessa del memory mapping:</strong></p>

<h3>🔍 Page Fault Flow</h3>
<p>1. Processo accede a indirizzo virtuale non mappato</p>
<p>2. CPU genera page fault exception</p>
<p>3. Kernel verifica validità indirizzo (VMA)</p>
<p>4. Kernel alloca pagina fisica e aggiorna page table</p>
<p>5. Processo riprende esecuzione</p>

<h3>📄 Strutture Dati Chiave</h3>
<ul>
<li><strong>struct mm_struct</strong> - Descrittore spazio indirizzamento processo</li>
<li><strong>struct vm_area_struct</strong> - Regione contigua memoria virtuale (VMA)</li>
<li><strong>pgd_t, pud_t, pmd_t, pte_t</strong> - Livelli page tables</li>
<li><strong>struct page</strong> - Descrittore pagina fisica</li>
</ul>

<h3>💻 Comandi Linux Essenziali</h3>
<ul>
<li><code>$ cat /proc/[PID]/maps</code> - Mostra mappature memoria processo</li>
<li><code>$ pmap [PID]</code> - Report dettagliato memoria processo</li>
<li><code>$ cat /proc/meminfo</code> - Statistiche memoria sistema</li>
<li><code>$ vmstat</code> - Statistiche virtual memory</li>
</ul>

<h3>🎯 Caso Reale: Memory Mapping File</h3>
<p>Quando un processo fa <code>mmap()</code> di un file:</p>
<ol>
<li>Kernel crea nuova VMA nello spazio processo</li>
<li>VMA collegata al file tramite vm_file</li>
<li>Nessuna pagina fisica allocata inizialmente</li>
<li>Primo accesso genera page fault</li>
<li>Kernel legge dati da file e mappa in memoria</li>
<li>Accessi successivi sono diretti (no I/O)</li>
</ol>

<h2>💾 Componenti e Architettura</h2>
        <ul>
            <li><strong>Page Tables</strong> - Strutture gerarchiche traduzione indirizzi (4 livelli su x86-64)</li>
            <li><strong>TLB</strong> - Translation Lookaside Buffer, cache traduzioni</li>
            <li><strong>VMA Tree</strong> - Red-black tree delle regioni memoria</li>
            <li><strong>Page Cache</strong> - Cache pagine file in memoria</li>
            <li><strong>Swap Space</strong> - Area disco per pagine non attive</li>
        </ul>

        <h2>✨ Caratteristiche Avanzate</h2>
<ul>
<li><strong>Copy-on-Write (COW)</strong> - Condivisione pagine fino a modifica</li>
<li><strong>Huge Pages</strong> - Pagine grandi (2MB/1GB) per ridurre TLB miss</li>
<li><strong>Transparent Huge Pages</strong> - Gestione automatica huge pages</li>
<li><strong>NUMA Awareness</strong> - Allocazione preferenziale su nodi vicini</li>
<li><strong>Memory Overcommit</strong> - Allocazione oltre memoria fisica disponibile</li>
<li><strong>KSM</strong> - Kernel Samepage Merging, unione pagine identiche</li>
</ul>

<h2>🔧 Configurazione e Tuning</h2>
<ul>
<li><code>/proc/sys/vm/overcommit_memory</code> - Politica overcommit (0=euristica, 1=sempre, 2=mai)</li>
<li><code>/proc/sys/vm/swappiness</code> - Aggressività swap (0-100)</li>
<li><code>/proc/sys/vm/dirty_ratio</code> - % memoria dirty prima flush</li>
<li><code>/sys/kernel/mm/transparent_hugepage/enabled</code> - Abilita THP</li>
</ul>

<h2>📊 Metriche e Monitoraggio</h2>
<ul>
<li><strong>Page Faults</strong> - Minor (già in RAM) vs Major (da disco)</li>
<li><strong>RSS</strong> - Resident Set Size, memoria fisica usata</li>
<li><strong>VSZ</strong> - Virtual Size, memoria virtuale totale</li>
<li><strong>Swap Usage</strong> - Quantità memoria swappata</li>
</ul>

<h2>🎓 Quiz sulla Virtual Memory</h2>
<div style="background: #f0f8ff; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #0288d1;">
    <h3 style="color: #0288d1; margin-bottom: 15px;">Domanda 1: Dimensione Pagina Standard</h3>
    <p style="margin-bottom: 10px;"><strong>Qual è la dimensione standard di una pagina su architettura x86-64?</strong></p>
    <div style="margin-left: 20px;">
        <p>A) 2 KB</p>
        <p>B) 4 KB ✅</p>
        <p>C) 8 KB</p>
        <p>D) 16 KB</p>
    </div>
    <p style="margin-top: 10px; font-style: italic; color: #555;">Risposta: B - La dimensione standard è 4 KB (4096 bytes)</p>
</div>

<div style="background: #f0f8ff; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #0288d1;">
    <h3 style="color: #0288d1; margin-bottom: 15px;">Domanda 2: Copy-on-Write</h3>
    <p style="margin-bottom: 10px;"><strong>Cosa succede durante un Copy-on-Write?</strong></p>
    <div style="margin-left: 20px;">
        <p>A) La pagina viene immediatamente copiata</p>
        <p>B) La pagina viene copiata solo quando modificata ✅</p>
        <p>C) La pagina viene eliminata</p>
        <p>D) La pagina viene condivisa permanentemente</p>
    </div>
    <p style="margin-top: 10px; font-style: italic; color: #555;">Risposta: B - COW copia la pagina solo al primo tentativo di scrittura</p>
</div>

<div style="background: #f0f8ff; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #0288d1;">
    <h3 style="color: #0288d1; margin-bottom: 15px;">Domanda 3: Livelli Page Tables</h3>
    <p style="margin-bottom: 10px;"><strong>Quanti livelli di page tables usa x86-64?</strong></p>
    <div style="margin-left: 20px;">
        <p>A) 2 livelli</p>
        <p>B) 3 livelli</p>
        <p>C) 4 livelli ✅</p>
        <p>D) 5 livelli</p>
    </div>
    <p style="margin-top: 10px; font-style: italic; color: #555;">Risposta: C - x86-64 usa 4 livelli: PGD, PUD, PMD, PTE</p>
</div>

<div style="background: #f0f8ff; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #0288d1;">
    <h3 style="color: #0288d1; margin-bottom: 15px;">Domanda 4: VMA (vm_area_struct)</h3>
    <p style="margin-bottom: 10px;"><strong>Cosa rappresenta una VMA?</strong></p>
    <div style="margin-left: 20px;">
        <p>A) Una singola pagina fisica</p>
        <p>B) Una regione contigua di memoria virtuale ✅</p>
        <p>C) Un processo in esecuzione</p>
        <p>D) Un file system virtuale</p>
    </div>
    <p style="margin-top: 10px; font-style: italic; color: #555;">Risposta: B - VMA descrive una regione contigua con stessi permessi</p>
</div>

<div style="background: #f0f8ff; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #0288d1;">
    <h3 style="color: #0288d1; margin-bottom: 15px;">Domanda 5: Demand Paging</h3>
    <p style="margin-bottom: 10px;"><strong>Qual è il vantaggio principale del Demand Paging?</strong></p>
    <div style="margin-left: 20px;">
        <p>A) Aumenta la velocità della CPU</p>
        <p>B) Carica le pagine solo quando necessario ✅</p>
        <p>C) Elimina i page fault</p>
        <p>D) Raddoppia la memoria disponibile</p>
    </div>
    <p style="margin-top: 10px; font-style: italic; color: #555;">Risposta: B - Demand paging carica pagine on-demand, risparmiando memoria</p>
</div>

<h2>🔗 Interazione con Altri Sottosistemi</h2>
<ul>
<li><strong>Page Allocator</strong> - Fornisce pagine fisiche per mappature</li>
<li><strong>Swap Manager</strong> - Gestisce spostamento pagine su disco</li>
<li><strong>VFS</strong> - Permette memory mapping di file</li>
<li><strong>Scheduler</strong> - Considera uso memoria per scheduling</li>
<li><strong>Device Drivers</strong> - Mappano memoria dispositivi</li>
</ul>

<h2>⚠️ Problemi Comuni e Soluzioni</h2>
<ul>
<li><strong>Memory Fragmentation</strong> - Usa huge pages o compaction</li>
<li><strong>TLB Thrashing</strong> - Riduci working set o usa huge pages</li>
<li><strong>OOM Killer</strong> - Configura overcommit e monitora memoria</li>
<li><strong>Swap Thrashing</strong> - Aumenta RAM o riduci swappiness</li>
</ul>

    </div>

    <footer>
        <p>© 2024 Linux Kernel Documentation - Virtual Memory Management</p>
    </footer>
    
    <div class="nav-buttons-right">
        <button class="nav-button" onclick="navigateToPage(-1)" id="prevBtn">◀ PAGINA PRECEDENTE</button>
        <button class="nav-button" onclick="navigateToPage(1)" id="nextBtn">PAGINA SUCCESSIVA ▶</button>
    </div>

    <script>
        const pageOrder = ["detail-functionalities.html", "detail-user-space-interfaces.html", "detail-virtual.html", "detail-bridges.html", "detail-logical.html", "detail-device-control.html", "detail-hardware-interfaces.html", "detail-electronics.html", "detail-hi-header.html", "detail-hi-char-devices.html", "detail-security.html", "detail-debugging.html", "detail-hi-subsystems.html", "detail-abstract-devices.html", "detail-hi-hardware-interfaces.html", "detail-user-peripherals.html", "detail-system-header.html", "detail-interfaces-core.html", "detail-driver-model.html", "detail-system-run.html", "detail-generic-hw-access.html", "detail-device-access.html", "detail-io.html", "detail-processing-header.html", "detail-processes.html", "detail-threads.html", "detail-synchronization.html", "detail-scheduler.html", "detail-interrupts.html", "detail-cpu-specific.html", "detail-cpu.html", "detail-memory-header.html", "detail-memory-access.html", "detail-virtual-memory.html", "detail-memory-mapping.html", "detail-logical-memory.html", "detail-page-allocator.html", "detail-physical-memory.html", "detail-memory.html", "detail-storage-header.html", "detail-files-access.html", "detail-vfs.html", "detail-page-cache.html", "detail-swap.html", "detail-logical-filesystems.html", "detail-block-devices.html", "detail-storage-drivers.html", "detail-storage-controllers.html", "detail-network-header.html", "detail-sockets-access.html", "detail-address-families.html", "detail-network-storage.html", "detail-socket-splice.html", "detail-protocols.html", "detail-network-interfaces.html", "detail-network-drivers.html", "detail-network-controllers.html"];

        function getCurrentPageIndex() {
            const currentPage = window.location.pathname.split('/').pop();
            return pageOrder.indexOf(currentPage);
        }

        function navigateToPage(direction) {
            const currentIndex = getCurrentPageIndex();
            const newIndex = currentIndex + direction;
            
            if (newIndex >= 0 && newIndex < pageOrder.length) {
                window.location.href = pageOrder[newIndex];
            }
        }

        window.addEventListener('DOMContentLoaded', function() {
            const currentIndex = getCurrentPageIndex();
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            
            if (prevBtn) prevBtn.disabled = currentIndex === 0;
            if (nextBtn) nextBtn.disabled = currentIndex === pageOrder.length - 1;
        });
    </script>
</body>
</html>'''

print("📝 Creazione detail-virtual-memory.html con struttura identica a detail-cpu.html...\n")

try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ File creato con successo!")
    print("\n📊 Caratteristiche:")
    print("   ✅ Layout identico a detail-cpu.html")
    print("   ✅ Stessi colori e dimensioni")
    print("   ✅ Stesso stile CSS")
    print("   ✅ 5 quiz sulla Virtual Memory")
    print("   ✅ Contenuto completo e dettagliato")
    print("   ✅ Pulsanti navigazione inclusi")
    print("   ✅ Responsive mobile ottimizzato")
    
except Exception as e:
    print(f"❌ Errore: {str(e)}")
