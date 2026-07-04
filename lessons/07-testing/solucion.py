def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error"
    return a / b


def ejecutar_pruebas():
    assert sumar(2, 3) == 5, "sumar(2, 3) debería ser 5"
    assert sumar(-1, 1) == 0, "sumar(-1, 1) debería ser 0"
    assert restar(10, 4) == 6, "restar(10, 4) debería ser 6"
    assert restar(3, 10) == -7, "restar(3, 10) debería ser -7"
    assert multiplicar(3, 4) == 12, "multiplicar(3, 4) debería ser 12"
    assert multiplicar(0, 5) == 0, "multiplicar(0, 5) debería ser 0"
    assert dividir(10, 2) == 5.0, "dividir(10, 2) debería ser 5.0"
    assert dividir(5, 0) == "Error", "dividir(5, 0) debería ser Error"
    return True


if __name__ == "__main__":
    if ejecutar_pruebas():
        print("✓ Todas las pruebas pasaron")
