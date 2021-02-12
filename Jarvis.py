import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning Harsha")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Harsha")

    else:
        speak("Good Evening Harsha")

    speak("My name is Jarvis. How may I help you?")


def takeCommand():
    # It takes microphones input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said :{query} \n ")

    except Exception as e:
        # print (e)
        print("Say that again please...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail('youremail@gmail.com',to,content)



if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()
    # Logic for executing task based on query.

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("Google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "music" in query:
            n = (random.randint(0, 2))
            music_dir = 'C:\\Users\\ASUS\\Desktop\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "open code" in query:
            codepath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email to ankit" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "ankit.nkit@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send email.")
