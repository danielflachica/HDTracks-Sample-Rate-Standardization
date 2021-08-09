from os import path, listdir
from tqdm import tqdm
import librosa
import soundfile as sf
import utils as au

STD_SAMPLE_RATE = 44100 # 44.1 kHz (https://www.izotope.com/en/learn/digital-audio-basics-sample-rate-and-bit-depth.html)
STD_BIT_RATE = 'PCM_16' # Signed 16 bit PCM = 1411kbps bit rate

BASE_DIR = '/Users/danielflachica/Desktop/Thesis/resample-hdtracks'
IN_DIR = path.join(BASE_DIR, 'wav_raw_sample_rate')
OUT_DIR = path.join(BASE_DIR, 'wav_std_sample_rate')

def resample(song_path, sample_rate=STD_SAMPLE_RATE, bit_rate=STD_BIT_RATE):
    song, sr = librosa.core.load(song_path, sr=sample_rate)
    out_file = f'{ OUT_DIR }/{ au.get_filename_minus_extension(song_path) }.wav'
    sf.write(out_file, song, sr, subtype=bit_rate)

if __name__=="__main__":
    if path.exists(IN_DIR) and path.exists(OUT_DIR):
        au.remove_DS_Store(IN_DIR)
        tracks = listdir(IN_DIR)

        for track in tqdm(tracks, desc='Resampling'):
            song_path = f'{ IN_DIR }/{ track }'
            resample(song_path)

    else:
        err_list = []
        if not path.exists(IN_DIR):
            err_list.append(IN_DIR)
        if not path.exists(OUT_DIR):
            err_list.append(OUT_DIR)
        raise OSError(f'Could not find { ", ".join(err_list) }')