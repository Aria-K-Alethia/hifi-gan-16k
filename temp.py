import os
import random
from os.path import join, basename, exists
from glob import glob

root = '/scratch/acc12076sp/hifigan-16k-wavs/'
datasets = ['jvs', 'vctk', 'ljs', 'jsut']
filelist = '16k_320hop_{mode}.txt'
trainfiles, valfiles = [], []
nval_per_ds = 16
for d in datasets:
    wavs = glob(join(root, d, '*.wav'))
    wavs = [join(d, basename(w)[:-4]) for w in wavs]
    random.shuffle(wavs)
    trainfiles.extend(wavs[:-nval_per_ds])
    valfiles.extend(wavs[-nval_per_ds:])
    
path = join('filelists', filelist.format(mode='train'))
with open(path, 'w') as f:
    for fn in trainfiles:
        string = fn + '|na'
        f.write(string+'\n')

path = join('filelists', filelist.format(mode='val'))
with open(path, 'w') as f:
    for fn in valfiles:
        string = fn + '|na'
        f.write(string+'\n')
