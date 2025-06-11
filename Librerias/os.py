import os

# Obtener el directorio actual
#current working directory
"""cwd = os.getcwd()
print("Current working directory:", cwd)"""

# Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ",txt_files)

#Renombrar un archivo
os.rename("caperucita.txt", "cuento.txt")
print("Archivo renombrado")

# Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ",txt_files)