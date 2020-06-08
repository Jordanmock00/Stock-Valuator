from gtts import gTTS 
#interface with Google Translate's text-to-speech API
from speech_recognition.Recogniser import Recogniser as sr
#recognises speech and audio input
import re
#'RE' specifies a set of strings that matches it
import time
#allows to get time and date
import webbrowser
#webbrowser module,provides an interface to display Web-based documents
import random
#This module implements pseudo-random number generators
from selenium import webdriver
#used to automate the testing of a web applications
from selenium.webdriver.common.keys import Keys#
import smtplib
#aka 'Simple Mail Transfer Protocol' send emails
import requests
#works with web browser to help request search of key word
from pygame import mixer
#acts like a mixer board
import urllib.request
#function is similar to search with google
import urllib.parse
#used to parse values into the url
import bs4#


def talk(audio):
    print(audio)
    for line in audio.splitlines(): 
        text_to_speech = gTTS(text=audio, lang='en')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        

  
def myCommand():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('how can i help you?')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
        print('one moment pleas')

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        time.sleep(2)

    except sr.UnknownValueError:
        print('i do not understand')
        command = myCommand();

    return command

    
   
def Confusion(command):
    errors=[
        "I don't know what you mean",
        "Excuse me?",
        "Can you repeat that?",
    ]
    
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + 'r/' + subgoogle
        talk('you got it!')
        driver = webdriver.Firefox(executable_path='/home/coderasha/Desktop/geckodriver')
        driver.get('http://www.google.com')
        search = driver.find_element_by_name('q')
        search.send_keys(str(search_for))
        search.send_keys(Keys.RETURN) 

    
    
    elif 'wikipedia' in command:
        reg_ex = re.search('wikipedia (.+)', command)
        if reg_ex: 
            query = command.split("wikipedia",1)[1] 
            response = requests.get("https://en.wikipedia.org/wiki/" + query)
            if response is not None:
                html = bs4.BeautifulSoup(response.text, 'html.parser')
                title = html.select("#firstHeading")[0].text
                paragraphs = html.select("p")
                for para in paragraphs:
                    print (para.text)
                intro = '\n'.join([ para.text for para in paragraphs[0:3]])
                print (intro)
                mp3name = 'speech.mp3'
                language = 'en'
                myobj = gTTS(text=intro, lang=language, slow=False)   
                myobj.save(mp3name)
                mixer.init()
                mixer.music.load("speech.mp3")
               while mixer.music.play()
    elif 'stop' in command:
        mixer.music.stop()

    
    elif 'youtube' in command:
        talk('Ok!')
        reg_ex = re.search('youtube (.+)', command)
        if reg_ex:
            domain = command.split("youtube",1)[1] 
            query_string = urllib.parse.urlencode({"search_query" : domain})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            #print("http://www.youtube.com/watch?v=" + search_results[0])
            webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
            pass



    elif 'hello' in command:
        talk('Hello jordan!How can I help you?')
        time.sleep(3)
    elif 'who are you' in command:
        talk('I am a your personal assistaint ')
        time.sleep(3)
    else:
        error = random.choice(errors)
        talk(error)
        time.sleep(3)


talk('HELLO ... HOW CAN I HELP YOU?!')

#loop to continue executing multiple commands
while True:
    time.sleep(4)
    lucy(myCommand())
