# ~~~~~ Registro de Stock ~~~~~~
# Dado un diccionario llamado stock que contiene productos como claves y una tupla con su
# precio y cantidad disponible como valor, escribí un programa que:
#   A- Le pida al usuario que ingrese el nombre de un producto
#   B- Verifique si el producto existe en el diccionario
#   C- Si existe, muestre por pantalla el precio y la cantidad disponible
#   D- Si no existe, deja un mensaje de que no se encontró el producto
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           RESPUESTA

stock = {
    "MANZANA" : (120,50),
    "PERA" : (90,38),
    "NARANJA" : (110,60),
    "MANDARINA" : (90,50),
    "SANDIA" : (150,70)
}

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
producto = input("INGRESE UN PRODUCTO:")
produ_mayu = producto.upper()

if produ_mayu in stock:
    precio, cantidad = stock[produ_mayu]
    print("****************************")
    print("El precio es:",precio)
    print("La cantidad de ", producto,"es de :", cantidad)
    print("****************************")
else:
    print("****************************")
    cantidad_nuevo = input("SU PRODUCTO NO ESTA EN STOCK!!! INGRESE LA CANTIDAD:")
    precio_nuevo = input("AHORA INGRESE EL PRECIO:")
    print("****************************")
    stock[produ_mayu] = (cantidad_nuevo,precio_nuevo)
    print(produ_mayu,"se agrego a la lista y la cantidad es de:", cantidad_nuevo," y el precio es de:", precio_nuevo)

print("****************************")
print("Entonces la lista completa del Stock es:",stock.items())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")