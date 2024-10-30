tabuleiro = []
vazio = 0

for i in range(8):
    linha = [vazio for i in range(8)]
    tabuleiro.append(linha)

print(tabuleiro)

vazio = 0

tabuleiro2 = [[vazio for i in range(8)] for j in range(8)]
tabuleiro2[0][0] =1
tabuleiro2[0][7] =1
tabuleiro2[7][0] =1
tabuleiro2[7][7] =1
tabuleiro2[3][4] =1

for linha in tabuleiro2:
    print(linha)