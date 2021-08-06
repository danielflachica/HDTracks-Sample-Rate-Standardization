from os import system, path
from termcolor import cprint

if not path.exists("wav_raw_sample_rate"):
    system("mkdir wav_raw_sample_rate")
if not path.exists("wav_std_sample_rate"):
    system("mkdir wav_std_sample_rate")
cprint("Setup complete.", "green")