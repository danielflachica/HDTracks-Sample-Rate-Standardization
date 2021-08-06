# HDTracks Sample Rate Standardization Project

### This project is a pre-processing step designed ONLY to be used BEFORE AMP and AF. 
Songs should be resampled to a standard sample rate before fingerprint storage (for consistency).

Instructions:
1. Download HDtracks songs into `/wav_raw_sample_rate`
2. Run `python resample.py`
3. Upload the standardized sample rate songs in `/wav_std_sample_rate` to Google Drive for use in AMP and AF projects
4. Run `python cleanup.py`
