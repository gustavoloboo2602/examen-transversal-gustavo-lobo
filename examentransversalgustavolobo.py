def validar_codigo(codigo, planes):
    if not codigo or codigo.strip() == "":
        return False
    lista_mayusculas = []
    for clave in planes.keys():
        lista_mayusculas.append(clave.upper())
    if codigo.upper() in lista_mayusculas:
        return False
    return True

def validar_nombre(nombre):
    if not nombre or nombre.strip() == "":
        return False
    return True

def validar_tipo(tipo):
    if tipo.lower() == 'mensual' or tipo.lower() == 'trimestral' or tipo.lower() == 'anual':
        return True
    return False

def validar_duracion(duracion_str):
    try:
        duracion = int(duracion_str)
        if duracion > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_piscina(piscina_str):
    if piscina_str.lower() == 's' or piscina_str.lower() == 'n':
        return True
    return False

def validar_clases(clases_str):
    if clases_str.lower() == 's' or clases_str.lower() == 'n':
        return True
    return False

def validar_horario(horario):
    if not horario or horario.strip() == "":
        return False
    return True

def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        if precio > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_cupos(cupos_str):
    try:
        cupos = int(cupos_str)
        if cupos >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def leer_opcion():
    try:
        opcion_str = input("Ingrese opción: ")
        opcion = int(opcion_str)
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            return -1
    except ValueError:
        return -1

def cupos_tipo(tipo, planes, inscripciones):
    total_cupos = 0
    tipo_buscado = tipo.lower()
    for codigo, datos in planes.items():
        if datos[1].lower() == tipo_buscado:
            if codigo in inscripciones:
                total_cupos = total_cupos + inscripciones[codigo][1]
    print("El total de cupos disponibles es:", total_cupos)

def busqueda_precio(p_min, p_max, planes, inscripciones):
    resultados = []
    for codigo, datos_ins in inscripciones.items():
        precio = datos_ins[0]
        cupos = datos_ins[1]
        if precio >= p_min and precio <= p_max and cupos > 0:
            if codigo in planes:
                nombre_plan = planes[codigo][0]
                resultados.append(nombre_plan + "--" + codigo)
    if len(resultados) == 0:
        print("No hay planes en ese rango de precios.")
    else:
        resultados.sort()
        print("Los planes encontrados son:", resultados)

def buscar_codigo(codigo, diccionario):
    codigo_buscado = codigo.upper()
    for clave in diccionario.keys():
        if clave.upper() == codigo_buscado:
            return True
    return False

def obtener_clave_real(codigo, diccionario):
    for clave in diccionario.keys():
        if clave.upper() == codigo.upper():
            return clave
    return codigo

def actualizar_precio(codigo, nuevo_precio, inscripciones):
    if buscar_codigo(codigo, inscripciones):
        clave_real = obtener_clave_real(codigo, inscripciones)
        inscripciones[clave_real][0] = nuevo_precio
        return True
    return False

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones):
    if buscar_codigo(codigo, planes):
        return False
    if acceso_piscina.lower() == 's':
        piscina_bool = True
    else:
        piscina_bool = False
    if incluye_clases.lower() == 's':
        clases_bool = True
    else:
        clases_bool = False
    planes[codigo] = [nombre, tipo.lower(), int(duracion), piscina_bool, clases_bool, horario]
    inscripciones[codigo] = [int(precio), int(cupos)]
    return True

def eliminar_plan(codigo, planes, inscripciones):
    if buscar_codigo(codigo, planes):
        clave_real_planes = obtener_clave_real(codigo, planes)
        clave_real_ins = obtener_clave_real(codigo, inscripciones)
        del planes[clave_real_planes]
        del inscripciones[clave_real_ins]
        return True
    return False

def main():
    planes = {
        'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
        'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
        'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
        'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
        'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
        'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
    }
    inscripciones = {
        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15]
    }
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por tipo de plan")
        print("2. Búsqueda de planes por rango de precio")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("=====================================")
        
        opcion = leer_opcion()
        if opcion == -1:
            print("Debe seleccionar una opción válida")
            continue
            
        if opcion == 1:
            tipo = input("Ingrese tipo de plan a consultar: ")
            cupos_tipo(tipo, planes, inscripciones)
            
        elif opcion == 2:
            while True:
                try:
                    p_min_str = input("Ingrese precio mínimo: ")
                    p_min = int(p_min_str)
                    p_max_str = input("Ingrese precio máximo: ")
                    p_max = int(p_max_str)
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max, planes, inscripciones)
                        break
                    else:
                        print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código del plan: ")
                nuevo_precio_str = input("Ingrese nuevo precio: ")
                try:
                    nuevo_precio = int(nuevo_precio_str)
                    if nuevo_precio > 0:
                        if actualizar_precio(codigo, nuevo_precio, inscripciones):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("Debe ingresar valores válidos")
                except ValueError:
                    print("Debe ingresar valores enteros")
                resp = input("¿Desea actualizar otro precio (s/n)?: ")
                if resp.lower() != 's':
                    break
                    
        elif opcion == 4:
            codigo = input("Ingrese código del plan: ")
            nombre = input("Ingrese nombre del plan: ")
            tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
            duracion = input("Ingrese duración (meses): ")
            piscina = input("¿Incluye acceso a piscina? (s/n): ")
            clases = input("¿Incluye clases grupales? (s/n): ")
            horario = input("Ingrese horario: ")
            precio = input("Ingrese precio: ")
            cupos = input("Ingrese cupos: ")
            
            if not validar_codigo(codigo, planes):
                print("Debe ingresar valores válidos")
            elif not validar_nombre(nombre):
                print("Debe ingresar valores válidos")
            elif not validar_tipo(tipo):
                print("Debe ingresar valores válidos")
            elif not validar_duracion(duracion):
                print("Debe ingresar valores válidos")
            elif not validar_piscina(piscina):
                print("Debe ingresar valores válidos")
            elif not validar_clases(clases):
                print("Debe ingresar valores válidos")
            elif not validar_horario(horario):
                print("Debe ingresar valores válidos")
            elif not validar_precio(precio):
                print("Debe ingresar valores válidos")
            elif not validar_cupos(cupos):
                print("Debe ingresar valores válidos")
            else:
                exito = agregar_plan(codigo, nombre, tipo, duracion, piscina, clases, horario, precio, cupos, planes, inscripciones)
                if exito:
                    print("Plan agregado")
                else:
                    print("El código ya existe")
                    
        elif opcion == 5:
            codigo = input("Ingrese código del plan: ")
            if eliminar_plan(codigo, planes, inscripciones):
                print("Plan eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()