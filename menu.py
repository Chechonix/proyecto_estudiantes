from actions import (
    add_students,
    view_students,
    top_3_students,
    general_average,
    delete_student,
    view_failing_students
)
from data import export_to_csv, import_from_csv

def show_menu(students):
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ingresar estudiantes")
        print("2. Ver todos los estudiantes")
        print("3. Ver Top 3 estudiantes")
        print("4. Ver promedio general")
        print("5. Exportar datos a CSV")
        print("6. Importar datos desde CSV")
        print("7. Eliminar estudiante")
        print("8. Ver estudiantes reprobados")
        print("9. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            add_students(students)
        elif option == "2":
            view_students(students)
        elif option == "3":
            top_3_students(students)
        elif option == "4":
            general_average(students)
        elif option == "5":
            export_to_csv(students)
        elif option == "6":
            import_from_csv(students)
        elif option == "7":
            delete_student(students)
        elif option == "8":
            view_failing_students(students)
        elif option == "9":
            print("Saliendo del programa...")
            break
        else:
            print("⚠ Opción inválida. Intente nuevamente.")