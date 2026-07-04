import subprocess
import sys
from helpers import has_if, has_for, has_while, has_dict_or_set, count_function_defs

def test_archivo_existe():
    try:
        with open("lessons/06-final-project/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/06-final-project/"

def _leer_contenido():
    with open("lessons/06-final-project/solucion.py", "r") as f:
        return f.read()

def test_tiene_funciones():
    contenido = _leer_contenido()
    assert count_function_defs(contenido) >= 2, "Debes definir al menos 2 funciones"

def test_tiene_condicionales():
    contenido = _leer_contenido()
    assert has_if(contenido), "No usaste condicionales"

def test_tiene_bucles():
    contenido = _leer_contenido()
    assert has_for(contenido) or has_while(contenido), "No usaste bucles"

def test_usa_diccionarios():
    contenido = _leer_contenido()
    assert has_dict_or_set(contenido), "Debes usar diccionarios para guardar datos"

def test_ejecucion_correcta():
    resultado = subprocess.run(
        [sys.executable, "lessons/06-final-project/solucion.py"],
        input="1\nAna\n95\n",
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa tiene errores"
    salida = resultado.stdout
    assert "Ana" in salida, "No muestra el nombre del estudiante"
    assert "95" in salida or "Sobresaliente" in salida, "No muestra la nota o cualificación"
