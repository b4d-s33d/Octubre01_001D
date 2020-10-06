#Crear ciclo for que permita ingresar diez números, contar y mostrar cuantos son pares e impares.
par=0
impar=0
for i in range(10):
    num=int(input("Digite un número: "))
    if num%2 == 0:
        par+=1
    else:
        impar+=1    
print("La cantidad de números pares es: "+str(par)+"\nLa cantidad de números impares es: "+str(impar))         