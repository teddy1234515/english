import os
from gtts import gTTS
from pygame import mixer
import tempfile

mixer.init()

# 念出來
def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence,lang="en")
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load("{}.mp3".format(fp.name))
        mixer.music.play()
        
speak("Hello my son")