from art import art
import time
import os
import webbrowser
import pyjokes
import requests
import json
import random


def main():
    draw_LOGO()
    heelp()
    while True:
        try:
            print("What can I help You With?")
            text = input(">>>")
            text = text.lower()
            if 'reminder' in text:
                set_reminder()
            elif 'help' in text:
                heelp()
            elif 'weather' in text:
                weather()
            elif 'news' in text:
                NewsFromBBC()
            elif "joke" in text:
                jokes("all")
            elif 'browser' in text:
                open_browser()
            elif 'gpt' in text:
                gpt()
            elif 'music' in text:
                music()
            elif 'calc' in text:
                calc()
            elif "chuck" in text:
                jokes("chuck")
            elif 'word' in text:
                word()
            elif 'note' in text:
                note()
            elif 'study' in text:
                folder_path = os.path.join(os.getcwd(), "C:\Users\Utkrishth\Ebooks")
                os.startfile(folder_path)
                webbrowser.open_new_tab('https://open.spotify.com/')
                Timer(50)
            elif 'game' or "fun" in text:
                game()
            else:
                print("Sorry please try again")
        except (ValueError, SyntaxError):
            print("Wrong Input Method... Please Retry")


def Timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print("Time remaining: {} seconds".format(remaining_time))
        time.sleep(1)  # Sleep for 1 second
    print("Time's up! Good job studying.")


def heelp():
    l = ['reminder', 'Chat_GPT', 'Game', 'Study', 'Word', 'Note', 'Calculator', 'Music', 'Joke', 'Chuck Norris Joke', 'Open Browser', 'News', 'weather']
    print("I can", l)


def game():
    print (":::___LETS HAVE SOME FUN___:::")
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    number = random.randint(1, 100)
    guess = 0
    tries = 0

    while guess != number:
        guess = int(raw_input("Enter your guess: "))
        tries += 1

        if guess < number:
            print("Too low! Guess again.")
        elif guess > number:
            print("Too high! Guess again.")
        elif guess == 'no':
            print"Ok"
        else:
            print("Congratulations, you guessed the number!")
            print("It took you", tries, "tries.")


def open_browser():
    url = 'https://www.google.com'
    webbrowser.open(url)


def draw_LOGO():
    art()
    print(" SSSSS   III  RRRRRR   III   UU   UU   SSSSS")
    print("SS       III  RR   RR  III   UU   UU  SS ")
    print(" SSSSS   III  RRRRRR   III   UU   UU   SSSSS")
    print("     SS  III  RR  RR   III   UU   UU       SS")
    print("SSSSS    III  RR   RR  III    UUUUU    SSSSS\n")


def NewsFromBBC():
    print("British Broadcasting Corporation\n")

    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        news = i + 1, results[i]
        print(news)


def weather():
    response = requests.get('https://api.weatherapi.com/v1/current.json?key=2f6908fd7ba5426799544701233004&q=Gorakhpur')
    weather_data = json.loads(response.content)
    temperature = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']

    print 'The temperature in {} is {} degrees Celsius and the condition is {}'.format("Your City", temperature,
                                                                                       condition)


def jokes(j):
    my_joke = pyjokes.get_joke(language="en", category=j)
    print(my_joke)


def gpt():
    url = 'https://chat.openai.com/?model=text-davinci-002-render'
    webbrowser.open(url)


def music():
    webbrowser.open('https://open.spotify.com/')


def set_reminder():
    print("What shall I remind you about?")
    remind = str(input())
    print("In how many minutes?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    print(remind)


def calc():
    import subprocess
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')


def word():
    import subprocess
    subprocess.Popen('C:\\Windows\\System32\\write.exe')


def note():
    import subprocess
    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')


main()