import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
volume = engine.getProperty('volume')
engine.setProperty('volume', 9.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mr. Rishikesh.")

    elif hour>=12 and hour<18:
        speak("Goodn Afternoon Mr. Rishikesh.")

    else:
        speak("Good Evening Mr. Rishikesh.")        
    
    speak("This is Friday your Artificial Inteligence.")

def takeComand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")  
    except Exception as e:
        # print(e)
        print("Say that again please...") 
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.login('yourmail@gmail.com', 'Your password')
    server.sendmail('yourmail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # takeComand()
    while True:
    # if 1:
     query = takeComand().lower()
     if 'hello' in query:
          speak('Hello Sir. How can i help you?')
          continue
     elif 'open window' in query:
           os.system('explorer C:\\ {}'.format(query.replace('open', '')))
           continue
     elif 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=3)
         speak("According to wikipedia")
         print(results)
         speak(results)
         continue
        

     elif 'open youtube' in query:
         speak("Opening Youtube")
         webbrowser.open("youtube.com")
         continue

     elif 'open google' in query:
         speak("Opening google")
         webbrowser.open("google.com") 
         continue 

     elif 'open facebook' in query:
         speak("Opening facebook")
         webbrowser.open("facebook.com")
         continue

     elif 'open whatsapp' in query:
         speak("Opening whatsapp")
         webbrowser.open("whatsapp.com")
         continue

     elif 'quit' in query or 'bye' in query:
         speak("Bye Mr Rishikesh. Happy to help you. Have a good day.")
         exit()  

     elif 'play music' in query:
         speak("Playing Music")
         music_dir = 'D:\\ASUS\\Music'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir))
         continue

     elif 'the time' in query:
         strTime = datetime.datetime.now().strTime("%H:%M:%S")
         speak(f"Sir, the time is{strTime}")
         continue

     elif 'email to hrushikesh' in query:
         try:
             content = takeComand()
             to = "hrushikeshrout@gmail.com"
             sendEmail(to, content)
             speak(" Sir, email has been sent")
         except Exception as e:
               print(e)
               speak("Sorry sir. I am not able to send this email")  
               continue

     elif 'who are you' in query:
         speak("I am Friday sir")   
         continue      
