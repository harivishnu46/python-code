import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Record audio from microphone
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

# Perform speech recognition
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
