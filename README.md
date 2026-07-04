# 🐍 Aprende Python con GitHub Actions

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Progress](https://img.shields.io/badge/Progress-0%25-red.svg)
![Issues](https://img.shields.io/github/issues/andres/python-learning-skills)
![Stars](https://img.shields.io/github/stars/andres/python-learning-skills)
![Forks](https://img.shields.io/github/forks/andres/python-learning-skills)
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
- [🤝 Contribuir](#-contribuir)
- [📜 Licencia](#-licencia)

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
| [**Lección 1**](lessons/01-intro/instructions.md) | Introducción a Python | ⭐ Fácil | 15-30 min | 🔓 **Disponible** |
| [**Lección 2**](lessons/02-variables/instructions.md) | Variables y Tipos de Datos | ⭐ Fácil | 20-40 min | 🔓 **Disponible** |
| [**Lección 3**](lessons/03-conditionals/instructions.md) | Estructuras de Control | ⭐⭐ Intermedio | 25-45 min | 🔓 **Disponible** |
| [**Lección 4**](lessons/04-loops/instructions.md) | Bucles y Listas | ⭐⭐ Intermedio | 30-50 min | 🔓 **Disponible** |
| [**Lección 5**](lessons/05-functions/instructions.md) | Funciones | ⭐⭐⭐ Avanzado | 30-50 min | 🔓 **Disponible** |
| [**Lección 6**](lessons/06-final-project/instructions.md) | Proyecto Final | ⭐⭐⭐⭐⭐ Experto | 45-90 min | 🔓 **Disponible** |

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
   ```
3. Completa las preguntas de reflexión
4. Haz clic en **"Submit new issue"**

#### **Paso 3: El robot revisa tu código**
- ⏱️ El robot (GitHub Actions) revisa automáticamente en ~30 segundos
- 💬 Recibirás un comentario con el feedback
- 🔄 Si hay errores, puedes editar tu Issue y el robot lo revisará de nuevo

#### **Paso 4: ¡Lección completada!**
- ✅ Cuando el robot apruebe tu código, cierra el Issue
- 🎉 ¡Has completado la lección!

</details>

**Ventajas del método Issues:**
- ✅ Más fácil para principiantes
- ✅ No necesitas crear ramas
- ✅ Todo en un solo lugar
- ✅ Ideal para aprender lo básico

---

### 🔀 **Método 2: Usando Pull Requests** (Recomendado para Avanzados)

> ⭐ **Ideal si:** Quieres aprender el flujo profesional de GitHub

<details>
<summary><b>📋 Guía paso a paso con Pull Requests</b></summary>

#### **Paso 1: Crear el archivo**
1. Ve a la carpeta de la lección: `lessons/XX-nombre/`
2. Haz clic en **"Add file"** → **"Create new file"**
3. Nombre: `solucion.py`
4. Escribe tu código
5. Haz clic en **"Commit new file"**

#### **Paso 2: Crear un Pull Request**
1. Ve a la pestaña **"Pull requests"**
2. Haz clic en **"New pull request"**
3. Selecciona: `base: main` y `compare: tu-rama`
4. Título: "Solución Lección X - [Tu Nombre]"
5. Haz clic en **"Create pull request"**

#### **Paso 3: El robot revisa tu código**
- 🤖 GitHub Actions revisa automáticamente
- ✅ El robot aprueba o solicita cambios
- 💬 Recibirás feedback detallado

#### **Paso 4: ¡Lección completada!**
- ✅ Cuando el robot apruebe, haz clic en **"Merge pull request"**
- 🎉 Tu solución queda integrada
- 🏆 Obtienes el badge de la lección

</details>

**Ventajas del método Pull Requests:**
- ✅ Flujo profesional de GitHub
- ✅ Historial de cambios visible
- ✅ Mejor para equipos
- ✅ Aprendes Git desde el principio

---

### 💡 ¿Qué método elegir?

| Si eres... | Usa... |
|------------|--------|
| 🐣 Nuevo en GitHub | Issues |
| 👨‍💻 Con experiencia | Pull Requests |
| 🎓 Estudiante autodidacta | Issues primero, luego PRs |
| 👨‍🏫 Profesor con estudiantes | Pull Requests |

---

## 🎮 ¡Empezar ahora!

### 🐍 Lección 1: Tu primer programa en Python
- **Dificultad:** ⭐ Fácil
- **Tiempo estimado:** 15-30 minutos
- **Objetivo:** Escribir un programa que salude a los usuarios

**En esta lección aprenderás:**
- ✍️ Cómo usar `input()` para obtener datos del usuario
- 🖨️ Cómo usar `print()` para mostrar mensajes
- 📐 Cómo calcular la longitud de un texto con `len()`

**📝 Ejemplo de lo que crearás:**
```python
nombre = input("¿Cómo te llamas? ")
print("¡Hola " + nombre + "! Bienvenido/a a Python")
print("Tu nombre tiene " + str(len(nombre)) + " letras")
```

---

## 💡 Consejos para el éxito

### 🌟 Antes de empezar:

| ✅ Do's | ❌ Don'ts |
|---------|----------|
| Lee las instrucciones cuidadosamente | No saltes directamente a escribir código |
| Prueba tu código localmente | No subas código sin probar |
| Usa nombres de variables descriptivos | No uses nombres como a, b, x |
| Comenta tu código cuando sea necesario | No escribas código desordenado |

### 🎯 Durante el curso:
- 🎨 Sé creativo - Hay muchas formas de resolver los problemas
- 🧪 Prueba diferentes enfoques - Aprende de tus errores
- 📝 Reflexiona sobre lo que aprendes en cada lección
- 💬 Pregunta cuando tengas dudas
- ⭐ No te rindas - Los errores son parte del aprendizaje

---

## 🆘 Solución de Problemas

### ❌ Error: "No se encontró el archivo"
**Solución:**
- Verifica que el archivo esté en: `lessons/XX-nombre/solucion.py`
- Asegúrate de que el nombre sea exacto (minúsculas)
- Verifica que la carpeta existe

### ❌ "Error de sintaxis"
**Solución:**
- Revisa paréntesis, comillas y dos puntos
- Prueba localmente: `python lessons/01-intro/solucion.py`
- Asegúrate de usar sintaxis correcta de Python

### ❌ "El workflow no se ejecuta"
**Solución:**
- Verifica que el archivo esté en `.github/workflows/`
- Asegúrate que termine en `.yml` o `.yaml`
- Revisa que la sintaxis YAML sea correcta
- Ve a la pestaña "Actions" para ver los logs

### 💻 Comandos útiles para probar tu código:

```bash
# Probar tu código localmente
python lessons/01-intro/solucion.py

# Verificar sintaxis (sin ejecutar)
python -m py_compile lessons/01-intro/solucion.py

# Ejecutar pruebas específicas
pytest tests/test_lesson_01.py -v

# Verificar estilo de código
flake8 lessons/01-intro/solucion.py
```

---

## 🏆 Sistema de Logros

| Logro | Condición | Icono | Recompensa |
|-------|-----------|-------|------------|
| 🐍 Primer Programa | Completar Lección 1 | 🥉 | Badge de principiante |
| 📊 Maestro de Variables | Completar Lección 2 | 🥈 | Badge de intermedio |
| 🔀 Control de Flujo | Completar Lección 3 | 🥈 | Badge de intermedio |
| 🔄 Bucle Pro | Completar Lección 4 | 🥇 | Badge de avanzado |
| ⚡ Función Cumplida | Completar Lección 5 | 🥇 | Badge de avanzado |
| 🎯 Python Master | Completar Proyecto Final | 👑 | Badge de experto + Certificado |

---

## 🎓 Certificado

Al completar todas las lecciones, puedes generar tu **certificado de completación** como imagen PNG.

### Cómo obtener tu certificado:

```bash
# Ejecuta el script con tu nombre
python3 scripts/generar_certificado.py "Tu Nombre"
```

**Ejemplo:**
```bash
python3 scripts/generar_certificado.py "María García"
```

Se generará un archivo `certificado_tu_nombre.png` que puedes:
- 📱 Compartir en redes sociales
- 📄 imprimir
- 💾 Guardar en tu portafolio

---

## 🤝 Contribuir

¡Tu ayuda es valiosa! Hay muchas formas de contribuir:

- 🐛 **Reportar errores** - Encuentra bugs y ayúdanos a solucionarlos
- 💡 **Sugerir mejoras** - Propón nuevas lecciones o ejercicios
- 📝 **Mejorar documentación** - Haz los textos más claros y útiles
- 🌍 **Traducir el curso** - Ayuda a estudiantes de otros idiomas
- ⭐ **Dar una estrella** - Demuestra que te gusta el proyecto

### 📝 Guía rápida para contribuir:
1. 🍴 Haz fork del repositorio
2. 🌿 Crea una rama para tus cambios
3. ✍️ Realiza tus cambios siguiendo la guía de estilo
4. 📤 Envía un Pull Request con descripción clara
5. 👀 Espera la revisión y responde a los comentarios

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.

---

## 🙏 Agradecimientos

- 📚 **GitHub Skills** - Por la inspiración y estructura
- 🐍 **Comunidad de Python** - Por su increíble documentación
- 🚀 **GitHub Actions** - Por hacer posible el feedback automático
- ❤️ **Todos los estudiantes** - Por ser la razón de este proyecto

---

## 📬 Contacto

¿Tienes preguntas o sugerencias? ¡Contáctanos!

- 🐙 GitHub: [@andres](https://github.com/andres)

---

⭐ ¡No olvides darle una estrella al repositorio!
