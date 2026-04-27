from services.voice import MotorVoz
import os
import time

tts = MotorVoz()

def restart():
    tts.falar("reiniciando em 30 segundos... você ainda pode cancelar")
    os.system("shutdown /r /t 30")

def shutdown():
    tts.falar("Claro, senhor. Desligando em 30 segundos. Até logo!")
    os.system("shutdown /s /t 30")

def suspend():
    #IMPLEMENTAR
    #PAREI AQUI