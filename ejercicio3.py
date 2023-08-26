contadorNotas = 1
totalNotas = 0
notas = []
notasFinal = []

while contadorNotas < 6:
    nota = int(input("Por favor, ingrese la nota {0}: ".format(contadorNotas)))
    notas.append(nota)
    contadorNotas += 1

for i in notas:
    totalNotas += i

mayor = notas[0]
for i in range(len(notas)):
    if notas[i] > mayor:
        mayor = notas[i]

menor = notas[0]
for i in range(len(notas)):
    if notas[i] < menor:
        menor = notas[i]

media = totalNotas / 5
notasFinal.append(media)
notasFinal.append(mayor)
notasFinal.append(menor)

print("Notas: {0}".format(notas))
print("Media de Notas, Nota Mayor y Nota Menor: {0}".format(notasFinal))