import os

def remove_DS_Store(dir):
    if os.path.exists(os.path.join(dir, '.DS_Store')):
        print(f'.DS_Store found. Removing...')
        os.remove(os.path.join(dir, '.DS_Store'))

def get_filename_minus_extension(fpath):
    return os.path.basename(fpath)[:-4]