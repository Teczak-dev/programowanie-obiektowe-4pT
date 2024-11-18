lista = list()
lista += ['a','c','c','d']
print(lista)
lista += ['f','e','g']
print(lista)
lista.insert(2,"L")
print(lista)
lista.pop(5)
print(lista)
lista.remove('L')
lista.reverse()
print(lista)
print(len(lista))


lista2 = [1,2,3,4,5,6,7,8,9]
print(max(lista2))
print( min(lista2) )

print( sum(lista2)/len(lista2) )
print(lista.index('c'))
print(lista.count('c'))
print( len(lista))

print( lista[-1:-7:-2] )
lista3 = [x**3 for x in range(1,11) if x**2>10]
print(lista3)
lista = sorted(lista)
print(lista)