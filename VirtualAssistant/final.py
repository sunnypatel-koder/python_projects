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
import screen_brightness_control as sbc 
from selenium.webdriver.common.keys import Keys



# ----------------------------Engine-Start------------------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
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

#---------Wish-Me-Function--------
def wishMe():
    columns = shutil.get_terminal_size().columns
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
    print("How may i assist you?")
    speak("how may i assist you?")
    # print('_-_-_-_-_-_-_-_-_'.center(columns))

    
#--------------Date/Time-Function--------------
def report_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    print(f"The current time is {current_time}")
    speak(f"The current time is {current_time}")

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
            print("user said: ",said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

# ----------------Automate-Chrome-Driver----------------
def autoGoogle(searchQuery):
    web.get('https://www.google.com/')
    time.sleep(2)
    search_box = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    for character in searchQuery:
        search_box.send_keys(character)
        time.sleep(0.2)
    time.sleep(1)
    pyautogui.press('enter')
    # time.sleep(1)
    mainLoop()

#---------------Brightness-Control--------------
def controlBrightness(instruction):
    if 'increase brightness' in instruction:
        current_brightness = sbc.get_brightness()
        i = 1
        while i<21:
            sbc.set_brightness(current_brightness+i)
            i = i+1
        print("Changed brigtness to: +",current_brightness+20)
        speak(f"Changed brigtness to, +{current_brightness+20}")

    elif 'decrease brightness' in instruction:
        current_brightness = sbc.get_brightness()
        i = 1
        while i<21:
            sbc.set_brightness(current_brightness-i)
            i = i+1
        print("Changed brigtness to: -",current_brightness-20)
        speak(f"Changed brigtness to, -{current_brightness-20}")

# -------------------Open-Drive---------------
def openDrive(driveName):
    global drive
    if 'open c drive' in driveName:
        drive = 'c:/'
        os.startfile('c:/')
    elif 'open d drive' in driveName:
        drive = 'd:/'
        os.startfile('d:/')
    elif 'open e drive' in driveName:
        drive = 'd:/'
        os.startfile('d:/')

#---------------Automate-Window-actions
def autoWindow_actions(command):
    if 'refresh window' in command:
        speak("refreshing now boss!")
        pyautogui.hotkey('win','d')
        time.sleep(1)
        count = 0
        while count<100:
            pyautogui.hotkey('fn','f5')
            count = count + 1
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
            print('not available!')
            speak('not available!')

# ------------------Login-to-urise---------------
def urisePortal():
    speak('Ok boss, as you wish!')           
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

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
#------------Enable low security in gmail----------
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()

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
                web = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
                web.get('https://www.google.com/')
              

            elif "search" in query:
                query = query.split("search",1)[1]
                try:
                    autoGoogle(query)
                except:
                    pywhatkit.search(query)
                    try:
                        info = wikipedia.summary(query,sentences=2)
                        print(info)
                        speak(info)
                    except:
                        None
                    # webbrowser.open(query)
                    


            elif "open google" in query:
                time.sleep(0.6)
                webbrowser.open('https://www.google.com')
            
            elif "open instagram" in query:
                time.sleep(0.6)
                webbrowser.open('https://www.instagram.com')
            
            elif "open facebook" in query:
                time.sleep(0.6)
                webbrowser.open('https://www.facebook.com')

            elif "open youtube" in query:
                time.sleep(0.6)
                webbrowser.open('https://www.youtube.com/')

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

            elif "what is" in query or "who is" in query:
                # query = query.replace('find',"")
                intelligentWolf(query)

            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20,0,"d:/Wallpapers/Music",0)
                speak("Background changed successfully")

            elif "who are you" in query:
                speak("I am a virtual assistant created by Team of Sunny Patel!, How can i help you?")

            elif 'send a mail to sunny' in query:
                try:
                    speak('Ok boss!')
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
                    speak('Login successful!')
                    print("Login Successfull!")
                    server.sendmail(sender_email, rec_email, message)
                    print("Email has been sent to ", rec_email)
                    speak(f"email has been sent to {rec_email}")

                    server.quit()

                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
                
            elif 'send a mail to sundaram' in query:
                try:
                    speak('Ok boss!')
                    sender_email = "honey37bunny@gmail.com"
                    rec_email = 'sundaramraj326@gmail.com'
                    speak('What is message you want to deliver!')
                    message = take_command()
                    message = message.replace('tell him','')

                    # password = input(str("Please enter your password : "))
                    password = "bunnyHoney8055"

                    server = smtplib.SMTP('smtp.gmail.com', 587)

                    server.starttls()

                    server.login(sender_email,password)
                    speak('Login successful!')
                    print("Login Successfull!")
                    server.sendmail(sender_email, rec_email, message)
                    print("Email has been sent to ", rec_email)
                    speak(f"email has been sent to {rec_email}")

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
                speak("ok, but please wait 2 minutes for this magic!")
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
                speak("done!")

            elif "play" in query:
                query = query.split("play",1)[1]
                speak(f"ok boss, Playing {query}")
                pywhatkit.playonyt(query)

            elif 'news' in query:               
                try:
                    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=087b9a2bfdbf43d0ac2ef38db5a916d2')
                    data = json.loads(r.content)
                    for i in range(4):
                        news = data['articles'][i]['title']
                        print(news+"\n")
                        speak(news)
                except Exception as e:
                    print(str(e))

            elif 'covid-19 status' in query:
                html_data = make_request('https://www.worldometers.info/coronavirus/')
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

