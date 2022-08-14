# classe que auxilia o processo de filtragem estabelecendo uma referência entre os Radio Buttons e os parâmetros sociais

def check_ano(valor):
    if valor[0]:
        r_ano = '1º ano'
    elif valor[1]:
        r_ano = '2º ano'
    elif valor[2]:
        r_ano = '3º ano'
    elif valor[3]:
        r_ano = '4º ano (EM Técnico)'
    else:
        r_ano = ''
   
    return r_ano

def check_pe(valor):
    if valor[0]:
        rpe = 'Pública'
    elif valor[1]:
        rpe = 'Privada'
    elif valor[2]:
        rpe = 'Mista (maioria em rede pública)'
    elif valor[3]:
        rpe = 'Mista (Maioria em rede privada)'
    else:
        rpe = ''
    
    return rpe

def check_g(valor):
    if valor[0]:
        rg = 'Feminino'
    elif valor[1]:
        rg = 'Masculino'
    else:
        rg = ''
    return rg

def cod_faixaetaria(coluna):
    if coluna == 'Faixa 1 (13 a 20)':
        cs = '='
    elif coluna == 'Faixa 2 (25-35)':
        cs = '-'
    elif coluna == 'Faixa 3 (40-55)':
        cs = '|'
    elif coluna == 'Faixa 4 (+ de 60)':
        cs = '+'
    return cs
        