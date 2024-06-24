#1 Añadir contacto:
def anadir_contacto(lista, nombre, telefono, correo):
    anadir = {'nombre': nombre, 'telefono': telefono, 'correo': correo, 'favorito': False}
    lista.append(anadir)

    print(f'\n¡Se ha añadido el contacto: {nombre}!')
    return

#2 Ver ocntacto
def ver_contactos(lista):
    if lista == []:
        print('\nNo hay ningún contacto añadido.\nAgrega un nuevo contacto desde la opción [1]')
    else:
        print('\nLista de contactos:')
        for indice, listado in enumerate(lista, start=1):

            favorito = '★' if listado['favorito'] == True else ' '

            print(f'{indice}. [{favorito} ] Nombre: {listado['nombre']}, Teléfono: {listado['telefono']}, Correo: {listado['correo']}')
    return

#3 Editar un contacto:
def editar_contacto_todo(indice_correcto, lista, nombre, telefono, correo):
    lista[indice_correcto]['nombre'] = nombre
    lista[indice_correcto]['telefono'] = telefono
    lista[indice_correcto]['correo'] = correo
    print('¡Se han actualizado los datos del contacto!')
    return

def editar_contacto_nombre(indice_correcto, lista, nombre):
    lista[indice_correcto]['nombre'] = nombre
    print('¡Se ha actualizado el nombre delcontacto!')
    return

def editar_contacto_telefono(indice_correcto, lista, telefono):
    lista[indice_correcto]['telefono'] = telefono
    print('¡Se ha actualizado el telefono del contacto!')
    return

def editar_contacto_correo(indice_correcto, lista, correo):
    lista[indice_correcto]['correo'] = correo
    print('¡Se ha actualizado el correo del contacto!')
    return

#4 Marcar/desmarcar como favorito
def marcar_desmarcar_como_favorito(indice, lista):
    indice_correcto = int(indice) - 1
    if indice_correcto >= 0 and indice_correcto < len(lista):
        if lista[indice_correcto]['favorito'] == False:
            lista[indice_correcto]['favorito'] = True
        else:
            lista[indice_correcto]['favorito'] = False
    else:
        print(f'\nNo se ha encontrado el contacto [{indice}].\n¡Operación cancelada!')
    return

#5 Visualizar favoritos
def visualizar_favoritos(lista):
    if lista == []:
        print('\nNo hay ningún contacto añadido.\nAgrega un nuevo contacto desde la opción [1]')
    else:
        hay_favoritos = False
        print('\nLista de contactos favoritos ★ :')
        for indice, listado in enumerate(lista, start=1):
            if listado['favorito'] == True:
                print(f'{indice}. [★] Nombre: {listado['nombre']}, Teléfono: {listado['telefono']}, Correo: {listado['correo']}')
        if not hay_favoritos:
            print(f'¡No hay contactos marcados como favorito!\nSe puede marcar un contacto como favorito [★] desde la opción [4]')
    return

#6 Eliminar contacto
def eliminar_contacto(indice, lista):
    indice_correcto = int(indice) -1
    if indice_correcto >= 0 and indice_correcto < len(lista):
        del lista[indice_correcto]
        print(f'¡Se ha eliminado el contacto {indice}')
    else:
        print(f'\nNo se ha encontrado el contacto [{indice}].\n¡Operación cancelada!')
    return