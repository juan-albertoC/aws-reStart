#Desafio de AWS Juan Alberto Cuevas Juarez
#Programa muestra numeros primos de 1 hasta 250, combina condicionales if-else, bucles for-while

#crete directorio de trabajo y archivos py, txt 

n = 250                                   # Opcion 1 variable n: numero maximo de primos
#n = int(input("Indica numero maximo de primos")) # Opcion 2 Entrada por teclado con la funcion input para diferentes numeros maximos de primos


for i in range(2, n+1):                   #En ciclo for variable i de un rango desde 2 hasta n + 1
       j = 2                              #comienza aqui j en 2
       esPrimo = True                     #variable booleano en True