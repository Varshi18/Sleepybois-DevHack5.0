import speech_recognition as sr
import pyttsx3
import webbrowser
#import openai
import datetime

# Set your OpenAI API key
#openai.api_key = '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'

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you repeat?")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_browser(url):
    webbrowser.open(url)

def execute_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak("The current time is " + current_time)

    elif "open browser" in command:
        speak("Sure, which website would you like to visit?")
        website = listen()
        speak(f"Opening {website} in the browser.")
        open_browser("https://" + website)

    elif "search" in command:
        search_query = command.replace("search", "")
        speak(f"Searching for {search_query} on the web.")
        open_browser(f"https://www.google.com/search?q={search_query}")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm sorry, I didn't understand that command.")

def main():
    speak("Initializing Friday. How can I assist you today?")

    while True:
        command = listen()

        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
