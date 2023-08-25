import ctypes
import json
import os
import re
import smtplib
import cv2
import time
from bs4 import BeautifulSoup
import requests
from plyer import notification
import shutil
import random
import pyjokes
import pyttsx3
import datetime
import pyautogui
import pywhatkit
import webbrowser
from wikipedia import wikipedia
import wolframalpha
from selenium import webdriver
import speech_recognition as sr
import wikipedia as googleScrap
import screen_brightness_control as sbc
from selenium.webdriver.common.keys import Keys



# ----------------------------Engine-Start------------------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)  


# ---------------Stablishing-Connection-to-wolframalpha-API-------------
try:
    app = wolframalpha.Client('XA9XH9-2JA94TKR4G')
except Exception:
    print('Error connection to intelligent wolf...')


# --------------------------Writing-Functions----------------------------

# ------Speak-Function-------
def speak(str):
    engine.say(str)
    engine.runAndWait()

# -------Cmd-text-align-center----------
columns = shutil.get_terminal_size().columns

#---------Wish-Me-Function--------
def wishMe():
    print('_#-#__#-#__#-#__#-#__#-#_\n'.center(columns))
    print('Welcome Boss!'.center(columns))
    speak('Welcome Boss!')

    payRespect = ['Good Morning!','Good Afternoon!','Good Evening!']
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(payRespect[0].center(columns))
        speak(payRespect[0])
    elif hour >= 12 and hour <18:
        print(payRespect[1].center(columns))
        speak(payRespect[1])
    else:
        print(payRespect[2].center(columns))
        speak(payRespect[2])
    print('-#_#--#_#--#_#--#_#--#_#-'.center(columns))
    # print('_-_-_-_-_-_-_-_-_'.center(columns))
    time.sleep(1)
    rand_ask = ["How can i help you?", "What can i do for you?","Is there something I can do for you?","How may I assist you?","Feel free to tell me if you want something." ]
    say = random.choice(rand_ask)
    print(say)
    speak(say)
    
#--------------Date/Time-Function--------------
def report_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    print(f"Sir, the current time is {current_time}")
    speak(f"Sir the current time is {current_time}")
    time.sleep(1)

# -------------------Take-Commands------------
def take_command():
    print("\nListening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            print('Recognizing...')
            said = r.recognize_google(audio, language ='en-in')
            print(f"User said: {said}")
        except Exception as e:
            print("Exception: " + str(e))
    return said

# ----------------Automate-Chrome-Driver----------------
def autoGoogle(searchQuery):
    web.get('https://www.google.com/')
    time.sleep(2)
    speak("ok boss!")
    speak(f'Searching {searchQuery}')
    search_box = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    for character in searchQuery:
        search_box.send_keys(character)
        time.sleep(0.2)
    time.sleep(1)
    pyautogui.press('enter')
    mainLoop()

#---------------Brightness-Control--------------
def controlBrightness(instruction):
    if 'increase brightness' in instruction:
        current_brightness = sbc.get_brightness()
        i = 1
        while i<21:
            sbc.set_brightness(current_brightness+i)
            i = i+1
        print("Increased brigtness to: +",current_brightness+20)
        speak(f"Increased brigtness to, +{current_brightness+20}")

    elif 'decrease brightness' in instruction:
        current_brightness = sbc.get_brightness()
        i = 1
        while i<21:
            sbc.set_brightness(current_brightness-i)
            i = i+1
        print("Decreased brigtness to: -",current_brightness-20)
        speak(f"Decreased brigtness to, -{current_brightness-20}")

# -------------------Open-Drive---------------
def openDrive(driveName):
    
    if 'open c drive' in driveName:
        print("opening C drive..")
        speak("opening C drive..")
        os.startfile('c:/')
        
    elif 'open d drive' in driveName:
        print("opening D drive..")
        speak("opening D drive...")
        os.startfile('d:/')
        
    elif 'open e drive' in driveName:
        print("opening E drive..")
        speak("opening E drive...")
        os.startfile('e:/')

#---------------Automate-Window-actions
def autoWindow_actions(command):
    if 'refresh' in command and 'window' in command:
        speak("Ok boss!")
        pyautogui.hotkey('win','d')
        time.sleep(1)
        count = 0
        speak("Started refreshing!")
        while count<200:
            pyautogui.hotkey('fn','f5')
            count = count + 1
            if count == 100:
                speak("Sir wait one second, I'm making your PC super fast.")
        pyautogui.hotkey('win','d')
        speak("done")

    elif 'change window' in command:
        pyautogui.hotkey('alt','tab')

    elif 'close window' in command:
        pyautogui.hotkey('alt','f4')

    #window action for chrome        
    elif 'new tab' in command:
        pyautogui.hotkey('ctrl','t')

    elif 'change tab' in command:
        pyautogui.hotkey('ctrl','tab')

    elif 'close tab' in command:
        pyautogui.hotkey('ctrl','w')


    
#-------------------Automate-Mouse-------------
def autoMouse(action):
    if "mouse right " in action:
        pyautogui.move(300,0,duration=0.2)

    elif "mouse down" in action:
        pyautogui.move(0,300,duration=0.2)

# ---------------intelligent-Wolframalpha----------
def intelligentWolf(query):
        try:
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)
        except Exception:
            print('Data not available!')
            speak('Data not available!')

# ------------------Login-to-urise---------------
def urisePortal():
    speak('opening u rise')           
    web.get('https://www.google.com')
    search_box = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    query = 'Login urise'
    for character in query:
        search_box.send_keys(character)
        time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(1)
    web.get('https://urise.up.gov.in/')
    time.sleep(2)
    popBox = web.find_element_by_xpath('/html/body')
    popBox.click()
    web.get('https://urise.up.gov.in/student/login')
    time.sleep(1)
    popBox1 = web.find_element_by_xpath('/html/body')
    popBox1.click()
    id_input = web.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/form/div[1]/div/input')
    time.sleep(1)
    for character in "UR202000175737":
        id_input.send_keys(character)
        time.sleep(0.2)
    pass_input = web.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/form/div[2]/div/input')
    time.sleep(1)
    for character in "Sunny@37":
        pass_input.send_keys(character)
        time.sleep(0.2)  
    submit = web.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/form/input[2]')
    time.sleep(1)
    submit.click()
    speak('login successful!') 
    
def make_request(url):
  response = requests.get(url)
  return response.text

#---------------get-Next-word-after-word-----------
def nextword(target,source):
    for i, w in enumerate(source):
        if w == target:
            return source[i + 1]



#---------------------Main-function-----------------
def mainLoop():
        while True:
            
            query = take_command().lower()
            sl = query.split()

        #Date/Time

            if "time" in query:
                report_time()
        
        #Automate-Chrome

            elif "open chrome" in query:
                global web
                try:
                    web = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
                    web.get('https://www.google.com/')
                except:
                    speak('Chrome Driver Not found!')
                    webbrowser.open("https://wwww.google.com/")

            elif "search" in query:
                query = query.split("search",1)[1]
                try:
                    autoGoogle(query)
                except:
                    speak("ok boss!")
                    speak(f'Searching {query}')
                    pywhatkit.search(query)
                    try:
                        info = wikipedia.summary(query,sentences=2)
                        print(info)
                        speak(info)
                    except:
                        None
                    


            elif "open google" in query:
                time.sleep(0.6)
                print("Opening Google...")
                speak("Opening Google...")
                webbrowser.open('https://www.google.com')
            
            elif "open instagram" in query:
                time.sleep(0.6)
                print("Opening Instagram...")
                speak("Opening Instagram")
                webbrowser.open('https://www.instagram.com')
            
            elif "open facebook" in query:
                time.sleep(0.6)
                print("Opening Facebook...")
                print("Opening Facebook...")
                webbrowser.open('https://www.facebook.com')

        #Brightness control

            elif "increase brightness" in query:
                controlBrightness(query)

            elif "decrease brightness" in query:
                controlBrightness(query)
         
        #Open-Drive

            elif "open c drive" in query:
                openDrive(query)

            elif "open d drive" in query:
                openDrive(query)

            elif "open e drive" in query:
                openDrive(query)
        
        #Automate-Window-actions

            elif "refresh window" in query:
                autoWindow_actions(query)

            elif "change window" in query:
                autoWindow_actions(query) 

            elif "close window" in query:
                autoWindow_actions(query)
            #browser-actions
            elif "new tab" in query:
                autoWindow_actions(query)

            elif "change tab" in query:
                autoWindow_actions(query)

            elif "close tab" in query:
                autoWindow_actions(query)
                
      
        #Automate-Mouse-actions

            elif "right" in query:
                autoMouse(query)

            elif "down" in query:
                autoMouse(query)

        #The-Intelligence-wolframalpha

            elif "what is" in query:
                intelligentWolf(query)

            elif 'lock window' in query:
                speak("Locking your device")
                ctypes.windll.user32.LockWorkStation()
                

            elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20,0,"d:/Wallpapers/Music",0)
                speak("Background changed successfully")

            elif "who are you" in query:
                speak("I am a virtual assistant created by Ved!")

            elif 'send' in query and 'email' or 'mail' in query and 'sunny' in query:
                try:
                    speak('Ok Boss!')
                    sender_email = "honey37bunny@gmail.com"
                    rec_email = 'musicloverved37@gmail.com'
                    speak('What is message you want to deliver!')
                    message = take_command()
                    message = message.replace('tell him','')

                    # password = input(str("Please enter your password : "))
                    password = "bunnyHoney8055"

                    server = smtplib.SMTP('smtp.gmail.com', 587)

                    server.starttls()

                    server.login(sender_email,password)
                    print('Login Successful!')
                    speak('Login Successful!')
                    server.sendmail(sender_email, rec_email, str(message))
                    print("Email has been sent to ", rec_email)
                    speak(f"Email has been sent to Sunny")
                 
                    server.quit()
                    
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
                    
            elif 'send' in query and 'email' or 'mail' in query and 'akhilesh' in query:
                try:
                    speak('Ok Boss!')
                    sender_email = "honey37bunny@gmail.com"
                    rec_email = 'akhileshmrj105@gmail.com'
                    speak('What is message you want to deliver!')
                    message = take_command()
                    message = message.replace('tell him','')

                    # password = input(str("Please enter your password : "))
                    password = "bunnyHoney8055"

                    server = smtplib.SMTP('smtp.gmail.com', 587)

                    server.starttls()

                    server.login(sender_email,password)
                    print('Login Successful!')
                    speak('Login Successful!')
                    server.sendmail(sender_email, rec_email, str(message))
                    print("Email has been sent to ", rec_email)
                    speak(f"Email has been sent to akhilesh")
                 
                    server.quit()

                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
                    
        #WikiPedia

            elif "wikipedia" in query:
                query = query.split("wikipedia",1)[1]
                summary = wikipedia.summary(query, sentences=2)
                print(summary)
                speak(summary)
        
        #Creating-Pause

            elif "wait" in query:
                seconds = 0
                while seconds < 10:
                    print(seconds)
                    time.sleep(1)
                    seconds = seconds +1

        #Funny-pyjokes

            elif 'joke' in query:
                random_joke = pyjokes.get_joke()
                print(random_joke)
                speak(random_joke)
        
        #thanking 

            elif 'thank you' in query:
                random_interjection = ["your welcome!","No sorry, no thank you in between friends..,ok?","it's ok!"]
                say = random.choice(random_interjection)
                print(say)
                speak(say)

        #DrawPy
            
            elif 'draw something' in query:

                os.startfile('C:\Windows\System32\mspaint.exe')
                time.sleep(5)

                x_start = 200
                y_start = 200

                pyautogui.moveTo(x_start, y_start)

                frame = 12

                for i in range(1, frame + 1):

                    originalImage = cv2.imread('./bulk/image' + str(i) + '.png')

                    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

                    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

                    for y in range(len(blackAndWhiteImage)):
                        row = blackAndWhiteImage[y]

                        for x in range(len(row)):
                            if row[x] == 0:
                                pyautogui.click(x_start + x, y_start + y, _pause = False)
                                print('Drawing at:', x_start + x, y_start + y)

                                time.sleep(0.008)

        #Exit

            elif "exit" in query:
                exit()

      #xampp control 

            elif "xampp server" in query:
                speak("ok boss! Opening xampp server")
                time.sleep(0.5)
                pyautogui.hotkey('win','s')
                time.sleep(0.6)
                pyautogui.write('xampp',interval=0.3)
                time.sleep(0.7)
                pyautogui.press('enter')

            elif "login portal" in query: 
                try: 
                    urisePortal()
                except:
                    web = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
                    urisePortal()
                        
            elif 'screenshot' in query:
                pyautogui.hotkey('win','printscreen')
                print("Screenshot has been taken succesfully!")
                speak("Done!")

            elif "play" in query:
                query = query.split("play",1)[1]
                speak(f"playing {query}")
                pywhatkit.playonyt(query)

            elif 'news' in query:
                try:
                    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=087b9a2bfdbf43d0ac2ef38db5a916d2')
                    data = json.loads(r.content)
                    speak("Breaking News!")
                    for i in range(3):
                        news = data['articles'][i]['title']
                        print(news+"\n")
                        speak(news)
                except Exception as e:
                    print(str(e))

        # Help
            # elif "help" in query and "jarvis" in query:
                # print(homem)
                
        #Selfie 
            # selfie code

            elif 'covid-19 status' in query:
                html_data = make_request('https://www.worldometers.info/coronavirus/')
                # print(html_data)
                soup = BeautifulSoup(html_data, 'html.parser')
                total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
                total_cases = total_global_row.find_all('td')[2].get_text()
                new_cases = total_global_row.find_all('td')[3].get_text()
                total_recovered = total_global_row.find_all('td')[6].get_text()
                print('total cases : ', total_cases)
                print('new cases : ', new_cases[1:])
                print('total recovered : ', total_recovered)
                notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
                notification.notify(
                    title="COVID-19 Statistics",
                    message=notification_message,
                    timeout=5
                )
                speak("here are the stats for COVID-19")
                speak(notification_message)

            
  
wishMe()
mainLoop()
