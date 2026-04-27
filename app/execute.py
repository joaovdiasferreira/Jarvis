from automatization.apps_init import chrome_init, app_init, lenovo_vantage_init
import os
from services.voice import MotorVoz

tts = MotorVoz()


def clean_command(command):
    command = command.lower().strip()

    # palavras que você quer ignorar
    garbage_words = ["por favor"]

    for palavra in garbage_words:
        command = command.replace(palavra, "")

    command = command.replace(",", " ")
    command = " ".join(command.split())
    return command


def execute_automation(command):
    command = clean_command(command)
    #print(f"DEBUG: Comando processado: ['{command}']")

    # ====================
    # OPEN APPS
    # ====================
    if command.startswith("abrir"):
        app = command.split("abrir", 1)[1].strip()

        if not app:
            tts.falar("Você precisa especificar um aplicativo para abrir")
            return

        match app:
            case "chrome" | "google chrome":
                tts.falar("Claro! Google Chrome será aberto!")
                chrome_init()
                tts.falar("Pronto! aqui está.")

            case "lenovo app":
                tts.falar("Abrindo seu app de configuração se desempenho")
                lenovo_vantage_init()
            case _:
                tts.falar(f"Sem problemas... abrindo {app}")
                app_init(app)

    # ====================
    # SYSTEM COMMANDS
    # ====================
    if "reiniciar" in command and "computador" in command:
        tts.falar("reiniciando em 30 segundos... você ainda pode cancelar")
        os.system("shutdown /r /t 30")

    elif "hora" in command and "dormir" in command:
        tts.falar("Claro, senhor. Desligando em 30 segundos. Até logo!")
        os.system("shutdown /s /t 30")


    elif "cancelar" in command:
        os.system("shutdown /a")
        tts.falar("Autodestruição cancelada")