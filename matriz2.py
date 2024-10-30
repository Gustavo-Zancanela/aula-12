quartos = [[[False for r in range(20)]for f in range(15)]for t in range(3)]
quartos[1][9][13] = True
quartos[0][0][0] = True
quartos[2][14][19] = True

print(quartos)