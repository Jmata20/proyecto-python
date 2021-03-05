import numpy as np
import os.path as path
import getpass, time, sys, os
from io import open
from itertools import zip_longest

tienda = {
  "nombre_tienda": "Tienda Simon",
  "sede": "Escazu",
  "departamentos": {
    "Damas": { "productos": []},
    "Caballeros": { "productos": []},
    "Niños": { "productos": []}
  }
}


def validacion_login():
    #Portada

    #Pantalla Principal
    portada='''
    ***Tienda Simón***
    Login
    Favor digite sus datos personales

    '''
    print(portada)
    
    ind=1
    ind_datos=0
    usuarios = {
            "admin": {
                "nombre": "Alejandro Sánchez",
                "password": "admin",
                "rol": 'admin'

        },
            "guest": {
                "nombre": "Josué Mata",
                "password": "guest",
                "rol": 'guest'
        }
    }

    user = input("Escriba su usuario: ")
    password = getpass.getpass("Escriba su password: ")

    while ind!=0:

        if ind_datos==1:
            user = input("Escriba su usuario: ")
            password = getpass.getpass("Escriba su password1: ")

        if user in usuarios and password == usuarios[user]['password']:
            print(f"Bienvenido al Sistema de inventarios de Tienda Simón, {usuarios[user]['nombre']}")
            ind=0
        else:
            print('Datos incorrectos, favor validar!')
            ind=int(input('¿Desea seguir? Pulse 1 para continuar y 0 para salir: '))
            if ind==1:
                ind_datos=1
            else:
                print('Saliendo del sistema...')
                sys.exit()
            continue
    
    rol= usuarios[user]['rol']
    return rol

def validacion_menu(rol):
    ind_validacion_menu=1
    ind_datos_validacion_menu=0
    
    ind_menu_rol=input("Desea ingresar al Menú Principal del Sistema de Inventarios(si/no):")
    creacion_archivos() #Creo los archivos al tener una inición correcta
   
    opcion_rol=ind_menu_rol.lower()
    
    while ind_validacion_menu!=0:
        #print("continuo")

        if ind_datos_validacion_menu==1:
            ind_menu_rol=input("Desea ingresar al Menú Principal de Categorías del Sistema de Inventarios(si/no):")
            opcion_rol=ind_menu_rol.lower()
            
        if opcion_rol== 'si':
            print(
            '''
            1- Damas.
            2. Caballeros.
            3. Niños.
            4. Salir            
            ''')

            opcion_consulta=int(input('Seleccione una opción: '))

            if opcion_consulta==4:
                print("Saliendo del sistema...")
                sys.exit()
            elif  1 <= opcion_consulta <= 3:
                ind_validacion_menu=0
                opciones_menu(rol, opcion_consulta)
            else:
                print("Saliendo del sistema...")
                print("Opción Incorrecta. Digite nuevamente una válida.")
                ind_validacion_menu=int(input('¿Desea seguir? Pulse 1 para continuar y 0 para salir: '))
                if ind_validacion_menu==1:
                    ind_datos_validacion_menu=1
                else:
                    print("Saliendo del sistema...")
                    sys.exit()
        elif opcion_rol=='no':
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción Incorrecta. Digite nuevamente una válida.")
            ind_validacion_menu=int(input('¿Desea seguir? Pulse 1 para continuar y 0 para salir: '))
            if ind_validacion_menu==1:
               ind_datos_validacion_menu=1
            else:
                print("Saliendo del sistema...")
                sys.exit()
                break       
    
def opciones_menu(rol, opcion_consulta):

    print(rol)
    departamentos = {
            1: {
                "nombre": "Damas",

        },
            2: {
                "nombre": "Caballeros",

        },
            3: {
                "nombre": "Niños",

        },
    }

    if opcion_consulta == 1:
        nombre_departamento=departamentos[opcion_consulta]['nombre']
        menu_rol(rol,nombre_departamento)

    elif opcion_consulta == 2:
        nombre_departamento=departamentos[opcion_consulta]['nombre']
        menu_rol(rol,nombre_departamento)
    
    elif opcion_consulta == 3:
        nombre_departamento=departamentos[opcion_consulta]['nombre']
        menu_rol(rol,nombre_departamento)

    elif opcion_consulta==4:
        print("Saliendo del sistema...")
        sys.exit()
    else:
        print('Opción incorrecta')

def opciones_menu_rol(rol, opcion_menu_rol, nombre_departamento): 
    if rol=="admin":

        if opcion_menu_rol==1:  
            print("Consulta de productos")
            time.sleep(0.5)
            consulta_producto(rol,nombre_departamento)
        elif opcion_menu_rol==2:  
            print("Ingrese el producto")
            time.sleep(0.5)
            agrega_producto(rol,nombre_departamento)  
        elif opcion_menu_rol==3:  
            print("Actualice el producto")
            time.sleep(0.5)
            lectura_producto(nombre_departamento)
        elif opcion_menu_rol==4:  
            print("Elimine el producto")
            eliminar_producto(nombre_departamento)
        elif opcion_menu_rol ==5:
                validacion_menu(rol)
        elif opcion_menu_rol ==6:
            time.sleep(0.5)
            union_archivos()  
        else:
            print("Saliendo del programa...")
    else:
        if opcion_menu_rol==1:  
            print("Consulta de productos")
            time.sleep(0.5)
            consulta_producto(rol,nombre_departamento)
        elif opcion_menu_rol ==2:
                validacion_menu(rol)
        else:
            print("Saliendo del programa...")

def menu_rol(rol,nombre_departamento):
    rol_opciones=""
    ind_control_opciones=1

    while ind_control_opciones!=0:

        if rol=="admin":
            #ind_opc_rol=0
            print(f"Menú de productos del departamento {nombre_departamento}")
            rol_opciones ='''
            ***Seleccione una opción***
            1-Consultar.
            2-Ingresar.
            3-Actualizar.
            4-Eliminar.
            5-Volver.
            6-Guardar.
            7-Salir.
            '''
            time.sleep(0.5)
            print(rol_opciones)
            opcion_menu_rol=int(input("Seleccione una opción: "))
            
            if opcion_menu_rol==7:
                print("Saliendo del sistema...")
                sys.exit()
                #break
            
            if opcion_menu_rol==5:
                ind_control_opciones=0

            opciones_menu_rol(rol, opcion_menu_rol, nombre_departamento)

        else:
            print(f"Menú de productos del departamento {nombre_departamento}")
            rol_opciones ='''
            ***Seleccione una opción***
            1-Consultar.
            2-Volver.
            3-Salir.
            '''
            time.sleep(0.5)
            print(rol_opciones)
            opcion_menu_rol=int(input("Seleccione una opción: "))

            if opcion_menu_rol==3:
                print("Saliendo del sistema...")
                sys.exit()
            
            if opcion_menu_rol==2:
                ind_control_opciones=0

            opciones_menu_rol(rol, opcion_menu_rol, nombre_departamento)


def agrega_producto(rol, nombre_departamento):
  
  ind_agregar=1
  ind_agregar_prod=0

  opcion_agrega_producto= input("¿Desea agregar un nuevo producto? (si/no): ")
  opcion_agregar=opcion_agrega_producto.lower()

  while ind_agregar!=0:
        if ind_agregar_prod==1:
            opcion_agrega_producto= input("¿Desea agregar un nuevo producto? (si/no): ")
            opcion_agregar=opcion_agrega_producto.lower()
            
        if opcion_agregar== 'si':
            print('***Agregue un nuevo producto*** ')
            nombre = input('Nombre del producto: ')
            
            time.sleep(0.5)
            while True:
                try:
                    precio = float(input('Precio del producto: '))
                except ValueError:
                    print("Favor digite un formato correcto para el precio.")
                    continue

                if precio < 0 or precio=='':
                    print("Favor digite un número mayor que cero.")
                    continue
                else:
                    break

            time.sleep(0.5)
            while True:
                try:
                    codigo = int(input("Código del producto: "))
                except ValueError:
                    print("Favor digite un formato correcto para el código.")
                    continue

                if codigo < 0 or codigo=='':
                    print("Favor digite un número mayor que cero.")
                    continue
                else:
                    break

            time.sleep(0.5)         
            while True:
                try:
                    cantidad = int(input("Cantidad del producto: "))
                except ValueError:
                    print("Favor digite un formato correcto para la cantidad.")
                    continue

                if cantidad < 0 or cantidad =='':
                    print("Favor digite un número mayor que cero.")
                    continue
                else:
                    break


            producto = {
            "Nombre": nombre,
            "Precio": precio,
            "Codigo": codigo,
            "Cantidad": cantidad,
            }

            tienda['departamentos'][nombre_departamento]['productos'].append(producto)

            if nombre_departamento=='Damas':
                lista= np.array(tienda['departamentos'][nombre_departamento]['productos'])
                np.savetxt('Productos_Damas.txt', lista, fmt='%s')
            elif nombre_departamento=='Caballeros':
                lista= np.array(tienda['departamentos'][nombre_departamento]['productos'])
                np.savetxt('Productos_Caballeros.txt', lista, fmt='%s')
            elif nombre_departamento=='Niños':
                lista= np.array(tienda['departamentos'][nombre_departamento]['productos'])
                np.savetxt('Productos_Niños.txt', lista, fmt='%s')

            time.sleep(0.5)

            ind_continuar=int(input('¿Desea agregar más productos? Pulse 1 para continuar y 0 para salir: '))
            if ind_continuar==1:
                opcion_agregar='si'
            else:
                print("Saliendo...")
                ind_agregar=0
                break
                menu_rol(rol,nombre_departamento)
                #
        elif opcion_agregar=='no':
            print("Saliendo...")
            break
        else:
            print("Opción Incorrecta. Digite nuevamente una válida.")
            ind_continuar=int(input('¿Desea seguir? Pulse 1 para continuar y 0 para salir: '))
            if ind_continuar==1:
               ind_agregar_prod=1
            else:
                print("Saliendo...")
                break     


def consulta_producto(rol,nombre_departamento):  
    time.sleep(0.5)
    
    if nombre_departamento == 'Damas':
        if path.isfile("Productos_Damas.txt") == False: 
            print('No existe el archivo.')
        else:            
            archivo= open("Productos_Damas.txt")
            contenido_archivo= archivo.read()
            if contenido_archivo=='' :
                print('No hay productos en stock.')
            else:
                print(contenido_archivo)
    elif nombre_departamento == 'Caballeros':
        if path.isfile("Productos_Caballeros.txt") == False: 
            print('No existe el archivo.')
        else:            
            archivo= open("Productos_Caballeros.txt")
            contenido_archivo= archivo.read()
            if contenido_archivo=='' :
                print('No hay productos en stock.')
            else:
                print(contenido_archivo)            
    elif nombre_departamento == 'Niños':
        if path.isfile("Productos_Niños.txt") == False: 
            print('No existe el archivo.')
        else:            
            archivo= open("Productos_Niños.txt")
            contenido_archivo= archivo.read()
            if contenido_archivo=='' :
                print('No hay productos en stock.')
            else:
                print(contenido_archivo)
   
 
    menu_rol(rol,nombre_departamento)

def lectura_producto(nombre_departamento):
    
    nombre_archivo=f'Productos_{nombre_departamento}.txt'

    if path.isfile(nombre_archivo) == False: 
            print('No existe el archivo.')
    else:
        buscar_codigo= input('Digite el número de código: ')
        codigo=f"'Codigo': {buscar_codigo}"

        archivo=open(nombre_archivo,"r")
        
        dimension_archivo= (len(archivo.readlines())) # devolvera 3
        linea=archivo.readline()

        #Inicializo dos contadores, uno para obtener el total de las líneas del archivo y uno específico para guardar la línea que deseo modificar
        contador=0
        contador_lineas=1
        ind_codigo=False
        

        while linea!='':
            contador=contador+1
            linea=archivo.readline()
        
            if linea.find(codigo)!= -1:
                contador_lineas=contador_lineas+contador
                respaldo_linea=linea.rstrip()
            else:
                print('Código no existe.')
                ind_codigo=True
                #break
                
        archivo.close()        
        
        if ind_codigo== False:
            #print (f'Linea {contador_lineas}')
            #print (f'Respaldo {respaldo_linea}')
            modificar_archivo(respaldo_linea, contador_lineas, nombre_archivo, buscar_codigo, nombre_departamento)


def modificar_archivo(respaldo_linea, contador_lineas, nombre_archivo, buscar_codigo, nombre_departamento):
    
    #print('Estoy en segunda función')

    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    archivo.close()
    
    archivo = open(nombre_archivo,"w")
    
    for linea in lineas:

        if linea!=respaldo_linea+"\n":
            archivo.write(linea)
        else:
            archivo.write("\n")
    
    archivo.close()

    archivo = open(nombre_archivo,'r+')
    texto = archivo.readlines()
    
    print(contador_lineas)

    print('***Agregue un nuevo producto - Modificado*** ')

    nombre = input('Nombre del producto: ')
    time.sleep(0.5)

    while True:
        try:
            precio = float(input('Precio del producto: '))
        except ValueError:
            print("Favor digite un formato correcto para el precio.")
            continue

        if precio < 0 or precio=='':
            print("Favor digite un número mayor que cero.")
            continue
        else:
            break
            time.sleep(0.5)
          
    while True:
        try:
            cantidad = int(input("Cantidad del producto: "))
        except ValueError:
            print("Favor digite un formato correcto para la cantidad.")
            continue

        if cantidad < 0 or cantidad =='':
            print("Favor digite un número mayor que cero.")
            continue
        else:
            break
   

    a='{'
    b='}'
    producto_modificado=(f"{a}'Nombre': {nombre}, 'Precio': {precio}, 'Codigo': {int(buscar_codigo)}, 'Cantidad': {cantidad}{b}\n")


    texto[contador_lineas-1] = producto_modificado

    #Puntero
    archivo.seek(0)
    archivo.writelines(texto)
    archivo.close()

    print('Fin')


def eliminar_producto(nombre_departamento):
    
    time.sleep(0.5)
    nombre_archivo=f'Productos_{nombre_departamento}.txt'

    if path.isfile(nombre_archivo) == False: 
            print('No existe el archivo.')
    else:
        buscar_codigo= input('Digite el número de código: ')
        codigo=f"'Codigo': {buscar_codigo}"
        
        archivo = open(nombre_archivo,"r")
        lineas = archivo.readlines()
        #archivo.close()

        for linea in lineas:
            if linea.find(codigo) >=0:
                ind_existe_codigo=False
            else:
                ind_existe_codigo=True

        archivo.close()
        
        if ind_existe_codigo==False:
            archivo = open(nombre_archivo,"w")
            for linea in lineas: 
                if linea.find(codigo)!= -1:
                    print('Producto eliminado.')
                else:
                    archivo.write(linea)
        else:
            print('Código digitado NO existe. Favor validar.')
            time.sleep(0.5)

        archivo.close()


def union_archivos():
    
    archivo1="Productos_Caballeros.txt"
    archivo2="Productos_Damas.txt"
    archivo3="Productos_Niños.txt"
    nuevo="nuevo.txt"

    if path.exists(archivo1) and path.exists(archivo2) and path.exists(archivo3):
        with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2, open(archivo3, 'r') as f3, open(nuevo, 'w') as f4:
                for l1, l2, l3 in zip(f1, f2, f3):
                    f4.write(str(l1))
                    f4.write(str(l2))
                    f4.write(str(l3))

                print('Guardando datos...')
    else:
        print('No existe ningún archivo.')


def creacion_archivos():

    archivo1="Productos_Caballeros.txt"
    archivo2="Productos_Damas.txt"
    archivo3="Productos_Niños.txt"
    #
    if path.exists(archivo1):
        print('Cargando inventario...')
    else:
        open(archivo1, "w").close()
    #
    if path.exists(archivo2):
        print('Cargando inventario...')
    else:
        open(archivo2, "w").close()
    
    if path.exists(archivo3):
        print('Cargando inventario...')
    else:
        open(archivo3, "w").close()

    
rol=validacion_login()
validacion_menu(rol)