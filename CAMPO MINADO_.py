import random

LINHAS = 8
COLUNAS = 8
MINAS = 10


def criar_matriz(linhas, colunas, valor):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


def posicao_valida(linha, coluna):
    if linha >= 0 and linha < LINHAS and coluna >= 0 and coluna < COLUNAS:
        return True
    else:
        return False


def colocar_minas(campo, quantidade):
    colocadas = 0
    while colocadas < quantidade:
        i = random.randint(0, LINHAS - 1)
        j = random.randint(0, COLUNAS - 1)
        if campo[i][j] != -1:
            campo[i][j] = -1
            colocadas = colocadas + 1


def contar_vizinhas(campo, i, j):
    total = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            li = i + di
            cj = j + dj
            if posicao_valida(li, cj) == True:
                if campo[li][cj] == -1:
                    total = total + 1
    return total


def calcular_numeros(campo):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if campo[i][j] != -1:
                campo[i][j] = contar_vizinhas(campo, i, j)


def abrir_casa(campo, visivel, i, j):

    if posicao_valida(i, j) == False:
        return

    if visivel[i][j] != "?":
        return

    visivel[i][j] = campo[i][j]

    if campo[i][j] != 0:
        return

    for di in range(-1, 2):
        for dj in range(-1, 2):
            abrir_casa(campo, visivel, i + di, j + dj)


def contar_abertas(visivel):
    total = 0
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if visivel[i][j] != "?" and visivel[i][j] != "F":
                total = total + 1
    return total


def mostrar(matriz):
    print()
    print("    ", end="")
    for j in range(COLUNAS):
        print(j, end=" ")
    print()
    for i in range(LINHAS):
        print(i, " |", end=" ")
        for j in range(COLUNAS):
            print(matriz[i][j], end=" ")
        print()
    print()


def revelar_campo(campo):
    final = criar_matriz(LINHAS, COLUNAS, 0)
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if campo[i][j] == -1:
                final[i][j] = "*"
            else:
                final[i][j] = campo[i][j]
    return final



campo = criar_matriz(LINHAS, COLUNAS, 0)
visivel = criar_matriz(LINHAS, COLUNAS, "?")

colocar_minas(campo, MINAS)
calcular_numeros(campo)

jogando = True
perdeu = False
total_seguras = LINHAS * COLUNAS - MINAS

print("=== CAMPO MINADO ===")
print("Digite a linha e a coluna para jogar.")
print("Depois escolha: A = abrir a casa, M = marcar/desmarcar bandeira.")
print("Existem", MINAS, "minas escondidas.")

while jogando:

    mostrar(visivel)

    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))

    if posicao_valida(linha, coluna) == False:
        print("essa posicao nem existe gurizao")
    else:
        acao = input("Abrir ou marcar (A/M)? ")
        acao = acao.upper()

        if acao == "M":
            if visivel[linha][coluna] == "?":
                visivel[linha][coluna] = "F"
            elif visivel[linha][coluna] == "F":
                visivel[linha][coluna] = "?"
            else:
                print("tenta outra ai gurizao")

        elif acao == "A":
            if visivel[linha][coluna] == "F":
                print(" TA MARCADA AI PAIZAO, DESMARCA.")
            elif visivel[linha][coluna] != "?":
                print("JA FOI JA ")
            elif campo[linha][coluna] == -1:
                jogando = False
                perdeu = True
            else:
                abrir_casa(campo, visivel, linha, coluna)
                if contar_abertas(visivel) == total_seguras:
                    jogando = False

        else:
            print("Opcao invalida! Use A ou M.")


mostrar(revelar_campo(campo))

if perdeu:
    print("XABLAU!!, EXPLODIDO.")
else:
    print(" TU É O BIXAO MERMO EM.")