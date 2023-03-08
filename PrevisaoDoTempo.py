"""

Previsão do tempo
Desenvolver um aplicativo de previsão do tempo que informe as condições climáticas em tempo real.

"""

import pyowm
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Dark')

owm = pyowm.OWM('9da1fe4fd35724a50deba5e284d914ee')

#layout from PysimpleGui with text, input and button
layout = [

[sg.Text("Where do you want to see the weather")],
[sg.Input(key='City')],
[sg.Button('See the weather', key='Button')],
]

#create the window with layout
window = sg.Window('Weather', layout)

#start the while to open the layout with 0 errors
while True:

    #i use print 1,2,3,4... to see where my code have an error

    eventos, valores = window.read()
    valor = valores['City']
    print("4")
    if eventos == sg.WINDOW_CLOSED:
        print("3")
        break
    print("5")
    if eventos == 'Button':
        print("2")
        observation = owm.weather_manager('City')
        w = observation.get_weather()

    if valores == "":
        sg.popup_ok('you didnt put any value')
        print('1')

    else:
        sg.popup_ok('The weather is ' + w)