numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida=("Numeros proporcionados: {} y {}. {}.")
if (numero1==numero2):
    #En caso de que los numeros proporcionados sean iguales, entrara aqui
    print(salida.format(numero1, numero2, "Los numeros dados son iguales"))
else:
    #Si los numeros proporcionados no son iguales, entrara aqui
    if numero1>numero2:
        #En este caso, entrara si el numero 1 es mayor que el segundo
        print(salida.format(numero1, numero2, "El mayor es el primer valor"))
    else:
        #O si el primer digito o valor NO es mayor que el segundo
        print(salida.format(numero1, numero2, "El mayor es el segundo valor"))