#Ingrese dos números como entero
a=int(input("Ingrese primer número: "))
b=int(input("Ingrese segundo número: "))
#Operaciones matemáticas
suma=a+b
multi=a*b
print("La suma entre "+str(a)+" y "+str(b)+" da como resultado "+str(suma))
print("La multiplicación entre "+str(a)+" y "+str(b)+" da como resultado "+str(multi))
#Creamos una condición
if a>b:
    print("El número "+str(a)+" es mayor que el número "+str(b))
elif a<b:
    print("El número "+str(a)+" es menor que el número "+str(b))
else:
    print("Los números son iguales")    
