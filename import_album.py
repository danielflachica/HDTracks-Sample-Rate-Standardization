import os
import sys
from tqdm import tqdm
from termcolor import cprint
import utils as au
from shutil import copy

OUT_DIR = '/Users/danielflachica/Desktop/Thesis/resample-hdtracks/wav_raw_sample_rate'

if __name__=="__main__":
    if len(sys.argv) != 2:
        raise OSError('Please supply the Album directory name as an argument')
    else:
        IN_DIR = sys.argv[1]

        # Check if all dirs are valid (exists and not empty)
        if not os.path.exists(IN_DIR):
            raise OSError(f'Could not find { IN_DIR }')
        au.remove_DS_Store(IN_DIR)
        if len(os.listdir(IN_DIR)) == 0:
            raise OSError(f'Empty dir found at { IN_DIR }')

        # Collect all audio files
        tracks = os.listdir(IN_DIR)
        audio_files = []
        for track in tqdm(tracks, desc='Collecting audio files from album'):
            if track.lower().endswith('.wav'):
                audio_files.append(f'{ IN_DIR }/{ track }')

        # Transfer files
        for audio_file in tqdm(audio_files, desc='Importing album'):
            # os.system(f'mv { audio_file } { OUT_DIR }')
            copy(audio_file, OUT_DIR)
    
        cprint(f'{ len(audio_files) } tracks imported successfully', 'green')