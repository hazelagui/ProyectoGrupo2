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
