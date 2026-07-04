import subprocess
import sys

def test_archivo_existe():
    """Verifica que el archivo existe"""
    try:
        with open("lessons/04-loops/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/04-loops/"

def test_tiene_bucle():
    """Verifica que usa un bucle"""
    with open("lessons/04-loops/solucion.py", "r") as f:
        contenido = f.read()
        assert "for " in contenido or "while " in contenido, "No usaste for o while"

def test_usa_lista():
    """Verifica que usa una lista"""
    with open("lessons/04-loops/solucion.py", "r") as f:
        contenido = f.read()
        assert "append(" in contenido or "[]= " in contenido or "[]," in contenido, "No usaste listas correctamente"

def test_usar_input():
    """Verifica que usa input()"""
    with open("lessons/04-loops/solucion.py", "r") as f:
        contenido = f.read()
        assert "input(" in contenido, "No usaste input() para obtener datos"

def test_ejecucion_correcta():
    """Ejecuta el programa y verifica que funciona"""
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
