import subprocess
import os

# Daftar nama file .py yang ingin dijalankan
python_scripts = [
    "Auto-JKT  (1).py",
    "Auto-JKT  (2).py",
    "Auto-JKT  (3).py",
    "Auto-JKT  (4).py",
    "Auto-JKT  (5).py",
    "Auto-JKT  (6).py",
    "Auto-JKT  (7).py",
    "Auto-JKT  (8).py",
    "Auto-JKT  (9).py"
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
        # Lanjutkan dengan eksekusi skrip lain di sini

if __name__ == '__main__':
    main()

# Inisialisasi counter untuk menghitung jumlah baris yang telah ditampilkan
line_counter = 0

# Jalankan setiap file .py menggunakan subprocess
for script in python_scripts:
    subprocess.Popen(["python", script], shell=True)
    time.sleep(20)  # Jeda 2 detik sebelum menjalankan file .py berikutnya
    
    # Update counter
    line_counter += 1
    
    # Setelah mencapai 3000 baris, bersihkan terminal
    if line_counter % 3000 == 0:
        os.system('cls' if os.name == 'nt' else 'clear')

# Tunggu semua subprocess selesai sebelum keluar
time.sleep(5 * len(python_scripts))