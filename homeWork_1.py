#~~Realizá un programa en Python que permita al usuario ingresar 10 números enteros. El programa debe:
# 1) - Almacenar los números ingresados en una lista.
#   a) - Calcular la suma de todos los números pares.
#   b) - Contar cuántos números impares se ingresaron.
# Mostrar por pantalla:
# 2) - La lista completa de números ingresados.
# 3) - La cantidad de los números pares.
# 4) - La cantidad de números impares
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Respuesta
# Lista de números ingresado

user_num = []

# Pedimos 10 números al usuario
for i in range(10):
    num = int(input(f"Ingrese 10 números enteros por favor: "))
    print(f"le quedan {9-i} intentos!!!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    user_num.append(num)

# Tratamiento a los pares e impares
pares = []
impares = []

for num in user_num:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostramos listas
print("****************************")
print("La lista completa de números ingresado es:", user_num)
print("****************************")

cantidad_pares = len(pares)
paresTotal = sum(pares)
print(f"Los números pares son:", pares,f"hay unos",cantidad_pares,f"numeros pares y la sumatoria total es de:", paresTotal)
print("****************************")
cantidad_impares = len(impares)
print("Los números impares son:",impares,"y la cantidad de impares es de:", cantidad_impares)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")