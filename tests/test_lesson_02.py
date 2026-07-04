import subprocess
import sys

def test_archivo_existe():
    """Verifica que el archivo existe"""
    try:
        with open("lessons/02-variables/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/02-variables/"

def test_tiene_variables():
    """Verifica que usa diferentes tipos"""
    with open("lessons/02-variables/solucion.py", "r") as f:
        contenido = f.read()
        assert "nombre" in contenido, "No definiste la variable 'nombre'"
        assert "edad" in contenido, "No definiste la variable 'edad'"
        assert "altura" in contenido, "No definiste la variable 'altura'"

def test_tiene_lista():
    """Verifica que usa una lista para hobbies"""
    with open("lessons/02-variables/solucion.py", "r") as f:
        contenido = f.read()
        assert "[" in contenido and "]" in contenido, "No definiste una lista para hobbies"

def test_usa_fstrings():
    """Verifica que usa f-strings para mostrar mensajes"""
    with open("lessons/02-variables/solucion.py", "r") as f:
        contenido = f.read()
        assert 'f"' in contenido or "f'" in contenido, "Debes usar f-strings para mostrar mensajes"

def test_ejecuta_sin_errores():
    """Verifica que el programa funciona"""
    resultado = subprocess.run(
        [sys.executable, "lessons/02-variables/solucion.py"],
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa tiene errores"
