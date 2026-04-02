import yt_dlp

def download_high_quality_m4a(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        
        # 1. Download thumbnail wajib diaktifkan
        'writethumbnail': True, 
        
        'postprocessors': [
            # 2. Konversi thumbnail ke JPG agar kompatibel dengan M4A
            {
                'key': 'FFmpegThumbnailsConvertor',
                'format': 'jpg',
            },
            # 3. Ekstrak Audio
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            },
            # 4. Masukkan Metadata (WAJIB sebelum EmbedThumbnail di beberapa versi)
            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            },
            # 5. Embed Thumbnail
            {
                'key': 'EmbedThumbnail',
            },
        ],
        
        'outtmpl': '%(title)s.%(ext)s',
        'ffmpeg_location': 'C:/Users/CERN/Documents/ffmpeg-master-latest-win64-gpl-shared/bin',
        
        # Menghapus file thumbnail .jpg setelah berhasil di-embed ke .m4a
        'writemetadata': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("\nSelesai! Audio 256kbps dengan thumbnail berhasil dibuat.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Masukkan URL YouTube: ")
    download_high_quality_m4a(link)