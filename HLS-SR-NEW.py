import os
import requests
import subprocess
from bs4 import BeautifulSoup
import datetime

def get_room_id(username):
    url = f"https://www.showroom-live.com/r/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    room_link = soup.find('a', {'class': 'st-header__link'}, href=True)['href']
    room_id = room_link.split('=')[-1]
    return room_id

def get_streaming_url(room_id, quality_label='original quality'):
    url = f"https://www.showroom-live.com/api/live/streaming_url?room_id={room_id}"
    response = requests.get(url)
    data = response.json()
    
    for stream_info in data['streaming_url_list']:
        if stream_info['label'].lower() == quality_label.lower():
            streaming_url = stream_info['url']
            return streaming_url
    
    return None

def download_stream(streaming_url, output_filename):
    subprocess.call(["ffmpeg", "-i", streaming_url, "-c", "copy", output_filename])

def main():
    username = input("Masukkan username ruangan Showroom Live: ")
    
    # Create 'downloads' directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    room_id = get_room_id(username)
    streaming_url = get_streaming_url(room_id, quality_label='original quality')
    
    if streaming_url:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        output_filename = f"downloads/{username}_{timestamp}.ts"
        
        download_stream(streaming_url, output_filename)
        print(f"Video berhasil diunduh dengan nama file: {output_filename}")
    else:
        print("Tidak dapat menemukan URL streaming dengan kualitas yang diminta.")

if __name__ == '__main__':
    main()
