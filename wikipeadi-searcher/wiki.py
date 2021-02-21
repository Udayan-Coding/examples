import sys
import wikipedia
import webbrowser

command = sys.argv

try:
    if command[1]:
        # get info about input
        result = wikipedia.page(command[1])
        # using the webbrowser
        # get()
        handler = webbrowser.get()
        handler.open(result.url)
except:
    print("No arguments were passed")
