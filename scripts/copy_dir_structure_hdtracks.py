# This script copies the directory struture of /Volumes/Gelo/HDTracks to the target dest wihtout copying files

import os
from tqdm import tqdm
from termcolor import cprint

inputpath = '/Volumes/Gelo/HDTracks'
outputpath = '/Volumes/Gelo/HDTracks (Std Sample Rate)'

if not os.path.exists(outputpath):
    os.mkdir(outputpath)

for dirpath, dirnames, filenames in tqdm(os.walk(inputpath), desc='Copying directory structure'):
    structure = os.path.join(outputpath, os.path.relpath(dirpath, inputpath))
    if not os.path.isdir(structure):
        os.mkdir(structure)

cprint(f'{inputpath} >> {outputpath}', 'green')