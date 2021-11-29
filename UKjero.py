import os
from sys import version

saldo = 12000


def validarUsuario():
    try:
        
        print("Bienvenido a UKBanco")
        user = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        if(user == 'Admin' and contrasena == 'Admin'):
            operaciones()
    except ValueError as err:
        print("Caracteres invalidos")
    finally:
        operaciones()

def ImprimirMenu():
    print("\n¿Que operación desea realizar en el UKajero?\nSeleccione la opción correspondiente: \n")
    accion = input("1. Ver Saldo\n2. Retiro de efectivo\n3. Deposito de efectivo\n4. Transferencia\n5. Recarga telefonica\n0. Salir\n")
    os.system("cls")
    return int(accion)

def salir():
    salida = input("¿Realmente desea salir?\n Confirme con 0\n")
    if(salida == "0"):
        return  False
    return True
    
def verSaldo():
    print("Estimado UKusuario, tu saldo es de: "+ str(saldo) + " UKPesos\n")

def retirar():
    global saldo
    try:
        cantidadRetiro = input("Ingrese la cantidad a retirar\n")
        if (float(cantidadRetiro) <= saldo):
            saldo = saldo - float(cantidadRetiro)  
            verSaldo()
        else:
            print("Saldo insuficiente\n")
    except ValueError as err:
        print("Caracteres invalidos")

def depositar():
    global saldo
    try:
        cantidadDeposito = input("Ingrese cantidad a depositar\n")
        saldo = saldo + float(cantidadDeposito)
        verSaldo()
    except ValueError as err:
        print("Caracteres invalidos")
            
def transeferencia():
    global saldo
    try:
        cuentaTransferencia = input("Ingrese cuenta a trasferir\n")
        cantidadTransferencia = input("Ingrese la cantidad a transferir\n")
        if (float(cantidadTransferencia) <= saldo):
            saldo = saldo - float(cantidadTransferencia) 
            print("Se transfirio la cantidad de: $" + str(cantidadTransferencia) + " a la cuenta " + str(cuentaTransferencia)+"\n") 
            verSaldo()
        else:
            print("Saldo insuficiente\n")
    except ValueError as err:
        print("Caracteres invalidos")

                
def RecargaTelefonica():
    global saldo
    try:
        numeroTelefonico = input("Ingrese número telefonico\n")
        cantidadRecarga = input("Ingrese el saldo a recargar\n")
        if (float(cantidadRecarga) <= saldo):
            saldo = saldo - float(cantidadRecarga) 
            print("Se recargo el saldo de: $" + str(cantidadRecarga) + " al número telefonico: " + str(numeroTelefonico)+"\n") 
            verSaldo()
        else:
            print("Saldo insuficiente\n")
    except ValueError as err:
        print("Caracteres invalidos")



def operaciones():
    bandera = True
    while(bandera):
        match ImprimirMenu():
            case 1:
                verSaldo()
            case 2:
                retirar()
            case 3:
                depositar()
            case 4:
                transeferencia()
            case 5:
                RecargaTelefonica()
            case 0:
                bandera = salir()
            case _:
                print("Operacion invalida")


validarUsuario()
