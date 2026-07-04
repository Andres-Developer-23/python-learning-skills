hobbies = []

for i in range(3):
    hobby = input(f"Ingresa tu hobby {i + 1}: ")
    hobbies.append(hobby)

print("\nTus hobbies son:")
for i, hobby in enumerate(hobbies, 1):
    print(f"{i}. {hobby}")

print(f"\nTienes {len(hobbies)} hobbies.")
