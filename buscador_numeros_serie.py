import shutil
import os
import time
import datetime
import re
from pathlib import Path
import math

inicio = time.time()

shutil.unpack_archive('archivo_comprimido.zip', 'archivo_descompimido', 'zip') # Especificar ruta 

# Adaptar la tura del archivo
ruta = "C:\\Users\\Usuario\\Desktop\\ruta_del_archivo"
mi_patron = r'N\D{3}-\d{5}'

fecha = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    mi_archivo = open(archivo, 'r')
    texto = mi_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != '':
                nros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print("-" * 50)
    print(f"Fecha de Búsqueda: {fecha.day}/{fecha.month}/{fecha.year}")
    print("\n")
    print("ARCHIVO\t\t\tNRO.SERIE")
    print("-------\t\t\t---------")
    for a in archivos_encontrados:
        print(f"{a}\t{nros_encontrados[indice]}")
        indice += 1
    print("\n")
    print(f"Números encontrados: {len(nros_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos")
    print("-" * 50)


def analis_numeros():
    crear_listas()
    mostrar_todo()


analis_numeros()
