import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _leer_solucion(leccion):
    path = ROOT / f"lessons/{leccion}/solucion.py"
    try:
        return path.read_text()
    except FileNotFoundError:
        return None


def _ejecutar_solucion(leccion, input_text=""):
    import subprocess
    result = subprocess.run(
        [sys.executable, str(ROOT / f"lessons/{leccion}/solucion.py")],
        input=input_text,
        capture_output=True,
        text=True,
    )
    return result
