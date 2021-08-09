import os
import sys
from tqdm import tqdm
from termcolor import cprint
import utils as au
from shutil import copy

OUT_DIR = '/Users/danielflachica/Desktop/Thesis/resample-hdtracks/wav_raw_sample_rate'

def main(in_dir):
    # Check if all dirs are valid (exists and not empty)
    if not os.path.exists(in_dir):
        raise OSError(f'Could not find { in_dir }')
    au.remove_DS_Store(in_dir)
    if len(os.listdir(in_dir)) == 0:
        raise OSError(f'Empty dir found at { in_dir }')

    # Collect all audio files
    tracks = os.listdir(in_dir)
    audio_files = []
    for track in tqdm(tracks, desc='Collecting audio files from album'):
        if track.lower().endswith('.wav'):
            audio_files.append(f'{ in_dir }/{ track }')

    # Transfer files
    for audio_file in tqdm(audio_files, desc='Importing album'):
        # os.system(f'mv { audio_file } { OUT_DIR }')
        copy(audio_file, OUT_DIR)

    cprint(f'{ len(audio_files) } tracks imported successfully', 'green')


if __name__=="__main__":
    if len(sys.argv) != 2:
        raise OSError('Please supply the Album directory name as an argument')
    else:
        main(sys.argv[1])