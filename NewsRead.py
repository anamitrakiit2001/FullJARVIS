import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# c54f6b0bbffc4cc1a17b923c8326d736
def latestnews():
    apidict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c54f6b0bbffc4cc1a17b923c8326d736",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c54f6b0bbffc4cc1a17b923c8326d736",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=c54f6b0bbffc4cc1a17b923c8326d736",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c54f6b0bbffc4cc1a17b923c8326d736",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c54f6b0bbffc4cc1a17b923c8326d736",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c54f6b0bbffc4cc1a17b923c8326d736"
        }
    content = None
    url = None
    speak("Which News field you want")
    field = input("Type the field: ")
    for key, value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print ("URL was found")
            break
        else:
            url=True
            if url is True:
                print("URL NOT FOUND")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("thats all")

