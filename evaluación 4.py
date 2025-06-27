compradores=[]
def ingreso_codigo():
    print('El código de confirmación debe tener largo mínimo de 6 caracteres')
    print('El código de confirmación debe tener al menos 1 letra mayúscula')
    print('El código de confirmación debe tener al menos 1 número ')
    print('El código de confirmación no puede tener espacio en blanco')
    while True:
        codigo=input('Ingrese código de confirmación:')
        mayuscula=0
        numero=0
        vacio=0
        for l in codigo:
            if l.isupper():
                mayuscula+=1
            if l.isnumeric():
                numero+=1
            if l=="":
                vacio+=1
        if mayuscula>0 and numero>0 or len(codigo)>5 or vacio!=0:
            print('Codigo validado')
            return codigo
        else:
            print('Codigo invalido, intente nuevamente')
            continue


def agregar_cliente(nombre,entrada,codigo):
    comprador={'nombre':nombre,'entrada':entrada,'codigo':codigo}
    compradores.append(comprador)
    print('Entrada registrada con exito')

def consultar_comprador(nombre):
    for i in compradores:
        if nombre==i['nombre']:
            print(f"Tipo de entrada: {i['entrada']}, Codigo: {i['codigo']}")
        else:
            print('El comprador no se encuentra')

def eliminar(nombre):
    for i in compradores:
        if nombre==i['nombre']:
            compradores.remove(i)
            print('¡Compra cancelada!')
        else:
            print('No se a encontrado a un comprador con ese nombre: ')


while True:
    print('_'*50)
    print('Menu principal')
    print('1.- Comprar entrada.')
    print('2.- Consultar comprador.')
    print('3.- Cancelar compra.')
    print('4.- Salir.')
    try:
        opcion=int(input('Ingrese opción: '))
        if opcion>4 or opcion<1:
            raise ValueError
    except ValueError:
        print('Debe ingresar una opción válida!!')
        continue
    if opcion==1:
        nombre=input('Ingrese nombre de comprador: ').capitalize()
        while True:
            entrada=input('Ingrese tipo de entrada (G/V): ').capitalize()
            if entrada=='G' or entrada=='V':
                break
            else:
                print('Debe ingresar una opción válida!!')
                continue
        codigo=ingreso_codigo()
        agregar_cliente(nombre,entrada,codigo)
    elif opcion==2:
        nombre=input('Ingrese nombre de comprador a buscar: ').capitalize()
        consultar_comprador(nombre)
    elif opcion==3:
        nombre=input('Ingrese nombre de comprador a eliminar: ').capitalize()
        eliminar(nombre)

    else:
        print('Programa terminado...')
