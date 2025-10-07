# ~~~~~ Sistema de votación ~~~~~~
# Se quiere implementar un sistema básico de votación donde cada persona puede votar una
# sola vez por su candidato favorito:
#   A- El programa debe permitir que tres personas voten
#   B- Antes de permitir votar, debe pedir el nombre del votante
#   C- Si el votante ya emitió su voto anteriormente, debe mostrar un mensaje: “Ya votaste” y
# no permitirle votar de nuevo
#   D- Si es la primera vez que vota, el sistema debe pedir el nombre del candidato al que desea
# votar.
#   E- Al finalizar, el programa debe mostrar los resultados con la cantidad de votos que recibió
# cada candidato
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       RESPUESTA       

candidatos = ["PINGUINO","LEON","LORO","GATO","CARPINCHO"]

votos = {candidato: 0 for candidato in candidatos}

votantes = set()

nombre_user = str(input("Ingrese su nombre"))

while True:
    if nombre_user in votantes:
        print("Ya has votado, no puedes votar 2 veces!!")
    elif
    eleccion = str(input(f"Escriba el nombre de su candidato: "))
    if eleccion in candidatos: