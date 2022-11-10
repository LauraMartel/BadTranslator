import speech_recognition as sr
import pyttsx3


def speak_to_text():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            listen = listener.recognize_google(voice)
            listen = listen.lower()
    except:
        pass
    return listen

 

def text_to_speak(text, tcombo):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    if tcombo.get() == "french":
        engine.setProperty("voice", voices[0].id)
    elif tcombo.get() == "english":
        engine.setProperty("voice", voices[1].id)
    elif tcombo.get() == "chinese (simplified)":
        engine.setProperty("voice", voices[4].id)
    else:
        engine.setProperty("voice", voices[3].id)
    engine.say(text)
    engine.runAndWait()
