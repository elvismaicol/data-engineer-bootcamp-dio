segundos = int(input())


minutos = int(segundos / 60) #TODO Implementar a formula para calcular os minutos.
horas = int(segundos / 3600)
segundos = int(segundos - (minutos * 60))
minutos = int(minutos - (horas * 60))


print("{}:{}:{}".format(horas, minutos, segundos))

print(minutos)
print(segundos)
print(horas)