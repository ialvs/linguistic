# define a tela responsável por inserir os códigos sociais numa tabela

import os.path  # importa biblioteca para manipular o caminho dos arquivos

import pandas as pd  # importa o pandas, biblioteca de data science
import PySimpleGUI as sg  # importa a biblioteca gráfica
from numpy import string_

colunas = [
    'Nome',
    'Sobrenome',
    'Data de nascimento',
    'Faixa etária',
    'Gênero',
    'Escolaridade',
    'Ensino Superior (indique o semestre)',
    'Turma',
    'Ano de entrada',
    'Naturalidade',
    'Localidade em que habita',
    'Procedência escolar',
    'Escolaridade do pai',
    'Escolaridade da mãe',
    'Naturalidade do pai',
    'Naturalidade da mãe',
    'Ocupação do pai',
    'Ocupação da mãe',
    'Leitura diária de mídias impressas',
    'Tempo médio diário de leitura de mídias impressas',
    'Meios de exposição diária a mídias audiovisuais',
    'Programa(s) preferidos',
    'Tempo médio diário de exposição às mídias audiovisuais',
    'Tempo médio diário de exposição à internet',
    'Site ou Rede Social mais acessado(a)',
    'Pratica alguma religião? Se sim, qual?',
    'Gêneros de leitura habitual',
    'Tempo médio diário de leitura literária ficcional',
    'Gênero literário favorito',
    'Autor literário preferido',
    'Uso da escrita',
    'Estuda outra língua? Se sim, qual?',
    'Participação em atividades complementares de leitura, escrita e produção textual',
]   # colunas do dataframe utilizado na pesquisa

simbolos = [
    ' =',
    '-',
    '|',
    '+',
    'F',
    'M',
    '1',
    '2',
    '3',
    '4',
    '5',
    'A',
    'N',
    'D',
    'C',
    'c',
    'H',
    'h',
    '>',
    '<',
    '"',
    'u',
    'v',
    'U',
    'V',
    'z',
    'Z',
    '_',
    '%',
    'e',
    'E',
    '&',
    'g',
    'G',
    'j',
    'J',
    'l',
    'L',
    '#',
    '~',
    '^',
    '}',
    '{',
    '!',
    '?',
    'Ç',
    'ç',
    '@',
    '$',
    '[',
    ']',
    ',',
    ':',
    ';',
    's',
    'S',
    'y',
    'Y',
    't',
    'T',
    'r',
    'R',
    'q',
    'Q',
    'O',
    'o',
    'k',
    'K',
    'b',
    'B',
]   # símbolos utilizados para codificar as colunas do dataframe


def quarta_tela():   # definição da aparência e elementos da tela
    layout = [
        [
            sg.Text(
                'LinguisTic - Codificação das variáveis sociais',
                font=(None, 25),
                text_color='Gold',
            )
        ],
        [
            sg.Text(
                'Escolha uma planilha Excel ',
                font=(None, 25),
                text_color='Gold',
            ),
            sg.In(
                size=(25, 1),
                enable_events=True,
                key='escolher3',
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
            sg.Button(
                'Adicionar \n codificação social',
                key='add_cod',
                font=(None, 15),
                size=(16, None),
            ),
            sg.Button('Sair', key='sair', font=(None, 15), size=(16, None)),
        ],
    ]
    return sg.Window(
        'Codificação variáveis sociais',
        layout,
        finalize=True,
        grab_anywhere=True,
        text_justification='center',
        element_justification='center',
    )


def ver_tabela(dataf):   # mostra o dataframe selecionado para inserção
    cabecalhos = []
    data = []

    cabecalhos = list(dataf.columns)
    data = dataf[0:].values.tolist()

    layout = [
        [
            sg.Table(
                values=data,
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
            sg.Button('Salvar planilha', key='salvar3'),
            sg.Input(key='nome_arquivo2', default_text=''),
        ],
    ]

    return sg.Window(
        'Tabela de dados dos informantes',
        layout,
        finalize=True,
        grab_anywhere=True,
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


def codificar(dataf):   # codifica a partir da tabela selecionada
    df = dataf
    cds = []
    cont_l = 0
    c = ''
    linha = ''
    cont_c = 0

    for x in range(len(df)):
        for y in range(len(colunas)):
            nome_c = colunas[y]
            r = df.iat[x, y]

            linha = str(cods(r, nome_c))

            if linha in simbolos:
                c = c + linha

        cds.append(c)
        c = ''

    sg.popup('COLUNA ADICIONADA', title='Confirmação')

    return cds


def salvar(valor_input, tela, dataf):   # salva a planilha codificada
    window4 = tela
    n_df = dataf

    button, values = window4.Read()
    nome = valor_input

    if nome != '':
        n_df.to_excel(
            f'linguistic/saidas/planilhas/{nome}.xlsx',
            sheet_name='com códigos sociais',
        )
    else:
        n_df.to_excel(
            'linguistic/saidas/planilhas/planilha_com_cod_soc.xlsx',
            sheet_name='com códigos sociais',
        )

    sg.popup('ARQUIVO SALVO', title='Confirmação')


def cods(
    valor, coluna
):   # faz a correspondência entre a as colunas e os códigos definidos
    cod = ''
    r = str(valor)

    if coluna == 'Escolaridade do pai':
        if r == 'Ensino Fundamental Incompleto':
            cod = 'z'
            return cod
        elif r == 'Ensino Fundamental Completo':
            cod = 'Z'
            return cod
        elif r == 'Ensino Médio Incompleto':
            cod = '_'
            return cod
        elif r == 'Ensino Médio Completo':
            cod = '%'
            return cod
        elif r == 'Ensino Superior Incompleto':
            cod = 'e'
            return cod
        elif r == 'Ensino Superior Completo':
            cod = '%'
            return cod
        else:
            cod = '&'

    elif coluna == 'Escolaridade da mãe':
        if r == 'Ensino Fundamental Incompleto':
            cod = 'g'
            return cod
        elif r == 'Ensino Fundamental Completo':
            cod = 'G'
            return cod
        elif r == 'Ensino Médio Incompleto':
            cod = 'j'
            return cod
        elif r == 'Ensino Médio Completo':
            cod = 'J'
            return cod
        elif r == 'Ensino Superior Incompleto':
            cod = 'l'
            return cod
        elif r == 'Ensino Superior Completo':
            cod = 'L'
            return cod
        else:
            cod = '#'

    elif coluna == 'Naturalidade':
        if 'Camaçari' in r:
            cod = 'C'
            return cod
        elif 'Salvador' in r:
            cod = 'c'
            return cod
        elif 'Bahia' in r:
            cod = 'H'
            return cod
        else:
            cod = 'h'
            return cod

    elif coluna == 'Naturalidade do pai':
        if 'Camaçari' in r:
            cod = '~'
            return cod
        elif 'Salvador' in r:
            cod = '^'
            return cod
        elif 'Bahia' in r:
            cod = '}'
            return cod
        else:
            cod = '{'
            return cod

    elif coluna == 'Naturalidade da mãe':
        if 'Camaçari' in r:
            cod = '!'
            return cod
        elif 'Salvador' in r:
            cod = '?'
            return cod
        elif 'Bahia' in r:
            cod = 'Ç'
            return cod
        else:
            cod = 'ç'
            return cod

    elif coluna == 'Tempo médio diário de leitura de mídias impressas':
        if r == '1-2 horas':
            cod = '@'
            return cod
        elif r == '2-4 horas':
            cod = '$'
            return cod
        elif r == '4-6 horas':
            cod = '['
            return cod
        elif r == 'Mais que 6 horas':
            cod = ']'
            return cod

    elif coluna == 'Tempo médio diário de exposição às mídias audiovisuais':
        if r == '1-2 horas':
            cod = ','
            return cod
        elif r == '2-4 horas':
            cod = ':'
            return cod
        elif r == '4-6 horas':
            cod = '.'
            return cod
        elif r == 'Mais que 6 horas':
            cod = ';'
            return cod

    elif coluna == 'Tempo médio diário de exposição à internet':
        if r == '1-2 horas':
            cod = 's'
            return cod
        elif r == '2-4 horas':
            cod = 'S'
            return cod
        elif r == '4-6 horas':
            cod = 'y'
            return cod
        elif r == 'Mais que 6 horas':
            cod = 'Y'
            return cod

    elif coluna == 'Tempo médio diário de leitura literária ficcional':
        if r == '1-2 horas':
            cod = 'r'
            return cod
        elif r == '2-4 horas':
            cod = 'R'
            return cod
        elif r == '4-6 horas':
            cod = 'q'
            return cod
        elif r == 'Mais que 6 horas':
            cod = 'Q'
            return cod

    elif coluna == 'Pratica alguma religião? Se sim, qual?':
        if r == 'Não' or r == 'não':
            cod = 'T'
            return cod
        else:
            cod = 't'
            return cod

    elif coluna == 'Estuda outra língua? Se sim, qual?':
        if r == 'Não' or r == 'não':
            cod = 'B'
            return cod
        else:
            cod = 'b'
            return cod

    elif r == 'Faixa 1 (13 a 20)':
        cod = ' ='
        return cod
    elif r == 'Faixa 2 (25-35)':
        cod = '-'
        return cod
    elif r == 'Faixa 3 (40-55)':
        cod = '|'
        return cod
    elif r == 'Faixa 4 (+ de 60)':
        cod = '+'
        return cod
    elif r == 'Feminino':
        cod = 'F'
        return cod
    elif r == 'Masculino':
        cod = 'M'
        return cod
    elif r == '1º ano':
        cod = '1'
        return cod
    elif r == '2º ano':
        cod = '2'
        return cod
    elif r == '3º ano':
        cod = '3'
        return cod
    elif r == '4º ano (EM Técnico)':
        cod = '4'
        return cod
    elif r == 'Ensino Superior':
        cod = '5'
        return cod
    elif r == '2014':
        cod = 'A'
        return cod
    elif r == '2015':
        cod = 'N'
        return cod
    elif r == '2016':
        cod = 'D'
        return cod
    elif r == 'Metropolitana':
        cod = '<'
        return cod
    elif r == 'Rural':
        cod = '>'
        return cod
    elif r == 'Urbana':
        cod = '“'
        return cod
    elif r == 'Pública':
        cod = 'u'
        return cod
    elif r == 'Privada':
        cod = 'v'
        return cod
    elif r == 'Mista (Maioria em rede privada)':
        cod = 'V'
        return cod
    elif r == 'Mista (maioria em rede pública)':
        cod = 'U'
        return cod
    elif r == 'Conto':
        cod = 'O'
        return cod
    elif r == 'Crônica':
        cod = 'o'
        return cod
    elif r == 'Poesia':
        cod = 'k'
        return cod
    elif r == 'Romance':
        cod = 'K'
        return cod
    else:
        return cods
