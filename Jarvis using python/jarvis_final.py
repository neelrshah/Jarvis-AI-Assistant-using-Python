import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("hi i am jarvis")

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)
# time()

def date():
    Year = int(datetime.datetime.now().year)
    Month =int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak("Todays date is ")
    speak(Date)
    speak(Month)
    speak(Year)
# date()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Welcome back sir")
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis!, Sir Please tell me how may I help you")

# wishMe()

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listning....")
#         r.pause_threshold=1
#         audio = r.listen(source)

#     try:
#         print("Recongnizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You said: {query}\n")

#     except Exception as e:
#         print(e)
#         print("Say that again please...")  
#         return "None"

#     return query

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


# takeCommand()
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e1:
                print(e1)
                speak("Sorry Sir!,I couldnt find it on wikipedia ,Please say it again!")

        elif 'quit jarvis' in query:
            quit()
