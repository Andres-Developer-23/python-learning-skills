import subprocess
import sys
from helpers import has_return, count_function_defs

def test_archivo_existe():
    try:
        with open("lessons/05-functions/solucion.py", "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/05-functions/"

def _leer_contenido():
    with open("lessons/05-functions/solucion.py", "r") as f:
        return f.read()

def test_tiene_funciones():
    contenido = _leer_contenido()
    assert count_function_defs(contenido) >= 1, "No definiste ninguna función con def"

def test_tiene_parametros():
    contenido = _leer_contenido()
    tree = None
    try:
        import ast
        tree = ast.parse(contenido)
    except SyntaxError:
        pass
    assert tree is not None, "Error de sintaxis en tu código"
    tiene_params = False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.args.args:
            tiene_params = True
            break
    assert tiene_params, "Las funciones deben tener parámetros"

def test_tiene_return():
    contenido = _leer_contenido()
    assert has_return(contenido), "No usaste return en tus funciones"

def test_ejecucion_correcta():
    resultado = subprocess.run(
        [sys.executable, "lessons/05-functions/solucion.py"],
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0, "Tu programa tiene errores"
    salida = resultado.stdout
    assert "promedio" in salida.lower() or "par" in salida.lower(), "No muestra resultados de las funciones"
