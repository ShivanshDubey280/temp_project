from urllib.request import urlopen
import urllib.parse
import webbrowser
from sys import platform
import os

if platform == "linux" or platform == "linux2":
    chrome_path = '/usr/bin/google-chrome'

elif platform == "darwin":
    chrome_path = 'open -a /Applications/Google\ Chrome.app'

elif platform == "win32":
    chrome_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
else:
    print('Unsupported OS')
    exit(1)

webbrowser.register('brave', None, webbrowser.BackgroundBrowser(chrome_path))


def youtube(textToSearch):
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.get('brave').open_new_tab(url)


if __name__ == '__main__':
    youtube('any text')
