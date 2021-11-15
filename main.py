import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    mic = sr.Microphone(device_index=1)
    with mic as data_taker:
        print("Say Something")
        listener.adjust_for_ambient_noise(data_taker)
        captured_audio = listener.record(source=mic, duration=5)

    try:
        instruction = listener.recognize_google(captured_audio)
        instruction = instruction.lower()
        print(instruction)

        if 'lola' in instruction:
            print(instruction)
    except:
        talk("I do not understand")
    return instruction

def run_Lola():
    while True:
        instruction = take_command()
        print('Instruct ' + str(instruction))
        if 'play' in instruction:

            song = instruction.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
            print(song)
        elif 'time' in instruction:
            time = datetime.datetime.now().strftime('%I: %M')
            print(time)
            talk('current time is' + time)
        elif 'tell me about' in instruction:
            thing = instruction.replace('tell me about', '')
            info = wikipedia.summary(thing, 2)
            print(info)
            talk(info)
        elif 'who are you' in instruction:
            talk('I am your personal Assistant Lola')
        elif 'what can you do for me' in instruction:
            talk('I can play songs, tell time, and help you go with wikipedia')
        else:
            talk('I did not understand, can you repeat again')


run_Lola()
