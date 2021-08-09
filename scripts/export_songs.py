import os
import sys
from tqdm import tqdm
from termcolor import cprint
import utils as au
from shutil import copy

IN_DIR = '/Users/danielflachica/Desktop/Thesis/resample-hdtracks/wav_std_sample_rate'

def main(out_dir):
    # Check if all dirs are valid (exists and not empty)
    if not os.path.exists(out_dir):
        raise OSError(f'Could not find { out_dir }')
    if not os.path.exists(IN_DIR):
        raise OSError(f'Could not find { IN_DIR }')

    # Collect all audio files
    tracks = os.listdir(IN_DIR)
    audio_files = []
    for track in tqdm(tracks, desc='Collecting standardized sample rate audio files'):
        if track.lower().endswith('.wav'):
            audio_files.append(f'{ IN_DIR }/{ track }')

    # Transfer files
    for audio_file in tqdm(audio_files, desc='Exporting songs'):
        copy(audio_file, out_dir)

    cprint(f'{ len(audio_files) } tracks exported successfully', 'green')


if __name__=="__main__":
    if len(sys.argv) != 2:
        raise OSError('Please supply the Album directory name as an argument')
    else:
        main(sys.argv[1])