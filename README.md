# HDTracks Sample Rate Standardization Project

### This project is a pre-processing step designed ONLY to be used BEFORE AMP and AF. 
Songs should be resampled to a standard sample rate before fingerprint storage (for consistency).

Instructions:
1. If first time use: Run `pip install -r requirements.txt && setup.py`
2. Download HDtracks songs into `/wav_raw_sample_rate`
3. Run `python resample.py`
4. Upload the standardized sample rate songs in `/wav_std_sample_rate` to Google Drive for use in AMP and AF projects
5. Run `python cleanup.py`
