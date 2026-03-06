import re

def is_valid_name(nombre):
    return nombre.strip() != "" and not any(char.isdigit() for char in nombre)

def is_valid_section(seccion):
    return re.match(r"^\d{1,2}[A-Za-z]$", seccion) is not None

def student_exists(estudiantes, nombre, seccion):
    for est in estudiantes:
        if est["nombre"] == nombre and est["seccion"] == seccion:
            return True
    return False

def pedir_nota(materia):
    while True:
        try:
            nota = float(input(f"Ingrese nota de {materia}: "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("Nota debe estar entre 0 y 100.")
        except:
            print("Debe ingresar un número válido.")

def ingresar_estudiantes(estudiantes):
    try:
        n = int(input("¿Cuántos estudiantes desea ingresar? "))
    except:
        print("Debe ingresar un número válido.")
        return

    for _ in range(n):
        while True:
            nombre = input("Nombre completo: ")
            if is_valid_name(nombre):
                break
            print("Nombre inválido.")

        while True:
            seccion = input("Sección (ej: 11B): ")
            if is_valid_section(seccion):
                if not student_exists(estudiantes, nombre, seccion):
                    break
                else:
                    print("Ya existe un estudiante con ese nombre y sección.")
            else:
                print("Sección inválida.")

        estudiante = {
            "nombre": nombre,
            "seccion": seccion,
            "espanol": pedir_nota("Español"),
            "ingles": pedir_nota("Inglés"),
            "sociales": pedir_nota("Sociales"),
            "ciencias": pedir_nota("Ciencias")
        }

        estudiantes.append(estudiante)

def ver_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for est in estudiantes:
        print(est)

def calcular_promedio(est):
    return (est["espanol"] + est["ingles"] + est["sociales"] + est["ciencias"]) / 4

def top_3_estudiantes(estudiantes):
    if len(estudiantes) < 1:
        print("No hay estudiantes registrados.")
        return

    ordenados = sorted(estudiantes, key=calcular_promedio, reverse=True)
    print("\n--- TOP 3 ---")
    for est in ordenados[:3]:
        print(est["nombre"], "-", calcular_promedio(est))

def promedio_general(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    suma = 0
    for est in estudiantes:
        suma += calcular_promedio(est)

    print("Promedio general:", suma / len(estudiantes))

def eliminar_estudiante(estudiantes):
    nombre = input("Nombre del estudiante a eliminar: ")
    seccion = input("Sección del estudiante: ")

    for est in estudiantes:
        if est["nombre"] == nombre and est["seccion"] == seccion:
            confirmacion = input("¿Seguro que desea eliminarlo? (s/n): ")
            if confirmacion.lower() == "s":
                estudiantes.remove(est)
                print("Estudiante eliminado.")
                return
            else:
                print("Cancelado.")
                return

    print("Estudiante no encontrado.")

def ver_reprobados(estudiantes):
    for est in estudiantes:
        materias_reprobadas = []
        for materia in ["espanol", "ingles", "sociales", "ciencias"]:
            if est[materia] < 60:
                materias_reprobadas.append((materia, est[materia]))

        if materias_reprobadas:
            print(f"\n{est['nombre']} - {est['seccion']}")
            for m in materias_reprobadas:
                print(f"{m[0]}: {m[1]}")