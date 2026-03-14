import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine= pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
print(voices) 
engine.setProperty('voice',voices)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello! I am Jarvis sir . Please say how may i help you")

def takecommand():# it takes microphone input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold= 1
        
        audio=r.listen(source)

    try:
        print("Recognizing .....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
        speak(query)


    except Exception as e:
        print("Say that again please....")
        return "None"

    return query


if __name__ == '__main__':
    wishMe()

    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query =query .replace("wikipedia","")
            results= wikipedia.summary(query, sentencees=3)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query :
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strTime}")

        elif 'open code' in query:
            codePath= "C:\\Users\\ujjaw\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)





         


