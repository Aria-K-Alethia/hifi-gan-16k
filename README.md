# HiFi-GAN for 16 kHz wav

This repo contains a modified version of original HiFi-GAN for 16 kHz wav.
Original HiFi-GAN only support 22.05 kHz wav, this version can be trained with 16 kHz wav.

## Training

1. See `README_hifi-gan.md` to install requirements.
2. Make your own filelist, see `LJSpeech-1.1/train.txt` or `LJSpeech-1.1/validation.txt` for reference.
3. Run `bash ./scripts/train.sh {wav_dir}`

## Inference
### Inference from wav
See `inference.py`

### Inference from mel
See `inference_e2e.py`
