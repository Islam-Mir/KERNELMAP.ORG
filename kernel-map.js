// Dati per le preview e i dettagli
const sectionData = {
    // Colonna 1 - Layers
    'functionalities': {
        title: 'Functionalities Layers',
        description: 'Livelli funzionali del kernel Linux. Struttura gerarchica dai servizi utente all\'hardware.',
        page: 'detail-functionalities.html'
    },
    'user-space-interfaces': {
        title: 'User Space Interfaces',
        description: 'Porte e API (system call, /proc, /sys) che permettono ai programmi utente di chiedere servizi al kernel.',
        page: 'detail-user-space-interfaces.html'
    },
    'virtual': {
        title: 'Virtual',
        description: 'Qui il kernel crea \'realtà\' virtuali per i programmi (es. memoria virtuale) in modo che ogni programma pensi di avere risorse dedicate.',
        page: 'detail-virtual.html'
    },
    'bridges': {
        title: 'Bridges',
        description: 'Moduli che collegano diverse aree del kernel per permettere comunicazione e riuso di funzionalità tra sottosistemi.',
        page: 'detail-bridges.html'
    },
    'logical': {
        title: 'Logical',
        description: 'Livello che astrae l\'hardware in servizi logici: gestione dei processi, file, memoria e rete, presentati in modo ordinato ai programmi.',
        page: 'detail-logical.html'
    },
    'device-control': {
        title: 'Device Control',
        description: 'La parte che controlla direttamente l\'hardware: contiene i driver, le funzioni di I/O e il codice che interagisce fisicamente con i dispositivi.',
        page: 'detail-device-control.html'
    },
    'hardware-interfaces': {
        title: 'Hardware Interfaces',
        description: 'Punti di contatto tra hardware e software: registri, interrupt e porte I/O che permettono al software di comunicare con l\'hardware.',
        page: 'detail-hardware-interfaces.html'
    },
    'electronics': {
        title: 'Electronics',
        description: 'Sono i componenti fisici del computer: CPU, RAM, controller di disco e periferiche come tastiera e mouse.',
        page: 'detail-electronics.html'
    },
    
    // Colonna 2 - Human Interfaces
    'hi-header': {
        title: 'Human Interfaces',
        description: 'Sottosistema per interfacce di input/output umane. Dispositivi e driver.',
        page: 'detail-hi-header.html'
    },
    'hi-char-devices': {
        title: 'HI Char Devices',
        description: 'Funzioni come cdev_add e register_chrdev che dicono al sistema che è stato aggiunto un dispositivo a caratteri.',
        page: 'detail-hi-char-devices.html'
    },
    'security': {
        title: 'Security',
        description: 'Funzioni che gestiscono permessi e controllo accessi (security_inode_create, security_ops).',
        page: 'detail-security.html'
    },
    'debugging': {
        title: 'Debugging',
        description: 'Strumenti come kprobe e register_kprobe che aiutano a ispezionare il kernel live per trovare problemi.',
        page: 'detail-debugging.html'
    },
    'hi-subsystems': {
        title: 'HI Subsystems',
        description: 'Set di file operations (input_fops, snd_fops, video_fops) che definiscono come gestire input, audio e video.',
        page: 'detail-hi-subsystems.html'
    },
    'abstract-devices-drivers': {
        title: 'Abstract Devices & HID Class Drivers',
        description: 'Console e frame buffer (console, fb_fops): come il kernel gestisce il testo dello schermo e l\'area di disegno.',
        page: 'detail-abstract-devices.html'
    },
    'hi-hardware-interfaces': {
        title: 'HI Peripherals Device Drivers',
        description: 'Driver per periferiche di interfaccia umana. Mouse, tastiera, touchpad.',
        page: 'detail-hi-hardware-interfaces.html'
    },
    'user-peripherals': {
        title: 'User Peripherals',
        description: 'Periferiche reali usate dall\'utente: tastiera, camera, audio, display.',
        page: 'detail-user-peripherals.html'
    },
    
    // Colonna 3 - System
    'system-header': {
        title: 'System',
        description: 'Livello di sistema del kernel. Gestione core del kernel.',
        page: 'detail-system-header.html'
    },
    'interfaces-core': {
        title: 'Interfaces Core',
        description: 'Interfaccia core di sistema. System call table e entry points.',
        page: 'detail-interfaces-core.html'
    },
    'driver-model': {
        title: 'Driver Model',
        description: 'Strutture come kobject e device_create per organizzare i driver e creare astrazioni software sui dispositivi.',
        page: 'detail-driver-model.html'
    },
    'system-run': {
        title: 'System Run',
        description: 'Azioni di avvio e spegnimento del kernel: boot, shutdown e gestione dell\'energia.',
        page: 'detail-system-run.html'
    },
    'generic-hw-access': {
        title: 'Generic HW Access',
        description: 'Strutture come kobject e bus_type che organizzano dispositivi hardware e i loro bus.',
        page: 'detail-generic-hw-access.html'
    },
    'device-access-bus-drivers': {
        title: 'Device Access and Bus Drivers',
        description: 'Accesso ai dispositivi e driver di bus. Operazioni di lettura/scrittura.',
        page: 'detail-device-access.html'
    },
    'io': {
        title: 'I/O',
        description: 'Input/Output di sistema. Porte I/O, ACPI, controller USB.',
        page: 'detail-io.html'
    },
    
    // Colonna 4 - Processing
    'processing-header': {
        title: 'Processing',
        description: 'Sottosistema di elaborazione del kernel. Processi, thread e scheduling.',
        page: 'detail-processing-header.html'
    },
    'processes': {
        title: 'Processes',
        description: 'Codice che esegue e avvia programmi (sys_execve, linux_binfmt) e gestisce i tipi di file eseguibili.',
        page: 'detail-processes.html'
    },
    'threads': {
        title: 'Threads',
        description: 'Strutture per creare thread nel kernel (kernel_thread, work_struct) e lavorare in parallelo.',
        page: 'detail-threads.html'
    },
    'synchronization': {
        title: 'Synchronization',
        description: 'Meccanismi come spinlock, mutex e semaphore che evitano conflitti quando più entità usano la stessa risorsa.',
        page: 'detail-synchronization.html'
    },
    'scheduler': {
        title: 'Scheduler',
        description: 'Il pianificatore che decide quale processo o thread usa la CPU (task_struct, schedule).',
        page: 'detail-scheduler.html'
    },
    'interrupts-core': {
        title: 'Interrupts Core',
        description: 'do_IRQ e irq_handler, il codice che gestisce le interruzioni hardware e risponde ai segnali esterni.',
        page: 'detail-interrupts.html'
    },
    'cpu-specific': {
        title: 'CPU Specific',
        description: 'Funzioni dipendenti dall\'architettura della CPU, per esempio lettura di registri speciali (read_msr).',
        page: 'detail-cpu-specific.html'
    },
    'cpu': {
        title: 'CPU',
        description: 'Processore. Registri, APIC, interrupt controller.',
        page: 'detail-cpu.html'
    },
    
    // Colonna 5 - Memory
    'memory-header': {
        title: 'Memory',
        description: 'Sottosistema di gestione della memoria. Allocazione e mapping di memoria.',
        page: 'detail-memory-header.html'
    },
    'memory-access': {
        title: 'Memory Access',
        description: 'Funzioni come copy_to_user e vm_map_ram per copiare dati tra kernel e user-space e mappare RAM.',
        page: 'detail-memory-access.html'
    },
    'virtual-memory': {
        title: 'Virtual Memory',
        description: 'vmalloc, vfree e vma: gestione della memoria virtuale e delle aree virtuali per i processi.',
        page: 'detail-virtual-memory.html'
    },
    'memory-mapping': {
        title: 'Memory Mapping',
        description: 'kmap, kmalloc e vmalloc_area: collegano memoria virtuale e fisica e allocano memoria nel kernel.',
        page: 'detail-memory-mapping.html'
    },
    'logical-memory': {
        title: 'Logical Memory',
        description: 'Come il kernel vede la memoria fisica e la gestisce (physically mapped memory).',
        page: 'detail-logical-memory.html'
    },
    'page-allocator': {
        title: 'Page Allocator',
        description: 'Funzioni come __get_free_pages per trovare e assegnare pagine libere di memoria.',
        page: 'detail-page-allocator.html'
    },
    'physical-memory-ops': {
        title: 'Physical Memory Operations',
        description: 'Operazioni sulle page table entries (pte) che traducono indirizzi virtuali in fisici e controllano protezioni.',
        page: 'detail-physical-memory.html'
    },
    'memory': {
        title: 'Memory',
        description: 'Memoria fisica. RAM, DMA, MMU.',
        page: 'detail-memory.html'
    },
    
    // Colonna 6 - Storage
    'storage-header': {
        title: 'Storage',
        description: 'Sottosistema di gestione dello storage. File system e dispositivi di blocco.',
        page: 'detail-storage-header.html'
    },
    'files-directories-access': {
        title: 'Files & Directories Access',
        description: 'Chiamate per aprire, leggere e scrivere file e accedere a /proc e /sys.',
        page: 'detail-files-access.html'
    },
    'vfs': {
        title: 'Virtual File System',
        description: 'VFS, inode e file_operations: il livello che unifica le operazioni sui file per tutti i file system.',
        page: 'detail-vfs.html'
    },
    'page-cache': {
        title: 'Page Cache',
        description: 'Cache in RAM delle pagine di file più usate per velocizzare l\'accesso ai file.',
        page: 'detail-page-cache.html'
    },
    'swap': {
        title: 'Swap',
        description: 'Uso del disco come memoria di appoggio: sys_swapon e gestione dell\'area swap.',
        page: 'detail-swap.html'
    },
    'logical-filesystems': {
        title: 'Logical File Systems',
        description: 'Gestisce quali file system sono montati e le operazioni sulle directory.',
        page: 'detail-logical-filesystems.html'
    },
    'block-devices': {
        title: 'Block Devices',
        description: 'Codice che legge/scrive dati in blocchi sui dischi (model: block_device_operations).',
        page: 'detail-block-devices.html'
    },
    'storage-drivers': {
        title: 'Storage Drivers',
        description: 'Driver per dispositivi di archiviazione nella directory drivers/block.',
        page: 'detail-storage-drivers.html'
    },
    'storage-controllers': {
        title: 'Storage Controllers',
        description: 'Chip e standard che controllano dischi: SCSI, SATA, NVMe.',
        page: 'detail-storage-controllers.html'
    },
    
    // Colonna 7 - Networking
    'network-header': {
        title: 'Networking',
        description: 'Sottosistema di rete del kernel. Protocolli, socket e interfacce di rete.',
        page: 'detail-network-header.html'
    },
    'sockets-access': {
        title: 'Socket Access',
        description: 'System call per creare socket e inviare/ricevere dati (sys_socket, sys_sendmsg).',
        page: 'detail-sockets-access.html'
    },
    'address-families': {
        title: 'Address Families',
        description: 'Inizializzazione e operazioni per famiglie di protocolli come inet (IPv4/IPv6).',
        page: 'detail-address-families.html'
    },
    'network-storage': {
        title: 'Network Storage',
        description: 'Rappresentazione interna di socket per l\'uso come canali di rete.',
        page: 'detail-network-storage.html'
    },
    'socket-splice': {
        title: 'Socket Splice',
        description: 'Strutture come socket, sock_create e sock_ioctl che rappresentano i punti di contatto per la rete.',
        page: 'detail-socket-splice.html'
    },
    'protocols': {
        title: 'Protocols',
        description: 'Implementazioni di TCP, UDP e routing (tcp_prot, udp_prot, ip_route).',
        page: 'detail-protocols.html'
    },
    'network-interfaces': {
        title: 'Network Interfaces',
        description: 'Strutture net_device_ops per definire come interagire con una scheda di rete.',
        page: 'detail-network-interfaces.html'
    },
    'network-device-drivers': {
        title: 'Network Device Drivers',
        description: 'Driver che permettono l\'uso di schede di rete fisiche (es. usb_ether).',
        page: 'detail-network-drivers.html'
    },
    'network-controllers': {
        title: 'Network Controllers',
        description: 'Hardware fisico per rete: Ethernet e Wi-Fi.',
        page: 'detail-network-controllers.html'
    }
};

// Funzione per ottenere ID univoco per ogni sottosezione
function getSubsectionId(element) {
    // Controlla se ha data-id direttamente
    if (element.hasAttribute('data-id')) {
        return element.getAttribute('data-id');
    }
    
    // Se no, controlla il parent section
    const parentSection = element.closest('.section');
    if (parentSection && parentSection.hasAttribute('data-id')) {
        return parentSection.getAttribute('data-id');
    }
    
    // Altrimenti, genera dal titolo
    const title = element.querySelector('.subsection-title') || element.querySelector('.section-title');
    if (!title) return null;
    return title.textContent.toLowerCase()
        .replace(/[\s<br>]+/g, '-')
        .replace(/[&]+/g, 'and')
        .replace(/[^a-z0-9-]/g, '')
        .replace(/-+/g, '-')
        .replace(/^-|-$/g, '');
}

let hideOverlayTimeout;

// Mostra preview al hover - per subsection
document.querySelectorAll('.subsection').forEach(subsection => {
    const id = getSubsectionId(subsection);
    if (!id) return;
    
    subsection.addEventListener('mouseenter', function() {
        clearTimeout(hideOverlayTimeout);
        const data = sectionData[id];
        if (data) {
            document.getElementById('previewTitle').textContent = data.title;
            document.getElementById('previewDescription').textContent = data.description;
            document.getElementById('hoverPreviewOverlay').classList.add('active');
        }
    });
    
    subsection.addEventListener('mouseleave', function() {
        hideOverlayTimeout = setTimeout(() => {
            document.getElementById('hoverPreviewOverlay').classList.remove('active');
        }, 200);
    });
});

// Mostra preview al hover - per section header-only (senza subsection)
document.querySelectorAll('.section-title').forEach(sectionTitle => {
    const section = sectionTitle.closest('.section');
    if (!section || section.querySelector('.subsection')) return; // Skip se ha subsection
    
    const id = section.getAttribute('data-id');
    if (!id) return;
    
    section.addEventListener('mouseenter', function() {
        clearTimeout(hideOverlayTimeout);
        const data = sectionData[id];
        if (data) {
            // Controlla se è una delle 3 celle speciali: THREADS, SYNCHRONIZATION, SCHEDULER
            const isSpecialCell = section.classList.contains('col4-row3') || 
                                 section.classList.contains('col4-row4') || 
                                 section.classList.contains('col4-row5');
            
            if (isSpecialCell) {
                // Usa il nuovo overlay a SINISTRA
                document.getElementById('previewTitleLeft').textContent = data.title;
                document.getElementById('previewDescriptionLeft').textContent = data.description;
                const overlayLeft = document.getElementById('hoverPreviewOverlayLeft');
                overlayLeft.classList.add('active');
            } else {
                // Usa l'overlay centrale
                document.getElementById('previewTitle').textContent = data.title;
                document.getElementById('previewDescription').textContent = data.description;
                const overlay = document.getElementById('hoverPreviewOverlay');
                overlay.classList.add('active');
            }
        }
    });
    
    section.addEventListener('mouseleave', function() {
        hideOverlayTimeout = setTimeout(() => {
            document.getElementById('hoverPreviewOverlay').classList.remove('active');
            document.getElementById('hoverPreviewOverlayLeft').classList.remove('active');
        }, 200);
    });
});

// Nascondi preview al mouseleave dal overlay (centrale)
const overlay = document.getElementById('hoverPreviewOverlay');
overlay.addEventListener('mouseleave', function() {
    document.getElementById('hoverPreviewOverlay').classList.remove('active');
});

// Nascondi preview al mouseleave dal overlay (sinistra)
const overlayLeft = document.getElementById('hoverPreviewOverlayLeft');
overlayLeft.addEventListener('mouseleave', function() {
    document.getElementById('hoverPreviewOverlayLeft').classList.remove('active');
});

// Click per aprire la pagina dettagli - per subsection
document.querySelectorAll('.subsection').forEach(subsection => {
    const id = getSubsectionId(subsection);
    if (!id) return;
    
    subsection.style.cursor = 'pointer';
    subsection.addEventListener('click', function(e) {
        e.stopPropagation();
        const data = sectionData[id];
        if (data && data.page) {
            window.location.href = data.page;
        }
    });
});

// Click per aprire la pagina dettagli - per section header-only
document.querySelectorAll('.section-title').forEach(sectionTitle => {
    const section = sectionTitle.closest('.section');
    if (!section || section.querySelector('.subsection')) return; // Skip se ha subsection
    
    const id = section.getAttribute('data-id');
    if (!id) return;
    
    section.style.cursor = 'pointer';
    section.addEventListener('click', function(e) {
        e.stopPropagation();
        const data = sectionData[id];
        if (data && data.page) {
            window.location.href = data.page;
        }
    });
});

// Chiudi preview cliccando fuori
document.getElementById('hoverPreviewOverlay').addEventListener('click', function(e) {
    if (e.target === this) {
        this.classList.remove('active');
    }
});