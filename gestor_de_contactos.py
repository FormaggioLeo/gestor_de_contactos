# TODO - Validar nombre, telefono y mail

import modulos_gestor

lista = []

while True:
    print('\nMenú del gestor de contactos, elija una opción:')

    print('\n1. Añadir contacto')
    print('2. Ver contactos')
    print('3. Editar contacto')
    print('4. Marcar/Desmarcar como favorito')
    print('5. Visualizar favoritos')
    print('6. Eliminar contacto')
    print('7. Salir')

    eleccion = input('\nEscribe tu elección: ')

    #1 Añadir contacto:
    if eleccion == '1':
        print('\nNecesitaremos los siguientes datos para añadirle: ')
        nombre = str(input('Nombre: '))
        telefono = int(input('Telefono: '))
        correo = str(input('Correo: '))
        modulos_gestor.anadir_contacto(lista, nombre, telefono, correo)

    #2 Ver ocntacto
    if eleccion == '2':
        modulos_gestor.ver_contactos(lista)

    #3 Editar contacto:
    if eleccion == '3':
        if lista == []:
            print('\nNo hay ningún contacto añadido para editarlo.\nAgrega un nuevo contacto desde la opción [1]')
        else:
            modulos_gestor.ver_contactos(lista)
            indice = input('\nEscriba el numero del contacto para editarlo: ')
            indice_correcto = int(indice) - 1
            if indice_correcto >= 0 or indice_correcto < len(lista):    
                contacto_editado = print(f'Que deseas editar en el contacto {indice}?')
                dato_contacto_editar = str(input('Escriba:\n[Todo] Para todo el contacto.\n[N] Para nombre\n[T] Para telefono\n[C] Para correo\n[S] Para salir\n> ')).lower()
            
                if dato_contacto_editar == 'todo': # Editar todo
                    print(f'\nEscriba los datos del contacto [{indice}] modificado: ')
                    nombre = str(input('Nombre: '))
                    telefono = int(input('Telefono: '))
                    correo = str(input('Correo: '))
                    modulos_gestor.editar_contacto_todo(indice_correcto, lista, nombre, telefono, correo)

                elif dato_contacto_editar == 'n': # Editar nombre
                    nombre = str(input(f'\nEscriba el nombre a ser editado del contacto [{indice}]: '))
                    modulos_gestor.editar_contacto_nombre(indice_correcto, lista, nombre)

                elif dato_contacto_editar == 't': # Editar telefono
                    telefono = str(input(f'\nscriba el telefono a ser editado del contacto [{indice}]: '))
                    modulos_gestor.editar_contacto_telefono(indice_correcto, lista, telefono)

                elif dato_contacto_editar == 'c': # Editar correo
                    correo = str(input(f'\nEscriba el correo a ser editado del contacto [{indice}]: '))
                    modulos_gestor.editar_contacto_correo(indice_correcto, lista, correo)

                elif dato_contacto_editar == 's': # Salir
                    print('\nOperación cancelada, ¡elija una nueva opción!')

                else: # Editar/Invalido
                    print('\nOpción invalida, ¡operación cancelada!')
            else:
                print(f'\nNo se ha encontrado el contacto [{indice}].\n¡Operación cancelada!')
            
    
    #4 Marcar/desmarcar como favorito
    if eleccion == '4':
        modulos_gestor.ver_contactos(lista)
        indice = input('Escriba el numero del contacto que deseas cambiar el status de favorito: ')
        modulos_gestor.marcar_desmarcar_como_favorito(indice, lista)
    
    #5 Visualizar favoritos
    if eleccion == '5':
        modulos_gestor.visualizar_favoritos(lista)
    
    #6 Eliminar contacto
    if eleccion == '6':
        modulos_gestor.ver_contactos(lista)
        indice = input('Elija un contacto para eliminarlo: ')
        modulos_gestor.eliminar_contacto(indice, lista)