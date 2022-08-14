# tela responsável pela inserção dos códigos sociais

import os.path  # importa biblioteca para manipular o caminho dos arquivos

import pandas as pd  # importa o pandas, biblioteca de data science
import PySimpleGUI as sg  # importa a biblioteca gráfica


def quinta_tela():   # definição da aparência e elementos da tela
    layout = [
        [
            sg.Text(
                'LinguisTic - Inserção do código social',
                font=(None, 25),
                text_color='Gold',
            )
        ],
        [
            sg.Text(
                'Escolha uma planilha de codificação linguística ',
                font=(None, 25),
                text_color='Gold',
            ),
            sg.In(
                size=(25, 1),
                enable_events=True,
                key='escolher4',
                font=(None, 15),
            ),
            sg.FileBrowse(
                button_text='Procurar',
                font=(None, 15),
                size=(16, None),
                initial_folder='linguistic/tests/planilhas',
            ),
        ],
        [
            sg.Text(
                'Escolha uma planilha com códigos sociais ',
                font=(None, 25),
                text_color='Gold',
            ),
            sg.In(
                size=(25, 1),
                enable_events=True,
                key='escolher5',
                font=(None, 15),
            ),
            sg.FileBrowse(
                button_text='Procurar',
                font=(None, 15),
                size=(16, None),
                initial_folder='linguistic/tests/planilhas',
            ),
        ],
        [
            sg.Text(
                'Escolha um informante ',
                visible=False,
                key='txt',
                font=(None, 25),
                text_color='Gold',
            ),
            sg.Listbox(
                values=['Insira a planilha'],
                select_mode='single',
                size=(100, 10),
                enable_events=True,
                visible=False,
                no_scrollbar=False,
                key='lista',
            ),
        ],
        [sg.Multiline(size=(50, 10), auto_size_text=True, key='out')],
        [
            sg.Button(
                'Inserir',
                key='colocar_cod',
                enable_events=True,
                disabled=False,
                font=(None, 15),
                size=(16, None),
            ),
            sg.Button(
                'Salvar planilha',
                key='salvar4',
                font=(None, 15),
                size=(16, None),
            ),
            sg.Input(key='nome_arquivo3', default_text='', font=(None, 15)),
            sg.Button('Sair', key='sair', font=(None, 15), size=(16, None)),
        ],
    ]
    return sg.Window(
        'Inserir código social',
        layout,
        finalize=True,
        grab_anywhere=True,
        text_justification='center',
        element_justification='center',
        resizable=True,
    )


def escolher(valor_input):   # abre o arquivo selecionado
    arquivo = valor_input
    try:
        caminho_arquivo = os.path.realpath(arquivo)
        df = pd.read_excel(caminho_arquivo)
        return df

    except:
        caminho_arquivo = []


def inserir(valor_lista):
    a = str(valor_lista)
    novelo = a.split()
    ultimo = len(novelo) - 1
    cod = novelo[ultimo]

    if cod[0] == '=':
        cod = ' ' + cod

    return cod


def salvar(valor_input, tela, dataf):   # salva a planilha com códigos sociais
    window5 = tela
    n_df = dataf

    button, values = window5.Read()
    nome = valor_input

    if nome != '':
        n_df.to_excel(
            f'/linguistic/saidas/planilhas/{nome}.xlsx',
            sheet_name='com códigos sociais',
        )
    else:
        n_df.to_excel(
            'linguistic/saidas/planilhas/tabela_linguistica_com_cod_soc.xlsx',
            sheet_name='com códigos sociais',
        )

    sg.popup('ARQUIVO SALVO', title='Confirmação')
