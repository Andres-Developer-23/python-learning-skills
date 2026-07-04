import subprocess
import sys
from helpers import has_function_call

def test_archivo_existe():
    try:
        with open("lessons/01-intro/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/01-intro/"

def _leer_contenido():
    with open("lessons/01-intro/solucion.py", "r") as f:
        return f.read()

def test_usar_input():
    contenido = _leer_contenido()
    assert has_function_call(contenido, "input"), "No usaste input() para preguntar el nombre"

def test_usar_print():
    contenido = _leer_contenido()
    assert has_function_call(contenido, "print"), "No usaste print() para mostrar mensajes"

def test_usar_len():
    contenido = _leer_contenido()
    assert has_function_call(contenido, "len"), "No usaste len() para contar letras"

def test_ejecucion_correcta():
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
