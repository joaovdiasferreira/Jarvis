import asyncio
import edge_tts
import pygame
import os
import time


class MotorVoz:
    def __init__(self, voz="pt-BR-FranciscaNeural"):
        self.voz = voz
        self.arquivo_temp = "output_voz.mp3"

    async def _gerar_e_tocar(self, texto):
        # Gera o áudio
        communicate = edge_tts.Communicate(texto, self.voz)
        await communicate.save(self.arquivo_temp)

        # Toca o áudio
        pygame.mixer.init()
        pygame.mixer.music.load(self.arquivo_temp)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # Deleta o arquivo após o uso
        if os.path.exists(self.arquivo_temp):
            os.remove(self.arquivo_temp)

    def falar(self, texto):
        asyncio.run(self._gerar_e_tocar(texto))