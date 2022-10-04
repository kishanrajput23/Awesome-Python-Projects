import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import random
import requests 
import psutil
import pywhatkit as kit
from bs4 import BeautifulSoup
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
     engine.say(audio)
     engine.runAndWait()
def wishMe():
     hour=int(datetime.datetime.now().hour) 
     if hour>=0 and hour<12:
          speak("Good morning!")
          
     elif hour>=12 and hour<18:
          speak("Good Afternoon!")
     elif hour>=18 and hour<=23:
          speak("Good Evening!")
     else:
          speak("It's time to sleep Yaara. Now no more laptop! Good night !!!!take care!!!! sweet dreams")
          exit() 
          
     speak("I am Alpha sir. Please tell me how may i Help You")
def takeCommand():
     #it takes microphone user input and returns string output
     r=sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening......")
          r.pause_threshold=1
          audio=r.listen(source)      
     try:
          print("Recognizing.....")
          query=r.recognize_google(audio,language='en-in')
          print(f"User said: {query}\n")
     except Exception as e:
          #print(e)
          speak("Say that again please...")
          return "None"  
     return query  
def sendEmail(to, content):
     server= smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('rktaakash@gmail.com', '9415628930')
     server.sendEmail('maskmanmotivation@gmail.com',to, content)
     server.close()
                        
if __name__=="__main__":
    wishMe()  
    while True:
       query=takeCommand().lower()
       if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=3)
            speak("According to Google wikipedia")
            print(results)
            speak(results)   
       elif 'open youtube' in query:
            webbrowser.open("youtube.com")
       elif 'open google' in query:
            webbrowser.open("google.com")
       elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
       elif'open brave' in query:
            webbrowser.open("brave.com") 
       elif 'open bing' in query:
            webbrowser.open("bing.com")           
       elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H hours %M minutes %S seconds")  
            speak(f"Sir !the time is{strTime}")  
       elif 'open code' in query:
            codePath="C:\\Users\\Mr.AK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    
       elif'send email' in query:
            try:
                 speak("what should i say?")
                 content=takeCommand() 
                 to="maskmanmotivation@gmail.com"  
                 sendEmail(to, content)
                 speak("Email has been sent!")
            except Exception as e:
                 print(e)
                 speak("sorry Aakash. I am not able to send this email") 
       elif "how are you" in query:
            speak("i am fine. thank you sir. What about you?")
       elif 'fine' in query:
            speak("it's good to know you are fine")                                  
       elif 'are you single Alpha' in query:
            speak('no! I am in relationship with Sophia') 
       elif 'joke' in query:
            speak(pyjokes.get_joke()) 
       elif 'would you come on a date with me' in query:
            speak('no I am having headache') 
       elif 'exit' in query:
            speak('thanks for giving me time')
            exit()
       elif 'who made you' in query or 'who created you' in query:
            speak("i have been created by AAkash") 
       elif 'tell me something about yourself' in query:
            speak("I am Jarvis sir. A virtual assistant made by Mr AK")
       elif 'temperature' in query:
            speak("name of the place sir")  
            place=takeCommand().lower()    
            search=(f"temperature in {place}")
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser") 
            temp= data.find("div",class_ = "BNeawe").text
            speak(f"current{search} is {temp}")       
       elif 'where i am' in query or 'where we are' in query :
            speak("wait sir! Let me Check!")
            try:
                 ip_Add=requests.get('https://api.ipify.org').text
                 print(ipAdd)
                 speak(ipAdd)
                 url='https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
                 geo_q=requests.get(url)
                 geo_d=geo_q.json()
                 city=geo_d['city']
                 state=geo_d['state']
                 country=geo.d['country']
                 speak(f'sir i am not sure but i think we are in {city}{state} city of {country} country')
            except Exception as e:
                 speak("Sorry sir. Due to network issues I am not able to locate where we are")
                 pass
       elif 'how much power left' in query or 'how much power we have' in query or 'battery' in query:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"sir our system have {percentage} percent battery")
      # elif 'play song' in query:
          #  kit.playonyt('play song'+ {name})
       elif'wake up jarvis'in query or 'hi jarvis' in query or 'are you there jarvis' in query:
            speak("yes sir i am available ")   
       elif 'play songs' in query:
            speak("name of the song sir")
            ps=takeCommand().lower()
            kit.playonyt(f"{ps}")  
