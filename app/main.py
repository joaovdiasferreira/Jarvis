from services.interpreter import listen
from execute import execute_automation
from services.voice import MotorVoz


SLEEP_WORDS = ["desligar", "sair", "encerrar", "parar"]

def main():
    tts = MotorVoz()
    tts.falar("Sistema iniciado... Olá! Jarvis pronto para te ajudar!")

    #speak("Olá, eu sou a Sexta-Feira. Estou pronta para te ajudar")
    while True:
        command = listen()
        if any(word in command for word in SLEEP_WORDS):
            return False
        else:
            execute_automation(command)

if __name__ == "__main__":
    main()