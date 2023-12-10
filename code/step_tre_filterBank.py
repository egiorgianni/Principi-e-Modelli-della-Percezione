# Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc, logfbank

# Leggiamo il file audio WAV ("fileAudio.wav") utilizzando scipy.io.wavfile.read()
sampling_freq, sig_audio = wavfile.read("fileAudio.wav")

# Le prime linee gialle orizzontali sotto ogni segmento sono la frequenza fondamentale e il suo massimo.
# Sotto la linea gialla ci sono le armoniche, che condividono tra loro la stessa distanza in termini di frequenza.

# Generazione delle feature del banco dei filtri
fb_feat = logfbank(sig_audio, sampling_freq)

# Stampa delle dimensioni delle feature del banco dei filtri
print('\nFilter bank\nWindow Count =', fb_feat.shape[0])
print('Individual Feature Length =', fb_feat.shape[1])

# Trasponiamo le features per una migliore visualizzazione
fb_feat = fb_feat.T

# Visualizziamo la matrice delle features con plt.matshow
plt.matshow(fb_feat, cmap='viridis')
plt.title('Features from Filter bank')
plt.show()