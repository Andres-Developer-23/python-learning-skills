try:
    edad = int(input("¿Cuántos años tienes? "))

    if edad < 0:
        print("Por favor, ingresa una edad válida.")
    elif edad < 13:
        print(f"Tienes {edad} años. Eres Niño.")
    elif edad < 18:
        print(f"Tienes {edad} años. Eres Adolescente.")
    elif edad < 65:
        print(f"Tienes {edad} años. Eres Adulto.")
    else:
        print(f"Tienes {edad} años. Eres Adulto mayor.")
except ValueError:
    print("Por favor, ingresa un número válido.")
