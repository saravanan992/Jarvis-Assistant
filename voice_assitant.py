import speech_recognition as sr
import pyttsx3
import time

# Initialize the recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Customize voice
engine.setProperty('rate', 160)  # Speed of speech
engine.setProperty('volume', 1.0)  # Max volume

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable right now.")
        return ""

# Main program
speak("Hello Saravanan, I am your Jarvis. How can I help you today?")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello! How are you?")
    elif "time" in command:
        current_time = time.strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "your name" in command:
        speak("I am Jarvis, your voice assistant.")
    elif "stop" in command or "exit" in command or "quit" in command:
        speak("Goodbye Saravanan. See you soon.")
        break
    elif command != "":
        speak("I heard you say " + command + ", but I’m still learning what to do with that.")
