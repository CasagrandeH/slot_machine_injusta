import random

MAX_LINHAS = ROWS = COLS = 3
MAX_APOSTA = 500
MIN_APOSTA = 10

quantia_simbolo= {'A': 2, 'B': 4, 'C': 6, 'D': 8}

def girar_caçaniquel(rows, cols, symbols):
    tod_simbolos = []
    for simbolo, quantia_simbolo in symbols.items():
        for _ in range(quantia_simbolo):
            tod_simbolos.append(simbolo)
    colunas = [[], [], []]
    for _ in range(cols):
        coluna = []
        simbolos_atuais = tod_simbolos[:]
        for _ in range(rows):
            valor = random.choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            coluna.append(valor)
        colunas.append(coluna)
    return colunas


def print_caçaniquel():
    for row in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(coluna) - 1:
                print(coluna[row], '|')
            else:
                print(coluna[row])


def deposito():
    while True:
        quantia = input('Quanto depositar?: R$')
        if not quantia.isnumeric():
            print('\033[0;31mErro! Digite uma quantia valida!\033[m')
        elif float(quantia) <= 0:
            print('\033[0;31mErro! Quantia deve ser maior que 0!\033[m')
        elif quantia.isnumeric():
            quantia = float(quantia)
            print(f'O valor de {conversor_real(quantia)} foi depositado com sucesso.')
            break
    return quantia


def get_aposta():
    while True:
        quantia = input('Quanto apostar em cada linha?: R$')
        if quantia.isdigit():
            quantia = float(quantia)
            if MAX_APOSTA <= quantia <= MIN_APOSTA:
                print(f'\033[0;31mErro! Quantia deve no minimo ser {conversor_real(MIN_APOSTA)} e no maximo {conversor_real(MAX_APOSTA)}!\033[m')
            else:
                break
        else:
            print('\033[0;31mErro! Digite uma quantia valida!\033[m')
    return quantia


def numero_de_linhas():
    while True:
        linhas = input('Em quantas linhas apostar? (1-'+ str(MAX_LINHAS) + ')? ')
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print('\033[0;31mErro! linhas deve ser maior que 0 e menor que 4!\033[m')
        else:
            print('\033[0;31mErro! Digite um numero de linhas valido!\033[m')
    return linhas


def conversor_real(valor):
    quantia = f'R${valor:.2f}'.replace('.', ',')
    return quantia


def main():
    extrato = deposito()
    linhas = numero_de_linhas()
    while True:
        aposta = get_aposta()
        aposta_total = aposta * linhas
        if aposta_total > extrato:
            print(f'\033[0;31mVocê nao tem fundos o suficiente para esta aposta, tente novamente!\033[m')
        else:
            print(f'Você esta apostando R${aposta} em {linhas} linhas. O total apostado foi {conversor_real(aposta_total)}')
            print(extrato, linhas)
            break


main()