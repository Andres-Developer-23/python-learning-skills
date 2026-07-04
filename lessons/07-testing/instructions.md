# 🧪 Lección 7: Testing con Python

## 🎯 Objetivo
Aprender a escribir pruebas automáticas con `assert` y pytest.

## 📝 Tu tarea
Crea un programa que:
1. Defina funciones matemáticas básicas:
   - `sumar(a, b)` → devuelve `a + b`
   - `restar(a, b)` → devuelve `a - b`
   - `multiplicar(a, b)` → devuelve `a * b`
   - `dividir(a, b)` → devuelve `a / b` (si b != 0), o `"Error"` si b == 0
2. Defina una función `ejecutar_pruebas()` que:
   - Use `assert` para verificar que cada función funciona correctamente
   - Imprima "✓" si pasa, "✗" si falla
   - Devuelva True si todas pasan, False si alguna falla
3. Llame a `ejecutar_pruebas()` al final

## 🔧 Requisitos
- Define las 4 funciones matemáticas
- Usa `assert` para las pruebas
- La función `ejecutar_pruebas()` debe manejar casos normales y casos borde
- El programa debe ejecutarse sin errores

## 💡 Ejemplo de salida

```
✓ sumar(2, 3) = 5
✓ restar(10, 4) = 6
✓ multiplicar(3, 4) = 12
✓ dividir(10, 2) = 5.0
✓ dividir(5, 0) = Error
✓ Todas las pruebas pasaron
```

## 💡 Pista
Usa `assert expresion, "mensaje"` para verificar resultados esperados.

```python
def sumar(a, b):
    return a + b

def ejecutar_pruebas():
    assert sumar(2, 3) == 5, "sumar(2, 3) debería ser 5"
    assert restar(10, 4) == 6, "restar(10, 4) debería ser 6"
    # ... más pruebas
    return True
```

## 🚀 ¡Manos a la obra!
Escribe tu código en un archivo llamado `solucion.py`
