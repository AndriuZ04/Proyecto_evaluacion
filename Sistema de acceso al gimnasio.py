
miembros_pins = ["1234", "5678", "9012"]          
miembros_edades = [18, 25, 16]                    
estados_membresia = ["activa", "activa", "activa"]


costo_membresia = 30000

def calcular_pase_casual():
    pase = costo_membresia * 0.04   
    return int(pase)                

def verificar_edad():
    while True:
        edad_texto = input("Ingrese su edad: ")
        if edad_texto.isdigit():   
            edad = int(edad_texto)
            if edad >= 14:
                print("Edad permitida. Puede continuar.")
                return edad
            else:
                print("Edad mínima 14 años. Acceso denegado.")
        else:
            print("Por favor ingrese solo números.")

def menu_principal():
    print("=====================================")
    print("  CONTROL DE ACCESO - GIMNASIO     ")
    print("=====================================")
    print("1. Ingresar con PIN (miembro)")
    print("2. Soy nuevo / pase casual")
    print("3. Salir")
    print("=====================================\n")


while True:
    menu_principal()
    opcion = input("Elija una opción: \n")

    if opcion == "1":
        pin_ingresado = input("Ingrese su PIN: \n")
        
        encontrado = False
        i = 0
        miembros_pins.append(pin_ingresado)
        while i < len(miembros_pins):
            if miembros_pins[i] == pin_ingresado:
                encontrado = True
                if estados_membresia[i] == "activa":
                    print("PIN correcto - Membresía activa")
                    print("¡Puerta abierta! Bienvenido.")
                else:
                    print("Membresía vencida o suspendida.")
                    print("Acceso denegado.")
                    break
            i = i + 1
        
        if encontrado == False:
            print("PIN incorrecto.")
            break
    elif opcion == "2":
        print("¿Qué desea hacer?")
        print("a) Registrarme como miembro nuevo")
        print("b) Comprar pase casual (día)")
        sub_opcion = input("Elija una opción:\n").lower()

        if sub_opcion == "a":
            edad = verificar_edad()
            if edad == -1:
                print("Registro cancelado.")
            else:
                intentos = 0
                while intentos < 3:
                    nuevo_pin = input("Cree su PIN de 4 dígitos: ")

        if sub_opcion == "a":
            edad = verificar_edad()
            if edad == -1:
                print("Registro cancelado.")
                break
            else:
                nuevo_pin = input("Cree su PIN de 4 dígitos: ")
                miembros_pins.append(nuevo_pin)
                miembros_edades.append(edad)
                estados_membresia.append("activa")
                print("Registro completado.\n")
                print("¡Puerta abierta! Bienvenido.\n")

        elif sub_opcion == "b":
            valor_pase = calcular_pase_casual()
            print("El pase casual cuesta:", valor_pase, "pesos")
            pago = input("¿Pagó el pase? (si/no):\n").lower()
            if pago == "si":
                pin_temporal = "9999"
                miembros_pins.append(pin_temporal)
                print("Pago procesado.\n")
                print("Su PIN temporal es:\n", pin_temporal)
                print("Ingrese este PIN para entrar hoy.\n")
                print("¡Puerta abierta por hoy!\n")
            else:
                print("Pago no realizado. Acceso denegado.")
                break
        else:
            print("Opción inválida.")

    elif opcion == "3":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")