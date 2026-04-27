from services.interpreter import listen
from execute import execute_automation
from services.voice import MotorVoz


def main():
    tts = MotorVoz()
    tts.falar("Sistema iniciado... Olá! Hemione pronta para te ajudar")

    #speak("Olá, eu sou a Sexta-Feira. Estou pronta para te ajudar")
    while True:
        command = listen()
        if any(word in command for word in ["desligar", "sair", "encerrar", "parar"]):
            return False
        else:
            execute_automation(command)

if __name__ == "__main__":
    main()