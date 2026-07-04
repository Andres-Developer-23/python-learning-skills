import subprocess
import sys

def test_archivo_existe():
    """Verifica que el archivo existe"""
    try:
        with open("lessons/05-functions/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/05-functions/"

def test_tiene_funciones():
    """Verifica que define funciones"""
    with open("lessons/05-functions/solucion.py", "r") as f:
        contenido = f.read()
        assert "def " in contenido, "No definiste ninguna función con def"

def test_tiene_parametros():
    """Verifica que usa parámetros"""
    with open("lessons/05-functions/solucion.py", "r") as f:
        contenido = f.read()
        assert "def " in contenido and "(" in contenido, "Las funciones deben tener parámetros"

def test_tiene_return():
    """Verifica que usa return"""
    with open("lessons/05-functions/solucion.py", "r") as f:
        contenido = f.read()
        assert "return " in contenido, "No usaste return en tus funciones"

def test_ejecucion_correcta():
    """Ejecuta el programa y verifica que funciona"""
    resultado = subprocess.run(
        [sys.executable, "lessons/05-functions/solucion.py"],
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa tiene errores"
    salida = resultado.stdout
    assert "promedio" in salida.lower() or "par" in salida.lower(), "No muestra resultados de las funciones"
