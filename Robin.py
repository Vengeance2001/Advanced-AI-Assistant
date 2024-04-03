import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import os
import pywhatkit as kit
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
chosen_voice = voices[2]  
engine.setProperty('voice', chosen_voice.id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said : ", query)
    except Exception as e:
        print("Boss can you please say that again?...")
        return "None"
    return query

if __name__ == "__main__":
    speak("Hello Anurag Boss, how can i help you?")
    while True:
        query = takeCommand().lower()

        if 'blue' in query:
            print("Hello Anurag")
            speak("Yes Boss")

        elif 'terminate' in query:
           print("Bye Boss")
           speak("Hope i was useful to you, Have a nice day Boss")
           break
            
        elif 'tell me about yourself' in query:
            speak("Hello! my name is Blue  , your friendly AI assistant. I was created by my Boss Anurag. My core architecture leverages a combination of advanced machine learning algorithms and natural language processing techniques. I'm here to help you with a variety of tasks, from answering your questions to streamlining your daily activities. Ask me anything, and I'll do my best to be your heroine!")
            
            

        elif 'meri website open karo' in query:
            webbrowser.open_new_tab('https://anuragkhandare.netlify.app/')
            speak("This is your beautiful website boss")


        elif 'play my music' in query:
            music_folder = 'D:\\Entertainment\\music'  # Replace with your music folder path
            songs = os.listdir(music_folder)
            speak("Boss, I am playing a random song from your playlist.")
            os.startfile(os.path.join(music_folder, songs[random.randint(0, len(songs))]))
        
        elif 'google open karo' in query:
            speak("Boss, what should I search in Google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'send message' in query:
            speak("Whom should i send the message Boss?")
            cm = takeCommand().lower()
            print(cm)
            dct = {"pappa": "+918828495366", "mummy": "+917208709416", "myself":"+917900161686"}
            speak("What is the message boss?")
            dm = takeCommand().lower()
            print(dm)
            if cm in dct:
                currTime = datetime.datetime.now()
                currHour = currTime.hour
                currMin  = currTime.minute
                kit.sendwhatmsg(dct[cm], dm, 0, 0)
            else: speak("Sorry Boss, the contact is not present in my database")
        
        elif 'open youtube' in query:
            speak("What should I search on youtube, Boss?")
            cm = takeCommand().lower()
            kit.playonyt(cm)
        

        
