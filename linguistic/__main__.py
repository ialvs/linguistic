# classe que cria, abre e manipula as telas do sistema, bem como chama o principais métodos


import pandas as pd  # importa o pandas, biblioteca de data science
import PySimpleGUI as sg  # importa a biblioteca gráfica
import tela_insere_cod  # importa a quinta tela
import tela_filtragem  # importa a segunda tela
import tela_opcoes  # importa a tela principal
import tela_cod_social # importa a quarta tela
import tela_analise_linguistica # importa a terceira tela

pd.set_option('display.max_rows', None)   # melhora a visualização dos datasets
c = 0   # ?
sg.theme('DarkBlue15')   # define o tema da interface gráfica

window1 = tela_opcoes.montar_tela()   # cria e abre a tela principal do programa
window2 = None   # definição da segunda tela
window3 = None   # definição da terceira tela
window4 = None   # definição da quarta tela
window5 = None   # definição da quinta tela

while True:   # abertura do loop pra manter o programa aberto
    (
        window,
        event,
        values,
    ) = sg.read_all_windows()   # lê as modificações das telas

    if (
        event == sg.WIN_CLOSED or event == 'sair'
    ):   # condições para fechamento da tela
        window.close()   # fechamento da tela (e do programa)

        if window == window2:
            window2 = None  # fecha a segunda tela se 'sair' for apertado nela
        elif window == window3:
            window3 = None  # fecha a terça tela se 'sair' for apertado nela
        elif window == window4:
            window4 = None   # fecha a quarta tela se 'sair' for apertado nela
        elif window == window5:
            window5 = None   # fecha a quinta tela se 'sair' for apertado nela
        elif window == window1:
            break   # fecha a primeira tela se 'sair' for apertado nela

    elif event == 'analisar_vs' and not window2:
        window2 = (
            tela_filtragem.montar_tela()
        )   # abre a segunda tela quando o botão for selecionado

    elif event == 'analisar_vl' and not window3:
        window3 = (
            tela_analise_linguistica.montar_tela()
        )   # abre a terceira tela quando o botão for selecionado

    elif event == 'cod_vs' and not window4:
        window4 = (
            tela_cod_social.montar_tela()
        )   # abre a quarta tela quando o botão for selecionado

    elif event == 'insert_cod' and not window5:
        window5 = (
            tela_insere_cod.montar_tela()
        )   # abre a quinta tela quando o botão for selecionado

    elif event == 'escolher':
        df = tela_filtragem.escolher(
            values['escolher']
        )   # chama o método responsável pela leitura do dataframe
        df_show = tela_filtragem.ver_tabela(df)   # mostra o dataframe como tabela

    elif event == 'escolher3':
        df2 = tela_cod_social.escolher(values['escolher3'])
        df_show2 = tela_cod_social.ver_tabela(df2)

    elif event == 'escolher4':
        df_codl = tela_insere_cod.escolher(values['escolher4'])
        sg.popup('PLANILHA ADICIONADA', title='Confirmação')

    elif event == 'escolher5':
        v_lista = []
        df_codsoc = tela_insere_cod.escolher(values['escolher5'])
        sg.popup('PLANILHA ADICIONADA', title='Confirmação')
        window5['out'].update(visible=False)

        for x in range(len(df_codsoc)):
            v = df_codsoc.iat[x, 1] + ' | ' + df_codsoc.iat[x, 58]
            v_lista.append(v)

        # print(v_lista)
        window5['txt'].update(visible=True)
        window5['lista'].update(values=v_lista, visible=True)

    elif event == 'escolher6':
        df_al = tela_analise_linguistica.escolher(values['escolher6'])

        tabela_al = tela_analise_linguistica.ver_tabela(df_al)

        graficos_al = tela_analise_linguistica.mostrar_graphs(df_al)
        nome_arquivo = df_al.iloc[1, 0]
        t = f'linguistic/saidas/gráficos/tipo_{nome_arquivo}.png'
        d = f'linguistic/saidas/gráficos/desvio_{nome_arquivo}.png'
        a = f'linguistic/saidas/gráficos/desvio_{nome_arquivo} (s).png'

        stat_tipo = df_al.groupby(by='tipo').size()
        st = stat_tipo.to_string() + '\n' + '\n'

        stat_desvio = df_al.groupby(by='desvio').size()
        sd = stat_desvio.to_string() + '\n' + '\n'

        stat_texto = df_al.groupby(by='texto').size()
        stx = stat_texto.to_string() + '\n' + '\n'

    elif event == 'salvar':
        tela_filtragem.salvar(
            values['nome_arquivo'], ndf_show, n_df
        )   # salva o dataframe como .xlsx

    elif event == 'salvar3':
        tela_cod_social.salvar(
            values['nome_arquivo2'], df_show2, df2
        )   # salva o dataframe como .xlsx

    elif event == 'salvar4':
        tela_insere_cod.salvar(
            values['nome_arquivo3'], window5, df_codl
        )   # salva o dataframe como .xlsx

    elif event == 'save_file':
        total = st + sd + stx
        tela_analise_linguistica.salvar_stats(values['nome_arqstats'], window3, total)

    elif event == 'add_cod':
        df_show2.close()
        df2['Código Social'] = tela_cod_social.codificar(df2)
        df_show2 = tela_cod_social.ver_tabela(df2)

    elif event == 'lista':
        selected = window5['lista'].get()
        df_codl['Código Social'] = tela_insere_cod.inserir(selected)
        sg.popup('CÓDIGO ADICIONADO', title='Confirmação')

        window5['lista'].update(visible=False)
        exib = df_codl.to_string(
            columns=['ocorrências', 'Código Social'], index=False
        )
        window5['out'].update(value=exib, visible=True)

    elif event == 'filtrar':

        df_show.close()

        if c > 0:
            ndf_show = None

        n_df = tela_filtragem.filtrar(df, window2)

        ndf_show = tela_filtragem.ver_tabela(n_df)
        c = c + 1

    elif event == 'atv_desvio':
        graficos_al['imagem'].update(filename=d)

    elif event == 'atv_ano':
        graficos_al['imagem'].update(filename=a)

    elif event == 'atv_tipo':
        graficos_al['imagem'].update(filename=t)

    elif event == 'addNI':
        graficos_al.close()
        tabela_al.close()
        window3['stats'].update(value='')

        ndf_al = tela_analise_linguistica.escolher(values['addNI'])
        frames = [df_al, ndf_al]
        conkat = pd.concat(frames)

        tabela_al = tela_analise_linguistica.ver_tabela(conkat)

        graficos_al = tela_analise_linguistica.mostrar_graphs(conkat)

        nome_arquivo = conkat.iloc[1, 0]
        t = f'tipo_{nome_arquivo}.png'
        d = f'desvio_{nome_arquivo} (s).png'
        a = f'ano_{nome_arquivo}.png'

        stat_tipo = conkat.groupby(by='tipo').size()
        st = stat_tipo.to_string() + '\n' + '\n'

        stat_desvio = conkat.groupby(by='desvio').size()
        sd = stat_desvio.to_string() + '\n' + '\n'

        stat_texto = conkat.groupby(by='texto').size()
        stx = stat_texto.to_string() + '\n' + '\n'
