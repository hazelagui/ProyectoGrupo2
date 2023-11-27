import os

usuarios = {}
paquetes = {}
facturas = {}
numero_guia_actual = 1

# Crear el archivo si no existe y cargar datos existentes
def inicializar_sistema():
    global usuarios, paquetes, facturas, numero_guia_actual
    if not os.path.exists("basedemensajeria.txt"):
        with open("basedemensajeria.txt", "w") as file:
            file.write("\n\n\n1")
    else:
        with open("basedemensajeria.txt", "r") as file:
            lines = file.readlines()
            usuarios_str = lines[0].strip() if lines else ""
            paquetes_str = lines[1].strip() if len(lines) > 1 else ""
            facturas_str = lines[2].strip() if len(lines) > 2 else ""
            numero_guia_actual = int(lines[3].strip()) if len(lines) > 3 else 1

            if usuarios_str:
                usuarios = eval(usuarios_str)
            if paquetes_str:
                paquetes = eval(paquetes_str)
            if facturas_str:
                facturas = eval(facturas_str)

# Guardar datos en el archivo
def guardar_datos():
    with open("basedemensajeria.txt", "w") as file:
        file.write(str(usuarios) + "\n")
        file.write(str(paquetes) + "\n")
        file.write(str(facturas) + "\n")
        file.write(str(numero_guia_actual))

# Funciones del segundo código

def crear_paquetes(usuario_id):
    print(f"Creando paquete {usuario_id}...")
    paquetes[usuario_id].update({
        'Nombre Destinatario': input("Nombre de destinatario: "),
        'Teléfono Destinatario': input("Teléfono de destinatario: "),
        'Número de Cédula': input("Número de cédula: "),
        'Peso de paquete': input("Peso de paquete(KG): "),
        'Cobro Contra Entrega': input("¿Cobro contra entrega? (Sí/No): ").lower(),
        'Monto de Cobro': float(input("Ingrese el monto a cobrar en colones: "))
            if input("¿Cobro contra entrega? (Sí/No): ").lower() == 'sí'
            else 0.0
    })
    print(f"Paquete {usuario_id} creado con éxito.")
    guardar_datos()

def factura_electronica(usuario_id):
    precio = paquetes[usuario_id]['Precio']
    print(f"Factura del paquete {usuario_id} - Total a pagar: ${precio}")

def crear_guia(usuario_id):
    print(f"Creando guía para el paquete {usuario_id}...")

def cambiar_estado():
    usuario_id = int(input("Ingrese el número de paquete: "))
    if usuario_id in paquetes:
        paquetes[usuario_id]['Estado'] = input("Ingrese el nuevo estado (Creado/Recolectado/Entregado/Entrega fallida): ")
        print(f"Estado del paquete {usuario_id} cambiado a: {paquetes[usuario_id]['Estado']}")
        guardar_datos()
    else:
        print("Número de paquete no válido. Registre el paquete primero.")

def rastrear_paquetes():
    usuario_id = int(input("Ingrese el número de paquete: "))
    if usuario_id in paquetes:
        print(f"Estado actual del paquete {usuario_id}: {paquetes[usuario_id]['Estado']}")
    else:
        print("Número de paquete no válido. Registre el paquete primero.")

# Funciones del primer código

def registrar_usuario():
    correo = input("Correo electrónico: ")
    nombre_comercio = input("Nombre del comercio: ")
    telefono_comercio = input("Teléfono del comercio: ")
    nombre_dueno = input("Nombre del dueño: ")
    ubicacion_local = input("Ubicación del local: ")

    usuarios[correo] = {
        'Nombre Comercio': nombre_comercio,
        'Teléfono Comercio': telefono_comercio,
        'Nombre Dueño': nombre_dueno,
        'Ubicación Local': ubicacion_local
    }

    print(f'Usuario con correo {correo} registrado con éxito.')
    guardar_datos()

def registrar_factura():
    tipo_cedula = input("Tipo de cédula (1 para Nacional / 2 para Extranjero): ")
    numero_cedula = input("Número de cédula: ")
    nombre_registrado = input("Nombre registrado: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    provincia = input("Provincia: ")
    canton = input("Cantón: ")
    distrito = input("Distrito: ")

    facturas[numero_cedula] = {
        'Tipo Cédula': 'Nacional' if tipo_cedula == '1' else 'Extranjero',
        'Número Cédula': numero_cedula,
        'Nombre Registrado': nombre_registrado,
        'Teléfono': telefono,
        'Correo': correo,
        'Provincia': provincia,
        'Cantón': canton,
        'Distrito': distrito
    }

    print('Factura electrónica registrada con éxito.')
    guardar_datos()

def crear_paquete(correo_usuario):
    global numero_guia_actual  # Agregar esta línea para indicar que se usará la variable global
    nombre_destinatario = input("Nombre de destinatario: ")
    telefono_destinatario = input("Teléfono de destinatario: ")
    numero_cedula_destinatario = input("Número de cédula de destinatario: ")
    peso_paquete = float(input("Peso de paquete (Kilogramos): "))
    cobro_contra_entrega = input("¿Cobro contra entrega? (1 para Sí / 2 para No): ")
    
    if cobro_contra_entrega == '1':
        monto_cobro = float(input("Monto a cobrar al momento de entregar el paquete (colones): "))
    else:
        monto_cobro = 0.0

    punto_recoleccion = usuarios[correo_usuario]['Ubicación Local']

    numero_guia = numero_guia_actual
    paquetes[numero_guia] = {
        'Estado': 'Creado',
        'Comercio': usuarios[correo_usuario],
        'Destinatario': {
            'Nombre': nombre_destinatario,
            'Teléfono': telefono_destinatario,
            'Número Cédula': numero_cedula_destinatario
        },
        'Peso': peso_paquete,
        'Cobro Contra Entrega': {
            'Requiere Cobro': cobro_contra_entrega == '1',
            'Monto': monto_cobro
        },
        'Numero Guia': numero_guia
    }
    numero_guia_actual += 1

    print(f'Paquete creado con éxito. Número de guía: {numero_guia}')

    # Cambiar el estado del paquete a 'Recolectado' automáticamente
    paquetes[numero_guia]['Estado'] = 'Recolectado'

    # Mostrar guía
    generar_guia(paquetes[numero_guia])

    guardar_datos()

def generar_guia(paquete):
    print(f"Número de guía: {paquete['Numero Guia']}")
    print("Información de comercio:")
    print(f"Nombre: {paquete['Comercio']['Nombre Comercio']}")
    print(f"Número de teléfono: {paquete['Comercio']['Teléfono Comercio']}")
    print("Información del destinatario:")
    print(f"Nombre: {paquete['Destinatario']['Nombre']}")
    print(f"Teléfono: {paquete['Destinatario']['Teléfono']}")
    print(f"Si requiere cobro, monto a cobrar: {paquete['Cobro Contra Entrega']['Monto']} colones.")

def estadisticas():
    print("Estadísticas:")
    print(f"1. Cantidad total de envíos: {len(paquetes)}")
    print("2. Lista de paquetes enviados:")
    for numero_guia, paquete in paquetes.items():
        print(f"   - Número de guía: {numero_guia}, Estado: {paquete['Estado']}")
    print(f"3. Monto total de cobro: {sum([paquete['Cobro Contra Entrega']['Monto'] for paquete in paquetes.values()])} colones")
    
    # Contar la cantidad de paquetes por número de teléfono
    cantidad_por_telefono = {}
    for paquete in paquetes.values():
        telefono_destinatario = paquete['Destinatario']['Teléfono']
        if telefono_destinatario in cantidad_por_telefono:
            cantidad_por_telefono[telefono_destinatario] += 1
        else:
            cantidad_por_telefono[telefono_destinatario] = 1

    print("4. Cantidad de paquetes por número de teléfono:")
    for telefono, cantidad in cantidad_por_telefono.items():
        print(f"   - Teléfono: {telefono}, Cantidad: {cantidad}")

    # Contar la cantidad de paquetes por número de cédula
    cantidad_por_cedula = {}
    for paquete in paquetes.values():
        numero_cedula_destinatario = paquete['Destinatario']['Número Cédula']
        if numero_cedula_destinatario in cantidad_por_cedula:
            cantidad_por_cedula[numero_cedula_destinatario] += 1
        else:
            cantidad_por_cedula[numero_cedula_destinatario] = 1

    print("5. Cantidad de paquetes por número de cédula:")
    for cedula, cantidad in cantidad_por_cedula.items():
        print(f"   - Cédula: {cedula}, Cantidad: {cantidad}")

# Menú principal
while True:
    print("Menú:")
    print("1. Registrar usuario del comercio")
    print("2. Crear paquete para envío")
    print("3. Registrar Factura Electrónica")
    print("4. Rastrear paquete")
    print("5. Estadísticas generales")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        correo_usuario = input("Ingrese el correo electrónico del usuario del comercio: ")
        if correo_usuario in usuarios:
            crear_paquete(correo_usuario)
        else:
            print("Correo electrónico no válido. Registre el usuario del comercio primero.")
    elif opcion == '3':
        registrar_factura()
    elif opcion == '4':
        rastrear_paquetes()
    elif opcion == '5':
        estadisticas()
    elif opcion == '6':
        print("Guardando datos en el archivo 'datosmensajeriafidelitas.txt'")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
