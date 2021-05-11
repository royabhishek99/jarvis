import pyttsx3 #library for text to speech conversion
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5') #Speech API used for voice recognition (provided by microsoft)
voices = engine.getProperty('voices') #every system has an inbuilt voice, we are using that voice to communicate with the system
#print(voices[0].id)
engine.setProperty('voice', voices[0].id) #there is 1 male and one female voice, thus using the first one




def speak(audio):  #audio is the string, we can make any string speak using 'speak()'
    engine.say(audio)  #the engine will speak the audio string
    engine.runAndWait() #a function

def wishMe(): #the computer will wish me according to the time, i.e. before 12pm Good Morning, post 12pm Good Afternoon and Post 6pm Good Evening
    hour = int(datetime.datetime.now().hour) #will give the current time in hour(s) format
    if hour>=0 and hour <12:
        speak("Good Morning, Death Honour!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon, Death Honour!")

    else:
        speak("Good Evening, Death Honour!")

    speak("Jarvis this side, what's good?")

def takeCommand(): #take microphone i/p from the user and returns string output
    r=sr.Recognizer()   #to recognize speech
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1
        r.pause_threshold = 1 #for 1 sec the computer will not speak anything
        audio = r.listen(source)  #capturing the i/p from microphone with listen(), and with mic as the source, we use it as the parameter

        try:  #for catching error
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            #print(e) #this is to show the error, since we don't want the error to be seen (if any), we don't use it
            print("Say that again please....") #so instead of showing the error, it'll show this, which will look much much better lol
            return "None"
        return query



if __name__ == "__main__" :  #c language ka void main() or int main() or only main()
    wishMe()   #uses the speak function and making the string speak
    takeCommand()