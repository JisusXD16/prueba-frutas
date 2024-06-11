frutas = {
    'platano' : 1.35,
    'manzana' : 0.80,
    'pera' : 0.85,
    'naranja' : 0.70
}

# Funcion para visualizar el precio del producto
def visualizar():
    print('Las frutas disponibles y su precio por kilo son: \nplatano = 1.35€. \nmanzana = 0.80€. \npera = 0.85€. \nnaranja = 0.70€.')

            
def calcular():
    fruta = input('Introduce la fruta a la que quieres calcular su precio').lower()
    while True:
        try:
            kg = float(input('Introduce la cantidad de kilos de fruta que quieres'))
            break
        except ValueError:
            print('Introduce un valor valido')
        
    if fruta in frutas.keys():
        precio = frutas[fruta] * kg
        print(f'{kg} kilos de {fruta} tienen un precio de {precio}€ ')
    else:
        print('Opcion no valida')
            
    # Funcion principal
def principal():
    while True:
        print('Bienvenido elije una opcion del programa: \n1.- Visualizar el precio de un producto. \n2.- Calcular el precio segun los kilos. \n3.- Salir.') 
        opcion = int(input('Introduce una de las opciones'))
        match opcion:
            case 1:
                print('Has elegido visualizar el precio de un producto')
                visualizar()
            case 2:
                print('Has elegido calcular el precio segun los kilos introducidos')
                calcular()
            case 3:
                print('Saliendo del programa')
                break
            case _:
                print('Opcion no valida. \nSaliendo del programa.')
                break            
principal()