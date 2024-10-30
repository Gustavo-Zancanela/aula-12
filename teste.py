vehicles_one = ['carro','bicicleta','motor']
print(vehicles_one)
vehicles_two = vehicles_one
del vehicles_one[0]
print(vehicles_two)

cores = ["vermelho", "verde", "laranja"]
parte_1 = cores[:]
print(parte_1)
parte_2 = cores[0:2]
print(parte_2)

lista = ['a','b','c','d','e']
nova_lista = lista[2:-1]
print(nova_lista)

my_list = [1,2,3,4,5]
slice_one = my_list[2:]
slice_two = my_list[:2]
slice_three = my_list[-2:]

print(slice_one)
print(slice_two)
print(slice_three)

my_list = [1,2,3,4,5]
del my_list[0:2]
print(my_list)
del my_list[:]
print(my_list)

my_list = ['a','b',1,2]
print('a' in my_list)
print('c' not in my_list)
print(2 not in my_list)

list_1 = ['a','b','c']
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

list_1 = ['a','b','c']
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

list_1 = ['a','b','c']
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)

list_1 = ['a','b','c']
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

my_list = [1,2,'in',True,'abc']

print(1 in my_list) # true
print('a' not in my_list) # true
print(3 not in my_list) # true
print(False in my_list) # false