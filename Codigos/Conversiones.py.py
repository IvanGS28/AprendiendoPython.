#Declaramos una variable de tipo str, con una cadena de digitos
numero="1234"
#Se mostrara el tipo que tiene la variable, la salida de type() no es un str, es un dato type
print(type(numero))
#La cadena se convertira a un equivalente int
numero=int(numero)
#Se mostrara como el tipo cambia aunque se utilice la misma variable
print(type(numero))
#Se declarara un str con meta de sustitucion (posiciones donde iran valores proporcionados usando el comando format)
salida="El numero utilizado es {}"
#Se mostrara el resultado. La meta sustitucion hara que donde esta {} se coloque el valor de la variable numero
print(salida.format(numero))