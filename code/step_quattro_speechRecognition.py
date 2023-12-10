# Importiamo la libreria per il riconoscimento vocale
import speech_recognition as sr

# Creiamo un oggetto recognizer per memorizzare l'input
rec = sr.Recognizer()

# Lista dei microfoni disponibili
microphones = sr.Microphone.list_microphone_names()

# Stampa gli indici e i nomi dei dispositivi
for index, device_name in enumerate(microphones):
    print(f"Index {index}: {device_name}")

# Utilizza il microfono con indice 1 (modifica l'indice se necessario)
with sr.Microphone(device_index=1) as source:
    try:
        # Regola automaticamente per il rumore ambientale
        print("Reach the Microphone and say something!")
        rec.adjust_for_ambient_noise(source, duration=3)
        
        # Ascolta l'audio dal microfono
        audio = rec.listen(source)
        print("Recording completed.")

        # Usa la funzione recognize per trascrivere il parlato in testo
        text = rec.recognize_google(audio)
        print("I think you said:", text)

    except sr.UnknownValueError:
        # Errore se il riconoscitore non riesce a comprendere l'audio
        print("Could not understand audio")
    except sr.RequestError as e:
        # Errore se c'è un problema nella richiesta al servizio di riconoscimento vocale (es. connessione a Internet)
        print(f"Error making the request: {e}")