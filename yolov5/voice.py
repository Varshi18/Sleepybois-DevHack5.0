import argparse
import csv
import os
import platform
import sys
from datetime import datetime  # Add this import
from pathlib import Path
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import subprocess

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
        open_browser("https://" + website + ".com")

    elif "search" in command:
        search_query = command.replace("search", "")
        speak(f"Searching for {search_query} on the web.")
        open_browser(f"https://www.google.com/search?q={search_query}")

    elif "info" in command:
        search_query = command.replace("info", "").strip()

        def get_wikipedia_summary(query, num_sentences=2):
            try:
                summary = wikipedia.summary(query, sentences=num_sentences)
                return summary
            except wikipedia.exceptions.DisambiguationError as e:
                print("Multiple pages match with the title. Please specify.")
                print(e.options)
                return None
            except wikipedia.exceptions.PageError:
                print("No Wikipedia page found for the given title.")
                return None

        info_summary = get_wikipedia_summary(search_query)

        if info_summary:
            speak(f"Here is some information about {search_query}: {info_summary}")
        else:
            speak(f"Sorry, I couldn't find information for {search_query} on Wikipedia.")
    #elif "detect" in command:
        # Adjust the path to your YOLOv5 detect.py script and specify the Conda environment
     #   yolo_script_path = "D:\yolov5\detect3.py"
      #  conda_environment = "yolov5"
        
       # speak("Running image detection. Please wait.")
        #subprocess.run(["conda", "activate", conda_environment], shell=True)
        #subprocess.run(["python", yolo_script_path, "--other", "--options"])
    elif "detect image" in command:
        # Specify the path to your YOLOv5 detect.py script
        yolo_script_path = r"D:\yolov5\detect3.py"
        
        speak("Running image detection. Please wait.")
        
        # Use subprocess to run the YOLOv5 detect.py script with the specified command
        subprocess.run(["python", yolo_script_path, "--source", "0"])
    # Example usage with a specific page title:
    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        search_query = command.replace("", "")
        speak(f"Searching for {search_query} on the web.")
        open_browser(f"https://www.google.com/search?q={search_query}")

def main():
    while True:
        command = listen()

        if command:
            execute_command(command)

if __name__ == "__main__":
    main()