import os
from scripts.utils import execute_script
from termcolor import cprint

BASE_HDTRACKS_DIR = '/Volumes/Gelo/HDTracks'

if __name__=="__main__":
    # Check if base dir exists
    if not os.path.exists(BASE_HDTRACKS_DIR):
        raise OSError(f'{ BASE_HDTRACKS_DIR } does not exist. Please plug in the external hard drive')

    artists = sorted(os.listdir(BASE_HDTRACKS_DIR))
    
    for artist in artists:
        # Get artist dirs from root
        artist_full_path = os.path.join(BASE_HDTRACKS_DIR, artist)
    
        # Get first album from that artist
        if os.path.isdir(artist_full_path):
            album = next(os.walk(artist_full_path))[1][0]
            album_full_path = os.path.join(artist_full_path, album)

            cprint(f'{artist} - {album}', 'blue')

            album_full_path = f'"{album_full_path}"'
            execute_script('resample.py', album_full_path)
            
            print()