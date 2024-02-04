import subprocess
import eyed3
import sys
import shutil
import os
from PIL import Image
import time
from open_spotify import main as open_spotify_main

def command_to_download(song_title, song_artist, youtube_link):

    # Replace 'your_command_here' with the actual terminal command you want to run
    command = f'yt-dlp --extract-audio --audio-format mp3 -P "/Users/tahmidimran/CS Side Projects/automation-projects/YouTube-to-spotify" -o "{song_title} - {song_artist}" --write-thumbnail --convert-thumbnails jpg "{youtube_link}"'

    # Run the command
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)

    # Print the output
    print(result.stdout)

def crop_to_square(input_path, output_path):
    # Open the image
    image = Image.open(input_path)

    # Get the dimensions of the original image
    original_width, original_height = image.size

    # Calculate the size for the square crop
    size = min(original_width, original_height)

    # Calculate the crop box (left, upper, right, lower)
    left = (original_width - size) // 2
    top = (original_height - size) // 2
    right = left + size
    bottom = top + size

    # Crop the image to a square
    square_image = image.crop((left, top, right, bottom))

    # Save the cropped image
    square_image.save(output_path)

def set_mp3_metadata(file_path, title, artist, album, album_art_path):
    audiofile = eyed3.load(file_path)
    
    if audiofile is not None:
        # Set the title
        if title:
            audiofile.tag.title = title

        # Set the artist/author
        if artist:
            audiofile.tag.artist = artist
        
        # Set the album
        if album:
            audiofile.tag.album = album

        # Set the album artwork
        if album_art_path:
            with open(album_art_path, "rb") as album_art_file:
                album_art_data = album_art_file.read()
                audiofile.tag.images.set(3, album_art_data, "image/jpeg")

        # Save the changes
        audiofile.tag.save()

        print(f"Metadata updated successfully for {file_path}")
    else:
        print(f"Error loading {file_path}")

def move_file(source_path, destination_path):
    try:
        # Move the file
        shutil.move(source_path, destination_path)
        print(f"File moved successfully from '{source_path}' to '{destination_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_file(file_path):
    try:
        # Delete the file
        os.remove(file_path)
        print(f"File deleted successfully: {file_path}")
    except OSError as e:
        print(f"Error deleting the file: {e}")

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Usage: python3 download-youtube.py 'youtube url' 'song-title' 'song-name' 'song-album'")
        sys.exit(1)

    youtube_url = sys.argv[1]
    song_title = sys.argv[2]
    song_artist = sys.argv[3]
    song_album = sys.argv[4] if len(sys.argv) > 4 else 'Local Files'
    mp3_file_path = f"/Users/tahmidimran/CS Side Projects/automation-projects/YouTube-to-spotify/{song_title} - {song_artist}.mp3"
    album_art_path = f"/Users/tahmidimran/CS Side Projects/automation-projects/YouTube-to-spotify/{song_title} - {song_artist}.jpg"

    print(f"Script name: {youtube_url}")
    print(f"Song Title: {song_title}")
    print(f"Song Artist: {song_artist}")
    print(f"Song Album: {song_album}")
    print(f"Downloaded MP3: {mp3_file_path}")
    print(f"Downloaded Thumbnail: {album_art_path}")
    command_to_download(song_title=song_title, song_artist=song_artist, youtube_link=youtube_url)
    crop_to_square(input_path=album_art_path, output_path=album_art_path)
    set_mp3_metadata(file_path=mp3_file_path, title=song_title, artist=song_artist, album=song_album, album_art_path=album_art_path)
    move_file(mp3_file_path, "/Users/tahmidimran/Downloads")
    delete_file(album_art_path)
    time.sleep(10)
    open_spotify_main()

    


