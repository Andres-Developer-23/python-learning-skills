import subprocess
import sys
from helpers import has_function_call, has_for, has_while, has_method_call

def test_archivo_existe():
    try:
        with open("lessons/04-loops/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/04-loops/"

def _leer_contenido():
    with open("lessons/04-loops/solucion.py", "r") as f:
        return f.read()

def test_tiene_bucle():
    contenido = _leer_contenido()
    assert has_for(contenido) or has_while(contenido), "No usaste for o while"

def test_usa_lista():
    contenido = _leer_contenido()
    assert has_method_call(contenido, "append"), "No usaste listas correctamente"

def test_usar_input():
    contenido = _leer_contenido()
    assert has_function_call(contenido, "input"), "No usaste input() para obtener datos"

def test_ejecucion_correcta():
    resultado = subprocess.run(
        [sys.executable, "lessons/04-loops/solucion.py"],
        input="Leer\nCorrer\nCocinar\n",
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa tiene errores"
    salida = resultado.stdout
    assert "Leer" in salida, "No muestra el primer hobby"
    assert "3" in salida, "No muestra la cantidad de hobbies"
