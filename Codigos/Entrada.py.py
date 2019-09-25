entrada=input()
print(type(entrada))
#La variable de tipo booleana contiene el resultado de verificar si lo capturado es digito, y si no encuentra un
#punto, indicaria que se trata de un numero decimal, es decir, un numero float. Si el comando find retorna un -1
#quiere decir que el punto decimal no fue encontrado. Si el valor encontrado es entero, sera true.
esEntero-(entrada.lsddigit() and entrada.find(".")---1)
if (esEntero):
    #Esta linea se ejecutara en caso de que la condicion sea verdadera(TRUE)
    print("Dato entero. ¡Muy bien!")
else:
     #Esta linea se ejecutaria en caso de que la condicion sea falsa(FALSE)
     print("Dato no es entero. Intentelo nuevamente.")