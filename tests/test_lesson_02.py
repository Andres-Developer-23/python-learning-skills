import subprocess
import sys
from helpers import has_variable, has_list_literal, has_fstring

def test_archivo_existe():
    try:
        with open("lessons/02-variables/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/02-variables/"

def _leer_contenido():
    with open("lessons/02-variables/solucion.py", "r") as f:
        return f.read()

def test_tiene_variables():
    contenido = _leer_contenido()
    assert has_variable(contenido, "nombre"), "No definiste la variable 'nombre'"
    assert has_variable(contenido, "edad"), "No definiste la variable 'edad'"
    assert has_variable(contenido, "altura"), "No definiste la variable 'altura'"

def test_tiene_lista():
    contenido = _leer_contenido()
    assert has_list_literal(contenido), "No definiste una lista para hobbies"

def test_usa_fstrings():
    contenido = _leer_contenido()
    assert has_fstring(contenido), "Debes usar f-strings para mostrar mensajes"

def test_ejecucion_correcta():
    resultado = subprocess.run(
        [sys.executable, "lessons/02-variables/solucion.py"],
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa tiene errores"
    salida = resultado.stdout
    assert len(salida.strip()) > 0, "Tu programa no muestra ningún mensaje"
    assert "nombre" in salida.lower() or "nombre" in salida, "No muestra información personal"
