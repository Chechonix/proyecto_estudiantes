import csv
import os

FILE_NAME = "students.csv"

def export_to_csv(students):
    if not students:
        print("No hay datos para exportar.")
        return

    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)

    print("Datos exportados correctamente.")

def import_from_csv(students):
    if not os.path.exists(FILE_NAME):
        print("No existe un archivo previamente exportado.")
        return

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        students.clear()
        for row in reader:
            students.append({
                "name": row["name"],
                "section": row["section"],
                "spanish_grade": float(row["spanish_grade"]),
                "english_grade": float(row["english_grade"]),
                "social_studies_grade": float(row["social_studies_grade"]),
                "science_grade": float(row["science_grade"])
            })

    print("Datos importados correctamente.")