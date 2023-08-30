import subprocess
import os
import requests
import time

def is_internet_available():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def main():
    max_retries = 88888
    retry_interval = 30  # Jeda 30 detik sebelum mencoba kembali
    
    retries = 0

    while not is_internet_available():
        print("Tidak ada koneksi internet. Menunggu koneksi kembali...")
        time.sleep(retry_interval)
        retries += 1
        
        if retries >= max_retries:
            print("Batas maksimum percobaan tercapai. Keluar dari skrip.")
            break

    if is_internet_available():
        print("Koneksi internet tersedia. Melanjutkan eksekusi skrip...")
        
        python_scripts = [
            "AutoJKT_1.py",
            "AutoJKT_2.py",
            "AutoJKT_3.py",
            "AutoJKT_4.py",
            "AutoJKT_5.py",
            "AutoJKT_6.py",
            "AutoJKT_7.py",
            "AutoJKT_8.py",
            "AutoJKT_9.py",
            "AutoJKT_10.py",
            "AutoJKT_11.py",
            "AutoJKT_12.py",
            "AutoJKT_13.py",
            "AutoJKT_14.py",
            "AutoJKT_15.py",
            "AutoJKT_16.py",
            "AutoJKT_17.py",
            "AutoJKT_18.py",
            "AutoJKT_19.py",
            "AutoJKT_20.py",
            "AutoJKT_21.py",
            "AutoJKT_22.py",
            "AutoJKT_23.py",
            "AutoJKT_24.py",
            "AutoJKT_25.py",
            "AutoJKT_26.py",
            "AutoJKT_27.py",
            "AutoJKT_28.py",
            "AutoJKT_29.py",
            "AutoJKT_30.py",
            "AutoJKT_31.py",
            "AutoJKT_32.py",
            "AutoJKT_33.py",
            "AutoJKT_34.py",
            "AutoJKT_35.py",
            "AutoJKT_36.py",
            "AutoJKT_37.py",
            "AutoJKT_38.py",
            "AutoJKT_39.py",
            "AutoJKT_40.py",
            "AutoJKT_41.py",
            "AutoJKT_42.py",
            "AutoJKT_43.py",
            "AutoJKT_44.py"
        ]
        
        line_counter = 0
        
        for script in python_scripts:
            subprocess.Popen(["python", script], shell=True)
            time.sleep(0)  # Jeda 20 detik sebelum menjalankan file .py berikutnya
            
            line_counter += 1
            
            if line_counter % 3000 == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
            
            # Tunggu semua subprocess selesai sebelum melanjutkan ke file .py berikutnya
            time.sleep(0.2)

if __name__ == '__main__':
    main()
