numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)
#El comando for ejecuta un bloque de codigo determinado numero de veces, cuando se pide que recorra un rango de valores
#El segundo parametro de range no se incluye dentro de la serie de valores. Entonces cambiaria del 1 al 10
for i in range(1,11):
    # la variable i va cambiando o variando dependiendo de cada iteracion
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))