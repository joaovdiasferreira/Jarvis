import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis está ouvindo...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", command)
        return command.lower()
    except Exception as e:
        print("Não entendi. Tente novamente.")
        return ""