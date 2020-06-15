import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import random
import webbrowser as wb
from translate import Translator
import os
import subprocess as sp
import win32gui,win32con
import psutil
import subprocess
import signal
import pyautogui

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

def login():
    speak('starting all system applications')
    speak('installing all drivers')
    os.system('start .\Rainmeter\Rainmeter.exe')
    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE) 
    speak('every driver is installed')
    speak('Establishing Secured Connections')
    speak('now i am online sir')
    speak('Please tell me how may I help you')



def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Welcome back sir")
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak('I am Jarvis !')
    
    

def gooffline():
    speak('ok sir')
    speak('closing all systems')
    os.system("TASKKILL /F /IM Rainmeter.exe")
    speak('disconnecting to servers')
    speak('going offline')
    quit()

def whoAreYou():
    speak('I am Jarvis !, Your personal Assistant')

def whoMadeYou():
    speak('I was Created by Neel Shah')

def screenshot():
    img = pyautogui.screenshot()
    img.save(".\screenshot\ss.png")



#TODO translate language

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    try:

        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    except Exception as err:
        speak('please connect microphone')

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
    login()

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

        elif query in ['hi','hey','whatsup','whatsapp','sup','hello'] :
            d = random.choice(['hey','hi','hello'])
            speak(d)

        elif 'who are you' in query:
            whoAreYou()

        elif 'who made you' in query:
            whoMadeYou()

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open google' in query:
            wb.open("google.com")

            # TODO fix Chrome Browser 
        elif 'search in chrome' in query:
            speak('what should i search ?')
            #chromepath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            #wb.register('chrome',None,wb.BackgroundBrowser(chromepath),1)
           
            # wb.get(chromepath).open_new_tab(search)
            wb.open(search+'.com')

        # elif 'translate' in query:
        #     translateLanguage()

        elif 'logout' in query:
            speak("sure sir")
            os.system("shutdown -l")

        elif 'shutdown' in query:
            speak("sure sir")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("sure sir")
            os.system("shutdown /r /t 1")

        elif 'open documents' in query:
            speak("sure sir")
            documentPath = "C:\\Users\\Neel\\Documents"
            os.startfile(documentPath) 

        elif 'open downloads' in query:
            speak("sure sir")
            downloadPath = "C:\\Users\\Neel\\Downloads"
            os.startfile(downloadPath) 

        elif 'open pictures' in query:
            speak("sure sir")
            picturesPath = "C:\\Users\\Neel\\Pictures"
            os.startfile(picturesPath) 

        elif 'open videos' in query:
            speak("sure sir")
            videosPath = "C:\\Users\\Neel\\Videos"
            os.startfile(videosPath) 

        elif 'play song' in query:
            songs_dir=".\songs"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir , songs[0]))

        elif 'screenshot' in query:
            screenshot()
            speak('screenshot taken')

        elif 'cpu usage' in query:
            usage=str(psutil.cpu_percent())
            speak("CPU usage  is" +usage)

        elif 'battery status' in query:
            battery = psutil.sensors_battery()
            speak("Battery is at an ")
            speak(battery.percent)

        elif 'ram' in query:
            ram =psutil.virtual_memory()
            #speak(ram)
            speak("RAM used is "+ str(psutil.virtual_memory()[2]))
        elif 'go offline' in query:
            gooffline()
 