import yt_dlp

def download_high_quality_m4a(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        
        # 1. Download thumbnail must be enabled
        'writethumbnail': True, 
        
        'postprocessors': [
            # 2. Convert thumbnail to JPG for compatibility with M4A
            {
                'key': 'FFmpegThumbnailsConvertor',
                'format': 'jpg',
            },
            # 3. Extract Audio
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            },
            # 4. Add Metadata (MANDATORY before EmbedThumbnail in some versions)
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
        # 'ffmpeg_location': 'C:/Users/CERN/Documents/ffmpeg-master-latest-win64-gpl-shared/bin', # Windows path, typically not needed on Mac if in PATH
        
        # Delete the .jpg thumbnail file after successfully embedding into .m4a
        'writemetadata': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("\nFinished! Audio with thumbnail successfully created.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Enter YouTube URL: ")
    download_high_quality_m4a(link)