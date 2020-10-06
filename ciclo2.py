#Ingresar n números donde n es un número ingresado por teclado (utilizar ciclo while).
#Mostrar cuantos son positivos, negativos e iguales a 0.
veces=int(input("Cuántos números desea ingresar?: "))
i=1
pos=0
neg=0
ig0=0
while i<=veces:
    num=int(input("Ingresar dígito: "))
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        ig0+=1        
    i+=1
print("Cantidad números positivos: "+str(pos))  
print("Cantidad números negativos: "+str(neg)) 
print("Cantidad números iguales a 0 (cero): "+str(ig0))       