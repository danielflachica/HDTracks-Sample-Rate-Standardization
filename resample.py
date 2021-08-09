import scripts.utils as utils
import sys
from os import path
from termcolor import cprint

if __name__=="__main__":
    if len(sys.argv) != 2:
        raise OSError('Please supply the Album directory name as an argument')
    else:
        in_dir = sys.argv[1]
        if path.isdir(in_dir):
            in_dir = f'"{in_dir}"'
            utils.execute_script('scripts/import_album.py', in_dir)
            utils.execute_script('scripts/resample_tracks.py')
            out_dir = in_dir.replace('HDTracks', 'HDTracks (Std Sample Rate)')
            utils.execute_script('scripts/export_songs.py', out_dir)
            utils.execute_script('scripts/cleanup.py')
        else:
            raise OSError(f'{ in_dir } is not a valid dir')