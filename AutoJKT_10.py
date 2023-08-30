import os
import requests
import subprocess
from bs4 import BeautifulSoup
import datetime
import time
import ctypes

# Daftar room ID yang ingin dipantau jika online
room_ids_to_monitor = [
    "400717"
]

def get_streaming_url(room_id, quality_label='original quality'):
    url = f"https://www.showroom-live.com/api/live/streaming_url?room_id={room_id}"
    response = requests.get(url)
    data = response.json()

    for stream_info in data.get('streaming_url_list', []):
        if stream_info['label'].lower() == quality_label.lower():
            streaming_url = stream_info['url']
            return streaming_url

    return None

def get_room_name(room_id):
    url = f"https://www.showroom-live.com/api/room/profile?room_id={room_id}"
    response = requests.get(url)
    data = response.json()
    room_url_key = data.get('room_url_key', 'Unknown')
    room_name = data.get('room_name', 'Unknown')

    cleaned_room_url_key = ''.join(c if c.isalnum() else '_' for c in room_url_key)
    cleaned_room_name = ''.join(c if c.isalnum() else '_' for c in room_name)
    return f"{cleaned_room_url_key}_{cleaned_room_name}"

def download_stream(streaming_url, output_filename):
    subprocess.call(["ffmpeg", "-i", streaming_url, "-c:v", "copy", "-c:a", "copy", output_filename])

def main():
    # Set judul jendela di Windows
    ctypes.windll.kernel32.SetConsoleTitleW("JKT48 Showroom Automation by Dimaskool © 2023")
    
    print("Automation JKT48 New Era Showroom by Dimaskool © 2023\n")
    
    while True:
        found = False

        for room_id in room_ids_to_monitor:
            streaming_url = get_streaming_url(room_id, quality_label='original quality')

            if streaming_url:
                found = True
                room_name = get_room_name(room_id)
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
                output_filename = f"downloadsJKT48/Live Showroom {room_name}_{timestamp}.mp4"

                download_stream(streaming_url, output_filename)
                print(f"Video dari room ID {room_id} berhasil diunduh dengan nama file: {output_filename}")
            else:
                print(f"Tidak dapat menemukan URL streaming untuk room ID {room_id}.")

        if not found:
            print("Tidak ada yang online. Menunggu beberapa saat sebelum mencoba lagi...")
            time.sleep(30)  # Jeda 1 menit sebelum mencoba lagi

        print("\nMenunggu untuk mencoba lagi...\n")
        time.sleep(5)  # Jeda 5 detik sebelum mencoba kembali

if __name__ == '__main__':
    while True:
        main()
        print("\nMenunggu untuk mencoba lagi setelah semua selesai...\n")
        time.sleep(30)  # Jeda 1 menit sebelum mencoba lagi setelah semua selesai
