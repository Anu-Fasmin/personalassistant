#pip install (module name)
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import pywhatkit
import pyjokes
import requests
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am jo,What can I do for you")

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        if 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'Hello jo' in query:
            speak("Hai sir")
            speak("How are you?")
            
        elif 'How are you' in query:
            speak("I am fine, Thankyou")
            speak("How are you?")

        elif 'weather' in query:
            search = "weather in kerala"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            strdate = datetime.datetime.now().strftime("%B:%D:%Y")
            speak(f"Sir, the date is {strdate}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
 
        elif 'who is' in query:
             person = query.replace('who is', '')
             info = wikipedia.summary(person, 2)
             print(info)
             speak(info)

        elif 'are you single?' in query:
             speak('I am in a relationship with wifi')

        elif 'my birthday' in query:
             speak('Happy birthday to my dearest friend')

        elif 'quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks you for using Jo,Have a great day sir")
            exit()
