# definição da tela principal, que dá acesso às outras telas

import PySimpleGUI as sg  # importa a biblioteca gráfica


def telaPrincipal():   # definição da aparência e elementos da tela

    layout = [
        [
            sg.Text(
                'Bem-vindo!',
                size=(20, 0),
                justification='center',
                font=(None, 25),
                text_color='Gold',
            )
        ],
        [
            sg.Text(
                'LinguisTic',
                size=(20, 0),
                justification='center',
                font=(None, 25),
                text_color='Gold',
            )
        ],
        [
            sg.Text(
                'Escolha uma função:',
                size=(20, 0),
                justification='center',
                font=(None, 25),
                text_color='Gold',
            )
        ],
        [
            sg.Button(
                'Selecionar informantes',
                key='analisar_vs',
                font=(None, 15),
                size=(16, None),
            ),
            sg.Button(
                'Codificar \n variáveis sociais',
                key='cod_vs',
                font=(None, 15),
                size=(16, None),
            ),
            sg.Button(
                'Inserir \n código social',
                key='insert_cod',
                font=(None, 15),
                size=(16, None),
            ),
            sg.Button(
                'Analisar \n variáveis linguísticas',
                key='analisar_vl',
                font=(None, 15),
                size=(17, None),
            ),
        ],
        [sg.Button('Sair', key='sair', font=(None, 15))],
    ]
    return sg.Window(
        'LinguisTic',
        layout,
        finalize=True,
        grab_anywhere=True,
        text_justification='center',
        element_justification='center',
    )
