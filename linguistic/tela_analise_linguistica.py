# definição da tela que analisa as variáveis linguísticas

import os.path  # importa biblioteca para manipular o caminho dos arquivos

import matplotlib.pyplot as plt
import pandas as pd  # importa o pandas, biblioteca de data science
import PySimpleGUI as sg  # importa a biblioteca gráfica
import seaborn as sns


def montar_tela():   # definição da aparência e elementos da tela
    layout = [
        [
            sg.Text(
                'LinguisTic - Análise das variáveis linguísticas',
                font=(None, 20),
                text_color='Gold',
            )
        ],
        [
            sg.Text(
                'Escolha uma planilha Excel com variáveis linguísticas ',
                font=(None, 20),
                text_color='Gold',
            ),
            sg.In(
                size=(25, 1),
                enable_events=True,
                key='escolher6',
                font=(None, 15),
            ),
            sg.FileBrowse(
                button_text='Procurar',
                font=(None, 15),
                size=(16, None),
                initial_folder='linguistic/tests/planilhas',
            ),
        ],
        [sg.Output(size=(100, 20), key='stats')],
        [
            sg.Button(
                'Salvar como arquivo',
                key='save_file',
                font=(None, 15),
                size=(16, None),
            ),
            sg.Input(key='nome_arqstats', default_text='', font=(None, 15)),
            sg.In(
                size=(25, 1), enable_events=True, key='addNI', font=(None, 15)
            ),
            sg.FileBrowse(
                button_text='Adicionar novo informante',
                font=(None, 15),
                size=(16, None),
            ),
            sg.Button('Sair', key='sair', font=(None, 15), size=(16, None)),
        ],
    ]

    return sg.Window(
        'Análise das variáveis linguísticas',
        layout,
        finalize=True,
        grab_anywhere=True,
        resizable=True,
        text_justification='center',
        element_justification='center',
    )


def ver_tabela(dataf):   # abre a visualização do dataframe selecionado
    cabecalhos = []
    data = []

    if (dataf != ''):
        data = dataf[0:].values.tolist()
        cabecalhos = list(dataf.columns)
    else:
        data.append('')

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
        ]
    ]

    return sg.Window(
        'Tabela de codificação linguística',
        layout,
        finalize=True,
        grab_anywhere=True,
        resizable=True,
        text_justification='center',
        element_justification='center',
    )


def mostrar_graphs(
    dataf,
):   # salva os gráficos de análise como arquivos e exibe eles
    df = dataf
    nome_arquivo = df.iloc[1, 0]

    sns.catplot(x='tipo', data=df, kind='count', height=5, aspect=2)
    t = f'linguistic/saidas/gráficos/tipo_{nome_arquivo}.png'
    plt.savefig(t)

    sns.catplot(x='desvio', data=df, kind='count', height=10, aspect=5)
    d = f'linguistic/saidas/gráficos/desvio_{nome_arquivo}.png'
    plt.savefig(d)

    sns.catplot(x='desvio', data=df, kind='count', height=5, aspect=2)
    d_s = f'linguistic/saidas/gráficos/desvio_{nome_arquivo} (s).png'
    plt.savefig(d_s)

    sns.catplot(x='ano', data=df, kind='count', height=5, aspect=2)
    a = f'linguistic/saidas/gráficos/ano_{nome_arquivo}.png'
    plt.savefig(a)

    layout = [
        [sg.Image(key='imagem')],
        [
            sg.Button(
                'Gráfico Tipo',
                key='atv_tipo',
                enable_events=True,
                disabled=False,
            ),
            sg.Button(
                'Gráfico Desvio',
                key='atv_desvio',
                enable_events=True,
                disabled=False,
            ),
            sg.Button(
                'Gráfico Ano',
                key='atv_ano',
                enable_events=True,
                disabled=False,
            ),
        ],
    ]

    return sg.Window(
        'Gráficos de contagem',
        layout,
        finalize=True,
        grab_anywhere=True,
        resizable=False,
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


def salvar_stats(
    valor_input, stats
):   # salva um arquivo com as estatísticas linguísticas
    dados = stats

    nome = valor_input

    if nome != '':
        arquivo = open(f'linguistic/saidas/análises/{nome}.txt', 'a')
        arquivo.write(dados)
    else:
        arquivo = open(
            'linguistic/saidas/análises/estatística planilha linguística.txt',
            'a',
        )
        arquivo.write(dados)

    sg.popup('ARQUIVO SALVO', title='Confirmação')
