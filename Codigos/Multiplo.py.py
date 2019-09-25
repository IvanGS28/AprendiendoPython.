#Capturamos un numero y se almacenara cuando sea covertido a int
numero=int(input("Dame un numero entero: "))
#Almacenaremos en valores booleanos la evaluacion de los residuos. Si el residuo es cero, el numero es multiplo
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
#En caso de usar and, todas las condiciones son verdaderas.
#En caso de usar or, resolveremos por verdadero si una de las condiciones es verdadera
#Los parentesis significa que las primeras dos condiciones van juntas y la tercera es independiente de ellas
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("CORRECTO")
else:
    print("INCORRECTO")