# Implementar un sistema de descarga de archivos asincronica, 
# donde cada archivo tarde un tiempo variable en descargarse
import asyncio
import random

async def descargar_archivo(nombre_archivo):
    tiempo_descarga = random.randint(1, 5)  # Tiempo de descarga aleatorio entre 1 y 5 segundos
    print(f"Descargando {nombre_archivo}... (esto tomará {tiempo_descarga} segundos)")
    await asyncio.sleep(tiempo_descarga)  # Simula la descarga del archivo
    print(f"{nombre_archivo} descargado.")

async def main():
    archivos = [f"archivo_{i}.txt" for i in range(1, 6)]  # Lista de archivos a descargar
    tareas = [descargar_archivo(archivo) for archivo in archivos]  # Crear tareas para cada descarga
    await asyncio.gather(*tareas)  # Ejecutar todas las descargas concurrentemente

asyncio.run(main())  # Ejecutar la función principal
