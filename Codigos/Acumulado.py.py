#Declaramos variables para trabajar de tipo explicito
acumulado=int(0)
numero=str("")

#Si se coloca True como condicion de while, se formara un ciclo que no tendra fin que no se rompera hasta que
#se utilice la instruccion break
while True:
    numero=input("Dame un numero entero")
    if numero=="":
        #Si el numero es vacio, solamente se reporta la situacion y abandona
        print("Vacio. Saliendo del programa")
        break
    else:
        #Si el usuario proporciona un valor, se hara la siguiente formula acumulado = acumulado + numero
        #El calculo se realizara mediante una suma incluyente(+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))