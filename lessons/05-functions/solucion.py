def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

def es_par(numero):
    return numero % 2 == 0

numeros = [10, 20, 30, 40, 50]
promedio = calcular_promedio(numeros)
print(f"Números: {numeros}")
print(f"Promedio: {promedio}")

print()
for num in [15, 20, 7, 100]:
    resultado = es_par(num)
    print(f"¿{num} es par? {resultado}")
