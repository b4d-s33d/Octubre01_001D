import os

def Temperaturas():
    print("--- Opción Temperaturas ---")
    veces=int(input("Cuántas temperaturas ingresa?: "))
    suma=0
    for i in range(veces):
        temp=float(input("Ingrese temperatura: "))
        suma=suma+temp  
    print("El promedio de las temperaturas es: ", round((suma/veces),2)) 
    tecla=input("Presione una tecla para continuar.")

def Personas():
    print("--- Opción Datos de personas ---")
    #Ingresar para n personas el nombre y la edad (n debe ser ingresado por teclado)
    #Mostrar: Cuántas personas son mayores y menores de edad
    

seguir=True
while seguir:
    os.system('cls')#cls sirve para limpiar pantalla
    print("1. Temperaturas")
    print("2. Datos de personas")
    print("3. Salir")
    op=int(input("Ingrese opción (1, 2 o 3): "))
    if op == 1:
        Temperaturas()#Invocamos función
    if op == 2:
        Personas()#Invocamos función
    if op == 3:
        print("Programa finalizado.")
        break        
