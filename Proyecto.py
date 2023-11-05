usuarios = {}
consultas = {}
#A partir de aquí, se definen cada método según la opción del usuario
def registrar_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cedula = input("Número de Cédula: ")
    tipo_estudiante = input("Tipo de estudiante (1 para Primer Ingreso, 2 para Regular): ")
    
    if tipo_estudiante == '1':
        tipo_estudiante = "Primer Ingreso"
    elif tipo_estudiante == '2':
        tipo_estudiante = "Regular"
    else:
        print("Tipo de estudiante no válido. Debe ser '1' para Primer Ingreso o '2' para Regular.")
        return
    
    usuarios[cedula] = {
        'Nombre': nombre,
        'Apellido': apellido,
        'Tipo Estudiante': tipo_estudiante
    }
    print(f'Usuario con Cédula {cedula} registrado con éxito.')

def enviar_consulta():
    cedula = input("Ingrese su número de cédula: ")
    if cedula in usuarios:
        print("Opciones de destinatario:")
        print("1. Profesores")
        print("2. Servicios Estudiantiles")
        print("3. Administración")
        print("4. Procesos de Matrícula")
        opcion = input("Seleccione el destinatario (1/2/3/4): ")

        destinatarios = {
            '1': "Profesores",
            '2': "Servicios Estudiantiles",
            '3': "Administración",
            '4': "Procesos de Matrícula"
        }

        destinatario = destinatarios.get(opcion, "Otros")

        consulta = input(f"Escriba su consulta para {destinatario}: ")
#Se una el len consultas para poder hacer un contador de las consultas y sumar 1 cada vez que se haga una nueva.
        numero_consulta = len(consultas) + 1
        consultas[numero_consulta] = {
            'Cédula': cedula,
            'Destinatario': destinatario,
            'Consulta': consulta
        }
        print(f"Consulta enviada con éxito (Número de consulta: {numero_consulta}).")
    else:
        print("Usuario con Cédula no registrado. Regístrese primero.")

def ver_consultas(cedula):
    print(f"Consultas realizadas por el usuario con Cédula {cedula}:")
    consultas_usuario = [consulta_info for consulta_info in consultas.values() if consulta_info['Cédula'] == cedula]
    if not consultas_usuario:
        print("Este usuario no ha realizado ninguna consulta.")
    else:
        #El método enumerate quisimos añadirlo para poder encasillar cada consulta, comienza desde el uno.
        for numero, consulta_info in enumerate(consultas_usuario, start=1): 
            print(f"Número de consulta: {numero}")
            print(f"Destinatario: {consulta_info['Destinatario']}")
            print(f"Consulta: {consulta_info['Consulta']}")
            print()

print("---BIENVENIDO A LA MENSAJERÍA DE FIDÉLITAS---")

while True:
    print("Menú:")
    print("1. Registrar usuario")
    print("2. Enviar consulta")
    print("3. Ver consultas realizadas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        enviar_consulta()
    elif opcion == '3':
        cedula = input("Ingrese su número de cédula para ver sus consultas: ")
        ver_consultas(cedula)
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print("---HASTA LUEGO, GRACIAS POR USAR NUESTRO SERVICIO---")
