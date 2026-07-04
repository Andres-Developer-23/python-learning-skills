import subprocess
import sys

def test_archivo_existe():
    """Verifica que el archivo existe"""
    try:
        with open("lessons/03-conditionals/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/03-conditionals/"

def test_tiene_condicionales():
    """Verifica que usa condicionales"""
    with open("lessons/03-conditionals/solucion.py", "r") as f:
        contenido = f.read()
        assert "if " in contenido, "No usaste if para condicionales"
        assert "elif " in contenido or "else:" in contenido, "No usaste elif o else"

def test_usar_input():
    """Verifica que usa input()"""
    with open("lessons/03-conditionals/solucion.py", "r") as f:
        contenido = f.read()
        assert "input(" in contenido, "No usaste input() para obtener datos"

def test_ejecucion_correcta():
    """Ejecuta el programa y verifica que funciona con edad válida"""
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
    """Verifica que maneja entrada no numérica"""
    resultado = subprocess.run(
        [sys.executable, "lessons/03-conditionals/solucion.py"],
        input="diez\n",
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa falla con entrada no numérica"
