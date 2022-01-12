import JarvisAI
import os
import re
import pprint
import random
import warnings

warnings.filterwarnings("ignore")
warnings.warn("second example of warning!")

obj = JarvisAI.JarvisAssistant(sync=True, token='71dd94xsxsxse48471ec7af2a733acfb', disable_msg=False,
                               load_chatbot_model=True, high_accuracy_chatbot_model=False,
                               chatbot_large=True, backend_tts_api='pyttsx3')


def t2s(text):
    obj.text2speech(text)


def start():
    while True:
        print("Say your AI name to activate")
        status, command = obj.hot_word_detect()
        print(status, command)
        if status:
            while True:
                # use any one of them
                print("Continue listening, say- 'stop listening to stop continue listening'")
                res = obj.mic_input()
                # res = obj.mic_input_ai(debug=True)
                res = res.lower()
                print("You said: " + res)

                if re.search("jokes|joke|Jokes|Joke", res):
                    joke_ = obj.tell_me_joke('en', 'neutral')
                    print(joke_)
                    t2s(joke_)

                elif re.search('setup|set up', res):
                    setup = obj.setup()
                    print(setup)

                elif re.search('google photos', res):
                    photos = obj.show_google_photos()
                    print(photos)

                elif re.search('local photos', res):
                    photos = obj.show_me_my_images()
                    print(photos)

                elif re.search('weather|temperature', res):
                    # city = res.split(' ')[-1]
                    # weather_res = obj.weather(city=city)
                    weather_res = obj.get_weather(res)
                    print(weather_res)
                    t2s(weather_res)

                elif re.search('news', res):
                    news_res = obj.news()
                    pprint.pprint(news_res)
                    t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
                    t2s(news_res[0])
                    t2s(news_res[1])

                elif re.search('tell me about', res):
                    topic = res[14:]
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    t2s(wiki_res)

                elif re.search('date', res):
                    date = obj.tell_me_date()
                    print(date)
                    print(t2s(date))

                elif re.search('time', res):
                    time = obj.tell_me_time()
                    print(time)
                    t2s(time)

                elif re.search('open', res):
                    domain = res.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    print(open_result)

                elif re.search('launch', res):
                    dict_app = {
                        'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                        'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
                    }

                    app = res.split(' ', 1)[1]
                    path = dict_app.get(app)
                    if path is None:
                        t2s('Application path not found')
                        print('Application path not found')
                    else:
                        t2s('Launching: ' + app)
                        obj.launch_any_app(path_of_app=path)

                elif re.search('hello|hi', res):
                    print('Hi')
                    t2s('Hi')

                elif re.search('how are you', res):
                    li = ['good', 'fine', 'great']
                    response = random.choice(li)
                    print(f"I am {response}")
                    t2s(f"I am {response}")

                elif re.search('your name|who are you', res):
                    print("I am your personal assistant")
                    t2s("I am your personal assistant")

                elif re.search('what can you do', res):
                    li_commands = {
                        "open websites": "Example: 'open youtube.com",
                        "time": "Example: 'what time it is?'",
                        "date": "Example: 'what date it is?'",
                        "launch applications": "Example: 'launch chrome'",
                        "tell me": "Example: 'tell me about India'",
                        "weather": "Example: 'what weather/temperature in Mumbai?'",
                        "news": "Example: 'news for today' ",
                    }
                    ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
                    I can open websites for you, launch application and more. See the list of commands-"""
                    print(ans)
                    pprint.pprint(li_commands)
                    t2s(ans)
                elif re.search('tech news', res):
                    obj.show_me_some_tech_news()

                elif re.search('tech videos', res):
                    obj.show_me_some_tech_videos()

                elif re.search(r"^add *.+ list$", res):
                    obj.create_new_list(res)

                elif re.search(r"^show *.+ list$", res):
                    obj.show_me_my_list()

                elif re.search(r"^delete *.+ list$", res):
                    obj.delete_particular_list(res)

                elif re.search("stop listening|stop", res):
                    break

                else:
                    chatbot_response = obj.chatbot_base(input_text=res)  # comment this line if you want to use chatbot large
                    # chatbot_response = obj.chatbot_large(input_text=res) # uncomment this line to use large model for heavy/complex tasks

                    print(chatbot_response)
                    t2s(chatbot_response)
        else:
            continue


if __name__ == "__main__":
    if not os.path.exists("configs/config.ini"):
        print(os.listdir())
        res = obj.setup()
        if res:
            print("Settings Saved. Restart your Assistant")
    else:
        start()
