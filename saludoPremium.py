#ingresar hora y saludar dependiendo de la hora ingresada

print(".-.-.-.-.-.-.-.-.-.-.-.-.-")
nombre = input("Ingresar Nombre: ")
print("_:_:_:_:_:_:_:_:_:_:_:_:_:")
hora = float(input("Ingresar hora (0-23): "))
print("-.-.-.-.-.-.-.-.-.-.-.-.-.")
print("                          ")

if 6 <= hora < 12: #Buenos Días --> 5 - 11
    saludar = "Buenos días"
elif 12 <= hora < 20: #Buenas Tardes --> 12 - 19
    saludar = "Buenas tardes"
else: #Buenas Noches 20 - 5
    saludar = "Buenas Noches"

print(saludar,nombre,"como te sentis hoy..")
print("                         ")
print("-------------------------")
