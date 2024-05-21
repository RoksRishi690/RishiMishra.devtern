import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}\n")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Can you please repeat?")
        return listen()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Main function
def main():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there! How can I help you?")
        elif "bye" in query:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I can't assist with that.")

if __name__ == "__main__":
    main()
