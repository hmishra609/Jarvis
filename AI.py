import wolframalpha

import wikipedia
import PySimpleGUI as sg
client = wolframalpha.Client("YYWJLH-9TXYV568PJ")

import pyttsx3
engine = pyttsx3.init()





sg.theme('Dark Green 5')
layout = [  [sg.Text('Tell me how can i help!'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]


window = sg.Window('Jarvis', layout)
engine.say("Hello boss")
engine.runAndWait()
while True:

    event, values = window.read()

    if event in (None, 'Cancel'):
        break

    try:
        wolf_res=next(client.query(values[0]).results).text
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wolf_res)
        engine.say(wiki_res)
        sg.PopupNonBlocking('Wolframe Result:',wolf_res,'Wikipedia result',wiki_res)
    except Exception:
            wolf_res = next(client.query(values[0]).results).text
            engine.say(wolf_res)
            sg.PopupNonBlocking('Wolframe Result:',wolf_res)

    except:
            wiki_res = wikipedia.summary(values[0], sentences=2)
            engine.say(wiki_res)
            sg.PopupNonBlocking('Wikipedia result',wiki_res)

    engine.runAndWait()


window.close()