class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def nombre_completo(self):
        print(f"El nombre completo es: {self.nombre}{self.apellido}")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)
        self.carrera = carrera
    def obtener_carrera(self):
        print(f"El estudiante {self.nombre} {self.apellido} esta aprendiendo {self.carrera}")

gente = Persona("Hichiro ","Tagomatchi")

alumno = Estudiante("Hichiro","Tagomatchi","POO en el INFOR")

gente.nombre_completo()
alumno.obtener_carrera()
