from datetime import datetime

# Fecha actual
fecha = datetime.now()

# Diccionario, para la cuenta del cliente
no_cuentas = [{"no_cuenta": 1, "Nip": 1235, "Nombre": "Gustavo", "Saldo": 1000}]

# Diccionario para ir registrando los movimientos
movimientos = []

# variables de apoyo
bandera = 1
valores = 0


# Funcion para realizar el registro del movimiento en el diccionario
def registo_movimientos(no_cuenta_registro, fecha_registro, cantida, saldo_anterior_registro, ):
    movimiento = {"no_cuenta": no_cuenta_registro, "fecha": fecha_registro, "movimiento": cantida,
                  "saldo_anterior": saldo_anterior_registro}
    movimientos.append(movimiento)
    no_cuentas[0]["Saldo"] = no_cuentas[0].get("Saldo") - cantida


# Instruccion while para apoyo del programa
while True:
    try:
        # Se solicita introducir el NIP del cliente
        nip = int(input("Digite su NIP: "))
        # Se valida si el nip corresponde con NIP registrado en el diccionario
        # Y se va sumando una variable cada vez que ingrese erroneamente el NIP
        if nip != no_cuentas[0].get("Nip"):
            bandera += 1
            print("Ingreso mal su NIP")
            if bandera > 3:
                print("Supero el numero de intentos en insertar su NIP")
                break
        else:
            # While para trabajar con el menú
            while True:
                print("""\t\t\t\t\t.:MENU:.
                1.- Consultar saldo
                2.- Retirar saldo
                3.- Histórico de Movimientos
                4.- Salir""")

                # Se solicita al usuario colocar una opción del menú
                opcion = int(input("Digite una opcion: "))

                # Bloques de IFs de acuerdo al menu
                # 1.- Se muestra su saldo actual
                if opcion == 1:
                    print(f"Su saldo actual {no_cuentas[0].get('Nombre')} es de ${no_cuentas[0].get('Saldo')} ")
                # 2.- Opcion para realizar un retiro de dinero y haciendo el registro del movimiento
                elif opcion == 2:
                    try:
                        cantidad = int(input("Ingrese la cantidad a retirar: "))
                        modulo = cantidad
                        modulo %= 100
                        # Se valida que la cantida ingresada se modulo de 100, para que solo acepte valores enterros
                        if modulo != 0:
                            print("No es una cantida valida, debe ser multiplo de 100")
                        else:
                            if cantidad > 0:
                                if cantidad < no_cuentas[0].get("Saldo"):
                                    # Se realiza el registro del movimiento
                                    registo_movimientos(no_cuentas[0].get("no_cuenta"), str(fecha), cantidad,
                                                        no_cuentas[0].get("Saldo"))
                                    print(f"Usted ha retirado la cantidad de ${cantidad}")
                                else:
                                    print("Usted no cuenta con el saldo suficiente para retirar")
                            else:
                                print("Debe de ingresar una cantidad mayor a 0")
                    except ValueError:
                        print("Error -> Digite correctamente los valores numericos o sin decimal")
                # 3.- Muestra los movimientos realizados por el usuario por cuenta
                elif opcion == 3:
                    # For para contar se si encuentran registros en el diccionario de movimientos
                    for i in movimientos:
                        if i["no_cuenta"] == no_cuentas[0].get("no_cuenta"):
                            valores += 1
                    if valores > 0:
                        # Se muestran los movimientos realizados por el usuario
                        for i in movimientos:
                            if i["no_cuenta"] == no_cuentas[0].get("no_cuenta"):
                                print(
                                    f"Fecha: {i['fecha']}, Movimiento: -{i['movimiento']}, Saldo Anterior: {i['saldo_anterior']}")
                    else:
                        print("No tiene movimientos realizados, gracias")
                # 4.- Salir del programa
                elif opcion == 4:
                    print("Gracias por utilizar el sistema de cajero automatico")
                    break
                else:
                    print("Se equivoco de opcion de menu")
            break
    except ValueError:
        print("Error -> Digite correctamente los valores numericos")
        bandera += 1
        if bandera > 3:
            print("Supero el numero de intentos en insertar su NIP")
            break
