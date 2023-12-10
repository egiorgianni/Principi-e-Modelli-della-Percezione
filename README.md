STATO: completare da parte tre in poi e rivedere reti neurali - inserire i percorsi delle immagini

***

## Sistema Uditivo e trasformata di _Fourier_
Approfondimento Principi e Modelli della Percezione a cura di _Edoardo Giorgianni_ e _Kristian Fabbro_.

[Consulta la presentazione](https://www.canva.com/design/DAF2evizlIY/g0-kZHcZTRG3HF4ySbb7Ag/edit?utm_content=DAF2evizlIY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

## Indice
1. [Introduzione](###Introduzione)
2. [Apparato Uditivo](###ApparatoUditivo)
      - [Orecchio esterno](####)
      - [Orecchio medio](####)
      - [Orecchio interno](####)
3. [Modello Strutturale](###)
      - [Testa](####)
      - [Orecchio esterno](####)
      - [Torso e Spalle](####)
4. [Reti Neurali](###)
5. [Riconoscimento Vocale](###)
      - [Lettura di un file audio e generazione di un grafico](####)
      - [Trasformazione delle frequenze audio](####)
      - [Segnali Monotoni](####)
      - [Estrazione delle feature dal discorso](####)


### Introduzione
***
In questo trattato introdurremo le principali componenti del sistema uditivo umano, per poi giungere alla spiegazione dell'applicazione della trasformata di _Fourier_ per il riconoscimento vocale.


### Apparato uditivo

***
Per rispondere razionalmente agli stimoli prodotti dall’ambiente circostante, l’uomo utilizza i **cinque sensi**. L'**udito** è uno di questi. L’organo che permette di percepire i suoni è l’**orecchio**, suddiviso in **esterno**, **medio** e **interno**.

![Anatomia dell'orecchio umano](../repository/images/anatomia_orecchio.png)

#### Orecchio esterno
Il ruolo principale dell'**orecchio esterno** è quello di _convogliare_ il _suono_, attraverso il timpano, verso l’orecchio medio.
È formato da:
- **pinna** (o padiglione auricolare): _localizza_ il _suono_ nello spazio, svolgendo la funzione di _antenna acustica_

- **canale uditivo esterno**: _tubo_ di larghezza costante con pareti ad alta impedenza acustica. Svolge il ruolo di _risonatore bidimensionale_

- faccia esterna del **timpano**: guarda in direzione dell'_apertura_ del _condotto uditivo esterno_

#### Orecchio medio
Ruolo fondamentale dell'**orecchio medio** è quello di _trasformatore_ il _suono_ in energia meccanica.
Contiene tre ossicini:
- **martello**: è la parte più grande e la sua funzione principale è quella di _trasmettere_ all’_incudine_ le _vibrazioni_ che le onde sonore producono sulla membrana del timpano.

- **incudine**: ha dimensioni di circa 7 mm ed è situato tra il martello e la staffa. Svolge la funzione di _trasmettere_ le _vibrazioni_ prodotte dalle onde sonore.

- **staffa** (collegata con l’orecchio interno): è il più leggero degli ossicini ed è situato tra l'incudine e la finestra ovale.
Il suo ruolo è quello di _collegare_ l'_orecchio interno_, permettendo la _comunicazione_ tra essi.
Un gioco di leve tra gli ossicini che compongono la staffa, provoca il suo spostamento, e quindi il raddoppio dell'energia trasmessa.

#### Orecchio interno
Le componenti principali dell’orecchio interno, che permette di percepire il suono, sono **coclea** e **finestra ovale**. Il collegamento tra orecchio medio e interno avviene mediante il collegamento tra la staffa e l’interno della coclea.


### Modello strutturale
***
Il modello strutturale permette di differenziare le componenti dell’essere umano che permettono di identificare i percorsi che le onde sonore percorrono per arrivare al timpano. 

#### Testa
La testa è un _ostacolo_ per la libera _propagazione_ del _suono_ e per questo motivo introduce _due effetti_ principali:
- **ITD** (_Interaural Time Difference_); causato dal fatto che le onde sonore devono percorrere una _maggiore distanza_ per raggiungere l’_orecchio più lontano_. Per intendere ciò è sufficiente considerare una sorgente e la testa come sferica. Come si può notare dalla figura, delle banali considerazioni geometriche permettono di affermare che il raggio per raggiungere l’orecchio più lontano è maggiore rispetto a quello dell'orecchio più vicino
![Modello Strutturale - Testa](../repository/images/modello_strutturale_testa.png)

- **ILD** (_Interaural Level Difference_); esprime la condizione secondo la quale l’_orecchio più lontano_ riceve un _suono_ di _minore intensità_. L'_ILD_ è fortemente legato alla _frequenza_: a basse frequenze non vi è alcuna differenza, mentre ad alte frequenze diventa particolarmente significativo

#### Orecchio esterno
Come mostrato precedentemente, l’orecchio esterno è caratterizzato dalla pinna, dal canale uditivo e dal timpano. La pinna è connessa al canale uditivo. L'orecchio esterno influenza la formazione del suono che arriva al timpano. Ruolo fondamentale dell'orecchio esterno è contribuire alla percezione del suono **amplificando** le **onde acustiche** con **frequenza** attorno ai **3.000 Hz** (frequenza del parlato) e indirizzandole verso il timpano, sede in cui avverrà una loro ulteriore amplificazione.

#### Torso e Spalle
Torso e spalle influenzano il suono che arriva al timpano, introducendo due contributi: **riflessione sonora** ed **effetto di oscuramento**. La sagoma delle due parti assomiglia a un pupazzo di neve, per questo motivo il modello viene chiamato _snowman model_.
- **Riflessioni**: quando si misura la risposta impulsiva all'orecchio destro, l'impulso iniziale è seguito da una serie di altri impulsi, il cui ritardo varia in base all'elevazione della sorgente sonora. Si può utilizzare la geometria semplificata del _modello snowman_ per calcolare i _ritardi_ dei _raggi riflessi_, considerando i parametri del modello e la posizione della sorgente sonora. Il ritardo tra il suono diretto e il riflesso non varia significativamente se la sorgente si muove su una _circonferenza orizzontale_, ma varia sensibilmente se si muove _verticalmente_.  
![Modello Strutturale - Riflessione Sonora](../repository/images/modello_strutturale_riflessioni.png)

- **Oscuramento**: man mano che la sorgente si muove verso il basso, le _riflessioni scompaiono_, dando spazio all'effetto di oscuramento. I raggi che vanno dall'orecchio ai punti di tangenza della parte superiore del torso delimitano il _cono di oscuramento_.  
![Modello Strutturale - Effetto di Oscuramento](../repository/images/modello_strutturale_oscuramenti.png)


### Reti neurali (DA RIVEDERE)
***
Le reti neurali sono fondamentali nel funzionamento del sistema uditivo. Il sistema uditivo del cervello è complesso e coinvolge una serie di reti neurali che elaborano le informazioni uditive in modo da permetterci di percepire e comprendere i suoni.
Le reti neurali includono:
1. Corteccia uditiva: regione principale del cervello coinvolta nella percezione uditiva. È suddivisa in diverse aree specializzate che elaborano informazioni specifiche sui suoni, come la frequenza, l'intensità e la localizzazione. Le reti neurali nella corteccia uditiva rappresentano e interpretano i segnali uditivi

2. Via uditiva: costituita da una serie di strutture neurali che trasmettono segnali uditivi dal condotto uditivo all'orecchio interno e poi al cervello. Questa via coinvolge il tronco encefalico, il talamo e altre strutture intermedie

3. Plasticità cerebrale: le reti neurali nel cervello, comprese quelle coinvolte nel sistema uditivo, sono in grado di modificarsi e adattarsi attraverso la plasticità cerebrale. Questo significa che il cervello può cambiare la sua organizzazione in risposta all'apprendimento e all'esperienza uditiva. Ad esempio, le persone che imparano a suonare uno strumento musicale possono sviluppare aree cerebrali più grandi dedicate al riconoscimento dei suoni musicali

4. Integrazione sensoriale: Il sistema uditivo interagisce con altri sistemi sensoriali, come il sistema visivo, per consentire un'esperienza completa e integrata del mondo circostante. Le reti neurali sono coinvolte nell'elaborazione di informazioni uditive in relazione a informazioni visive, tattili e altre per fornire un quadro complessivo della realtà

In sintesi, le reti neurali svolgono un ruolo centrale nel sistema uditivo, contribuendo alla percezione, all'elaborazione e all'interpretazione dei suoni nell'ambiente circostante.


### Riconoscimento vocale
***
Un generico sistema di _Speech Recognition_ è progettato per eseguire tre task:
1. la **cattura** delle **parole** e delle **frasi** dette da un essere umano. Questo passaggio si concentra quindi solo sulla parte di workflow relativa all’**acquisizione** dei **dati**;

2. l’applicazione del _Natural Language Processing_ sui dati acquisiti, per **riconoscere** il **contenuto** del **discorso**;

3. la **sintesi** delle **parole riconosciute** per aiutare una macchina a parlare lo stesso linguaggio.

Affinché una macchina possa elaborare informazioni come quelle uditive, bisogna memorizzare tali dati sotto forma di **segnali digitali** e analizzarli con dei programmi ad hoc.

I processi per convertire un segnale analogico in digitale sono campionamento e quantizzazione.
- **Campionamento**: è la procedura usata per **convertire** un **segnale `s(t)`**, che varia in funzione del tempo, **in una progressione discreta `x(n)`** composta da numeri reali. L’intervallo tra due campioni consecutivi è il **periodo** di **campionamento `Ts`**

- **Quantizzazione**: è il processo di sostituzione dei numeri reali del campionamento in **valori approssimati** definiti in un certo intervallo di bit (solitamente si usano 16 bit). La risoluzione dei campioni, si misura in _bit/sample_.

***

Nel seguito sarà mostrato del codice _Python_ per effettuare il riconoscimento vocale.

#### Primo passo: lettura di un file audio e generazione di un grafico
Lo step iniziale di un algoritmo di _speech recognition_ è la creazione di un sistema in grado di leggere file audio (.wav, .mp3, ecc) e di capirne le informazioni presenti all’interno. _Python_ dispone di librerie per leggere e interpretare questi file. Impostiamo il nostro ambiente di sviluppo per far sì che tutti i seguenti codici funzionino. Installiamo le seguenti librerie:
```text
$ pip install numpy matplotlib scipy
```
Utilizzata per lo step uno e due e per i segnali monotoni.
```text
INSERIRE ALTRE LIBRERIE
```
```text
INSERIRE ALTRE LIBRERIE
```

SciPy (`scipy.io`) dispone di vari metodi per effettuare operazioni coi file in _Python_ (nel nostro caso la usiamo per la lettura, step uno e due, o la scrittura, segnali monotoni, del file audio).

NumPy (`numpy`) è una libreria _Python_ per la computazione scientifica.

Matplotlib (`matplotlib.pyplot`) è una libreria _Python_ per la visualizzazione dei dati.

Lo scopo di questo step è visualizzare i segnali audio come **punti strutturati**, cioè sotto forma di curva all’interno di un **grafico**.

- **Registrazione**: una registrazione è il _file_ fornito in input all’algoritmo, il quale ne analizza il contenuto e costruisce un modello di _speech recognition_. Questo record può essere un file in memoria oppure può essere registrato live e _Python_ permette di lavorare con entrambi i casi (noi vedremo la lettura di un file in memoria locale).

- **Campionamento**: tutti i segnali di una registrazione vengono salvati in forma digitale. I digit sono difficili da elaborare per un software, dal momento che le macchine lavorano con input numerici. Il campionamento è infatti la tecnica usata per _convertire i segnali digitali in segnali numerici discreti_. Il campionamento viene fatto a una certa frequenza e genera segnali numerici. La scelta dei livelli di frequenza dipende dalla percezione del suono, ad esempio si sceglie una frequenza elevata se percepiamo l’audio come continuo.

```python
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
```

_Output_:
```
$ python3 step_uno_letturaFile.py 

Shape of Signal: (66150,)
Signal Datatype: int16
Signal duration: 3.0 seconds
```
![output_step_uno](../repository/code/images/step_uno.png)

***

#### Secondo passo: trasfromazione delle frequenze audio
La rappresentazione di un file audio viene fatta, in primo luogo, nel dominio del tempo per ottenere l’intensità (ampiezza) dell’onda sonora. Il limite di questa misurazione è che essa si concentra solo sul volume dell’audio.
Per questo motivo, il suono viene osservato nel **dominio delle frequenze**. Questo tipo di rappresentazione ci fornisce dettagli sulla presenza di variazioni di frequenza all’interno del segnale. Il concetto matematico usato per la conversione di un segnale continuo dal dominio del tempo a quello delle frequenze è la **_Trasformata di Fourier_**. Useremo la trasformata di Fourier (**FT**) in _Python_ per _convertire i segnali audio in rappresentazioni basate sulla frequenza_.

**Trasformata di _Fourier_ in _Python_**

I segnali audio sono tutti composti da un insieme di tante onde di frequenza, che viaggiano insieme per creare una perturbazione nel mezzo di trasmissione, che può essere, ad esempio, una stanza. Per catturare il suono è fondamentale catturare l’intensità di frequenza generata nello spazio da queste onde.

La trasformata di _Fourier_ permette di **decomporre un segnale estraendo le singole frequenze**. Questo è fondamentale per comprendere quali sono le frequenze che si combinano insieme nel formare i suoni che ascoltiamo. La trasformata di _Fourier_ (FT) fornisce tutte le frequenze presenti nel segnale e mostra anche l'ampiezza di ciascuna di esse.
Nella sezione di codice che segue, trasformeremo il file `fileAudio.wav` nel suo dominio di frequenza, rappresentando le singole frequenze e la loro ampiezza.

![Trasformata di Fourier](../repository/images/trasformata_fourier.png)

La funzione `np.fft.fft` di NumPy, nel codice successivo, ci permette di calcolare una trasformata discreta di _Fourier_ monodimensionale. La funzione usa l’**algoritmo _Fast Fourier Transform_** (FFT) per convertire una sequenza data in una trasformata di _Fourier_ discreta (DFT). Nel file che stiamo elaborando, abbiamo una sequenza di ampiezze tratte da un file audio che erano state originariamente campionate da un segnale continuo. Useremo la funzione **FFT** per convertire questo dominio del tempo in un segnale discreto nel dominio della frequenza.

```python
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
```

_Output_:
```
$ python3 step_due_trasformataFourier.py

Shape of the Signal: (66150,)
Signal Datatype: int16
Signal duration: 3.0 seconds
```
![Alt text](../repository/code/images/step_due.png)

***

#### Importanza dei segnali audio monotoni
Un aspetto fondamentale nello studio del riconoscimento vocale, e in generale in campo sonoro, è la differenza tra **segnali stereo** e **segnali monotoni**. I suoni generati in qualsiasi ambiente sono sempre suoni stereo. Un segnale monotono invece è un segnale che viene prodotto su un solo canale ed è più facile da analizzare.

Dal punto di vista fisico, le onde che si muovono in un mezzo isolato, come l'aria, sono l'origine del suono. Le onde sonore emettono e trasferiscono energia tra le particelle d’aria fino a raggiungere una destinazione (ad esempio le nostre orecchie).

Due attributi fondamentali che definiscono il suono sono l'**ampiezza**, che si concentra sull'intensità/volume dell'onda sonora, e la **frequenza**, che misura le vibrazioni dell'onda nell’unità di tempo.

Attraverso _Python_ possiamo creare segnali audio e scriverli in un file in formato _.wav_.

```python
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
```

_Output_: viene generato il file `segnaleMonotono_generato.wav` e la sua rappresentazione sul grafico.
Nota: ad ogni esecuzione del codice il file generato viene sovrascritto.

![Segnale Monotono](../repository/code/images/segnaleMonotono.png)

***

#### Terzo passo: estrazione delle feature dal discorso

### DA COMPLETARE
