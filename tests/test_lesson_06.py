import subprocess
import sys

def test_archivo_existe():
    """Verifica que el archivo existe"""
    try:
        with open("lessons/06-final-project/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/06-final-project/"

def test_tiene_funciones():
    """Verifica que define al menos 2 funciones"""
    with open("lessons/06-final-project/solucion.py", "r") as f:
        contenido = f.read()
        assert contenido.count("def ") >= 2, "Debes definir al menos 2 funciones"

def test_tiene_condicionales():
    """Verifica que usa condicionales"""
    with open("lessons/06-final-project/solucion.py", "r") as f:
        contenido = f.read()
        assert "if " in contenido, "No usaste condicionales"

def test_tiene_bucles():
    """Verifica que usa bucles"""
    with open("lessons/06-final-project/solucion.py", "r") as f:
        contenido = f.read()
        assert "for " in contenido or "while " in contenido, "No usaste bucles"

def test_usa_diccionarios():
    """Verifica que usa diccionarios o listas de datos"""
    with open("lessons/06-final-project/solucion.py", "r") as f:
        contenido = f.read()
        assert "{" in contenido and "}" in contenido, "Debes usar diccionarios para guardar datos"

def test_ejecucion_correcta():
    """Ejecuta el programa y verifica que funciona"""
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
