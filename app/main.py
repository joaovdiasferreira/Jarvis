from services.interpreter import listen
from execute import execute_automation, ACTIVATION_WORDS
from services.voice import MotorVoz


SLEEP_WORDS = ["descansar", "obrigado", "encerrar", "beleza"]
WAKE_WORDS = ["voltar a ouvir", "acordar", "ativar escuta", "continuar"]


def has_activation_word(command):
    return any(word in command for word in ACTIVATION_WORDS)


def main():
    tts = MotorVoz()
    tts.falar("Sistema iniciado... Olá! Jarvis pronto para te ajudar!")
    escutando = True

    while True:
        heard = listen()
        if not heard:
            continue

        if any(word in heard for word in SLEEP_WORDS):
            escutando = False
            tts.falar("Se precisar de algo mais é só chamar")
            continue

        if not escutando:
            if any(word in heard for word in WAKE_WORDS + ACTIVATION_WORDS):
                escutando = True
                tts.falar("Voltando a ouvir.")
            continue

        if has_activation_word(heard):
            tts.falar("Como posso ajudar?")

            command = listen()
            if not command:
                continue

            if any(word in command for word in SLEEP_WORDS):
                escutando = False
                tts.falar("Escuta pausada.")
                continue

            execute_automation(command)
            continue

        execute_automation(heard)


if __name__ == "__main__":
    main()
