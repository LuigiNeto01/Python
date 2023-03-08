from PySimpleGUI import PySimpleGUI as sg



sg.theme('Dark')

layout = [
    [sg.Text('Coloque o tempo em HORAS')],
    [sg.Input(key='input')],
    [sg.Radio("Minutos", "group 1",key='min', default=True),
     sg.Radio("Segundos", "group 1",key='Sec')],
    [sg.Text("CLIQUE PARA")],
    [sg.Button('Calcular')],
]

window = sg.Window('Conversor de HORAS', layout)

while True:

    eventos, valores = window.read()
    valor = valores['input']
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Calcular':
        
        alorada = valores['Sec']
        valorada = valores['min']

        if valor == '':
             sg.popup_ok('Você não colocou o valor em HORAS', title='Erro', keep_on_top=True)

        else: 

            if valorada == True:
                    
                      
                    rese = float(valor) * 60
                    sg.popup_ok('O resultado de ' + valor + ' horas pra MINUTOS é ' + str(rese), title='Resultado', keep_on_top=True)


            if alorada == True:
                     
                    res = float(valor) * 3600
                    sg.popup_ok('O resultado de ' + valor + ' horas pra SEGUNDOS é ' + str(res), title='Resultado', keep_on_top=True)

        
            






 