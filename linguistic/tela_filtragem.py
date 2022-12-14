# definição da tela responsável pela filtragem das variáveis sociais

import os.path  # importa biblioteca para manipular o caminho dos arquivos

from pathlib import Path 

import checagem as chk  # importa classe utilizada no processo de filtragem
import pandas as pd  # importa o pandas, biblioteca de data science
import PySimpleGUI as sg  # importa a biblioteca gráfica

pasta_atual = Path.cwd()


def montar_tela():   # definição da aparência e elementos da tela

    layout = [
        [
            sg.Text(
                'LinguisTic - Análise das variáveis sociais',
                font=(None, 20),
                text_color='Gold',
            )
        ],
        [
            sg.Text(
                'Escolha uma planilha Excel com dados de informantes ',
                font=(None, 20),
                text_color='Gold',
            ),
            sg.In(
                size=(30, 10),
                enable_events=True,
                key='escolher',
                font=(None, 15),
            ),
            sg.FileBrowse(
                button_text='Procurar',
                font=(None, 15),
                size=(16, None),
                initial_folder= '..\tests\planilhas',
            ),
        ],
        [
            sg.Text('Série:', font=(None, 20), text_color='Gold'),
            sg.Radio(
                '1º ano',
                'Anos',
                default=False,
                key='primeiro_ano',
                font=(None, 25),
                text_color='Gold',
            ),
            sg.Radio(
                '2º ano',
                'Anos',
                default=False,
                key='segundo_ano',
                font=(None, 25),
                text_color='Gold',
            ),
            sg.Radio(
                '3º ano',
                'Anos',
                default=False,
                key='terceiro_ano',
                font=(None, 25),
                text_color='Gold',
            ),
            sg.Radio(
                '4º ano',
                'Anos',
                default=False,
                key='quarto_ano',
                font=(None, 25),
                text_color='Gold',
            ),
        ],
        [
            sg.Text('Gênero:', font=(None, 20), text_color='Gold'),
            sg.Radio(
                'Feminino',
                'Gênero',
                default=False,
                key='feminino',
                font=(None, 20),
                text_color='Gold',
            ),
            sg.Radio(
                'Masculino',
                'Gênero',
                default=False,
                key='masculino',
                font=(None, 20),
                text_color='Gold',
            ),
            sg.Text('Outro:', font=(None, 20), text_color='Gold'),
            sg.Input(
                key='outro',
                default_text='',
                font=(None, 15),
                text_color='Gold',
            ),
        ],
        [
            sg.Text(
                'Procedência escolar:', font=(None, 20), text_color='Gold'
            ),
            sg.Radio(
                'Pública',
                'PE',
                default=False,
                key='publica',
                font=(None, 20),
                text_color='Gold',
            ),
            sg.Radio(
                'Privada',
                'PE',
                default=False,
                key='privada',
                font=(None, 20),
                text_color='Gold',
            ),
            sg.Radio(
                'Mista Pública',
                'PE',
                default=False,
                key='mista_publica',
                font=(None, 20),
                text_color='Gold',
            ),
            sg.Radio(
                'Mista Privada',
                'PE',
                default=False,
                key='mista_privada',
                font=(None, 20),
                text_color='Gold',
            ),
        ],
        [
            sg.Button(
                'Filtrar',
                key='filtrar',
                enable_events=True,
                disabled=False,
                font=(None, 15),
                size=(16, None),
            ),
            sg.Button('Sair', key='sair', font=(None, 15), size=(16, None)),
        ],
    ]

    return sg.Window(
        'Análise das variáveis sociais',
        layout,
        finalize=True,
        grab_anywhere=True,
        text_justification='center',
        element_justification='center',
    )


def ver_tabela(dataf):   # abre a visualização do dataframe filtrado
    cabecalhos = []
    data = []

    if (dataf.empty == False):
        data = dataf[0:].values.tolist()
        cabecalhos = list(dataf.columns)
    else:
        data.append('')

    layout = [
        [
            sg.Table(
                values=data,
                text_color='Gold',
                headings=cabecalhos,
                font='Helvetica',
                key='tabela',
                vertical_scroll_only=False,
                pad=(25, 25),
                display_row_numbers=False,
                auto_size_columns=True,
                num_rows=min(25, len(data)),
            )
        ],
        [
            sg.Button(
                'Salvar planilha',
                key='salvar',
                font=(None, 15),
                size=(16, None),
            ),
            sg.Input(key='nome_arquivo', default_text=''),
        ],
    ]

    return sg.Window(
        'Tabela de dados dos informantes',
        layout,
        finalize=True,
        grab_anywhere=True,
        resizable=True,
        element_justification='center',
    )


def escolher(valor_input):   # abre o arquivo selecionado
    arquivo = valor_input
    
    if (os.path.realpath(arquivo) != ''):
        caminho_arquivo = os.path.realpath(arquivo)
        df = pd.read_excel(caminho_arquivo)
        return df
    else:
        caminho_arquivo = []
        return ''


def filtrar(dataf, tela):   # filtra o dataframe de acordo com o parâmetros
    window2 = tela
    df = dataf
    resultado = 'Nenhum dado encontrado'
    values = window2.Read()

    testes_ano = []
    testes_ano.append(values['primeiro_ano'])
    testes_ano.append(values['segundo_ano'])
    testes_ano.append(values['terceiro_ano'])
    testes_ano.append(values['quarto_ano'])

    ano = chk.check_ano(testes_ano)

    testes_genero = []
    testes_genero.append(values['feminino'])
    testes_genero.append(values['masculino'])

    genero = chk.check_g(testes_genero)

    testes_procedencia = []
    testes_procedencia.append(values['publica'])
    testes_procedencia.append(values['privada'])
    testes_procedencia.append(values['mista_publica'])
    testes_procedencia.append(values['mista_privada'])

    proced = chk.check_pe(testes_procedencia)

    contadores = []
    contadores = [0, 0, 0]

    for ocorrencia in testes_ano:
        if ocorrencia:
            contadores[0] = contadores[0] + 1
    for ocorrencia in testes_genero:
        if ocorrencia:
            contadores[1] = contadores[1] + 1
    for ocorrencia in testes_procedencia:
        if ocorrencia:
            contadores[2] = contadores[2] + 1
    # 1
    if (contadores[0] > 0) and (contadores[1] == 0) and (contadores[2] == 0):
        n_df = df.loc[(df['Escolaridade'] == ano)]
        resultado = n_df
    # 2
    elif (contadores[1] > 0) and (contadores[0] == 0) and (contadores[2] == 0):
        n_df = df.loc[(df['Gênero'] == genero)]
        resultado = n_df
    # 3
    elif (contadores[2] > 0) and (contadores[0] == 0) and (contadores[1] == 0):
        n_df = df.loc[(df['Procedência escolar'] == proced)]
        resultado = n_df
    # 1e2
    elif (contadores[0] > 0) and (contadores[1] > 0) and (contadores[2] == 0):
        n_df = df.loc[(df['Escolaridade'] == ano) & (df['Gênero'] == genero)]
        resultado = n_df
    # 2e3
    elif (contadores[1] > 0) and (contadores[2] > 0) and (contadores[0] == 0):
        n_df = df.loc[
            (df['Gênero'] == genero) & (df['Procedência escolar'] == proced)
        ]
        resultado = n_df
    # 1e2
    elif (contadores[0] > 0) and (contadores[1] > 0) and (contadores[2] == 0):
        n_df = df.loc[(df['Escolaridade'] == ano) & (df['Gênero'] == genero)]
        resultado = n_df
    # 1e3
    elif (contadores[0] > 0) and (contadores[2] > 0) and (contadores[1] == 0):
        n_df = df.loc[
            (df['Escolaridade'] == ano) & (df['Procedência escolar'] == proced)
        ]
        resultado = n_df
    # 123
    elif (contadores[0] > 0) and (contadores[2] > 0) and (contadores[1] > 0):
        n_df = df.loc[
            (df['Escolaridade'] == ano)
            & (df['Procedência escolar'] == proced)
            & (df['Gênero'] == genero)
        ]
        resultado = n_df
    # 2(outro)
    elif (
        (contadores[1] == 0) and (contadores[0] == 0) and (contadores[2] == 0)
    ):
        if values['outro'] != '':
            n_df = df.loc[(df['Gênero'] == values['outro'])]
            resultado = n_df
    # 1e2(outro)
    elif (contadores[0] > 0) and (contadores[1] == 0) and (contadores[2] == 0):
        if values['outro'] != '':
            n_df = df.loc[
                (df['Escolaridade'] == ano) & (df['Gênero'] == values['outro'])
            ]
            resultado = n_df
    # 2e3(outro)
    elif (contadores[1] == 0) and (contadores[2] > 0) and (contadores[0] == 0):
        if values['outro'] != '':
            n_df = df.loc[
                (df['Gênero'] == values['outro'])
                & (df['Procedência escolar'] == proced)
            ]
            resultado = n_df
    # 123(outro)
    elif (contadores[0] > 0) and (contadores[2] > 0) and (contadores[1] == 0):
        if values['outro'] != '':
            n_df = df.loc[
                (df['Escolaridade'] == ano)
                & (df['Procedência escolar'] == proced)
                & (df['Gênero'] == values['outro'])
            ]
            resultado = n_df

    window2['primeiro_ano'].update(value=False)
    window2['segundo_ano'].update(value=False)
    window2['terceiro_ano'].update(value=False)
    window2['quarto_ano'].update(value=False)
    window2['masculino'].update(value=False)
    window2['feminino'].update(value=False)
    window2['publica'].update(value=False)
    window2['privada'].update(value=False)
    window2['mista_privada'].update(value=False)
    window2['mista_publica'].update(value=False)

    return resultado


def salvar(valor_input, dataf):   # salva o dataframe filtrado

    n_df = dataf

    nome = valor_input

    if nome != '':
        n_df.to_excel(
            f'..\saidas\planilhas\{nome}.xlsx', sheet_name='filtrado'
        )
    else:
        n_df.to_excel(
            '..\saidas\planilhas\arquivo_modificado.xlsx',
            sheet_name='filtrado',
        )

    sg.popup('ARQUIVO SALVO', title='Confirmação')
