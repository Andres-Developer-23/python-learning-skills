import subprocess
import sys

def test_archivo_existe():
    """Verifica que el archivo existe"""
    try:
        with open("lessons/01-intro/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/01-intro/"

def test_usar_input():
    """Verifica que usa input()"""
    with open("lessons/01-intro/solucion.py", "r") as f:
        contenido = f.read()
        assert "input(" in contenido, "No usaste input() para preguntar el nombre"

def test_usar_print():
    """Verifica que usa print()"""
    with open("lessons/01-intro/solucion.py", "r") as f:
        contenido = f.read()
        assert "print(" in contenido, "No usaste print() para mostrar mensajes"

def test_ejecucion_correcta():
    """Ejecuta el programa y verifica que funciona"""
    resultado = subprocess.run(
        [sys.executable, "lessons/01-intro/solucion.py"],
        input="Ana\n",
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa tiene errores"
    salida = resultado.stdout
    assert "Ana" in salida, "No muestra el nombre correctamente"
    assert "3" in salida or "tres" in salida.lower(), "No muestra la cantidad de letras"
