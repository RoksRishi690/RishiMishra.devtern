import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 0.7
        audio = recognizer.listen(source)
        try:
            print('Recognizing...')
            query = recognizer.recognize_google(audio, language='en-in')
            print('Command:', query)
            return query.lower()
        except Exception as e:
            print(e)
            print('Say that again, please.')
            return 'None'

def main():
    speak('Hello! I am your virtual assistant. How can I assist you today?')
    while True:
        query = takeCommand()
        if 'open geeksforgeeks' in query:
            speak('Opening GeeksforGeeks')
            webbrowser.open('https://www.geeksforgeeks.org')
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('https://www.google.com')
        elif 'which day is it' in query:
            # Implement your logic to tell the day
            pass
        elif 'tell me the time' in query:
            # Implement your logic to tell the time
            pass
        elif 'bye' in query:
            speak('Goodbye! Check out GeeksforGeeks for more exciting things.')
            exit()
        elif 'from wikipedia' in query:
            speak('Checking Wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=4)
            speak('According to Wikipedia:')
            speak(result)
        elif 'tell me your name' in query:
            speak('I am Jarvis. Your desktop assistant.')

if __name__ == '__main__':
    main()
