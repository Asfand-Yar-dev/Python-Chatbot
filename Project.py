import pyttsx3
import speech_recognition as sr
import os
import requests 
import datetime 
from datetime import date
import time
import warnings
import random
import wikipedia
import webbrowser
from pywhatkit import sendwhatmsg_instantly
import smtplib
import sys
import pyjokes
import pyautogui
import PyPDF2
from tkinter.filedialog import *
import psutil
import speedtest
import wolframalpha
import socket

warnings.filterwarnings("ignore") #ignoring all the warnings

if sys.platform == "win32":
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
else:
    engine=pyttsx3.init('nsss')   #sapi5 - SAPI5 on Windows
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[10].id)
    
    
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def take_command():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Go ahead,I am listening....')
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        print('Hold on a momment,Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said:{query}\n')
    except:
        speak("Please hold on...")  
        return "None"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    
    speak("I am your Virtual Assistant. How may I help you")

import smtplib

def sendEmail(to, content):
    # Replace with your email credentials
    sender_email = "muhammadbalach369@gmail@gmail.com"
    sender_password = "muhammad03@369"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # Identify yourself to the server
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, content)
        print(f"Email successfully sent to {to}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()


def news():
    api_key= 'dbc9e0bb65894032bfa6ff2df46f9785'
    main_url = f'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    numbers=["first","second","third","fourth","fifth"]
    
    for ar in articles:
        head.append(ar["title"])
    
    for i in range (len(numbers)):
        speak(f"today's {numbers[i]} news is: {head[i]}")

def crypto(slug):
    apiurl='https://pro-api.coinmarketcap.com'
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': '1104789a-dbfe-4927-870d-4029f1d3cb17',}

    session=requests.session()
    session.headers.update(headers)

    def coins_price(apiurl,slug):
        url=apiurl+'/v1/cryptocurrency/quotes/latest'
        parameters={'slug':slug}
        r=session.get(url,params=parameters)
        data=r.json()['data']
        all=str(data)
        x=all.find('price')
        all=all[x:x+20]
        
        for p in all.split():
            try: 
                float(p)
                price=p
            except:
                pass
        speak(f'{slug} price is {price}')
        return price
    
    coins_price(apiurl,slug)

def weather():
    def loc():
        try:
            ipadd=requests.get("https://api.ipify.org").text
            url="https://get.geojs.io/v1/ip/geo/"+ipadd+".json"
            geo_requests= requests.get(url)
            geo_data=geo_requests.json()
            city=geo_data['city']
        except:
            city='Quetta'
        return city

    api_key = '86320b603f8e8b33555dad84e8bca164'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    city_name = loc()
    url = base_url + "&q=" + city_name + "&appid=" + api_key 
    session=requests.session()
    r = session.get(url)
    data = r.json()
    
    if data["cod"] != "404":
        y = data["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = data["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature is " +str(int(current_temperature-273.15)) +" degree celcius\n humidity is " +
              str(current_humidiy) +"%\n with  " + str(weather_description)+'in '+city_name)
                    
def pdf_reader():
    book=askopenfilename()
    try: 
        pdfreader=PyPDF2.PdfFileReader(book)
        pages=pdfreader.numPages
        speak(f"Total numbers of pages in this pdf are {pages}")
        speak("sir please enter the page number you want me to read")
        pg=int(input("please enter the page number:"))
        
        for num in range(pg,pages):
            page=pdfreader.getPage(pg)
            text=page.extractText()
            speak(text)
    except :
        speak("Operation Cancelled !")   
        import speedtest

def check_internet_speed():
    try:
        speak("Checking internet speed")
        st = speedtest.Speedtest()
        dl = round(st.download() / 1_000_000, 2)  # Convert to megabits (Mb)
        up = round(st.upload() / 1_000_000, 2)  # Convert to megabits (Mb)
        speak(f"Current download speed is {dl} Mb/s and upload speed is {up} Mb/s.")   
        speak("Do you want me to do anything else?")
    except Exception as e:
        speak("I encountered an issue while checking the internet speed.")
        print(f"Error: {e}")     
            
def adv_search():
    query=input('Question: ')
    app_id='W3KQ4X-3WWETGEJQ2'
    client=wolframalpha.Client(app_id)
    
    if 'no thanks' in query or 'thanks' in query or 'close advance search mode' in query:
        speak('closing advance search mode')
    else:
        res=client.query(query)
        ans=next(res.results).text
        speak(ans)
        speak('want to search anything else?')
        adv_search() 




def TaskExecution():
    # function for coin toss task
    def htLine1():
        speak("It's " + res)
    def htLine2():
        speak("You got " + res)
    def htLine3():
        speak("It landed on " + res)

    wish()
    bye=True
    while bye:
        query=take_command().lower()
        #query=input()

        if "what is your name" in query:
            speak('I am Virtual Assistant.')
            continue
        
        if "tell me about yourself" in query:
            speak('I am Virtual Assistant. What can I do for you?')
            continue

        elif 'price of' in query or 'tell me the price of' in query or 'the price of' in query:
            query=query.replace('tell me the price of ','')
            query=query.replace('price of ','')
            crypto(query)
            speak('need something else?')

        elif 'weather' in query or "show weather" in query:
            weather()
            speak('need something else?')

        elif "open notepad" in query:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open calculator" in query or 'calculator' in query:
            npath="C:\\WINDOWS\\system32\\calc.exe"
            os.startfile(npath)

        elif "open chrome" in query or 'chrome' in query:
            npath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd") 
            bye=False 

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M')
            speak(f'its {strTime}')
            speak('you want me to do anything else?')

        elif "todays date" in query or "the date"in query:
            today = date.today()
            d2 = today.strftime("%B %d, %Y")
            speak(f"Today is {d2}") 
            speak('you want me to do anything else?')

        elif "ip address" in query:
            try:
                hostname = socket.gethostname()
                local_ip = socket.gethostbyname(hostname)
                speak(f"Your current internet connection's IP Address is {local_ip}")
            except Exception as e:
                speak("I couldn't fetch your IP address. Please check your internet connection.")
            speak('Do you want me to do anything else?')

        elif 'wikipedia' in query:
            speak('Searching in wikipedia')
            query=query.replace('wikipedia',' ')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            #print(results)
            speak(results)
            speak('you want me to do anything else')
            
        elif 'open google' in query:
            webbrowser.open("https://google.com")
            bye=False

        elif "send email" in query:
            try:
        # Ask for recipient email ID
                speak("To whom do you want to send the mail?")
                to = input("Enter the email ID to whom you want to send: ")

        # Ask for email content
                speak("What should I say?")
                subquery = take_command().lower()

        # Send email
                sendEmail(to, subquery)
                speak("Email has been sent.")
                speak("Do you want to do anything else?")
        
            except Exception as e:
        # Handle errors and inform the user
                speak("Sorry, the internet connection is not stable, or there was an error sending the email. Please try again later.")
                print(f"Error: {e}")
                speak("Do you want me to do anything else?")

        
        elif 'open youtube' in query:
            webbrowser.open('https://youtube.com')
            bye=False

        elif 'what is' in query:
            result=wikipedia.summary(query,sentences=2)
            speak(result)
            speak('anything else?')
        
        elif 'search in youtube' in query or 'open in youtube' in query:
            query=query.replace('search in youtube',' ')
            query=query.replace('open in youtube',' ')
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            speak(f'searchin in youtube {query}')
            bye=False

        #walframalpha
        elif 'advance search mode' in query or 'advanced search mode' in query:
            speak('Advance search mode activated')
            try:
                adv_search()
            except Exception as e:
                speak("Please hold on we are doing but there is unstable internet connection")  
            speak('do you want me to do anything else?')    
            continue

        elif 'search' in query or 'search in google' in query or 'open in google' in query:
            query=query.replace('search',' ')
            query=query.replace('search in google',' ')
            query=query.replace('open in google',' ')
            webbrowser.open(f"https://google.com/search?q={query}")
            speak(f'searching in google {query}')
            bye=False


        elif ("open gfg" in query or "open geeksforgeeks" in query):
            webbrowser.open("https://www.geeksforgeeks.org")
            bye=False

        elif "send message on whatsapp" in query or 'send message' in query or 'message on whatsapp' in query:
            speak("To whom should I send a message")
            speak(" Please type the number ")
            no=input("Enter the number:")
            speak(" what should I send ?")
            speak('You will have to scan for whatsapp web.')
            subquery=take_command().lower()
            sendwhatmsg_instantly(f"+92{no}",f"{subquery}")
            bye=False

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill/f /im notepad.exe")
            speak('you want me to do anything else?')
            
        elif ("close cmd"in query or "close command prompt" in query):
            speak("okay sir, closing cmd")
            os.system("taskkill /f /im cmd.exe")
            speak('you want me to do anything else?')

        elif 'joke' in query or 'jokes' in query:
            joke = pyjokes.get_joke('en','all')
            #print(joke)
            speak(joke)
            speak('anything else?')

        elif 'jobs' in query or 'job' in query or 'job recommandation' in query or 'work' in query:
            platforms = ['linkedin', 'indeed', 'rozee', 'Mustaqbil', 'bayt','career okay']
            speak("Select a platform that you prefer:")
            print('\n'.join(platforms))
            statement1 = take_command().lower()
            #statement1 = input()
            
            if (statement1 == 0):
                continue
            
            if 'linkedin' in statement1 or 'LinkedIn' in statement1 or 'Linkedin' in statement1:
                webbrowser.open_new_tab("https://www.linkedin.com/jobs")
                speak("LinkedIn is open now")
                break
            
            elif 'indeed' in statement1:
                webbrowser.open_new_tab("https://www.indeed.com/jobs")
                speak("Indeed is open now")
                break
            
            elif 'rozee' in statement1:
                webbrowser.open_new_tab("https://www.rozee.pk/")
                speak("Rozee is open now")
                break
            
            elif 'mustaqbil' in statement1:
                webbrowser.open_new_tab(
                    "https://www.mustakbil.com/")
                speak("Mustaqbil is open now")
                break
            
            elif 'bayt' in statement1:
                webbrowser.open_new_tab("https://www.bayt.com/en/pakistan/")
                speak("Bayt is open now")
                break
            
            elif 'career ok' in statement1:
                webbrowser.open_new_tab('https://www.careerokay.com/')
                speak('Career Okay is open now')
                break
            
            else:
                speak("Sorry we couldn't find your search!!!")
                speak('you want me to do anything else?')
            #time.sleep(3)
            
        elif "shutdown the system" in query or "shutdown" in query:
            os.system("shutdown /s /t 0")
        
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
        elif 'movie ticket booking' in query or 'movie booking' in query or 'movie ticket' in query:
            speak('opening bookme')
            webbrowser.open_new_tab("https://bookme.pk/movie-tickets-online")
            speak(" Book me show website is open now")
            bye=False

        elif 'online courses' in query or 'course' in query:
            platforms = ['coursera', 'udemy', 'edx', 'skillshare', 'datacamp', 'udacity']
            speak("Select a platform that you prefer : ")
            print("\n".join(platforms))
            statement1 = take_command().lower()
            
            if statement1 == 0:
                continue
            
            if 'coursera' in statement1:
                webbrowser.open_new_tab("https://www.coursera.org")
                speak("Coursera is open now")
                bye=False
            
            elif 'udemy' in statement1:
                webbrowser.open_new_tab("https://www.udemy.com")
                speak("udemy is open now")
                bye=False
            
            elif 'edx' in statement1:
                webbrowser.open_new_tab("https://www.edx.org/")
                speak("edx is open now")
                bye=False
            
            elif 'skillshare' in statement1:
                webbrowser.open_new_tab("https://www.skillshare.com")
                speak("skill share is open now")
                bye=False
            
            elif 'datacamp' in statement1:
                webbrowser.open_new_tab("https://www.datacamp.com")
                speak("datacamp is open now")
                bye=False
            
            elif 'udacity' in statement1:
                webbrowser.open_new_tab("https://www.udacity.com")
                speak("udacity is open now")
                bye=False
            
            else:
                speak("Sorry we couldn't find your search!!!")
                speak('you want me to do anything else?')

        elif 'train ticket booking' in query or 'train booking' in query or 'train ticket' in query or 'train ticket' in query:
            speak('opening website for train ticket booking')
            webbrowser.open_new_tab("https://www.pakrail.gov.pk/")
            speak(" Railway website is open now, have a good journey !")
            bye=False

        elif 'bus ticket booking' in query or 'bus booking' in query or 'bus ticket' in query:
            speak('opening website for bus ticket booking')
            webbrowser.open_new_tab("https://bookme.pk/buy-bus-tickets-online")
            speak(" Book me website is open now, have a good journey !")
            bye=False

        elif 'airplane ticket booking' in query or 'airplane booking' in query or 'airplane ticket' in query:
            speak('opening website for airplane ticket booking')
            webbrowser.open_new_tab("https://bookme.pk/book-flights-online")
            speak(" Book me website is open now, have a good journey !")
            bye=False

        elif "hotel" in query or "hotel booking" in query:
            speak('Opening go bookme.com.pk')
            webbrowser.open_new_tab('https://bookme.pk/book-hotels-online')
            bye=False

        elif 'switch the window' in query or 'change window' in query:
            if sys.platform == "win32":
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")  
                bye=False
            else:
                pyautogui.keyDown("command")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("command")  
                bye=False

        elif ("tell me news" in query or "news" in query):
            speak("Please wait, Fetching the latest news")
            news()
            speak('need something else?')

        elif ("tell me my location" in query or "location" in query):
            speak("Hold on,Locating our current location")
            try:
                ipadd=requests.get("https://api.ipify.org").text
                url="https://get.geojs.io/v1/ip/geo/"+ipadd+".json"
                geo_requests= requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                country=geo_data['country']
                speak(f"We are in {city},{country}")
                speak('need something else?')

            except Exception as e:
                speak("Sorry,I am unable to locate our current location due to poor connectivity. Please try after sometime.")
                bye=False

        elif "take a screenshot" in query or "take screenshot" in query:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            speak("Taking a screenshot...")
            time.sleep(3)
            screenshot = pyautogui.screenshot()
            save_directory = "Screenshots"
            
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            file_name = os.path.join(save_directory, f"screenshot_{timestamp}.png")
            screenshot.save(file_name)
            speak(f"Screenshot taken and saved in the folder {save_directory}.")
            speak("Do you need anything else?")
            
        elif "how much battery is left" in query or "how much power is left" in query or "battery" in query:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"We have {percentage} percent battery. ")
            if percentage>=50:
                speak("We have enough power to go on.")
            elif percentage>=20 and percentage<50:
                speak("You shall connect the system to a charging point")    
            elif percentage<20:
                speak("Battery about to die,connect to a charging point as soon as possible")
            speak('you want me to do anything else')

        elif "internet speed" in query:
            speak("Checking internet speed")
            st=speedtest.Speedtest()
            dl=round(float(st.download())/8000000,2)
            up=round(float(st.upload())/8000000,2)
            speak(f"Current downloading speed is {dl}mb/s while uploading speed is {up}")   
            speak('you want me to do anything else?')

        elif "volume up" in query:
            pyautogui.press("volumeup")
            speak('you want me to do anything else?')
        elif "volume down" in query:
            pyautogui.press("volumedown")
            speak('you want me to do anything else?')
        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")   
            speak('you want me to do anything else?')

        elif 'flip the coin' in query or 'toss the coin' in query or 'toss a coin' in query or 'flip a coin' in query:
            chances = ['Heads', 'Tails']
            res = random.choice(chances)
            picLine = random.randint(1, 3)
            lines = [htLine1, htLine2, htLine3]
            lines[picLine - 1]()
            speak('you want me to do anything else?')

        elif 'dice' in query:
            num = random.randint(1, 6)
            speak("Your rolled " + str(num))   
            speak('you want me to do anything else?')

        elif 'bye' in query or 'no' in query or ' no thanks' in query:
            speak('Untill next time Bye Bye')
            bye=False

        else:
            speak("Sorry,I don't know how to do that right now but i am still learning how to be more helpful")
            speak('anything else?')
        #time.sleep(2)
        
if __name__=="__main__":
    TaskExecution()