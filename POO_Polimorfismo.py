class Vehiculo:
    def Mover(self):
        pass

class Coche (Vehiculo):
    def Mover(self):
        return print(f"El coche está conduciendo por la carretera")

class Bike (Vehiculo):
    def Mover(self):
        return print(f"El de la Bike esta tirando Willy")

class Avion (Vehiculo):
    def Mover(self):
        return print(f"El del Avión esta re volaadoo")


vehiculos = [Coche(), Bike(), Avion()]

for Vehiculo in vehiculos:
    print(Vehiculo.Mover())