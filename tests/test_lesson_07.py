import subprocess
import sys
import importlib.util
from helpers import has_return, count_function_defs

MODULE_PATH = "lessons/07-testing/solucion.py"

def _importar_modulo():
    spec = importlib.util.spec_from_file_location("solucion", MODULE_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_archivo_existe():
    try:
        with open(MODULE_PATH, "r") as f:
            assert f.read() != "", "El archivo está vacío"
    except FileNotFoundError:
        assert False, "No encontré solucion.py en lessons/07-testing/"


def test_tiene_funciones():
    mod = _importar_modulo()
    for nombre in ["sumar", "restar", "multiplicar", "dividir"]:
        assert hasattr(mod, nombre), f"Falta la función {nombre}()"


def test_sumar():
    mod = _importar_modulo()
    assert mod.sumar(2, 3) == 5, "sumar(2, 3) debería ser 5"
    assert mod.sumar(-1, 1) == 0, "sumar(-1, 1) debería ser 0"


def test_restar():
    mod = _importar_modulo()
    assert mod.restar(10, 4) == 6, "restar(10, 4) debería ser 6"
    assert mod.restar(3, 10) == -7, "restar(3, 10) debería ser -7"


def test_multiplicar():
    mod = _importar_modulo()
    assert mod.multiplicar(3, 4) == 12, "multiplicar(3, 4) debería ser 12"
    assert mod.multiplicar(0, 5) == 0, "multiplicar(0, 5) debería ser 0"


def test_dividir():
    mod = _importar_modulo()
    assert mod.dividir(10, 2) == 5.0, "dividir(10, 2) debería ser 5.0"
    assert mod.dividir(5, 0) == "Error", "dividir(5, 0) debería ser Error"


def test_tiene_ejecutar_pruebas():
    mod = _importar_modulo()
    assert hasattr(mod, "ejecutar_pruebas"), "Falta la función ejecutar_pruebas()"


def test_ejecutar_pruebas_funciona():
    mod = _importar_modulo()
    resultado = mod.ejecutar_pruebas()
    assert resultado is True, "ejecutar_pruebas() debería devolver True si todo pasa"


def test_usa_assert():
    with open(MODULE_PATH, "r") as f:
        contenido = f.read()
    assert "assert" in contenido, "Debes usar assert para las verificaciones"
