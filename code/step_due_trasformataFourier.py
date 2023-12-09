# Caratterizzazione del segnale dal file di input
# Useremo la trasformata di Fourier per convertire i segnali in una distribuzione sul dominio di frequenza
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Leggiamo il file audio e otteniamo la frequenza di campionamento e il segnale
freq_sample, sig_audio = wavfile.read("fileAudio.wav")
print('\nShape of the Signal:', sig_audio.shape)
print('Signal Datatype:', sig_audio.dtype)
print('Signal duration:', round(sig_audio.shape[0] / float(freq_sample), 2), 'seconds')

# Normalizziamo i valori del segnale
sig_audio = sig_audio / np.power(2, 15)

# Calcoliamo la lunghezza del segnale e la metà della lunghezza da utilizzare nella trasformata di Fourier
sig_length = len(sig_audio)
half_length = int(np.ceil((sig_length + 1) / 2.0))

# Eseguiamo la trasformata di Fourier per ottenere il dominio delle frequenze del segnale
signal_freq = np.fft.fft(sig_audio)

# Normalizziamo il dominio delle frequenze e eleviamo al quadrato
signal_freq = abs(signal_freq[0:half_length]) / sig_length
signal_freq **= 2
transform_len = len(signal_freq)

# "Aggiustiamo" il segnale trasformato per i casi pari e dispari
if sig_length % 2:
    signal_freq[1:transform_len] *= 2
else:
    signal_freq[1:transform_len - 1] *= 2  # Corretto il simbolo meno (-)

# Estraiamo la potenza in decibel del segnale
exp_signal = 10 * np.log10(signal_freq)

# Creiamo l'asse delle x in kHz
x_axis = np.arange(0, half_length, 1) * (freq_sample / sig_length) / 1000.0

# Visualizziamo il grafico
plt.figure()
plt.plot(x_axis, exp_signal, color='green', linewidth=1)
plt.xlabel('Frequency Representation (kHz)')
plt.ylabel('Power of Signal (dB)')
plt.show()

# NON INSERIRE QUESTA PARTE NEL README
# ricordare l'installazione delle librerie:
# pip install numpy matplotlib scipy
# SciPy (scipy.io) dispone di vari metodi per effettuare operazioni coi file in Python (nel nostro caso la usiamo per la lettura del file audio)
# NumPy (numpy) è una libreria Python per la computazione scientifica
# Matplotlib (matplotlib.pyplot) è una libreria Python per la visualizzazione dei dati

# OUTPUT:
# $ python3 step_due_trasformataFourier.py
#
# Shape of the Signal: (66150,)
# Signal Datatype: int16
# Signal duration: 3.0 seconds
# + foto del grafico