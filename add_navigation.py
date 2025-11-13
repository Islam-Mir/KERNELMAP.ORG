import os
import re

page_order = [
    'detail-functionalities.html',
    'detail-user-space-interfaces.html',
    'detail-virtual.html',
    'detail-bridges.html',
    'detail-logical.html',
    'detail-device-control.html',
    'detail-hardware-interfaces.html',
    'detail-electronics.html',
    'detail-hi-header.html',
    'detail-hi-char-devices.html',
    'detail-security.html',
    'detail-debugging.html',
    'detail-hi-subsystems.html',
    'detail-abstract-devices.html',
    'detail-hi-hardware-interfaces.html',
    'detail-user-peripherals.html',
    'detail-system-header.html',
    'detail-interfaces-core.html',
    'detail-driver-model.html',
    'detail-system-run.html',
    'detail-generic-hw-access.html',
    'detail-device-access.html',
    'detail-io.html',
    'detail-processing-header.html',
    'detail-processes.html',
    'detail-threads.html',
    'detail-synchronization.html',
    'detail-scheduler.html',
    'detail-interrupts.html',
    'detail-cpu-specific.html',
    'detail-cpu.html',
    'detail-memory-header.html',
    'detail-memory-access.html',
    'detail-virtual-memory.html',
    'detail-memory-mapping.html',
    'detail-logical-memory.html',
    'detail-page-allocator.html',
    'detail-physical-memory.html',
    'detail-memory.html',
    'detail-storage-header.html',
    'detail-files-access.html',
    'detail-vfs.html',
    'detail-page-cache.html',
    'detail-swap.html',
    'detail-logical-filesystems.html',
    'detail-block-devices.html',
    'detail-storage-drivers.html',
    'detail-storage-controllers.html',
    'detail-network-header.html',
    'detail-sockets-access.html',
    'detail-address-families.html',
    'detail-network-storage.html',
    'detail-socket-splice.html',
    'detail-protocols.html',
    'detail-network-interfaces.html',
    'detail-network-drivers.html',
    'detail-network-controllers.html'
]

navigation_css = '''
        .nav-buttons-right {
            position: fixed;
            top: 20px;
            right: 20px;
            display: flex;
            gap: 10px;
            z-index: 1000;
        }

        .nav-button {
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
        }

        .nav-button:hover {
            background: linear-gradient(135deg, #45a049 0%, #388e3c 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        .nav-button:disabled {
            background: linear-gradient(135deg, #BDBDBD 0%, #9E9E9E 100%);
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
'''

page_order_js = str(page_order).replace("'", '"')

navigation_js = f'''
    <script>
        const pageOrder = {page_order_js};

        function getCurrentPageIndex() {{
            const currentPage = window.location.pathname.split('/').pop();
            return pageOrder.indexOf(currentPage);
        }}

        function navigateToPage(direction) {{
            const currentIndex = getCurrentPageIndex();
            const newIndex = currentIndex + direction;
            
            if (newIndex >= 0 && newIndex < pageOrder.length) {{
                window.location.href = pageOrder[newIndex];
            }}
        }}

        window.addEventListener('DOMContentLoaded', function() {{
            const currentIndex = getCurrentPageIndex();
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            
            if (prevBtn) prevBtn.disabled = currentIndex === 0;
            if (nextBtn) nextBtn.disabled = currentIndex === pageOrder.length - 1;
        }});
    </script>
'''

navigation_html = '''
    <div class="nav-buttons-right">
        <button class="nav-button" onclick="navigateToPage(-1)" id="prevBtn">◀ PAGINA PRECEDENTE</button>
        <button class="nav-button" onclick="navigateToPage(1)" id="nextBtn">PAGINA SUCCESSIVA ▶</button>
    </div>
'''

base_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0"

print("🚀 Inizio aggiornamento pagine...\n")

for page in page_order:
    file_path = os.path.join(base_path, page)
    
    if not os.path.exists(file_path):
        print(f"⚠️  File non trovato: {page}")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'nav-buttons-right' in content:
            print(f"⏭️  Già aggiornato: {page}")
            continue
        
        if '</style>' in content:
            content = content.replace('</style>', navigation_css + '\n    </style>', 1)
        
        if '</body>' in content:
            content = content.replace('</body>', navigation_html + navigation_js + '\n</body>', 1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Aggiornato: {page}")
    
    except Exception as e:
        print(f"❌ Errore su {page}: {str(e)}")

print("\n🎉 Completato! Tutti i file sono stati aggiornati.")
