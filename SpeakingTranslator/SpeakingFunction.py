#import speech_recognition as sr
import pyaudio

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# pa = pyaudio.PyAudio()
# print(pa.get_default_input_device_info())

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)


# listener = sr.Recognizer()
# try:
#     with sr.Microphone() as source:
#         print('listening...')
#         voice = listener.listen(source)
#         command = listener.recognize_google(voice)
#         print(command)
# except:
#     pass
