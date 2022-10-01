from gtts import gTTS
import playsound
import pyttsx3

def speak1(text, file = "ques.mp3"):
    tts = gTTS(text = text, lang = "en-ca")
    filename = file
    tts.save(filename)
    playsound.playsound(filename)

speak1("A heart that's broke is a heart that's been loved")

def speak2(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

speak2("Hi sir, what can I do for you?")