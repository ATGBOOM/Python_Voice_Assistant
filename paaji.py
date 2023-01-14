import pywhatkit
import speech_recognition as sr
import pyttsx3 as tts
import datetime
import wikipedia
import pyjokes
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',145)
r = sr.Recognizer()

def talk(x):
 engine.say(x)
 engine.runAndWait()

def take_command():
   try:
     with sr.Microphone() as source:
        print("start")
        voice = r.listen(source)
        print("time over")
        command = r.recognize_google(voice)
        command = command.lower()
        if "paaji" in command:
         command = command.replace("paaji", "")
         print(command)
   except:
       run_alex()
   return command
def run_alex():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("current time is" + time)
    elif "what is" in command:
        wiki = command.replace("what is", "")
        info = wikipedia.summary(wiki, 1)
        talk(info)
    elif "joke" in command:
        talk (pyjokes.get_joke())

run_alex()