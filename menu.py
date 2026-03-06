from actions import (
    ingresar_estudiantes,
    ver_estudiantes,
    top_3_estudiantes,
    promedio_general,
    eliminar_estudiante,
    ver_reprobados
)
from data import exportar_csv, importar_csv

def mostrar_menu(estudiantes):
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

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_estudiantes(estudiantes)
        elif opcion == "2":
            ver_estudiantes(estudiantes)
        elif opcion == "3":
            top_3_estudiantes(estudiantes)
        elif opcion == "4":
            promedio_general(estudiantes)
        elif opcion == "5":
            exportar_csv(estudiantes)
        elif opcion == "6":
            importar_csv(estudiantes)
        elif opcion == "7":
            eliminar_estudiante(estudiantes)
        elif opcion == "8":
            ver_reprobados(estudiantes)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("⚠ Opción inválida. Intente nuevamente.")