import JarvisAI
import os
import re
import pprint
import random
import warnings

warnings.filterwarnings("ignore")
warnings.warn("second example of warning!")


obj = JarvisAI.JarvisAssistant(sync=True, token='b848560382ba0d15819bc2f44ae2eb', disable_msg=False,
                               load_chatbot_model=False, high_accuracy_chatbot_model=False,
                               chatbot_large=False, backend_tts_api='pyttsx3')


def t2s(text):
    obj.text2speech(text)


def start():
    while True:
        # use any one of them
        print("Continue listening, \nsay- 'stop listening to stop continue listening'")
        res = obj.mic_input()
        # res = obj.mic_input_ai(debug=True)
        print(res)

        if re.search("jokes|joke|Jokes|Joke", res):
            joke_ = obj.tell_me_joke('en', 'neutral')
            print(joke_)
            t2s(joke_)

        if re.search('setup|set up', res):
            setup = obj.setup()
            print(setup)

        if re.search('google photos', res):
            photos = obj.show_google_photos()
            print(photos)

        if re.search('local photos', res):
            photos = obj.show_me_my_images()
            print(photos)

        if re.search('weather|temperature', res):
            city = res.split(' ')[-1]
            weather_res = obj.weather(city=city)
            print(weather_res)
            t2s(weather_res)

        if re.search('news', res):
            news_res = obj.news()
            pprint.pprint(news_res)
            t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
            t2s(news_res[0])
            t2s(news_res[1])

        if re.search('tell me about', res):
            topic = res[14:]
            wiki_res = obj.tell_me(topic, sentences=1)
            print(wiki_res)
            t2s(wiki_res)

        if re.search('date', res):
            date = obj.tell_me_date()
            print(date)
            print(t2s(date))

        if re.search('time', res):
            time = obj.tell_me_time()
            print(time)
            t2s(time)

        if re.search('open', res):
            domain = res.split(' ')[-1]
            open_result = obj.website_opener(domain)
            print(open_result)

        if re.search('launch', res):
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

        if re.search('hello|hi', res):
            print('Hi')
            t2s('Hi')

        if re.search('how are you', res):
            li = ['good', 'fine', 'great']
            response = random.choice(li)
            print(f"I am {response}")
            t2s(f"I am {response}")

        if re.search('your name|who are you', res):
            print("I am your personal assistant")
            t2s("I am your personal assistant")

        if re.search('what can you do', res):
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

        if re.search("stop listening|stop", res):
            break
        else:
            chatbot_response = obj.chatbot_base(input_text=res)
            print(chatbot_response)
            t2s(chatbot_response)


if __name__ == "__main__":
    if not os.path.exists("configs/config.ini"):
        res = obj.setup()
        if res:
            print("Settings Saved. Restart your Assistant")
    else:
        obj.jarvisai_configure_hand_detector(camera=0, detectionCon=0.7, maxHands=2,
                                             cam_display=True, cam_height=720, cam_width=1280)
        while True:
            try:
                fingers, hand_type, cv2, img, cap = obj.jarvisai_detect_hands()
                # print(fingers, hand_type)
                cv2.putText(img, 'Up four fingers of right hand to wake up assistant', (50, 200),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.imshow("img", img)
                cv2.waitKey(1)
                if fingers == [1, 1, 1, 1, 0] and hand_type == 'Right':
                    cv2.destroyAllWindows()
                    cap.release()
                    start()
                if fingers == [0, 1, 1, 1, 1] and hand_type == 'Left':
                    cv2.destroyAllWindows()
                    cap.release()
                    city = "Indore"
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    t2s(weather_res)
            except:
                obj.jarvisai_configure_hand_detector(camera=0, detectionCon=0.7, maxHands=2,
                                                     cam_display=True, cam_height=720, cam_width=1280)
