import json
import os
from datetime import datetime

ARCHIVO = "cocurriculares.json"

# Clases
class Cocurricular:
    def __init__(self, nombre, participantes=None, asistencias=None):
        self.nombre = nombre
        self.participantes = participantes if participantes else []
        self.asistencias = asistencias if asistencias else []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "participantes": self.participantes,
            "asistencias": self.asistencias
        }

#  Funciones de archivo
def guardar(lista):
    with open(ARCHIVO, "w") as f:
        json.dump([c.to_dict() for c in lista], f, indent=2)

def cargar():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        datos = json.load(f)
        return [Cocurricular(d["nombre"], d["participantes"], d["asistencias"]) for d in datos]

# === Menú principal ===
def mostrar_menu():
    lista = cargar()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar cocurricular")
        print("2. Ver cocurriculares")
        print("3. Administrar cocurricular")
        print("4. Salir")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre de cocurricular: ")
            lista.append(Cocurricular(nombre))
            guardar(lista)
            print("Cocurricular agregada.")

        elif op == "2":
            for i, c in enumerate(lista, 1):
                print(f"{i}. {c.nombre}")

        elif op == "3":
            for i, c in enumerate(lista, 1):
                print(f"{i}. {c.nombre}")
            idx = int(input("Seleccione número: ")) - 1

            if 0 <= idx < len(lista):
                administrar(lista[idx])
                guardar(lista)

        elif op == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción inválida")

# === Submenú de administración ===
def administrar(c):
    while True:
        print(f"\n--- {c.nombre.upper()} ---")
        print("1. Ver participantes")
        print("2. Agregar participante")
        print("3. Quitar participante")
        print("4. Registrar asistencia")
        print("5. Ver asistencias")
        print("6. Volver")
        op = input("Opción: ")

        if op == "1":
            if c.participantes:
                for p in c.participantes:
                    print(f"- {p}")
            else:
                print("Sin participantes.")
        elif op == "2":
            nombre = input("Nombre participante: ")
            if nombre not in c.participantes:
                c.participantes.append(nombre)
                print("Participante agregado.")
            else:
                print("Ya existe.")
        elif op == "3":
            nombre = input("Nombre a quitar: ")
            if nombre in c.participantes:
                c.participantes.remove(nombre)
                print("Participante eliminado.")
            else:
                print("No encontrado.")
        elif op == "4":
            if not c.participantes:
                print("No hay participantes.")
                continue
            asistencia = {}
            print("Registrar asistencia (A=asistió, F=faltó)")
            for p in c.participantes:
                estado = input(f"{p}: ").upper()
                asistencia[p] = "Asistió" if estado == "A" else "Faltó"
            c.asistencias.append({
                "fecha": datetime.now().strftime("%Y-%m-%d"),
                "registro": asistencia
            })
            print("Asistencia registrada.")
        elif op == "5":
            if not c.asistencias:
                print("No hay registros.")
            else:
                for a in c.asistencias:
                    print(f"Fecha: {a['fecha']}")
                    for nombre, estado in a["registro"].items():
                        print(f"  {nombre}: {estado}")
        elif op == "6":
            break
        else:
            print("Opción inválida")

# === Ejecutar programa ===
if __name__ == "__main__":
    mostrar_menu()