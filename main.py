import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import winshell 
from time import sleep


MASTER='Prem'

print("Initializing Jarvis .....")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning "+ MASTER)
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon " + MASTER)  
  
    else:
        speak("Good Evening " + MASTER) 
    #speak("I am jarvis.How may I help you?")

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Say that again ,please.") 
        return "None"
     
    return query
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    server.login('premkumark.18cse@kongu.edu', '8667082123')
    server.sendmail('premkumark.18cse@kongu.edu', to, content)
    server.close()
    
if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    
    speak("Initializing Jarvis...")
    wishMe()

    while True:

        query=takeCommand().lower()
        if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences = 3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
        elif 'open youtube' in query:
                    speak("Here you go to Youtube\n")
                    chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open("youtube.com")
        elif 'open google' in query:
                    speak("Here you go to google\n")
                    chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open("google.com")
        elif 'play music' in query or "play song" in query:
                    speak("Here you go with music")
                    music_dir = "E:/Songs/my favorite"
                    songs = os.listdir(music_dir)
                    print(songs)   
                    random = os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")   
                    speak(f"{MASTER}, the time is {strTime}")
        elif 'how are you' in query:
                    speak("I am fine, Thank you")
                    speak("How are you, Sir")
        
        elif 'fine' in query or "good" in query:
                    speak("It's good to know that your fine")
        elif 'exit' in query:
                    speak("Thanks for giving me your time")
                    exit()
        elif 'empty recycle bin' in query:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
                    speak("for how much time you want to stop jarvis from listening commands")
                    a = int(takeCommand())
                    sleep(a)
                    speak("I am back")
        elif "who i am" in query:
                    speak("you are my love,my master.")
 
        elif "why you came to world" in query:
                    speak("Thanks to "+MASTER+". further It's a secret")
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = "raghulsiva2018@gmail.com"  
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 

        