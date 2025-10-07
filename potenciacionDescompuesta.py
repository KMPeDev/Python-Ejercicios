#generar un algoritmo de potenciación sin la función hecha

print("------------------------------------")
base = int(input("Ingrese el número base: "))
print("------------------------------------")
exponente = int(input("Ingrese el Exponente de la base: "))

potencia = 1
contador = 1

if base or exponente != 0:
    while contador <= exponente:
        potencia = potencia * base
        contador = contador + 1
    print("------------------------------------")
    print("El resultado es",potencia)
    print("------------------------------------")
else:
    potencia = 0
    contador = 0
    print("------------------------------------")
    print("¡Esta expresión es invalida!")
    print("------------------------------------")