import speech_recognition
import pyttsx3
import pyaudio
import pywhatkit
import webbrowser
from wikipedia import wikipedia
import wikipedia as googleScrap

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300

        audio = r.listen(source, 0, 4)

    try:
        print("Understanding")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Repeat Once")
        return "None"

    return query


query = takeCommand().lower()


def searchGoogle(query):
    if "search google" in query:
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")

        speak("This is what I found on Google")

        try:
            pywhatkit.search(query)
            results = googleScrap.summary(query, 1)
            speak(results)
        except:
            speak("No speakable output is available")


def searchYoutube(query):
    if "search youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


def searchWikipedia(query):
    if "search wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("jarvis", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia..")
        print(results)
        speak(results)
