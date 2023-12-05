## Sistema Uditivo e trasformata di _Fourier_
Approfondimento Principi e Modelli della Percezione a cura di _Edoardo Giorgianni_ e _Kristian Fabbro_.

Presentazione: **inserire link**.

### Introduzione
***
In questo approfondimento introdurremo il sistema uditivo umano, spiegando le sue componenti, per poi giungere alla trasformata di _Fourier_, applicazione pratica del suono.

### Apparato uditivo
***
Per rispondere razionalmente agli stimoli prodotti dall’ambiente circostante, l’uomo utilizza i cinque sensi. L'udito è uno di questi. L’organo che permette di percepire i suoni è l’orecchio, suddiviso in esterno, medio e interno.

#### Orecchio esterno
L'orecchio esterno, che convoglia il suono verso l’orecchio medio, è formato da:
- pinna: localizza il suono nello spazio e svolge la funzione di antenna acustica
- canale uditivo esterno: risonatore bidimensionale; tubo di larghezza costante con pareti ad alta impedenza acustica

#### Orecchio medio
L'orecchio medio, trasformatore di energia meccanica, contiene tre ossicini:
- martello: è l’ossicino più grande della catena ossiculare e la sua funzione principale è quella di trasmettere all’incudine le vibrazioni che le onde sonore producono sulla membrana del timpano. È composto da cinque parti: la testa, il collo, il manico, il processo anteriore e il processo laterale.
- incudine: è un piccolo osso di circa 7 mm che si frappone tra il martello e la staffa, a cui trasmette le vibrazioni prodotte dalle onde sonore. Il corpo dell'incudine ha forma cuboidale ed è leggermente schiacciato in senso trasversale. Dal corpo si distaccano i due rami: quello breve si dirige verso la parete posteriore del cavo del timpano; quello lungo si porta in basso e termina con il processo lenticolare, grazie al quale l’incudine si articola con la staffa
- staffa (collegata con l’orecchio interno): è il più leggero degli ossicini ed è situata tra l'incudine e la finestra ovale. Permette quindi la comunicazione tra l'orecchio medio e quello interno. È formata da: una testa, due archi e una base. La testa si articola con il processo lenticolare dell’incudine e i due archi (anteriore e posteriore) uniscono la testa con la base
Un gioco di leve tra questi ossicini provoca lo spostamento della staffa, che permette di raddoppiare l’energia trasmessa.

#### Orecchio interno
Le componenti principali dell’orecchio interno, che permette di percepire il suono, sono coclea e finestra ovale. Il collegamento tra orecchio medio e interno avviene mediante il collegamento tra staffa e l’interno della coclea.

![image](https://github.com/egiorgianni/Principi-e-Modelli-della-Percezione/assets/116444536/c4c2a791-3dc4-4cc2-a589-f2e92d47b88d)

### Modello strutturale
Il modello strutturale permette di differenziare le componenti dell’essere umano che permettono di identificare i percorsi che le onde sonore percorrono per arrivare al timpano.

#### Testa
La testa è un ostacolo per la libera propagazione del suono e per questo motivo introduce due effetti principali:
- ITD (Interaural Time Difference); causato dal fatto che le onde sonore devono percorrere una maggiore distanza per raggiungere l’orecchio più lontano. Per intendere ciò è sufficiente considerare la sorgente e la testa sferica. Come si può notare dalla figura, delle banali considerazioni geometriche permettono di affermare che il raggio per raggiungere l’orecchio più lontano è maggiore
  <p align="center">
    <img src="image.png" alt="Descrizione dell'immagine">
  </p>
- ILD (Interaural Level Difference); esprima la condizione secondo la quale l’orecchio più lontano riceve un suono di minore intensità. L'ILD è fortemente legato alla frequenza: a basse frequenze non vi è alcuna differenza, mentre ad alte frequenze diventa particolarmente significativo

#### Orecchio esterno
Come mostrato precedentemente, l’orecchio esterno è caratterizzato dalla pinna, dal canale uditivo e dal timpano. La pinna è connessa al canale uditivo.
L'orecchio esterno influenza la formazione del suono che arriva al timpano.

#### Torso e Spalle
Torso e spalle influenzano il suono che arriva al timpano, introducendo due contributi: riflessione sonora ed effetto di oscuramento.
La sagoma delle due parti assomiglia a un pupazzo di neve, per questo motivo il modello viene chiamato snowman model.
Riflessioni: quando si misura la risposta impulsiva all'orecchio destro, si osserva che l'impulso iniziale è seguito da una serie di altri impulsi, il cui ritardo varia in base all'elevazione della sorgente sonora.
Si può utilizzare la geometria semplificata del modello snowman per calcolare analiticamente i ritardi dei raggi riflessi, considerando i parametri del modello e la posizione della sorgente sonora. Il ritardo tra il suono diretto e il riflesso non varia significativamente se la sorgente si muove su una circonferenza orizzontale, ma varia sensibilmente se si muove verticalmente.
Oscuramento: man mano che la sorgente si muove verso il basso, le riflessioni scompaiono, dando spazio all'effetto di oscuramento. I raggi che vanno dall'orecchio ai punti di tangenza della parte superiore del torso delimitano il cono di oscuramento, rappresentato nella figura 1.3b.

![Alt text](image-1.png)

### Reti neurali: cenni
***
Le reti neurali sono fondamentali nel funzionamento del sistema uditivo. Il sistema uditivo del cervello è complesso e coinvolge una serie di reti neurali che elaborano le informazioni uditive in modo da permetterci di percepire e comprendere i suoni. Queste reti neurali includono:
1)	Corteccia uditiva: La corteccia uditiva è la regione principale del cervello coinvolta nella percezione uditiva. È suddivisa in diverse aree specializzate che elaborano informazioni specifiche sui suoni, come la frequenza, l'intensità e la localizzazione. Le reti neurali nella corteccia uditiva rappresentano e interpretano i segnali uditivi.
2)	Via uditiva: La via uditiva è costituita da una serie di strutture neurali che trasmettono segnali uditivi dal condotto uditivo all'orecchio interno e poi al cervello. Questa via coinvolge il tronco encefalico, il talamo e altre strutture intermedie.
3)	Plasticità cerebrale: Le reti neurali nel cervello, comprese quelle coinvolte nel sistema uditivo, sono in grado di modificarsi e adattarsi attraverso la plasticità cerebrale. Questo significa che il cervello può cambiare la sua organizzazione in risposta all'apprendimento e all'esperienza uditiva. Ad esempio, le persone che imparano a suonare uno strumento musicale possono sviluppare aree cerebrali più grandi dedicate al riconoscimento dei suoni musicali.
4)	Integrazione sensoriale: Il sistema uditivo interagisce con altri sistemi sensoriali, come il sistema visivo, per consentire un'esperienza completa e integrata del mondo circostante. Le reti neurali sono coinvolte nell'elaborazione di informazioni uditive in relazione a informazioni visive, tattili e altre per fornire un quadro complessivo della realtà.

In sintesi, le reti neurali svolgono un ruolo centrale nel sistema uditivo, contribuendo alla percezione, all'elaborazione e all'interpretazione dei suoni nell'ambiente circostante.

### Riconoscimento vocale
***
Un generico sistema di Speech Recognition è progettato per eseguire tre task:
- la cattura delle parole e delle frasi dette da un essere umano. Questo passaggio si concentra quindi solo sulla parte di workflow relativa all’acquisizione dei dati;
- l’applicazione del Natural Language Processing sui dati acquisiti, per riconoscere il contenuto del discorso;
- la sintesi delle parole riconosciute per aiutare una macchina a parlare lo stesso linguaggio.

Affinché una macchina possa elaborare informazioni come quelle uditive, bisogna memorizzare tali dati sotto forma di segnali digitali e analizzarli con dei programmi ad hoc. Sono due i processi che servono a convertire un segnale analogico in digitale:
- Campionamento: è la procedura usata per convertire un segnale s(t) che varia in funzione del tempo in una progressione x(n) discreta di numeri reali. Il termine che definisce l’intervallo tra due campioni consecutivi è il periodo di campionamento Ts
- Quantizazzione: è il processo di sostituzione dei numeri reali del campionamento in valori approssimati definiti in un certo intervallo di bit. Solitamente si usano 16 bit per rappresentare un esempio quantizzato. La risoluzione dei campioni, si misura in bit/sample.

***

Nel seguito sarà mostrato del codice Python per effettuare il riconoscimento vocale.

#### Primo passo: lettura di un file audio e generazione di un grafico
Lo step iniziale di un algoritmo di speech recognition è la creazione di un sistema in grado di leggere file audio (.wav, .mp3, ecc) e di capirne le informazioni presenti all’interno. Python dispone di librerie per leggere e interpretare questi file. Lo scopo di questo step è visualizzare i segnali audio come punti strutturati.
- Registrazione: Una registrazione è il file fornito in input all’algoritmo, il quale ne analizza il contenuto e costruisce un modello di speech recognition. Questo record può essere un file in memoria oppure può essere registrato live e Python permette di lavorare con entrambi i casi.
- Campionamento: Tutti i segnali di una registrazione vengono salvati in forma digitale. I digit sono difficili da elaborare per un software, dal momento che le macchine lavorano con input numerici. Il campionamento è infatti la tecnica usata per convertire i segnali digitali in segnali numerici discreti. Il campionamento viene fatto a una certa frequenza e genera segnali numerici. La scelta dei livelli di frequenza dipende dalla percezione del suono, ad esempio si sceglie una frequenza elevata se percepiamo l’audio come continuo.

```python
# Fonte dell’audio: Sample Audio File Download
# Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Leggiamo il file audio e verifichiamo la dimensione del segnale e la frequenza di campionamento
# Forniamo il path del file
freq_sample, sig_audio = wavfile.read("testAudio.wav")
# Parametri di output: dimensione del segnale, frequenza di campionamento e durata
print('\nShape of Signal:', sig_audio.shape)
print('Signal Datatype:', sig_audio.dtype)
print('Signal duration:', round(sig_audio.shape[0] / float(freq_sample), 2),
      'seconds')

# Normalizziamo i valori del segnale
pow_audio_signal = sig_audio / np.power(2, 15)
# Estraiamo i primi 100 valori
pow_audio_signal = pow_audio_signal[:100]
time_axis = 1000 * np.arange(0, len(pow_audio_signal), 1) / float(freq_sample)

# Visualizziamo il segnale
plt.plot(time_axis, pow_audio_signal, color='blue')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()
```

_Output_:
![Alt text](image-2.png)

#### Secondo passo: trasformare le frequenze audio
La rappresentazione di un file audio viene fatta innanzitutto nel dominio del tempo per ottenere l’intensità (ampiezza) dell’onda sonora. Il limite di questa misurazione è che essa si concentra solo sul volume dell’audio. Per questo motivo, il suono viene osservato nel dominio delle frequenze.
Questo tipo di rappresentazione ci fornisce dettagli sulla presenza di variazioni di frequenza all’interno del segnale. Il concetto matematico usato nella conversione di un segnale continuo dal dominio del tempo a quello delle frequenze è la Trasformata di Fourier. Useremo la trasformata di Fourier (FT) in Python per convertire i segnali audio in rappresentazioni basate sulla frequenza.

**Trasformata di Fourier in Python**

I segnali audio sono tutti composti da un insieme di tante onde di frequenza, che viaggiano insieme per creare una perturbazione nel mezzo di trasmissione, che può essere, ad esempio, una stanza. Per catturare il suono è fondamentale catturare l’intensità di frequenza generata nello spazio da queste onde.

La trasformata di Fourier è un concetto matematico che serve a decomporre un segnale estraendo le singole frequenze che lo compongono. Questo è fondamentale per comprendere quali sono le frequenze che si combinano insieme nel formare i suoni che ascoltiamo. La trasformata di Fourier (FT) fornisce tutte le frequenze presenti nel segnale e mostra anche l'ampiezza di ciascuna frequenza. Nella sezione di codice che segue, trasformeremo il file fileAudio.wav nel suo dominio di frequenza. Rappresenteremo anche le singole frequenze e la loro ampiezza.

![Alt text](image-3.png)

La funzione np.fft.fft di NumPy ci permette di calcolare una trasformata di Fourier discreta monodimensionale. La funzione usa l’algoritmo Fast Fourier Transform (FFT) per convertire una sequenza data in una trasformata di Fourier discreta (DFT). Nel file che stiamo elaborando, abbiamo una sequenza di ampiezze tratte da un file audio che erano state originariamente campionate da un segnale continuo. Useremo la funzione FFT per convertire questo dominio del tempo in un segnale discreto nel dominio della frequenza.

```python
# Caratterizzazione del segnale dal file di input
# Useremo la trasformata di Fourier per convertire i segnali in una distribuzione sul dominio di frequenza
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

freq_sample, sig_audio = wavfile.read("fileAudio.wav")
print('\nShape of the Signal:', sig_audio.shape)
print('Signal Datatype:', sig_audio.dtype)
print('Signal duration:', round(sig_audio.shape[0] / float(freq_sample), 2), 'seconds')
# Shape of the Signal: (645632,)
# Signal Datatype: int16
# Signal duration: 40.35 seconds

# Normalizziamo
sig_audio = sig_audio / np.power(2, 15)
# Estraiamo la lunghezza e la metà della lunghezza del segnale da immettere nella trasformata di Fourier
sig_length = len(sig_audio)
half_length = int(np.ceil((sig_length + 1) / 2.0))
# Useremo la trasformata di Fourier per generare il dominio di frequenza del segnale
signal_freq = np.fft.fft(sig_audio)
# Normalizziamo il dominio e eleviamolo al quadrato
signal_freq = abs(signal_freq[0:half_length]) / sig_length
signal_freq **= 2
transform_len = len(signal_freq)

# Il segnale trasformato ora necessita di essere "aggiustato" per i casi pari e dispari
if sig_length % 2:
  signal_freq[1:transform_len] *= 2
else:
  signal_freq[1:transform_len - 1] *= 2  # Corretto il simbolo meno (-)

# Estraiamo la potenza in decibel del segnale
exp_signal = 10 * np.log10(signal_freq)
x_axis = np.arange(0, half_length, 1) * (freq_sample / sig_length) / 1000.0
plt.figure()
plt.plot(x_axis, exp_signal, color='green', linewidth=1)
plt.xlabel('Frequency Representation (kHz)')
plt.ylabel('Power of Signal (dB)')
plt.show()
```

_Output_:
```
Shape of the Signal: (66150,)
Signal Datatype: int16
Signal duration: 3.0 seconds
```
![Alt text](image-4.png)

#### Importanza dei segnali audio monotoni
Un aspetto fondamentale nello studio del riconoscimento vocale, ma in generale in campo sonoro è la differenza tra segnali stereo e segnali monotoni. I suoni generati in qualsiasi ambiente sono sempre suoni stereo. Un segnale monotono invece è un segnale che viene prodotto su un solo canale ed è più facile da analizzare.

Dal punto di vista fisico, le onde che si muovono in un mezzo isolato come l'aria sono l'origine del suono. Le onde sonore emettono e trasferiscono energia tra le particelle d’aria fino a raggiungere una destinazione (ad esempio le nostre orecchie).

Due attributi fondamentali che definiscono il suono sono l'ampiezza, che si concentra sull'intensità/volume dell'onda sonora, e la frequenza, che misura le vibrazioni dell'onda nell’unità di tempo.

Attraverso Python possiamo creare segnali audio e di scriverli in un file in formato .wav. In modo tale da fornire una struttura predefiniti ai segnali durante il riconoscimento vocale.

```python
# Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Specifichiamo il file di output su cui salvare i dati
output_file = 'segnale_audio_generato.wav'

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
```

_Output_:

![Alt text](image-5.png)

#### Terzo passo: estrarre le feature dal discorso

**Da completare**
