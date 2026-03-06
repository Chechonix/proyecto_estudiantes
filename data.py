import csv
import os

ARCHIVO = "estudiantes.csv"

def exportar_csv(estudiantes):
    if not estudiantes:
        print("No hay datos para exportar.")
        return

    with open(ARCHIVO, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=estudiantes[0].keys())
        writer.writeheader()
        writer.writerows(estudiantes)

    print("Datos exportados correctamente.")

def importar_csv(estudiantes):
    if not os.path.exists(ARCHIVO):
        print("No existe un archivo previamente exportado.")
        return

    with open(ARCHIVO, mode="r") as file:
        reader = csv.DictReader(file)
        estudiantes.clear()
        for row in reader:
            estudiantes.append({
                "nombre": row["nombre"],
                "seccion": row["seccion"],
                "espanol": float(row["espanol"]),
                "ingles": float(row["ingles"]),
                "sociales": float(row["sociales"]),
                "ciencias": float(row["ciencias"])
            })

    print("Datos importados correctamente.")