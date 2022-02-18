import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')    #speaks engine itself they ask what you want to do   //girl voice
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)   #say() will say whatever we have written
    engine.runAndWait()  #This function will make the speech audible in the system

def wishMe():    #This function wishme whenever we will run our program they wish me 
    hour = int(datetime.datetime.now().hour)   #now() tells the exact time 
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Naveen Sir.Please tell me how may I help you") 
#It takes microphone input from the user and return string output
def takeCommand():   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:                                 
        print("Recognizing...")         #condition that they recognizing or listening user
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:           #Exception condition if computer not listen properly then they will execute
        # print(e)  
        print("Say that again Please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('19bcs1724@gmail.com','Naveen1234@')
    server.sendmail('19bcs1724@gmail.com',to, content)
    server.close() 

if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower() #whatever user speaking they convert into lower letter STRING bcoz open browser only in small letter

    #Logic for executing takes based on query
        if 'wikipedia' in query:        #when wikipedia search they go to particular topic in wikipedia then return their 2 sentences
            speak("Searching Wikipedia..")
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
        elif 'open codechef' in query:
            webbrowser.open("codechef.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open blackboard' in query:
            webbrowser.open("cuchd.blackboard.com")
        elif 'open online compiler' in query:
            webbrowser.open("onlinegdb.com")
        
        elif 'play music' in query:
            music_dir="D:\Favourite songs"
            #listdir() method in python is used to get the list of all files and directories in the specified directory
            songs = os.listdir(music_dir)  #listdir play all the songs in folder
            print(songs)
            os.startfile(os.path.join(music_dir,songs[2]))   #they join the path of operating system with music
        elif 'the time' in query:     
            strTime=datetime.datetime.now().strftime("%H:%M:%S")  #tell the exact time and strftime() will convert the time into string
            speak(f"Sir, The time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email to naveen' in query:
            try:
                speak("What Should I Say?")
                content = takeCommand()
                to = "19bcs1724@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Naveen,I am not able to send this email")