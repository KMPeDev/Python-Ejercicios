#Cronómetro que mida el tiempo entre click (enter)

import time 

print("------------------")
input("|ENTER| - para Iniciar: ")
t0 = time.time()

print("~~~~~~~~~~~~~~~~~~")
input("|ENTER| - para Parar: ")
t1 = time.time()
Resultado = t1 - t0

print("--------------------------")
print("El tiempo es ", Resultado,"Seg.")
print("-------------------------------")