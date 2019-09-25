#Python cuenta con librerias que estan listas para ser utilizadas, que son llamadas modulos
#Para usar un modulo en un programa, primero deberemos importarlo, usando la instruccion import
import random

#Definimos una variable de tipo float, y le asignaremos un valor
numero1=float(10.5)

#En Python tambien tenemos lo que son las funciones, es un conjunto de instrucciones que procesan una tarea especifica
#Se declara con def. y todo el codigo que este posicionado a la derecha de la definicion, formara parte de la funcion
def Mifuncion():
    #El numero aleatorio generado por random.randrage() se convertira a una variable de tipo float.
    #Solo estara disponible si se importa el modulo random
    numero2=float(random.randrange(1,10))
    #Se utilizaran las metas sustituciones ya antes vistas para reflejar los resultados
    mensaje="La suma de {} y {} es igual a {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

#Se ejecuta la funcion definida en el codigo
Mifuncion()