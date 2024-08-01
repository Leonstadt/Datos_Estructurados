tupla= (10, 20, 30, 40, 50)
# Accede e imprime el tercer elemento de la tupla
print(tupla[2])
# Desempaqueta los elementos de la tupla en variables individuales.
a,b,c,d,e=tupla
print("Desempaquetado", a, b, c, d, e)
#Crea una nueva tupla que contenga los primeros tres elementos de la tupla original.
tupla2=tupla[:3]
print(tupla2)