# Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Specifichiamo il file di output su cui salvare i dati
output_file = 'segnaleMonotono_generato.wav'

# Parametri del segnale audio
sig_duration = 5  # Durata del segnale audio in secondi
sig_frequency_sampling = 44100  # Frequenza di campionamento in Hz
sig_frequency_tone = 440  # Frequenza del tono in Hz
sig_amplitude = 0.5  # Ampiezza del segnale

# Generazione del segnale audio
time_points = np.linspace(0, sig_duration, int(sig_duration * sig_frequency_sampling), endpoint=False)
temp_audio_signal = sig_amplitude * np.sin(2 * np.pi * sig_frequency_tone * time_points)

# Normalizza il segnale tra -1 e 1
temp_audio_signal = temp_audio_signal / np.max(np.abs(temp_audio_signal))

# La funzione write() crea e scrive su file un segnale sonoro basato su frequenza
write(output_file, sig_frequency_sampling, (temp_audio_signal * 32767).astype(np.int16))

# Visualizzazione grafica del segnale
plt.plot(time_points[:100], temp_audio_signal[:100], color='green')
plt.xlabel('Time (seconds)')
plt.ylabel('Sound Amplitude')
plt.title('Audio Signal Generation')
plt.show()

# NON INSERIRE QUESTA PARTE NEL README
# ricordare l'installazione delle librerie:
# pip install numpy matplotlib scipy
# SciPy (scipy.io) dispone di vari metodi per effettuare operazioni coi file in Python (nel nostro caso la usiamo per la scrittura del file audio)
# NumPy (numpy) è una libreria Python per la computazione scientifica
# Matplotlib (matplotlib.pyplot) è una libreria Python per la visualizzazione dei dati

# OUTPUT:
# $ python3 segnaleMonotono.py
# creazione segnaleMonotono_generato.wav [nota che ogni esecuzione del programma sovrascrive il file]
# + foto del grafico