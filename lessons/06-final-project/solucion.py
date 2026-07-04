def obtener_cualificacion(nota):
    if nota >= 90:
        return "Sobresaliente"
    elif nota >= 70:
        return "Notable"
    elif nota >= 50:
        return "Aprobado"
    else:
        return "Suspenso"

def calcular_promedio_grupo(estudiantes):
    if not estudiantes:
        return 0
    total = sum(e["nota"] for e in estudiantes)
    return total / len(estudiantes)

estudiantes = []

num_estudiantes = int(input("¿Cuántos estudiantes vas a registrar? "))

for i in range(num_estudiantes):
    print(f"\nEstudiante {i + 1}:")
    nombre = input("¿Nombre? ")
    nota = float(input("¿Nota? "))
    cualificacion = obtener_cualificacion(nota)
    estudiantes.append({"nombre": nombre, "nota": nota, "cualificacion": cualificacion})

print("\n=== RESUMEN DEL GRUPO ===")
for est in estudiantes:
    print(f"{est['nombre']} - Nota: {est['nota']:.0f} - {est['cualificacion']}")

promedio = calcular_promedio_grupo(estudiantes)
print(f"\nPromedio del grupo: {promedio:.1f}")
