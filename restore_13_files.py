import os
import shutil

backup_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 4.0\KERNEL 3.0 backup"
dest_path = r"C:\Users\islam\Desktop\kernel.3.0\KERNEL 3.0\KERNELMAP.ORG"

files_to_restore = [
    'detail-device-access-bus-drivers.html',
    'detail-driver-model.html',
    'detail-electronics.html',
    'detail-generic-hw-access.html',
    'detail-hi-hardware-interfaces.html',
    'detail-hi-subsystems.html',
    'detail-interfaces-core.html',
    'detail-logical-filesystems.html',
    'detail-memory.html',
    'detail-network-controllers.html',
    'detail-network-storage.html',
    'detail-security.html',
    'detail-user-peripherals.html'
]

print("🔄 RIPRISTINO FILE DAL BACKUP...\n")

restored = 0

for file in files_to_restore:
    src = os.path.join(backup_path, file)
    dst = os.path.join(dest_path, file)
    
    if not os.path.exists(src):
        print(f"⚠️  Backup non trovato: {file}")
        continue
    
    try:
        shutil.copy2(src, dst)
        print(f"✅ Ripristinato: {file}")
        restored += 1
    except Exception as e:
        print(f"❌ Errore: {file} - {str(e)}")

print(f"\n🎉 COMPLETATO! {restored} file ripristinati dal backup.")
print("✅ Le pagine sono tornate come erano prima.")
