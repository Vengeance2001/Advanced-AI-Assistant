import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import os

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
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said : ", query)
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'heroine' in query:
            print("Hello Anurag")
            speak("Hello Anurag, how can i help you")

        elif 'terminate' in query:
           print("Bye Boss")
           speak("Hope i was useful to you, Have a nice day Boss")
           break

        elif 'youtube open karo' in query:
            speak("Boss I am opening youtube now")
            webbrowser.open_new_tab('youtube.com/')
            
        elif 'tell me about yourself' in query:
            speak("Hello! I'm Heroine, your friendly AI assistant. I was created by my Boss Anurag. My core architecture leverages a combination of advanced machine learning algorithms and natural language processing techniques. I'm here to help you with a variety of tasks, from answering your questions to streamlining your daily activities. Ask me anything, and I'll do my best to be your heroine!")
            
            

        elif 'meri website open karo' in query:
            speak("मैं यूट्यूब खोलने वाली हूँ")
            webbrowser.open_new_tab('https://anuragkhandare.netlify.app/')


        elif 'play my music' in query:
            music_folder = 'D:\\Entertainment\\music'  # Replace with your music folder path
            songs = os.listdir(music_folder)
            os.startfile(os.path.join(music_folder, songs[random.randint(0, len(songs))]))

        
