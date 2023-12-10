# Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc, logfbank

# Leggiamo il file audio WAV ("fileAudio.wav") utilizzando scipy.io.wavfile.read()
sampling_freq, sig_audio = wavfile.read("fileAudio.wav")

# Per l’analisi prendiamo i primi 15mila esempi del segnale originale 
sig_audio = sig_audio[:15000]

# Usiamo MFCC per estrarre le feature dal segnale
mfcc_feat = mfcc(sig_audio, sampling_freq)

# Stampa le dimensioni delle feature MFCC
print('\nMFCC Parameters\nWindow Count =', mfcc_feat.shape[0])
print('Individual Feature Length =', mfcc_feat.shape[1])

# Trasponiamo le features per una migliore visualizzazione
mfcc_feat = mfcc_feat.T

# Visualizziamo la matrice delle features con plt.matshow
plt.matshow(mfcc_feat, cmap='viridis')
plt.title('MFCC Features')
plt.show()