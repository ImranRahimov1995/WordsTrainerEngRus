import subprocess
from typing import List,Literal



class SpeechSynthesizer:
    VOLUME_CHOICES = {
        1: '-v -1',
        2: '',
        3: '-v 1'
    }

    def __init__(
            self,
            speaker:Literal[
                    'Anna',
                    'Irina',
                    'Elena',
                    'Aleksandr'
                ]='Anna',
            volume: int=2):


        self.speaker = speaker
        self.volume = self.VOLUME_CHOICES[volume]


    def say(self,text:str):
        """
            Using Rhvoice, execute command in terminal

        """
        return subprocess.call(
            f"echo '{text}' | RHVoice-client -s {self.speaker} {self.volume}| aplay",
            shell=True
        )
