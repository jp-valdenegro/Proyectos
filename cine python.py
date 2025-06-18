cartelera=[]
lista_clientes=[]
butacas=[['0','0','0','X'],
         ['X','X','0','0'],
         ['0','0','X','0'],
         ['0','0','X','X']]
def comprobación_inicial():
    if len(cartelera)==0:
        print('Ingrese primero una pelicula')
        return True
    else:
        return False
def ver_cartelera():
    for pelicula in cartelera:
        print(f"titulo: {pelicula['titulo']}")
        print(f"categoria: {pelicula['categoria']}")
        print(f"horarios: {pelicula['horarios']}")
        
def agregar_pelicula(titulo,categoria,horarios):
    pelicula={'titulo':titulo,'categoria':categoria,'horarios':horarios}
    cartelera.append(pelicula)

def agregar_cliente(nombre,rut,edad):
    cliente={'nombre':nombre,'rut': rut,'edad':edad}
    lista_clientes.append(cliente)

def mostrar_butacas():
    for fila in range(len(butacas)):
        print(f'Fila {fila+1}: {butacas[fila]}')

def elegir_butaca():
    mostrar_butacas()
    while True:
        try:
            fila=int(input('ingrese el numero de la fila de su butaca: '))
            asiento=int(input('ingrese el numero de su butaca: '))
        except ValueError:
            print('Opcion no disponible, intente nuevamente ')
            continue
        except IndexError:
            print('Opcion no disponible, intente nuevamente ')
            continue
        if  butacas[fila-1][asiento-1]!='X':
            butacas[fila-1][asiento-1]='X'
            print('Butaca comprada con exito')
            break
        else:
            print('No puede elegir esa butaca, porfavor elija otra')
            continue
def precios(precio):
    while True:
        try:
            promo=int(input('¿Desea agregar una promo? Si(1)/No(2): '))
            if promo==1:
                tipo=int(input('Elija el tipo de promo: \nCabritas: Tamaño M | Precio: 2000 \nCabritas: Tamaño L | Precio: 3000 \nCabritas: Tamaño XL | Precio: 4000 '))
                if tipo==1:
                    precio+=2000
                elif tipo==2:
                    precio+=3000
                elif tipo==3:
                    precio+=2000
                else:
                    raise ValueError
            elif promo==2:
                return
            else:
                raise ValueError
        except ValueError:
            print('ERROR. Intente nuevamente')
            continue
        return precio
def descuento(precio):
    rut=input('ingrese su rut (sin puntos y con guion): ')
    for cliente in lista_clientes:
        if rut==cliente['rut']:
            precio=precio*0.8
        else:
            precio=precio
    return precio
def boleta(precio):
    print('Boleta')
    print('-'*60)
    print(f'Precio final: {precio}')
    while True:
        try:
            compra=int(input('¿Desea efectuar la compra? Si(1)/No(2): '))
            if compra==1:
                print('Compra realizada con exito')
            elif compra==2:
                print('Se le devolvera el menu inicial')
            else:
                raise ValueError
        except ValueError:
            print('Error, elija nuevamente')
            continue
        
def compra_entrada(titulo):
    for pelicula in cartelera:
        if pelicula['titulo']== titulo:
            precio=3000
            elegir_butaca()
            precio=precios(precio)
            precio=descuento(precio)
            boleta(precio) 
            return   
    print('no se encuetra la pelicula ingresada')

while True:
    print('=== 🎬 CINE PYTHON ===')
    print('1. 📜 Ver Cartelera  \n2. ➕ Registrar Nueva Película  \n3. 💺 Ver Butacas  \n4. 👤 Registrar Cliente  \n5. 🎟️ Comprar Entrada/Promo  \n6. 🚪 Salir  ')
    try:
        opcion=int(input('Ingrese la opcion a realizar: '))
        if opcion<1 or opcion>6:
            raise ValueError
    except ValueError:
        print('Ingrese solo los valores correspodientes')
        continue

    if opcion==1:
        if comprobación_inicial():
            continue
        ver_cartelera()
    elif opcion==2:
        titulo=input('ingrese el titulo de la pelicula: ').capitalize()
        categoria=input('ingrese la categoria de la pelicula: ').capitalize()
        horarios=[]
        for i in range(3):
            if len(horarios)==0:
                 horario=input("Ingrese el  primer horario de la película(formato hh:mm): ")
            else:
                horario=input("Ingrese el  siguiente horario de la película(formato hh:mm): ") 
            horarios.append(horario)
        agregar_pelicula(titulo,categoria,horarios)
    elif opcion==3:
        mostrar_butacas()
    elif opcion==4:
        while True:
            nombre=input('ingrese su nombre: ').capitalize()
            rut=input('ingrese su rut (sin puntos y con guion): ')
            try:
                edad=int(input('ingrese su edad'))
                if edad<1:
                    raise ValueError
            except ValueError:
                print('no se admite esa clase de dato, intente nuevamente')
                continue
            break
        agregar_cliente(nombre,rut,edad)
    elif opcion==5:
        if comprobación_inicial():
            continue
        titulo=input('ingrese el titulo de la pelicula: ').capitalize()
        compra_entrada(titulo)
    else:
        print('Saliendo...')
        exit() 