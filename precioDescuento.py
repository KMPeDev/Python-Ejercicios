#Calcular el precio luego de un descuento aplicado

print("...................................")
precio = float(input("Precio del Producto $: "))
print("...................................")
porcentaje = int(input("Porcentaje de Descuento %: "))
print("...................................")

descuento = precio * (1 - porcentaje / 100)

print("El Precio Final es $",descuento,)
print("...................................")