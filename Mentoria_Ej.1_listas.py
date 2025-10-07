#Ejercicio 2: Contar apariciones
#Dada la lista:
#colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
#1- Mostrá cuántas veces aparece “rojo” usando .count().
#2- Reemplazá el primer “verde” por “amarillo”
#3- Mostrá la lista final
#El objetivo es usar el método .count(), acceso por índice, asignación de valor.


#Enunciado 1
lista_de_colores = ["rojo","azul","verde","rojo","azul","rojo"]
num_rojo = lista_de_colores.count("rojo")

print("el color rojo aparece",num_rojo)

#Enunciado 2

lista_de_colores[2] = "amarillo"

print(lista_de_colores)