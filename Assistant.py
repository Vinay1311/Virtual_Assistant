import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyowm
from pyowm import OWM

listener = sr.Recognizer()

machine = pyttsx3.init()


def talk(text):
    machine.say(text)  # Give O/p of Text
    machine.runAndWait()


print("How may I help You!!")
talk("How may I help You!!")


# Function to take instruction and s=show it on screen
def input_instruction():
    # Listening Part Of Assistant
    # Try Block is used to check there is any kind of error in microphone
    global instruction
    try:

        with sr.Microphone() as source:
            print("Listening...")

            speech = listener.listen(source, timeout=20)
            instruction = listener.recognize_google(speech)  # Google API
            instruction = instruction.lower()
            if "Hey Assistant" in instruction:  # Assistant listening the Command
                instruction = instruction.replace('Hey Assistant', " ")
                print(instruction)

            return instruction


    except sr.WaitTimeoutError:
        print("Listening timed out.")

    except sr.RequestError:
        print("Could not request results; check your network connection.")

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")


# Weather Function to check specific city weather

def get_weather(city):
    # install & import pyown library
    # fir api key read the documentation of pyowm library
    api_key = 'b8b003a3400a284c51c635679cab555c'
    owm = OWM(api_key)
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(city + ',IN')
        w = observation.weather
        weather_info = w.detailed_status
        temperature = w.temperature('celsius')['temp']
        print(f"The weather in {city} is {weather_info}. The temperature is {temperature} degrees Celsius.")
        talk(f"The weather in {city} is {weather_info}. The temperature is {temperature} degrees Celsius.")
    except pyowm.exceptions.api_response_error.NotFoundError:
        talk(f"Sorry, I couldn't find weather information for {city}.")


def play_assistant():
    instruction = input_instruction()
    print(instruction)
    if instruction is None:
        talk("No commands to execute,Okay Thnx")
    # 1. Command to Play Youtube_Video. Say - Hey Assistant Play "Video_name"
    elif "play" in instruction:
        song = instruction.replace('play', "")  # instaead of play the Assistant say the name of video
        talk("playing" + song)
        pywhatkit.playonyt(song)


    # 2. Command to ask current time. Say - Hey Assistant any sentence where time word is mentioned
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time is ' + time)

    # 3. Command to ask Today's date. Say - Hey Assistant any sentence where 'today's date' word is mentioned
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m / %y')
        talk("Today's'is " + date)

    elif 'How are you' in instruction:
        talk("I'm Fine , how about you")

    # 5. Command to ask about a particular person. Say - Hey Assistant who is 'person name'
    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    # 6. Command to ask about any thing. Say - Hey Assistant any sentence what is 'thing name'
    elif 'what is' in instruction:
        query = instruction.replace('what is', " ")
        info = wikipedia.summary(query, 1)
        print(info)
        talk(info)

    # 7. Command to add 2 digits.Say - Hey Assistant add two number and provide it number one by one
    elif "add" in instruction:
        talk("Ok! Please tell first digit")
        spokent_text1 = input_instruction()
        talk("First Digit is: " + spokent_text1)
        talk("Ok! Please tell second digit")
        spokent_text2 = input_instruction()
        talk("Second Digit is: " + spokent_text2)
        sum = int(spokent_text1) + int(spokent_text2)
        talk("Sum of this 2 digit is: " + str(sum))

    # 8. Command to ask weather of any city. Say - weather of 'city name'
    # Tell only city name once again when Assistant asks
    elif 'weather' in instruction:
        talk("Okay can you please say city name again?")
        cityname = input_instruction()
        get_weather(cityname)

    # else condition
    else:
        talk("Please Repeat!!")


play_assistant()  # play_Assistant funtion called
