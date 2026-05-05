import re

def is_valid_name(name):
    return name.strip() != "" and not any(char.isdigit() for char in name)

def is_valid_section(section):
    return re.match(r"^\d{1,2}[A-Za-z]$", section) is not None

def student_exists(students, name, section):
    for student in students:
        if student["name"] == name and student["section"] == section:
            return True
    return False

def request_grade(subject):
    while True:
        try:
            grade = float(input(f"Ingrese nota de {subject}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Nota debe estar entre 0 y 100.")
        except:
            print("Debe ingresar un número válido.")

# ✅ FIX: ahora no se rompe si el usuario mete mal el número
def add_students(students):
    while True:
        try:
            count = int(input("¿Cuántos estudiantes desea ingresar? "))
            break
        except:
            print("Debe ingresar un número válido.")

    for _ in range(count):
        while True:
            name = input("Nombre completo: ")
            if is_valid_name(name):
                break
            print("Nombre inválido.")

        while True:
            section = input("Sección (ej: 11B): ")
            if is_valid_section(section):
                if not student_exists(students, name, section):
                    break
                else:
                    print("Ya existe un estudiante con ese nombre y sección.")
            else:
                print("Sección inválida.")

        student = {
            "name": name,
            "section": section,
            "spanish_grade": request_grade("Español"),
            "english_grade": request_grade("Inglés"),
            "social_studies_grade": request_grade("Sociales"),
            "science_grade": request_grade("Ciencias")
        }

        students.append(student)

# ✅ FIX: ahora se muestra bonito y ordenado
def view_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    print("\n===== LISTA DE ESTUDIANTES =====")
    for student in students:
        avg = calculate_average(student)
        print(f"Nombre: {student['name']}")
        print(f"Sección: {student['section']}")
        print(f"Promedio: {avg:.2f}")
        print("----------------------------")

def calculate_average(student):
    return (
        student["spanish_grade"] +
        student["english_grade"] +
        student["social_studies_grade"] +
        student["science_grade"]
    ) / 4

def top_3_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    sorted_students = sorted(students, key=calculate_average, reverse=True)
    print("\n===== TOP 3 ESTUDIANTES =====")

    for i, student in enumerate(sorted_students[:3], start=1):
        avg = calculate_average(student)
        print(f"{i}. {student['name']} - {avg:.2f}")

def general_average(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    total_sum = 0
    for student in students:
        total_sum += calculate_average(student)

    print(f"Promedio general: {total_sum / len(students):.2f}")

def delete_student(students):
    name = input("Nombre del estudiante a eliminar: ")
    section = input("Sección del estudiante: ")

    for student in students:
        if student["name"] == name and student["section"] == section:
            confirmation = input("¿Seguro que desea eliminarlo? (s/n): ")
            if confirmation.lower() == "s":
                students.remove(student)
                print("Estudiante eliminado.")
                return
            else:
                print("Cancelado.")
                return

    print("Estudiante no encontrado.")

# ✅ FUNCIÓN CORRECTA (independiente, como pidió el profe)
def view_failing_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    print("\n===== ESTUDIANTES REPROBADOS =====")

    found = False

    for student in students:
        avg = calculate_average(student)

        if avg < 70:
            print(f"Nombre: {student['name']}")
            print(f"Sección: {student['section']}")
            print(f"Promedio: {avg:.2f}")
            print("----------------------------")
            found = True

    if not found:
        print("No hay estudiantes reprobados.")