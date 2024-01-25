#Desafio de AWS Juan Alberto Cuevas Juarez
#Programa muestra numeros primos de 1 hasta 250, combina condicionales if-else, bucles for-while

#crete directorio de trabajo y archivos py, txt
#create variable new_file

new_file = open("results.txt", "w")       #Asignar funcion open con 2 parametros: archivo ubicacion local y palabra reservada "w" de write

n = 250                                   # Opcion 1 variable n: numero maximo de primos
#n = int(input("Indica numero maximo de primos")) # Opcion 2 Entrada por teclado con la funcion input para diferentes numeros maximos de primos


for i in range(2, n+1):                   #En ciclo for variable i de un rango desde 2 hasta n + 1
       j = 2                              #comienza aqui j en 2
       esPrimo = True                     #variable booleano en True

       while esPrimo and j < i:           #Mientras condicion que esPrimo y j=2 < i
           if (i % j ==  0):              #"division", indica si el operador residuo es cero ejemplo: 7/7 exacto 7/1 exacto
               esPrimo = False            #variable booleano cambia a False
           else:                          #es falso j incrementa en uno una iteracion
                 j += 1
                                          #Termina el while
       if esPrimo:                        # si es verdadero entonces imprime y escribe variable i en el archivo de texto
          new_file.write(str(i) + " Este numero es primo" + "\n") #conversion de string y texto 

new_file.close()                          #Cerrar el archivo de texto con variable new_file.funcion close  

#-----------------------------------------Appened---"No borrar lo que se tiene en el archivo"-------------------------------
new_file = open("results.txt", "a")       #Se cambia el parametro de "a"    

new_file.write(" Desafio de Juan Alberto Cuevas 24/01/24 ")     #crea un nuevo string
       
new_file.close()                                                #cerrar el archivo
#-----------------------------------------------------------------------
