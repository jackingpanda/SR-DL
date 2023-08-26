import subprocess

# Daftar nama file .py yang ingin dijalankan
python_scripts = [
    "test - Auto AKB (1).py",
    "test - Auto AKB (2).py",
    "test - Auto AKB (3).py",
    "test - Auto AKB (4).py",
    "test - Auto AKB (5).py"
]

# Jalankan setiap file .py menggunakan subprocess
for script in python_scripts:
    subprocess.Popen(["python", script], shell=True)

import requests
import time

def is_internet_available():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def main():
    max_retries = 88888888
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
        # Lanjutkan dengan eksekusi skrip lain di sini

if __name__ == '__main__':
    main()