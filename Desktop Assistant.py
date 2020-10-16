import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! ")

    elif hour>=12 and hour<17:
        speak("Good Afternoon! ")

    elif hour>=17 and hour<19 :
        speak("Good Evening! ")

    else:
        speak("Good Night! ")

    speak("I am your  Vertual  Assistant Suzi. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    rr = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rr.pause_threshold = 1
        audio = rr.listen(source)

    try:
        print("Recognizing...")
        query = rr.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Connection error")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "hello" in query or "hello Suzi" in query:
            hello1 = "Hello ! How May i Help you.."
            print(hello1)
            speak(hello1)

        elif "who are you" in query or "about you" in query or "your details" in query:
            who_are_you = "I am Suzi an A I based computer program but i can help you lot like a your assistant ! try me to give simple command !"
            print(who_are_you)
            speak(who_are_you)

        elif 'who make you' in query or 'who made you' in query or 'who created you' in query or 'who develop you' in query:
            speak(" For your information Prasun Roy Created me !    I can show you his Linked In profile if you want to see.    Yes or no .....")
            ans_from_user_who_made_you = takeCommand()
            if 'yes' in ans_from_user_who_made_you or 'ok' in ans_from_user_who_made_you or 'yeah' in ans_from_user_who_made_you:
                webbrowser.open("https://www.linkedin.com/in/prasun-roy-")
                speak('opening his profile...... please wait')

            elif 'no' in ans_from_user_who_made_you or 'no thanks' in ans_from_user_who_made_you or 'not' in ans_from_user_who_made_you:
                speak("All right ! OK...")
            else :
                speak("I can't understand. Please say that again !")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")   

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")

        elif 'play music' in query:
            speak("ok i am playing music")
            music_dir = 'E:\\My MUSIC'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = 'E:\\\My Videos'
            Videos = os.listdir(video_dir)
            print(Videos)
            os.startfile(os.path.join(video_dir,Videos[0]))

        elif 'good bye' in query:
            speak("good bye")
            exit()

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif "your name" in query or "sweat name" in query:
            naa_mme = "Thanks for Asking my self ! Suzi"
            print(naa_mme)
            speak(naa_mme)

        elif "you feeling" in query:
            print("feeling Very happy to help you")
            speak("feeling Very happy to help you")

        elif query == 'none':
            continue

        elif 'exit' in query or 'stop' in query or 'quit' in query :
            exx_exit = 'See you soon. Bye'
            speak(exx_exit)
            exit() 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\vs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening visual studio code")

        elif 'email to prasun' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "prasunroy988@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.... I am not able to send this email")

        elif 'how are you' in query:
            setMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            ans_qus = random.choice(setMsgs)
            speak(ans_qus)
            speak(" How are you'")
            ans_from_user_how_are_you = takeCommand()
            if 'fine' in ans_from_user_how_are_you or 'happy' in ans_from_user_how_are_you or 'okey' in ans_from_user_how_are_you:
                speak('Great')  
            elif 'not' in ans_from_user_how_are_you or 'sad' in ans_from_user_how_are_you or 'upset' in ans_from_user_how_are_you:
                speak('Tell me how can i make you happy')
            else :
                speak("I can't understand. Please say that again !")
                
       else:
        print("I cant understand, Say that again please!")
