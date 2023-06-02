# J.A.R.V.I.S
# It is an ai dekstop assitance which will let you perform many task just by saying it
#Note-> this code is applicable for windows

import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
# from config import apikey
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
chatStr=""
def ai(prompt):
    global chatStr
    openai.api_key ="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"
    text=f"Open AI response for prompt:{prompt}\n******\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    ak = response["choices"][0]["text"]
    speaker.Speak(ak)
    print(ak)

    chatStr +=f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"User said :{query}")
            return query
        except Exception as e:
            return "Some error occured sorry from jarvis"
a="HI I AM JARVIS"
speaker.Speak(a)
while True:
    print("Listening.....")
    query=takeCommand()
    sites=[["Youtube","https://www.youtube.com/"],["Google","https://www.google.com/"],
           ["Github","https://github.com/"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            Y = f"Opening {site[0]} sir"
            speaker.Speak(Y)
            webbrowser.open(site[1])
    if "the time" in query:
        strfTime=datetime.datetime.now().strftime("%H %M ")
        a=f"Sir the time is{strfTime}"
        speaker.Speak(a)
    accessibilities = [["desktop", r"C:\Users\gamer\Desktop"],
                       ["camera", r"C:\Users\gamer\Desktop\accesibilities\Camera.lnk"],
                       ["calculator",r"C:\Users\gamer\Desktop\accesibilities\Calculator.lnk"]]
    for accessibilitie in accessibilities:
        if f"open {accessibilitie[0]}" in query:
            os.startfile(accessibilitie[1])
            Y = f"Opening {accessibilitie[0]} sir"
            speaker.Speak(Y)
    else:
        ai(query)
