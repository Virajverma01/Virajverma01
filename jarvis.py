import instaloader
import pyttsx3;
import requests
import speech_recognition as sr;
import datetime;
import os;
from requests import get 
import cv2;
import wikipedia;
import webbrowser;
import time;
import pywhatkit as kit
import pyjokes;
import sys;
from requests import get
import pyautogui;

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)
#text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}")


    except Exception as e:
        speak("say that again please...")
        return "none"
    return query   

#wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning sir, ")
        speak('I am  your Assistant. please tell me how can i help you')
    elif hour>=12 and hour<=18:
        speak('Good afternoon sir, ')
        speak('Hi, I am chitti the robot, speed one terahertz, memory 1 zigabyte.')
    else:
        speak('Good evening sir, ')
        speak('I am  your Assistant. please tell me how can i help you')




if __name__ == "__main__":
    wish()

    while True:
    # if 1:

        query = takecommand().lower()
        
        # logic building for the tasks 

        if "open notepad" in query:
            speak("okay sir, opening notepad...")
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)


        elif 'close notepad' in query:
            speak('okay sir, closing notepad')
            os.system('taskkill /f /im notepad.exe')

        
        elif "open command prompt" in query:
            speak("Okay sir, opening command prompt... ")
            os.system("start cmd")

        elif 'close command prompt' in query:
            speak('okay, closing command prompt')
            os.system('taskkill /f /im cmd.exe')
            

        
        elif "open camera" in query:
            speak("okay sir, opening camera...")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            speak("Ok sir, playing music...")
            music_dir = "E:\\songs\\VidMate\\music"   
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                   os.startfile(os.path.join(music_dir, song))
                   time.sleep(5)

        
        elif "play video" in query:
            speak("okay sir, playing video...")
            video_dir = "E:\\songs\\VidMate\\music"
            videos = os.listdir(video_dir)
            for video in videos:
                if video.endswith('.mp4'):
                    # os.startfile(os.path.join(video_dir, video))
                    os.startfile(os.path.join(video_dir, video))
                    time.sleep(10)
        
        elif  "stop music" in query:
              speak("Ok sir, stop music")
              os.system("taskkill /f /im music.exe")



        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP addrss is {ip}")
            

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia...")
            speak(result)
            # print(result)

        elif  "open youtube" in query:
            speak("Ok sir, opening youtube...")
            webbrowser.open("www.youtube.com")
            time.sleep(15) 


        elif  "open my youtube channel" in query:
            speak("Ok sir, i will open you tube channel...")
            webbrowser.open("https://www.youtube.com/channel/UCJsQWhl5eDgGc-0Yxgyjc_g") 
            time.sleep(7) 

        elif "open my facebook account" in query:
            speak("Ok sir, i will open your facebook account...")
            webbrowser.open("https://www.facebook.com/viraj.verma.3192479")
            time.sleep(10)

        elif "open whatsapp" in query: 
            speak("Ok sir, i will open whatsapp...")
            webbrowser.open("https://web.whatsapp.com/")
            time.sleep(6)
    
        elif "open google" in query:
            speak("okay sir, opening google...")
            webbrowser.open("www.google.com")
            time.sleep(3)

        elif 'play youtube' in query:
            song = query.replace('play', 'machi machi')
            speak('what should i play on youtube...')
            time.sleep(2)
            speak('playing' + song)
            kit.playonyt(song)
            time.sleep(30)

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)


        elif "open calculator" in query:
            speak("ok sir, opening calculator...")
            os.system("C:\\Windows\\system32\\calc.exe")



        elif 'close calculator' in query:
            speak('okay, sir closing calculator...')
            os.system('taskkill /f /im calculator.exe')


        elif "yes" in query:
            speak("okay sir, i'm waiting...") 
            time.sleep(10)

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.keyUp("alt")
                    

  
        elif "go to sleep" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        elif 'check instagram profile' in query:
            speak('please enter the username of the profile')
            name = input('enter username here: ')
            webbrowser.open(f'www.instagram.com/{name}')
            speak(f'welcome on your profile {name}')
            time.sleep(15)


