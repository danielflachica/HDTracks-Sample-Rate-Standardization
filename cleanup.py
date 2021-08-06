import os
import utils
from termcolor import cprint

BASE_DIR = '/Users/danielflachica/desktop/resample-hdtracks'

if __name__=="__main__":
    dirs = [
        'wav_raw_sample_rate',
        'wav_std_sample_rate'
    ]

    for dir in dirs:
        # Delete audio files (wav)
        utils.remove_DS_Store(dir)
        if len(os.listdir(dir)) > 0:
            os.system(f'cd { os.path.join(BASE_DIR, dir) } && find . -type f -name "*.wav" -delete')

cprint("Done cleaning up files", "green")
