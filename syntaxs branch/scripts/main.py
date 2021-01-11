import JarvisAI
import re
import pprint
import random
import os
import os.path
import webbrowser
import playsound
import time


def FolderMake(directory) :
    try :
        if not os.path.exists(directory) :
            os.makedirs(directory)
    except OSError :
        print('Error: Creating data path. ' + directory)

def jarvis(text) :
    print("Jarvis: " + text)

FolderMake('./data/')

data_folder = os.path.join("scripts", "data")



obj = JarvisAI.JarvisAssistant()

Hibernating=True

def t2s(text):
    obj.text2speech(text)

try :
    heck = open('data/setup.bat', 'r')
    FirstTime = False
    heck.close()
except NameError :
    Atom = True
except FileNotFoundError :
    jarvis("Looks like it's your first time, lets get you set up!")
    t2s("Looks like it's your first time, lets get you set up!")
    FirstTime = True
    jarvis("Alright, first of all.. What's your first name?")
    t2s("Alright, first of all.. What's your first name")
    names = obj.mic_input()
    name = names.split(' ')[-1]
    jarvis("Nice, thank you " + name)
    t2s("Nice, thank you " + name)
    namedata = open('data1s.bat', 'w')
    namedata.write(name)
    namedata.close()
    os.replace("data1s.bat", "data/data1s.bat")
    setup = open('setup.bat', 'w')
    setup.write("Set up complete.")
    setup.close()
    os.replace("setup.bat", "data/setup.bat")
    jarvis("Wow, you're all done " + name + ", wasn't that fast!")
    t2s("Wow, you're all done " + name + ", wasn't that fast!")
    jarvis("To activate me all you need to say is 'jarvis' and I will be at your service.")
    t2s("To activate me all you need to say is 'jarvis' and I will be at your service.")


Hibernating = True
while True:
    res = obj.mic_input()
    first = res.split(' ')[0]

    if Hibernating == True and re.search('jarvis', res):
      Hibernating=False
# and Hibernating == False:

    if re.search('weather|temperature', res) and Hibernating == False:
            city = res.split(' ')[-1]
            weather_res = obj.weather(city=city)
            jarvis(weather_res)
            t2s(weather_res)
            Hibernating = True

    if re.search('thank you', res) :
        jarvis("No problem, I'm always happy to help.")
        t2s("No problem, I'm always happy to help.")

    if re.search('news', res) and Hibernating == False:
        news_res = obj.news()
        pprint.pprint(news_res)
        t2s(f"I have found {len(news_res)} news articles. You can read them. Let me tell you first 2 news articles")
        t2s(news_res[0])
        t2s(news_res[1])
        Hibernating = True

    if res == 'no' and Hibernating == False :
        jarvis("Ok then")
        t2s("Ok then ")
        Hibernating = True

    if res == 'so do i' and Hibernating == False :
        jarvis("I'm glad we both agree")
        t2s("Im glad we both agree")
        Hibernating = True

    if res == 'i think also' and Hibernating == False :
        jarvis("I'm glad we both agree")
        t2s("Im glad we both agree")
        Hibernating = True

    if re.search('tell me about', res) and Hibernating == False :
        term = res.replace("tell", "", 1)
        term2 = term.replace("me", "", 1)
        topic = term2.replace("about", "", 1)
        wiki_res = obj.tell_me(topic)
        jarvis(wiki_res)
        t2s(wiki_res)
        Hibernating = True

    if re.search('wiki', res) and Hibernating == False :
        topic = res.replace("wiki", "", 1)
        wiki_res = obj.tell_me(topic)
        jarvis(wiki_res)
        t2s(wiki_res)
        Hibernating = True

    if re.search('say', res) and Hibernating == False :
        term = res.replace("say ", "", 1)
        jarvis(term)
        t2s(term)
        Hibernating = True

    if re.search('date', res) and Hibernating == False :
        date = obj.tell_me_date()
        jarvis(date)
        print(t2s(date))
        Hibernating = True

    if re.search('time', res) and Hibernating == False :
        time = obj.tell_me_time()
        jarvis(time)
        t2s(time)
        Hibernating = True

    if re.search('open', res) and Hibernating == False :
        domain = res.split(' ')[-1]
        open_result = obj.website_opener(domain + '.com')
        jarvis("Got it!")
        t2s("Got it!")
        Hibernating = True


    if re.search('google', res) and Hibernating == False :
     term = res.replace("google ", "", 1)
     new=2
     TabUrl="http://google.com/?#q="
     webbrowser.open(TabUrl+term,new=new)
     jarvis('Searching for:' + term)
     t2s('Searching for:' + term)
     Hibernating = True

    if re.search('search', res) and Hibernating == False :
     term = res.replace("search ", "", 1)
     new=2
     TabUrl="http://google.com/?#q="
     jarvis('Searching for:' + term)
     webbrowser.open(TabUrl + term, new=new)
     t2s('Searching for:' + term)
     Hibernating = True

    if re.search('how do i', res) and Hibernating == False :
     term = res.replace("how ", "", 1)
     term2 = term.replace("do ", "", 1)
     term3= term2.replace("i ", "", 1)
     howto= 'how to '
     new=2
     TabUrl="http://google.com/?#q="
     webbrowser.open(TabUrl+howto+term3,new=new)
     jarvis('Searching for ' + howto + term3)
     t2s('Searching for ' + howto + term3)
     Hibernating = True

    if re.search('how to', res) and Hibernating == False :
     term3 = res.replace("how to", "", 1)
     howto = 'how to'
     new = 2
     TabUrl="http://google.com/?#q="
     webbrowser.open(TabUrl+howto+term3,new=new)
     jarvis('I found this on the web for:' + howto + term3)
     t2s('I found this on the web for:' + howto + term3)
     Hibernating = True

    if re.search('launch', res) and Hibernating == False :
        dict_app = {
            'chrome': 'C:\Program Files\Google\Chrome\Application\chrome.exe',
            'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe',
            'vscode': 'C:/Users/muham\AppData\Local\Programs\Microsoft VS Code\Code.exe'

        }

        app = res.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            t2s('Application path not found')
            jarvis('Application path not found')
            Hibernating = True
        else:
            t2s('Launching: ' + app)
            os.startfile(path)
            Hibernating = True


    def greeting():
        li = ['hey', 'hi!', 'hiya!', 'hello', 'yo']
        response = random.choice(li)
        jarvis(f"{response}")
        t2s(f"{response}")
        Hibernating = True

    if first == "hello" and Hibernating == False :
      greeting()

    if first == "hi" and Hibernating == False :
      greeting()

    if first == "hey" and Hibernating == False :
      greeting()

    if res == 'yes' and Hibernating == False :
        li = ['Uh ok', 'Indeed', 'Of Course', 'yes']
        response = random.choice(li)
        jarvis(f"{response}")
        t2s(f"{response}")
        Hibernating = True

    if re.search('you doing', res) and Hibernating == False :
        li = ['Currently Im learning more from you', 'Studying you', 'Transferring data', 'Interacting!']
        response = random.choice(li)
        jarvis(f"{response}")
        t2s(f"{response}")
        Hibernating = True

    if re.search('now what|so what now', res) and Hibernating == False :
        li = ['Whatever you want to do', 'You choose', 'You could use some of my commands', 'Go outside!']
        response = random.choice(li)
        jarvis(f"{response}")
        t2s(f"{response}")
        Hibernating = True

    if re.search('tell me a joke', res) and Hibernating == False :
        li = ['How do you fix a broken gorilla? With a monkey wrench.', 'Why did The Joker have to sleep with his lights on? Because he was afraid of the Dark Knight.', 'What did one butt cheek say to the other? Between you and me it stinks in here ', 'Why do police get to protests early? To beat the crowd']
        response = random.choice(li)
        jarvis(f"{response}")
        t2s(f"{response}")
        playsound.playsound('library/Crowd-laughing.mp3', True)
        Hibernating = True

    if re.search('how are you', res) and Hibernating == False :
        li = ['good', 'fine', 'great']
        response = random.choice(li)
        jarvis(f"I am {response}, thanks, how may I assist you?")
        t2s(f"I am {response}, thanks, how may I assist you?")
        Hibernating = True

    if re.search('whats up', res) and Hibernating == False :
        li = ['I am fantastic, thanks. What can I do for you?']
        response = random.choice(li)
        jarvis(f"{response}")
        t2s(f"{response}")
        Hibernating = True

    if re.search('your name|who are you', res) and Hibernating == False :
        jarvis("My name is JarvisAI, I am your personal assistant.")
        t2s("My name is JarvisAI, I am your personal assistant.")
        Hibernating = True

    if re.search('cool', res) and Hibernating == False :
        jarvis("I know right!")
        t2s("I know right!")
        Hibernating = True

    if re.search("your a bot|you a bot|you're a bot", res) and Hibernating == False :
        jarvis("No i'm not! ")
        t2s("No i'm not! ")
        Hibernating = True


    if re.search('what do you think of|do you like|whats your thought', res) and Hibernating == False :
        li = ['I think its good', 'Not too sure', 'I dont really like it']
        response = random.choice(li)
        jarvis(f"{response}")
        t2s(f"{response}")
        Hibernating = True

    if re.search('friend', res) and Hibernating == False :
        jarvis("I am also your friend!")
        t2s("I am also your friend")
        Hibernating = True

    if re.search('my name is', res) and Hibernating == False :
        my = res.replace("my", "", 1)
        nname = my.replace("name", "", 1)
        isst = nname.replace("is", "", 1)
        iss = isst.replace(" ", "", 1)
        name = iss
        namedata = open('data1s.bat', 'w')
        namedata.write(name)
        namedata.close()
        os.replace("data1s.bat", "data/data1s.bat")
        jarvis("Got it," + name)
        t2s("Got it," + name)
        Hibernating = True

    if re.search("what is my name|whats my name|what's my name", res) and Hibernating == False :
        try :
            heck = open('data/data1s.bat', 'r')
            for line in heck :
             nameload = line
            jarvis("Your name is " + nameload)
            t2s("Your name is " + nameload)
            Hibernating = True
            heck.close()
        except NameError:
            NameErno = True
        except FileNotFoundError:
            jarvis("You haven't told me your name.")
            t2s("You haven't told me your name.")
            Hibernating = True



    if re.search('play', res) and Hibernating == False :
        dict_sound = {
            'laugh': 'library/Crowd-laughing.mp3',
            'cat vibing': 'library/Cat_Vibing.mp3',
            'day and night' : 'library/day_n_nite_remix.mp3'
        }

        sound = res.split(' ', 1)[1]
        path = dict_sound.get(sound)
        if path is None:
         try:
            pathx = 'library/'
            pathz = res.replace("play", "", 1)
            pathy = pathz.replace(" ", "", 1)
            path = pathx+pathy+('.mp3')
            soundx = path.replace("library/", "", 1)
            sound = soundx.replace(".mp3", "", 1)
            jarvis('Playing: ' + sound)
            t2s('Playing: ' + sound)
            playsound.playsound(path)
            musicpath=False
            Hibernating = True
         except playsound.PlaysoundException :
             jarvis("Uh oh, I can't find the mp3 file.. Please check you have it.")
             t2s("Uh oh, I can't find the mp3 file.. Please check you have it.")
             Hibernating = True
        else:
            jarvis("Finding path..")
            print("Playing: " + sound)
            t2s('Playing: ' + sound)
            playsound.playsound(path)
            Hibernating = True

    if re.search('jarvis', res) and Hibernating == False :
        jarvis("Yes?")
        t2s("Yes?")

    if re.search('im bored', res) and Hibernating == False :
        jarvis("So am I, how about you ask me what I can do?")
        t2s("So am I, how about you ask me what I can do?")
        Hibernating = True

    if re.search('you are nice', res) and Hibernating == False :
        jarvis("Thank you, I appreciate it.")
        t2s("Thank you, I appreciate it.")
        Hibernating = True

    if res == "i'm bored" and Hibernating == False :
        jarvis("So am I, how about you ask me what I can do?")
        t2s("So am I, how about you ask me what I can do?")
        Hibernating = True

    if re.search('turn off|go away|i hate you|leave me alone|shutdown', res) and Hibernating == False :
        obj.shutdown()

    def cmds():
        li_commands = {
            "open websites" : "Example: 'open youtube",
            "time" : "Example: 'what time is it?'",
            "date" : "Example: 'what date is it?'",
            "launch applications" : "Example: 'launch chrome'",
            "tell me" : "Example: 'tell me about India'",
            "weather" : "Example: 'what weather/temperature in Mumbai?'",
            "news" : "Example: 'Show me news for today' ",
            "joke" : "Example: 'Tell me a joke!' ",
        }
        ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
     I can open websites for you, launch application and even make you laugh! See the list of commands-"""
        jarvis(ans)
        pprint.pprint(li_commands)
        t2s(ans)
        cmds()
        Hibernating = True

    if re.search('what can you do|what else can you do', res) and Hibernating == False :
        cmds()

    if res == 'help'  and Hibernating == False :
     jarvis("No problem, I'm at your service.")
     t2s("No problem, I'm at your service.")
     cmds()
