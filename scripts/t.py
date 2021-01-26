import os, wget, playsound
from download import download


# playsound.playsound('utils/wake_up.mp3')

url = 'https://raw.githubusercontent.com/Dipeshpal/Jarvis_AI/master/JarvisAI/JarvisAI/utils/wake_up.mp3'
download(url, "wake.mp3")

