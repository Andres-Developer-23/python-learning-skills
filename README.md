# 🐍 Aprende Python con GitHub Actions

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Progress](https://img.shields.io/badge/Progress-0%25-red.svg)
![Issues](https://img.shields.io/github/issues/tu-usuario/python-learning-skills)
![Stars](https://img.shields.io/github/stars/tu-usuario/python-learning-skills)
![Forks](https://img.shields.io/github/forks/tu-usuario/python-learning-skills)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

> 📚 **Curso interactivo de Python** - Aprende programación resolviendo ejercicios con feedback automático

---

## 📋 Tabla de Contenidos

- [🎯 ¿Qué es este curso?](#-qué-es-este-curso)
- [📚 Lecciones Disponibles](#-lecciones-disponibles)
- [🚀 ¿Cómo funciona?](#-cómo-funciona)
  - [Método 1: Usando Issues](#método-1-usando-issues-recomendado-para-principiantes)
  - [Método 2: Usando Pull Requests](#método-2-usando-pull-requests-recomendado-para-avanzados)
- [🎮 ¡Empezar ahora!](#-empezar-ahora)
- [💡 Consejos para el éxito](#-consejos-para-el-éxito)
- [🆘 Solución de Problemas](#-solución-de-problemas)
- [🏆 Sistema de Logros](#-sistema-de-logros)
- [📊 Tu Progreso](#-tu-progreso)
- [🤝 Contribuir](#-contribuir)
- [📜 Licencia](#-licencia)
- [🙏 Agradecimientos](#-agradecimientos)

---

## 🎯 ¿Qué es este curso?

Este es un curso **gratuito e interactivo** de Python donde:

- ✅ Resuelves ejercicios prácticos
- ✅ Recibes **feedback automático** de un robot (GitHub Actions)
- ✅ Aprendes a tu propio ritmo
- ✅ Obtienes un **certificado** al finalizar
- ✅ Desarrollas habilidades de programación reales
- ✅ Aprendes a usar Git y GitHub (habilidades muy valoradas)

### 🎓 ¿Para quién es?

- 👶 **Principiantes absolutos** - Sin experiencia previa en programación
- 🧑‍💻 **Estudiantes** - Que quieren practicar Python
- 👨‍🏫 **Profesores** - Que buscan recursos interactivos para sus clases
- 🔄 **Autodidactas** - Que prefieren aprender haciendo

---

## 📚 Lecciones Disponibles

| Lección | Tema | Dificultad | Duración | Estado |
|---------|------|------------|----------|--------|
| [**Lección 1**](#lección-1-mi-primer-programa) | Introducción a Python | ⭐ Fácil | 15-30 min | 🔓 **Disponible** |
| [**Lección 2**](#) | Variables y Tipos de Datos | ⭐⭐ Intermedio | 20-40 min | 🔒 **Próximamente** |
| [**Lección 3**](#) | Estructuras de Control | ⭐⭐ Intermedio | 25-45 min | 🔒 **Próximamente** |
| [**Lección 4**](#) | Bucles y Listas | ⭐⭐⭐ Avanzado | 30-50 min | 🔒 **Próximamente** |
| [**Lección 5**](#) | Funciones | ⭐⭐⭐ Avanzado | 30-50 min | 🔒 **Próximamente** |
| [**Lección 6**](#) | Proyecto Final | ⭐⭐⭐⭐⭐ Experto | 45-90 min | 🔒 **Próximamente** |

---

## 🚀 ¿Cómo funciona?

### **Dos formas de participar:**

El curso ofrece **dos métodos** para enviar tus soluciones. Elige el que más te acomode:

---

### 📝 **Método 1: Usando Issues** (Recomendado para Principiantes)

> ⭐ **Ideal si:** Eres nuevo en GitHub y quieres empezar rápido

<details>
<summary><b>📋 Guía paso a paso con Issues</b></summary>

#### **Paso 1: Abrir un Issue**
1. Ve a la pestaña **"Issues"** en el repositorio
2. Haz clic en **"New Issue"**
3. Selecciona la plantilla de la lección (ej: "Lección 01 - Mi primer programa")
4. ¡Ya estás listo para escribir tu código!

#### **Paso 2: Escribir tu código**
1. Lee las instrucciones de la lección
2. Escribe tu código en el bloque de código de Python:
   ```python
   # Tu código aquí
   nombre = input("¿Cómo te llamas? ")
   print("¡Hola " + nombre + "!")
   print("Tu nombre tiene " + str(len(nombre)) + " letras")
Completa las preguntas de reflexión

Haz clic en "Submit new issue"

Paso 3: El robot revisa tu código
⏱️ El robot (GitHub Actions) revisa automáticamente en ~30 segundos

💬 Recibirás un comentario con el feedback

🔄 Si hay errores, puedes editar tu Issue y el robot lo revisará de nuevo

Paso 4: ¡Lección completada!
✅ Cuando el robot apruebe tu código, cierra el Issue

🎉 ¡Has completado la lección!

</details>
Ventajas del método Issues:

✅ Más fácil para principiantes

✅ No necesitas crear ramas

✅ Todo en un solo lugar

✅ Ideal para aprender lo básico

🔀 Método 2: Usando Pull Requests (Recomendado para Avanzados)
⭐ Ideal si: Quieres aprender el flujo profesional de GitHub

<details> <summary><b>📋 Guía paso a paso con Pull Requests</b></summary>
Paso 1: Crear el archivo
Ve a la carpeta de la lección: lessons/01-intro/

Haz clic en "Add file" → "Create new file"

Nombre: solucion.py

Escribe tu código:

python
nombre = input("¿Cómo te llamas? ")
print("¡Hola " + nombre + "!")
print("Tu nombre tiene " + str(len(nombre)) + " letras")
Haz clic en "Commit new file"

Paso 2: Crear un Pull Request
Ve a la pestaña "Pull requests"

Haz clic en "New pull request"

Selecciona:

base: main

compare: tu-rama (si creaste una)

Título: "Solución Lección 1 - [Tu Nombre]"

Descripción: Explica tu solución

Haz clic en "Create pull request"

Paso 3: El robot revisa tu código
🤖 GitHub Actions revisa automáticamente

✅ El robot aprueba o solicita cambios

💬 Recibirás feedback detallado

Paso 4: ¡Lección completada!
✅ Cuando el robot apruebe, haz clic en "Merge pull request"

🎉 Tu solución queda integrada

🏆 Obtienes el badge de la lección

</details>
Ventajas del método Pull Requests:

✅ Flujo profesional de GitHub

✅ Historial de cambios visible

✅ Mejor para equipos

✅ Aprendes Git desde el principio

🎮 ¡Empezar ahora!
🐍 Lección 1: Tu primer programa en Python
Dificultad: ⭐ Fácil
Tiempo estimado: 15-30 minutos
Objetivo: Escribir un programa que salude a los usuarios

En esta lección aprenderás:

✍️ Cómo usar input() para obtener datos del usuario

🖨️ Cómo usar print() para mostrar mensajes

📐 Cómo calcular la longitud de un texto con len()

📝 Ejemplo de lo que crearás:
python
nombre = input("¿Cómo te llamas? ")
print("¡Hola " + nombre + "! Bienvenido/a a Python")
print("Tu nombre tiene " + str(len(nombre)) + " letras")
🚀 Elige tu método:
📝 Método Issues (Fácil):
Haz clic aquí para abrir un Issue con la plantilla

🔀 Método Pull Requests (Profesional):

Crea lessons/01-intro/solucion.py con tu código

Crea un Pull Request

El robot revisará automáticamente

💡 ¿Qué método elegir?
Si eres...	Usa...
🐣 Nuevo en GitHub	Issues
👨‍💻 Con experiencia	Pull Requests
🎓 Estudiante autodidacta	Issues primero, luego PRs
👨‍🏫 Profesor con estudiantes	Pull Requests
💡 Consejos para el éxito
🌟 Antes de empezar:
✅ Do's	❌ Don'ts
Lee las instrucciones cuidadosamente	No saltes directamente a escribir código
Prueba tu código localmente	No subas código sin probar
Usa nombres de variables descriptivos	No uses nombres como a, b, x
Comenta tu código cuando sea necesario	No escribas código desordenado
🎯 Durante el curso:
🎨 Sé creativo - Hay muchas formas de resolver los problemas

🧪 Prueba diferentes enfoques - Aprende de tus errores

📝 Reflexiona sobre lo que aprendes en cada lección

💬 Pregunta cuando tengas dudas

⭐ No te rindas - Los errores son parte del aprendizaje

🚀 Después de cada lección:
📝 Escribe notas sobre lo que aprendiste

🔄 Revisa las soluciones de otros estudiantes

🌟 Intenta el desafío extra si te sientes seguro

🎯 Pasa a la siguiente lección con confianza

🆘 Solución de Problemas
❌ Error: "El robot dice que mi código está mal pero está bien"
Problema común: El robot no encuentra el archivo porque estás usando Issues sin el workflow correcto.

Soluciones:

<details> <summary><b>✅ Solución 1: Usar Pull Requests</b></summary>
Ve a la carpeta lessons/01-intro/

Crea el archivo solucion.py

Escribe tu código

Crea un Pull Request

El robot lo revisará correctamente

</details><details> <summary><b>✅ Solución 2: Configurar el workflow para Issues</b></summary>
Actualiza tu workflow en .github/workflows/validar-leccion.yml con el código para Issues (ver abajo).

</details><details> <summary><b>✅ Solución 3: Usar el método de Issues correctamente</b></summary>
Asegúrate de usar ```python y ``` alrededor de tu código

El código debe estar entre esos bloques

El robot extraerá el código automáticamente

</details>
❌ "No se encontró el archivo"
Solución:

Verifica que el archivo esté en: lessons/01-intro/solucion.py

Asegúrate de que el nombre sea exacto (minúsculas)

Verifica que la carpeta existe

❌ "Error de sintaxis"
Solución:

Revisa paréntesis, comillas y dos puntos

Prueba localmente: python lessons/01-intro/solucion.py

Asegúrate de usar sintaxis correcta de Python

❌ "El workflow no se ejecuta"
Solución:

Verifica que el archivo esté en .github/workflows/

Asegúrate que termine en .yml o .yaml

Revisa que la sintaxis YAML sea correcta

Ve a la pestaña "Actions" para ver los logs

❌ "Permission denied"
Solución:

Ve a Settings → Actions → General

Habilita "Read and write permissions"

Guarda los cambios

💻 Comandos útiles para probar tu código:
bash
# Probar tu código localmente
python lessons/01-intro/solucion.py

# Verificar sintaxis (sin ejecutar)
python -m py_compile lessons/01-intro/solucion.py

# Ejecutar pruebas específicas (si existen)
pytest tests/test_lesson_01.py -v

# Verificar estilo de código
flake8 lessons/01-intro/solucion.py
📋 Checklist de verificación:
Si tienes problemas, verifica:

El archivo existe en lessons/01-intro/solucion.py

El código usa input() y print()

La sintaxis es correcta (probar localmente)

El workflow está en .github/workflows/

Los permisos de Actions están habilitados

🏆 Sistema de Logros
Logros que puedes desbloquear:
Logro	Condición	Icono	Recompensa
🐍 Primer Programa	Completar Lección 1	🥉	Badge de principiante
📊 Maestro de Variables	Completar Lección 2	🥈	Badge de intermedio
🔀 Control de Flujo	Completar Lección 3	🥈	Badge de intermedio
🔄 Bucle Pro	Completar Lección 4	🥇	Badge de avanzado
⚡ Función Cumplida	Completar Lección 5	🥇	Badge de avanzado
🎯 Python Master	Completar Proyecto Final	👑	Badge de experto + Certificado
📊 Tu Progreso
Barra de progreso interactiva:
text
[████████░░░░░░░░░░░░] 40% (2/5 lecciones completadas)

Lección 1: ████████████████████ ✅ Completada
Lección 2: ████████████████████ ✅ Completada
Lección 3: ████████████░░░░░░░░ 🔄 En progreso
Lección 4: ░░░░░░░░░░░░░░░░░░░░ ⏳ Pendiente
Lección 5: ░░░░░░░░░░░░░░░░░░░░ ⏳ Pendiente
Lección 6: ░░░░░░░░░░░░░░░░░░░░ ⏳ Pendiente
Estadísticas de la comunidad:
Métrica	Valor
👥 Estudiantes activos	0
📝 Lecciones completadas	0
⭐ Puntuación promedio	0/10
🏆 Logros desbloqueados	0
⏱️ Tiempo promedio por lección	0 min
🤝 Contribuir
¡Tu ayuda es valiosa! Hay muchas formas de contribuir:

🛠️ Formas de contribuir:
🐛 Reportar errores - Encuentra bugs y ayúdanos a solucionarlos

💡 Sugerir mejoras - Propón nuevas lecciones o ejercicios

📝 Mejorar documentación - Haz los textos más claros y útiles

🌍 Traducir el curso - Ayuda a estudiantes de otros idiomas

⭐ Dar una estrella - Demuestra que te gusta el proyecto

📝 Guía rápida para contribuir:
🍴 Haz fork del repositorio

🌿 Crea una rama para tus cambios

✍️ Realiza tus cambios siguiendo la guía de estilo

📤 Envía un Pull Request con descripción clara

👀 Espera la revisión y responde a los comentarios

📜 Licencia
Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.

🙏 Agradecimientos
📚 GitHub Skills - Por la inspiración y estructura

🐍 Comunidad de Python - Por su increíble documentación

🚀 GitHub Actions - Por hacer posible el feedback automático

❤️ Todos los estudiantes - Por ser la razón de este proyecto

📬 Contacto
¿Tienes preguntas o sugerencias? ¡Contáctanos!

🐦 Twitter: @tu-usuario

📧 Email: tu-email@ejemplo.com

💬 Discord: Únete a la comunidad

🐙 GitHub: @tu-usuario

⭐ ¡No olvides darle una estrella al repositorio!
https://img.shields.io/github/stars/tu-usuario/python-learning-skills?style=social

📊 Estadísticas del proyecto
https://img.shields.io/github/last-commit/tu-usuario/python-learning-skills
https://img.shields.io/github/contributors/tu-usuario/python-learning-skills
https://img.shields.io/github/repo-size/tu-usuario/python-learning-skills

🚀 ¡Comienza tu viaje de aprendizaje de Python hoy!

Creado con ❤️ por la comunidad de Python

text

---

## 📋 **Instrucciones para personalizar**

### **Reemplaza estos valores:**

1. **`tu-usuario`** → Tu nombre de usuario de GitHub
2. **`[Tu Nombre]`** → Tu nombre real
3. **`tu-email@ejemplo.com`** → Tu email de contacto
4. **`@tu-usuario`** → Tu usuario de Twitter
5. **URLs de Discord** → Tus enlaces reales

### **Actualiza los enlaces de las lecciones:**

```markdown
[**Lección 1**](https://github.com/tu-usuario/python-learning-skills/issues/new?template=leccion-01.md)
✅ Lo que incluye este README:
Sección	Descripción
✅ Dos métodos	Issues y Pull Requests explicados
✅ Solución de problemas	Errores comunes y cómo arreglarlos
✅ Guía paso a paso	Instrucciones claras para cada método
✅ Comparativa	Cuándo usar cada método
✅ Checklist	Verificación rápida de problemas
✅ Comandos útiles	Para probar tu código localmente
✅ Sistema de logros	Motivación para completar el curso
✅ Tabla de progreso	Seguimiento visual de avance
🎯 ¡Tu README está listo!
Solo necesitas:

✅ Copiar todo el contenido

✅ Reemplazar tu-usuario con tu usuario real

✅ Guardar como README.md

✅ Subirlo a tu repositorio

¡Ahora los estudiantes sabrán exactamente cómo participar en el curso! 🚀

quiero todo el texto en el readme
¡Perfecto! Aquí tienes el README completo con todo el texto para que solo copies y pegues. 📋

📄 README.md - TEXTO COMPLETO (Copia y Pega)
markdown
# 🐍 Aprende Python con GitHub Actions

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Progress](https://img.shields.io/badge/Progress-0%25-red.svg)
![Issues](https://img.shields.io/github/issues/tu-usuario/python-learning-skills)
![Stars](https://img.shields.io/github/stars/tu-usuario/python-learning-skills)
![Forks](https://img.shields.io/github/forks/tu-usuario/python-learning-skills)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

> 📚 **Curso interactivo de Python** - Aprende programación resolviendo ejercicios con feedback automático

---

## 📋 Tabla de Contenidos

- [🎯 ¿Qué es este curso?](#-qué-es-este-curso)
- [📚 Lecciones Disponibles](#-lecciones-disponibles)
- [🚀 ¿Cómo funciona?](#-cómo-funciona)
  - [Método 1: Usando Issues](#método-1-usando-issues-recomendado-para-principiantes)
  - [Método 2: Usando Pull Requests](#método-2-usando-pull-requests-recomendado-para-avanzados)
- [🎮 ¡Empezar ahora!](#-empezar-ahora)
- [💡 Consejos para el éxito](#-consejos-para-el-éxito)
- [🆘 Solución de Problemas](#-solución-de-problemas)
- [🏆 Sistema de Logros](#-sistema-de-logros)
- [📊 Tu Progreso](#-tu-progreso)
- [🤝 Contribuir](#-contribuir)
- [📜 Licencia](#-licencia)
- [🙏 Agradecimientos](#-agradecimientos)

---

## 🎯 ¿Qué es este curso?

Este es un curso **gratuito e interactivo** de Python donde:

- ✅ Resuelves ejercicios prácticos
- ✅ Recibes **feedback automático** de un robot (GitHub Actions)
- ✅ Aprendes a tu propio ritmo
- ✅ Obtienes un **certificado** al finalizar
- ✅ Desarrollas habilidades de programación reales
- ✅ Aprendes a usar Git y GitHub (habilidades muy valoradas)

### 🎓 ¿Para quién es?

- 👶 **Principiantes absolutos** - Sin experiencia previa en programación
- 🧑‍💻 **Estudiantes** - Que quieren practicar Python
- 👨‍🏫 **Profesores** - Que buscan recursos interactivos para sus clases
- 🔄 **Autodidactas** - Que prefieren aprender haciendo

---

## 📚 Lecciones Disponibles

| Lección | Tema | Dificultad | Duración | Estado |
|---------|------|------------|----------|--------|
| [**Lección 1**](#lección-1-mi-primer-programa) | Introducción a Python | ⭐ Fácil | 15-30 min | 🔓 **Disponible** |
| [**Lección 2**](#) | Variables y Tipos de Datos | ⭐⭐ Intermedio | 20-40 min | 🔒 **Próximamente** |
| [**Lección 3**](#) | Estructuras de Control | ⭐⭐ Intermedio | 25-45 min | 🔒 **Próximamente** |
| [**Lección 4**](#) | Bucles y Listas | ⭐⭐⭐ Avanzado | 30-50 min | 🔒 **Próximamente** |
| [**Lección 5**](#) | Funciones | ⭐⭐⭐ Avanzado | 30-50 min | 🔒 **Próximamente** |
| [**Lección 6**](#) | Proyecto Final | ⭐⭐⭐⭐⭐ Experto | 45-90 min | 🔒 **Próximamente** |

---

## 🚀 ¿Cómo funciona?

### **Dos formas de participar:**

El curso ofrece **dos métodos** para enviar tus soluciones. Elige el que más te acomode:

---

### 📝 **Método 1: Usando Issues** (Recomendado para Principiantes)

> ⭐ **Ideal si:** Eres nuevo en GitHub y quieres empezar rápido

<details>
<summary><b>📋 Guía paso a paso con Issues</b></summary>

#### **Paso 1: Abrir un Issue**
1. Ve a la pestaña **"Issues"** en el repositorio
2. Haz clic en **"New Issue"**
3. Selecciona la plantilla de la lección (ej: "Lección 01 - Mi primer programa")
4. ¡Ya estás listo para escribir tu código!

#### **Paso 2: Escribir tu código**
1. Lee las instrucciones de la lección
2. Escribe tu código en el bloque de código de Python:
   ```python
   # Tu código aquí
   nombre = input("¿Cómo te llamas? ")
   print("¡Hola " + nombre + "!")
   print("Tu nombre tiene " + str(len(nombre)) + " letras")
Completa las preguntas de reflexión

Haz clic en "Submit new issue"

Paso 3: El robot revisa tu código
⏱️ El robot (GitHub Actions) revisa automáticamente en ~30 segundos

💬 Recibirás un comentario con el feedback

🔄 Si hay errores, puedes editar tu Issue y el robot lo revisará de nuevo

Paso 4: ¡Lección completada!
✅ Cuando el robot apruebe tu código, cierra el Issue

🎉 ¡Has completado la lección!

</details>
Ventajas del método Issues:

✅ Más fácil para principiantes

✅ No necesitas crear ramas

✅ Todo en un solo lugar

✅ Ideal para aprender lo básico

🔀 Método 2: Usando Pull Requests (Recomendado para Avanzados)
⭐ Ideal si: Quieres aprender el flujo profesional de GitHub

<details> <summary><b>📋 Guía paso a paso con Pull Requests</b></summary>
Paso 1: Crear el archivo
Ve a la carpeta de la lección: lessons/01-intro/

Haz clic en "Add file" → "Create new file"

Nombre: solucion.py

Escribe tu código:

python
nombre = input("¿Cómo te llamas? ")
print("¡Hola " + nombre + "!")
print("Tu nombre tiene " + str(len(nombre)) + " letras")
Haz clic en "Commit new file"

Paso 2: Crear un Pull Request
Ve a la pestaña "Pull requests"

Haz clic en "New pull request"

Selecciona:

base: main

compare: tu-rama (si creaste una)

Título: "Solución Lección 1 - [Tu Nombre]"

Descripción: Explica tu solución

Haz clic en "Create pull request"

Paso 3: El robot revisa tu código
🤖 GitHub Actions revisa automáticamente

✅ El robot aprueba o solicita cambios

💬 Recibirás feedback detallado

Paso 4: ¡Lección completada!
✅ Cuando el robot apruebe, haz clic en "Merge pull request"

🎉 Tu solución queda integrada

🏆 Obtienes el badge de la lección

</details>
Ventajas del método Pull Requests:

✅ Flujo profesional de GitHub

✅ Historial de cambios visible

✅ Mejor para equipos

✅ Aprendes Git desde el principio

🎮 ¡Empezar ahora!
🐍 Lección 1: Tu primer programa en Python
Dificultad: ⭐ Fácil
Tiempo estimado: 15-30 minutos
Objetivo: Escribir un programa que salude a los usuarios

En esta lección aprenderás:

✍️ Cómo usar input() para obtener datos del usuario

🖨️ Cómo usar print() para mostrar mensajes

📐 Cómo calcular la longitud de un texto con len()

📝 Ejemplo de lo que crearás:
python
nombre = input("¿Cómo te llamas? ")
print("¡Hola " + nombre + "! Bienvenido/a a Python")
print("Tu nombre tiene " + str(len(nombre)) + " letras")
🚀 Elige tu método:
📝 Método Issues (Fácil):
Haz clic aquí para abrir un Issue con la plantilla

🔀 Método Pull Requests (Profesional):

Crea lessons/01-intro/solucion.py con tu código

Crea un Pull Request

El robot revisará automáticamente

💡 ¿Qué método elegir?
Si eres...	Usa...
🐣 Nuevo en GitHub	Issues
👨‍💻 Con experiencia	Pull Requests
🎓 Estudiante autodidacta	Issues primero, luego PRs
👨‍🏫 Profesor con estudiantes	Pull Requests
💡 Consejos para el éxito
🌟 Antes de empezar:
✅ Do's	❌ Don'ts
Lee las instrucciones cuidadosamente	No saltes directamente a escribir código
Prueba tu código localmente	No subas código sin probar
Usa nombres de variables descriptivos	No uses nombres como a, b, x
Comenta tu código cuando sea necesario	No escribas código desordenado
🎯 Durante el curso:
🎨 Sé creativo - Hay muchas formas de resolver los problemas

🧪 Prueba diferentes enfoques - Aprende de tus errores

📝 Reflexiona sobre lo que aprendes en cada lección

💬 Pregunta cuando tengas dudas

⭐ No te rindas - Los errores son parte del aprendizaje

🚀 Después de cada lección:
📝 Escribe notas sobre lo que aprendiste

🔄 Revisa las soluciones de otros estudiantes

🌟 Intenta el desafío extra si te sientes seguro

🎯 Pasa a la siguiente lección con confianza

🆘 Solución de Problemas
❌ Error: "El robot dice que mi código está mal pero está bien"
Problema común: El robot no encuentra el archivo porque estás usando Issues sin el workflow correcto.

Soluciones:

<details> <summary><b>✅ Solución 1: Usar Pull Requests</b></summary>
Ve a la carpeta lessons/01-intro/

Crea el archivo solucion.py

Escribe tu código

Crea un Pull Request

El robot lo revisará correctamente

</details><details> <summary><b>✅ Solución 2: Configurar el workflow para Issues</b></summary>
Actualiza tu workflow en .github/workflows/validar-leccion.yml con el código para Issues (ver abajo).

</details><details> <summary><b>✅ Solución 3: Usar el método de Issues correctamente</b></summary>
Asegúrate de usar ```python y ``` alrededor de tu código

El código debe estar entre esos bloques

El robot extraerá el código automáticamente

</details>
❌ "No se encontró el archivo"
Solución:

Verifica que el archivo esté en: lessons/01-intro/solucion.py

Asegúrate de que el nombre sea exacto (minúsculas)

Verifica que la carpeta existe

❌ "Error de sintaxis"
Solución:

Revisa paréntesis, comillas y dos puntos

Prueba localmente: python lessons/01-intro/solucion.py

Asegúrate de usar sintaxis correcta de Python

❌ "El workflow no se ejecuta"
Solución:

Verifica que el archivo esté en .github/workflows/

Asegúrate que termine en .yml o .yaml

Revisa que la sintaxis YAML sea correcta

Ve a la pestaña "Actions" para ver los logs

❌ "Permission denied"
Solución:

Ve a Settings → Actions → General

Habilita "Read and write permissions"

Guarda los cambios

💻 Comandos útiles para probar tu código:
bash
# Probar tu código localmente
python lessons/01-intro/solucion.py

# Verificar sintaxis (sin ejecutar)
python -m py_compile lessons/01-intro/solucion.py

# Ejecutar pruebas específicas (si existen)
pytest tests/test_lesson_01.py -v

# Verificar estilo de código
flake8 lessons/01-intro/solucion.py
📋 Checklist de verificación:
Si tienes problemas, verifica:

El archivo existe en lessons/01-intro/solucion.py

El código usa input() y print()

La sintaxis es correcta (probar localmente)

El workflow está en .github/workflows/

Los permisos de Actions están habilitados

🏆 Sistema de Logros
Logros que puedes desbloquear:
Logro	Condición	Icono	Recompensa
🐍 Primer Programa	Completar Lección 1	🥉	Badge de principiante
📊 Maestro de Variables	Completar Lección 2	🥈	Badge de intermedio
🔀 Control de Flujo	Completar Lección 3	🥈	Badge de intermedio
🔄 Bucle Pro	Completar Lección 4	🥇	Badge de avanzado
⚡ Función Cumplida	Completar Lección 5	🥇	Badge de avanzado
🎯 Python Master	Completar Proyecto Final	👑	Badge de experto + Certificado
📊 Tu Progreso
Barra de progreso interactiva:
text
[████████░░░░░░░░░░░░] 40% (2/5 lecciones completadas)

Lección 1: ████████████████████ ✅ Completada
Lección 2: ████████████████████ ✅ Completada
Lección 3: ████████████░░░░░░░░ 🔄 En progreso
Lección 4: ░░░░░░░░░░░░░░░░░░░░ ⏳ Pendiente
Lección 5: ░░░░░░░░░░░░░░░░░░░░ ⏳ Pendiente
Lección 6: ░░░░░░░░░░░░░░░░░░░░ ⏳ Pendiente
Estadísticas de la comunidad:
Métrica	Valor
👥 Estudiantes activos	0
📝 Lecciones completadas	0
⭐ Puntuación promedio	0/10
🏆 Logros desbloqueados	0
⏱️ Tiempo promedio por lección	0 min
🤝 Contribuir
¡Tu ayuda es valiosa! Hay muchas formas de contribuir:

🛠️ Formas de contribuir:
🐛 Reportar errores - Encuentra bugs y ayúdanos a solucionarlos

💡 Sugerir mejoras - Propón nuevas lecciones o ejercicios

📝 Mejorar documentación - Haz los textos más claros y útiles

🌍 Traducir el curso - Ayuda a estudiantes de otros idiomas

⭐ Dar una estrella - Demuestra que te gusta el proyecto

📝 Guía rápida para contribuir:
🍴 Haz fork del repositorio

🌿 Crea una rama para tus cambios

✍️ Realiza tus cambios siguiendo la guía de estilo

📤 Envía un Pull Request con descripción clara

👀 Espera la revisión y responde a los comentarios

📜 Licencia
Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.

🙏 Agradecimientos
📚 GitHub Skills - Por la inspiración y estructura

🐍 Comunidad de Python - Por su increíble documentación

🚀 GitHub Actions - Por hacer posible el feedback automático

❤️ Todos los estudiantes - Por ser la razón de este proyecto

📬 Contacto
¿Tienes preguntas o sugerencias? ¡Contáctanos!

🐦 Twitter: @tu-usuario

📧 Email: tu-email@ejemplo.com

💬 Discord: Únete a la comunidad

🐙 GitHub: @tu-usuario

⭐ ¡No olvides darle una estrella al repositorio!
https://img.shields.io/github/stars/tu-usuario/python-learning-skills?style=social

📊 Estadísticas del proyecto
https://img.shields.io/github/last-commit/tu-usuario/python-learning-skills
https://img.shields.io/github/contributors/tu-usuario/python-learning-skills
https://img.shields.io/github/repo-size/tu-usuario/python-learning-skills

🚀 ¡Comienza tu viaje de aprendizaje de Python hoy!

