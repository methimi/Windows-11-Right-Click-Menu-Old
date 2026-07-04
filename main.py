import winreg as reg
import sys
import subprocess

def klasik_menuyu_ac():
    """Windows 11'de sağ tık menüsünü klasik (Windows 10) haline getirir."""
    try:
        anahtar_yolu = r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32"
        
        # Anahtarı oluştur
        anahtar = reg.CreateKey(reg.HKEY_CURRENT_USER, anahtar_yolu)
        reg.SetValueEx(anahtar, "", 0, reg.REG_SZ, "")
        reg.CloseKey(anahtar)
        
        print("Klasik sağ tık menüsü aktif edildi.")
        
        # Explorer'ı yeniden başlat
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"])
        subprocess.run(["explorer.exe"])
        
    except Exception as e:
        print(f"Hata oluştu: {e}")

def yeni_menuyu_geri_getir():
    """Windows 11'in yeni sağ tık menüsünü geri getirir (değişikliği geri alır)."""
    try:
        anahtar_yolu = r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}"
        
        def sil_recursive(kok, yol):
            with reg.OpenKey(kok, yol, 0, reg.KEY_ALL_ACCESS) as anahtar:
                while True:
                    try:
                        alt_anahtar = reg.EnumKey(anahtar, 0)
                        sil_recursive(kok, f"{yol}\\{alt_anahtar}")
                    except OSError:
                        break
            reg.DeleteKey(kok, yol)
        
        sil_recursive(reg.HKEY_CURRENT_USER, anahtar_yolu)
        
        print("Yeni sağ tık menüsü geri getirildi.")
        
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"])
        subprocess.run(["explorer.exe"])
        
    except FileNotFoundError:
        print("Bu anahtar zaten mevcut değil, yapılacak bir şey yok.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    if sys.platform != "win32":
        print("Bu script sadece Windows üzerinde çalışır.")
        sys.exit(1)
    
    print("1 - Klasik menüyü aç (Windows 10 tarzı)")
    print("2 - Yeni menüyü geri getir (Windows 11 varsayılan)")
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        klasik_menuyu_ac()
    elif secim == "2":
        yeni_menuyu_geri_getir()
    else:
        print("Geçersiz seçim.")