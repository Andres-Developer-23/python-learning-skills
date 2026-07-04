#!/usr/bin/env python3
"""
Generador de Certificados - Python Learning Skills
Genera un certificado PNG cuando el estudiante completa todas las lecciones.
"""

import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("❌ Necesitas instalar Pillow: pip install Pillow")
    sys.exit(1)


def buscar_fuentes():
    """Busca fuentes disponibles en el sistema"""
    rutas_fuentes = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ]
    for ruta in rutas_fuentes:
        if Path(ruta).exists():
            return ruta
    return None


def generar_certificado(nombre_estudiante, lecciones_completadas=6, fecha=None):
    """Genera un certificado PNG"""
    # Si no se proporciona fecha, usar la actual
    if fecha is None:
        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        ahora = datetime.now()
        fecha = f"{ahora.day} de {meses[ahora.month - 1]} de {ahora.year}"
    
    # Configuración
    ANCHO, ALTO = 1200, 850
    COLOR_FONDO = (255, 253, 245)  # Crema claro
    COLOR_BORDE = (41, 98, 255)    # Azul profesional
    COLOR_TEXTO = (33, 33, 33)     # Gris oscuro
    COLOR_TITULO = (41, 98, 255)   # Azul
    COLOR_ORO = (218, 165, 32)     # Dorado

    # Crear imagen
    img = Image.new('RGB', (ANCHO, ALTO), COLOR_FONDO)
    draw = ImageDraw.Draw(img)

    # Buscar fuentes
    fuente_path = buscar_fuentes()
    
    if fuente_path:
        try:
            fuente_titulo = ImageFont.truetype(fuente_path, 48)
            fuente_nombre = ImageFont.truetype(fuente_path, 56)
            fuente_texto = ImageFont.truetype(fuente_path, 24)
            fuente_pequeña = ImageFont.truetype(fuente_path, 18)
        except Exception:
            fuente_titulo = ImageFont.load_default()
            fuente_nombre = ImageFont.load_default()
            fuente_texto = ImageFont.load_default()
            fuente_pequeña = ImageFont.load_default()
    else:
        fuente_titulo = ImageFont.load_default()
        fuente_nombre = ImageFont.load_default()
        fuente_texto = ImageFont.load_default()
        fuente_pequeña = ImageFont.load_default()

    # Dibujar borde decorativo
    for i in range(8):
        draw.rectangle(
            [30 + i, 30 + i, ANCHO - 30 - i, ALTO - 30 - i],
            outline=COLOR_BORDE
        )

    # Línea decorativa dorada
    draw.line([(100, 150), (ANCHO - 100, 150)], fill=COLOR_ORO, width=3)
    draw.line([(100, ALTO - 150), (ANCHO - 100, ALTO - 150)], fill=COLOR_ORO, width=3)

    # Título
    titulo = "CERTIFICADO DE COMPLETACIÓN"
    bbox = draw.textbbox((0, 0), titulo, font=fuente_titulo)
    ancho_texto = bbox[2] - bbox[0]
    draw.text(((ANCHO - ancho_texto) // 2, 180), titulo, fill=COLOR_TITULO, font=fuente_titulo)

    # Subtítulo
    subtitulo = "Python Learning Skills"
    bbox = draw.textbbox((0, 0), subtitulo, font=fuente_texto)
    ancho_texto = bbox[2] - bbox[0]
    draw.text(((ANCHO - ancho_texto) // 2, 250), subtitulo, fill=COLOR_BORDE, font=fuente_texto)

    # Texto principal
    texto1 = "Se certifica que"
    bbox = draw.textbbox((0, 0), texto1, font=fuente_texto)
    ancho_texto = bbox[2] - bbox[0]
    draw.text(((ANCHO - ancho_texto) // 2, 330), texto1, fill=COLOR_TEXTO, font=fuente_texto)

    # Nombre del estudiante
    bbox = draw.textbbox((0, 0), nombre_estudiante, font=fuente_nombre)
    ancho_texto = bbox[2] - bbox[0]
    draw.text(((ANCHO - ancho_texto) // 2, 390), nombre_estudiante, fill=COLOR_TITULO, font=fuente_nombre)

    # Línea bajo el nombre
    draw.line([(200, 470), (ANCHO - 200, 470)], fill=COLOR_ORO, width=2)

    # Descripción
    desc1 = f"ha completado exitosamente todas las {lecciones_completadas} lecciones"
    bbox = draw.textbbox((0, 0), desc1, font=fuente_texto)
    ancho_texto = bbox[2] - bbox[0]
    draw.text(((ANCHO - ancho_texto) // 2, 500), desc1, fill=COLOR_TEXTO, font=fuente_texto)

    desc2 = "del curso de Python con GitHub Actions"
    bbox = draw.textbbox((0, 0), desc2, font=fuente_texto)
    ancho_texto = bbox[2] - bbox[0]
    draw.text(((ANCHO - ancho_texto) // 2, 540), desc2, fill=COLOR_TEXTO, font=fuente_texto)

    # Habilidades adquiridas
    habilidades = "Habilidades: Python, Git, GitHub Actions, Programación"
    bbox = draw.textbbox((0, 0), habilidades, font=fuente_pequeña)
    ancho_texto = bbox[2] - bbox[0]
    draw.text(((ANCHO - ancho_texto) // 2, 610), habilidades, fill=(100, 100, 100), font=fuente_pequeña)

    # Fecha
    fecha_texto = f"Fecha: {fecha}"
    draw.text((150, ALTO - 120), fecha_texto, fill=COLOR_TEXTO, font=fuente_texto)

    # Firma
    firma_texto = "Python Learning Skills"
    bbox = draw.textbbox((0, 0), firma_texto, font=fuente_texto)
    ancho_firma = bbox[2] - bbox[0]
    draw.text((ANCHO - 150 - ancho_firma, ALTO - 120), firma_texto, fill=COLOR_BORDE, font=fuente_texto)

    # Guardar
    nombre_limpio = nombre_estudiante.replace(" ", "_").lower()
    nombre_archivo = f"certificado_{nombre_limpio}.png"
    img.save(nombre_archivo, "PNG", quality=95)
    
    return nombre_archivo


def main():
    if len(sys.argv) < 2:
        print(" uso: python generar_certificado.py <Nombre del Estudiante>")
        print(" ejemplo: python generar_certificado.py María García")
        sys.exit(1)

    nombre = " ".join(sys.argv[1:])
    
    print(f" Generando certificado para: {nombre}")
    archivo = generar_certificado(nombre)
    print(f"✅ Certificado generado: {archivo}")
    print(f" Puedes abrirlo con cualquier visor de imágenes")


if __name__ == "__main__":
    main()
