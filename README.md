# Virtual Assistant with Speech Recognition

## Project Description: 
"Experience the convenience of a Virtual Assistant with Speech Recognition. This Python project leverages libraries like SpeechRecognition, pyttsx3, pywhatkit, and more to empower the assistant to perform various tasks based on voice commands. From playing YouTube videos to providing real-time information, such as the current time and date, or even offering quick general knowledge answers, this assistant has you covered. Just say 'Hey Assistant' to activate it, and it's ready to assist. With robust error handling and a 20-second timeout, it's designed for a seamless and interactive user experience. Share this project on GitHub to make it accessible to a wider audience and possibly receive contributions for future enhancements."

## Project Details

- **Languages Used:** Python

## Libraries and Dependencies:

#SpeechRecognition for capturing and recognizing user's speech commands.
#pyttsx3 for text-to-speech capabilities, enabling audible responses.
#pywhatkit for playing YouTube videos based on user commands.
#datetime for real-time information, including the current time and date.
#wikipedia for quick lookups and brief summaries about people and topics.
#pyowm for retrieving weather data for specific cities.

## Functionality Overview:

Core functionality resides in the play_assistant function, serving as the heart of the virtual assistant.
Features include:
Playing YouTube videos with voice commands using #pywhatkit.
Providing real-time information like the current time and date.
Offering quick answers to general knowledge queries via #wikipedia.
Performing basic arithmetic operations based on user input.
Fetching weather information for a specified city using #pyowm.
Includes a timeout mechanism, automatically raising an UnknownValueError after 20 seconds of inactivity.

## Getting Started

1. Clone this repository to your local machine.
2. Run 'Assistant.py' in Your Code Editor
3. Install all the Python libraries that are Mentioned in Librarries and Dependencies Section.


## Key Points:

Trigger the virtual assistant by saying "Hey Assistant."
Robust error handling for microphone issues, network problems, and unrecognized commands.
Designed for a seamless and interactive user experience, addressing a variety of user inquiries.





## Contributions and Questions

Feel free to contribute to this project by submitting pull requests. If you have any questions, suggestions, or need assistance, please create an issue on GitHub.
