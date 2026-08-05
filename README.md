# RoboSpeaker 2.0

A command-line text-to-speech assistant built in Python. Type any text and it's read aloud, with support for repeating the same line multiple times and an adjustable speech rate.

## Features
- Converts typed text to speech in real time
- Repeat any message a custom number of times
- Personalized greeting and sign-off using your name
- Reuses a single TTS engine instance for efficient, glitch-free audio

## Tech used
Python 3, [`pyttsx3`](https://pypi.org/project/pyttsx3/) (offline text-to-speech engine)

## How to run
```bash
pip install -r requirements.txt
python robospeaker.py
```

## Example
```
Enter your name: Talha
(speaks) "Hello Talha, RoboSpeaker is ready!"

Enter text to speak (or 'q' to quit): Good morning
How many times to repeat? (default 1): 2
(speaks "Good morning" twice)
```
