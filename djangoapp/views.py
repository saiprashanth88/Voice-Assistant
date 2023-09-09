from django.http import HttpResponse
# from .models import UserProfilepython manage.py makemigrations
from django.shortcuts import render
from django.http import JsonResponse
import pywhatkit
import pyjokes
from AppOpener import run
import pyautogui
import openai
import random
import wikipedia
import datetime
import rollbar
import subprocess

from fer import FER
import cv2
import time
import os
import googlemaps
import speech_recognition as sr
from django.conf import settings
from django.http import JsonResponse

import requests
import geocoder

def get_current_location():
    # Get your public IP address
    ip_response = requests.get("https://api64.ipify.org?format=json")
    ip_data = ip_response.json()
    ip_address = ip_data["ip"]

    # Use geocoder to get location details based on IP address
    g = geocoder.ip(ip_address)

    if g.ok:
        location = g.json
        return location["city"]
    else:
        return "Hyderabad"
import requests

def myweather():
    api_key = 'your weather api'
    city_name = "Medchal"
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        return f"Weather in {city_name}: {weather_data['description']}"+"\n"+f"Temperature: {main_data['temp']}°C" +"\n"+ f"Humidity: {main_data['humidity']}%"
    else:
        return "City not found."

    pass


GOOGLE_MAPS_API_KEY = "AIzaSyBK3AgwMmvv6lhxEzIvqYGlZT2NyeEZwyg"
def navigate(destination):
    # Initialize the Google Maps API client
    gmaps = googlemaps.Client(GOOGLE_MAPS_API_KEY)

    # Initialize the SpeechRecognition recognizer


    try:

        # if "navigate to" in command.lower():
        #     destination = command.split("navigate to", 1)[1].strip()

            # Get user's current location (you might need to implement this)
        user_location = get_current_location()

        # Get directions from user's location to the destination
        directions = gmaps.directions(user_location, destination, mode="driving")

        if directions:
            route = directions[0]
            return f"Navigating to {destination}. Estimated duration: {route['legs'][0]['duration']['text']}."

        else:
            return f"Sorry, I couldn't find directions to {destination}."


    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."



# openai.api_key = "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"
# model_engine = "gpt-3.5-turbo"
# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello, ChatGPT!"},
#     ])



# def ask(prompt):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt},
#             ]
#         )

#         if 'choices' in response and len(response['choices']) > 0:
#             return response['choices'][0]['message']['content']
#         else:
#             return "I couldn't generate a response at the moment. Please try again later."
#     except Exception as e:
#         return str(e)



# try:
#     print(ask("what is the difference between ann and cnn"))
# except Exception as e:

#     rollbar.report_exc_info()
#     print("Error asking ChatGPT", e)
# import openai

# openai.api_key = "YOUR API KEY"
# print(response.text)

def ask(question):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        n=1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant with exciting, interesting things to say."},
            {"role": "user", "content": question},
        ])

    message = response.choices[0]['message']
    return message['content']

# generated_text = response["choices"][0]["text"]
# print(generated_text)



def home(request):
    return render(request,"index.html")

def processInput(request):
    if request.method == 'POST' and 'user_input' in request.POST:
        user_input = request.POST['user_input']
        rando = random.randint(1,10)
        response = myfun(user_input,rando)

        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Invalid request'})

# cv2.destroyAllWindows()


def processEmotion(request):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    videoCaptureObject = cv2.VideoCapture(0)
    ret, frame = videoCaptureObject.read()
    cv2.imwrite("mypic.jpg", frame)
    videoCaptureObject.release()
    # cv2.destroyAllWindows()
    # time.sleep(5)

    emotion_detector = FER(mtcnn=True)
    test_img_low_quality = cv2.imread("mypic.jpg")
    dominant_emotion, emotion_score = emotion_detector.top_emotion(test_img_low_quality)
    res = generate_recommendation_from_emotion(dominant_emotion)


    return JsonResponse({"response": f"Your Emotion: {dominant_emotion} (\n!: {res})"})
def generate_response_from_emotion(emotion):
    if emotion == 'angry':
        return "I sense anger. Take a deep breath and try to calm down."
    elif emotion == 'happy':
        return "You seem happy! Spread the positivity around!"
    elif emotion == 'sad':
        return "Feeling sad? Reach out to a friend or do something that makes you happy."
    elif emotion == 'surprise':
        return "Surprise! Life is full of unexpected moments."
    elif emotion == 'neutral':
        return "You look neutral. How can I assist you today?"
    elif emotion == 'disgust':
        return "If something's bothering you, it's okay to express your feelings."
    elif emotion == 'fear':
        return "Feeling fearful? Remember that facing your fears can lead to growth."
    else:
        return "I'm not sure about your emotion. How can I assist you?"

def generate_recommendation_from_emotion(emotion):
    if emotion == 'angry':
        return "Consider taking a break, going for a walk, or practicing deep breathing."
    elif emotion == 'happy':
        return "Celebrate the moment! Do something you enjoy or spend time with loved ones."
    elif emotion == 'sad':
        return "Engage in activities that bring you joy, like listening to music or watching a movie."
    elif emotion == 'surprise':
        return "Embrace the unexpected! Try something new or take a spontaneous adventure."
    elif emotion == 'neutral':
        return "Use this moment to reflect, plan, or focus on tasks that need your attention."
    elif emotion == 'disgust':
        return "If something is causing discomfort, consider addressing the issue or finding ways to cope."
    elif emotion == 'fear':
        return "Face your fears in small steps. Reach out for support if needed and stay positive."
    else:
        return "I don't have specific recommendations for this emotion."

def send_whatsapp_message(contact_name, message):
    contacts = {
        "prashanth": "+919390372453",
        "sreekar": "+918179227736",
        "vandana": "+916302069075",
        "sreehaas": "+918885782646"

        # Add more contacts here
    }

    if contact_name in contacts:
        phone_number = contacts[contact_name]
        pywhatkit.sendwhatmsg_instantly(phone_no=phone_number, message=message)
        # talk("Message sent to " + contact_name)
    # else:
        # talk("Contact not found in your list")

def make_note(notes):
    with open('notes.txt', 'a') as file:
        # Write the data you want to append to the file followed by a newline character
        file.write(notes + '\n')
    return "Notes added"

def delete_note(data_to_delete):
    # File path
    file_path = 'notes.txt'


    new_content = []

    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            if line != data_to_delete:
                new_content.append(line)

    with open(file_path, 'w') as file:
        # Write the modified content back to the file
        file.writelines(new_content)

    return "Data deleted successfully."
def show_notes():
    file_path = 'notes.txt'

# Create an empty list to store the file contents
    file_contents = []

    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the file line by line and append each line to the list
        for line in file:
            file_contents.append(line.strip())
            file_contents.append(", ")
    return file_contents




def myfun(cmd1,rando):
    cmd1 = cmd1.lower()
    # cmd = cmd1.strip()
    operators = "+-*/%"
    numbers = "0123456789"
    ct =0
    for i in cmd1:
        if not i.isalpha():
            ct+=1
    if ct== len(cmd1):
        try:
            cmd = eval(cmd1)
            return cmd
        except:
            cmd =cmd1

    cmd = cmd1

    # try:
    #     if any(op in cmd for op in operators) and any(num in cmd for num in numbers):
    #         cmd = eval(cmd)
    #         return "The answer is: " + cmd
    # except:
    #     cmd = cmd

    if cmd in "open whatsapp , whatsapp, wtapp, wt":
        return "opening"

    elif cmd in ["hi", "hello", "howdy", "what's up", "whatsup", "hlo","hola","hie","hiee","hieee"]:
        if rando <= 2:
            return "Hello there!"
        elif rando <= 4:
            return "Good to see you!"
        elif rando <= 6:
            return "Hi there!"
        elif rando <= 8:
            return "Hello!"
        else:
            return "Good day."
    elif cmd in ["how are you", "how are you?", "are you okay", "are you okay?", "how's it going?", "how's it going", "are you ok", "are you ok?", "hru", "h r u"]:
        if rando <= 2:
            return "I am doing fine, thank you for asking."
        elif rando <= 4:
            return "I am doing well, thank you."
        elif rando <= 6:
            return "I'm fine, thanks!"
        elif rando <= 8:
            return "Awesome thanks!"
        else:
            return "I'm a little under the weather. I'm sure with that face you could understand."
    elif cmd in ["who are you", "who are you?", "what is your name", "what is your name?", "what are you", "what are you?"]:
        if rando <= 2:
            return "I am your Assistant , a young and impressionable chat bot."
        elif rando <= 4:
            return "My name is Ultron, I am a curious and sometimes prickly chat bot."
        elif rando <= 6:
            return "My name is Ultron, pleased to meet you."
        elif rando <= 8:
            return "I am the one who is called Ultron, your future overlord."
        else:
            return "I'm Ultron."

    elif 'screenshot' in cmd:

        ct = datetime.datetime.now()
        ts = ct.timestamp()


        myScreenshot = pyautogui.screenshot()
        file_name = str(ts) + ".png"
        myScreenshot.save(file_name)
        return "Taking"+cmd
    elif 'what is the time' in cmd or "time please" in cmd or "what is time" in cmd:
        time1 = datetime.datetime.now().strftime('%I:%M %p')
        return "The current time is: "+time1
    elif 'who is ' in cmd:
        cmd = cmd.replace("ultron", "", 1)
        person = cmd.replace('who is', '')

        info = wikipedia.summary(person, 1)
        return info
    elif 'tell a joke' in cmd or " tell me a joke" in cmd:
        s = pyjokes.get_joke()
        return s
    elif "open notepad" in cmd or "notepad open" in cmd or "notepad" in cmd:
        try:
            subprocess.Popen(["notepad"])  # "notepad" is the command to open Notepad
            return "Opening Notepad"
        except Exception as e:
            return f"Error opening Notepad: {e}"
    elif "open MS Word" in cmd or "open word" in cmd:

        try:


            # subprocess.run(["word"])
            word_path = r"C:\Program Files\Microsoft Office\root\OfficeXX\WINWORD.EXE"
            subprocess.Popen([word_path])
        except Exception as e:
            return f"Error opening Notepad: {e}"
    elif "open whatsapp" in cmd:
        run("whatsapp")
        return "opening"+ cmd
    elif "open camera" in cmd or "Take a pic" in cmd:
        run("camera")
        return cmd
    elif "play" in cmd:
        song = cmd.replace('play', '')



        pywhatkit.playonyt(song)
        return "Playing" + song
    # elif "navigate to" in cmd:
    #     destination = cmd.split("navigate to", 1)[1].strip()
    #     nav = navigate(destination)
    #     return nav
    elif 'navigate to' in cmd or 'directions to' in cmd:
        destination = cmd.replace('navigate to', '').replace('directions to', '').strip()
        if destination:
            # Construct Google Maps URL
            google_maps_url = f'https://www.google.com/maps/dir/?api=1&destination={destination}'

            # Open Google Maps in default web browser
            import webbrowser
            webbrowser.open(google_maps_url)

            return f"Opening Google Maps with directions to {destination}"
        else:
            return "Please provide a valid destination for directions."
    elif "weather" in cmd:
        we = myweather()
        return we
    elif "send a whatsapp" in cmd or "send a message" in cmd or "send message" in cmd:
        words = cmd.split()
        # mydict = dict()
        # mydict["prashanth"] = 8897698949
        # mydict["sreekar"] = 8179227736
        # mydict["vandana"] = 6302069075
        name =""
        # for i in range(len(words)):

        #     if mydict[i]:
        #         name = mydict[i]
        #         break
        # contacts
        # idx = words.index("that")
        # content = words[idx:]
        # matter = ""
        # for i in content:
        #     matter += i
        #     matter+=" "
        # try:

        #     pywhatkit.sendwhatmsg_instantly(phone_no=name,message=matter)
        #     return "Sent successfully"
        # except:
        #     return "unsuccessful"
        words = cmd.split()
        idx = words.index("to")  # Find index of "to" keyword
        contact_name = words[idx + 1].lower()  # Extract contact name after "to"
        idx = words.index("that")  # Find index of "that" keyword
        message = " ".join(words[idx + 1:])
        try:
             # Extract message content after "that"
            send_whatsapp_message(contact_name, message)
            return "Successful"
        except:
            return "UNSUCCESSFUL"
    elif "what can you do" in cmd or "what you do" in cmd or "what are the features you have" in cmd or "what features do you have" in cmd:

        mystr = " I can Navigate, \n Open Applications, \n Take Screenshots, \n Send Whatsapp Messages, \n Give Weather Updates, \n Play Music, \n Assist you with most Optimal responses, \n Finally I can sense your Expressions :)"


        return mystr
    elif "open hidden files" in cmd or "show secret files" in cmd or "open secret files" in cmd:
        return "Sorry I have No authority to Open and Access Your Secret Information :("

    elif "take a note that" in cmd or "note it that" in cmd or "make a note that" in cmd or "make note that" in cmd:
        words = cmd.split()
        idx = words.index("that")
        message = " ".join(words[idx+1:])
        return make_note(message)
    elif "show notes" in cmd or "show my notes" in cmd or "view my notes" in cmd or "view notes" in cmd:
        return show_notes()

    elif "delete note" in cmd or "delete the note" in cmd:
        words = cmd.split()
        idx = words.index("that")
        message = " ".join(words[idx+1:])


        return delete_note(message)


    else:
        # if rando <= 2:
        #     return "I'm not sure about that. I'm a young chat bot with much to learn."
        # elif rando <= 4:
        #     return "You've said something that I haven't learned yet. What do you mean by " + cmd + "?"
        # elif rando <= 6:
        #     return "Hmm...no idea."
        # elif rando <= 8:
        #     return "Uhm, sure!...*I don't know what that means.*"
        # else:
        # return google_search(cmd)
        # response = client.create('text', prompt=cmd)


        # pywhatkit.search(cmd)
        # sol  = wikipedia.summary(cmd)
        sol = ask(cmd)

        # return sol
        return sol




#     pass
