# Fonte dell’audio: 'fileAudio.wav'
# Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Leggiamo il file audio e verifichiamo la dimensione del segnale e la frequenza di campionamento
# Forniamo il percorso del file
freq_sample, sig_audio = wavfile.read("fileAudio.wav")

# Parametri di output: dimensione del segnale, frequenza di campionamento e durata
print('\nShape of Signal:', sig_audio.shape)
print('Signal Datatype:', sig_audio.dtype)
print('Signal duration:', round(sig_audio.shape[0] / float(freq_sample), 2),
      'seconds')

# Normalizziamo i valori del segnale
pow_audio_signal = sig_audio / np.power(2, 15)

# Estraiamo i primi 100 valori
pow_audio_signal = pow_audio_signal[:100]

# Creiamo l'asse del tempo in millisecondi
time_axis = 1000 * np.arange(0, len(pow_audio_signal), 1) / float(freq_sample)

# Visualizziamo il segnale su un grafico
plt.plot(time_axis, pow_audio_signal, color='blue')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()