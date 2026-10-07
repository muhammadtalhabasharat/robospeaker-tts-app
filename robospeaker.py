
#RoboSpeaker 2.0
#A text-to-speech assistant: type text, choose how many times to repeat it.
#Supports adjustable speech rate.

import pyttsx3


def speak(engine, text, speed=160):
    engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()


def main():
    engine = pyttsx3.init()  # created once, reused for every line spoken

    print("----------------------------------------")
    print(" Welcome to RoboSpeaker 2.0 by Talha")
    print("----------------------------------------")
    name = input("Enter your name: ")
    speak(engine, f"Hello {name}, RoboSpeaker is ready!")

    while True:
        text = input("\nEnter text to speak (or 'q' to quit): ")

        if text.lower() == "q":
            speak(engine, f"Goodbye {name}, see you next time!")
            print("Exiting program...")
            break

        times = input("How many times to repeat? (default 1): ")
        repeat_count = int(times) if times.isdigit() else 1
        repeat_count = max(repeat_count, 1)  # guard against 0 or bad input

        for _ in range(repeat_count):
            speak(engine, text)


if __name__ == "__main__":
    main()
