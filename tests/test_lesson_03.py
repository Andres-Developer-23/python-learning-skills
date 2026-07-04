import subprocess
import sys
from helpers import has_function_call, has_if, has_elif, has_else

def test_archivo_existe():
    try:
        with open("lessons/03-conditionals/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/03-conditionals/"

def _leer_contenido():
    with open("lessons/03-conditionals/solucion.py", "r") as f:
        return f.read()

def test_tiene_condicionales():
    contenido = _leer_contenido()
    assert has_if(contenido), "No usaste if para condicionales"
    assert has_elif(contenido) or has_else(contenido), "No usaste elif o else"

def test_usar_input():
    contenido = _leer_contenido()
    assert has_function_call(contenido, "input"), "No usaste input() para obtener datos"

def test_ejecucion_correcta():
    resultado = subprocess.run(
        [sys.executable, "lessons/03-conditionals/solucion.py"],
        input="25\n",
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa tiene errores"
    salida = resultado.stdout.lower()
    assert "adulto" in salida, "No clasifica correctamente la edad 25"

def test_manejo_errores():
    resultado = subprocess.run(
        [sys.executable, "lessons/03-conditionals/solucion.py"],
        input="diez\n",
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa falla con entrada no numérica"
    salida = resultado.stdout.lower()
    assert any(p in salida for p in ["error", "inválido", "válido", "numero", "número", "por favor", "incorrecto"]), \
        "No muestra un mensaje de error cuando la entrada no es numérica"
