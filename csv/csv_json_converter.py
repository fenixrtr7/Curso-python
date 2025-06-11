import csv
import json
import os
from typing import List, Dict, Any

def csv_to_json(csv_file_path: str, json_file_path: str) -> None:
    """
    Convierte un archivo CSV a JSON.
    
    Args:
        csv_file_path (str): Ruta del archivo CSV de entrada
        json_file_path (str): Ruta del archivo JSON de salida
    """
    try:
        # Leer el archivo CSV
        data: List[Dict[str, Any]] = []
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        # Escribir el archivo JSON
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        
        print(f"Conversión exitosa: {csv_file_path} -> {json_file_path}")
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csv_file_path}")
    except Exception as e:
        print(f"Error durante la conversión: {str(e)}")

def json_to_csv(json_file_path: str, csv_file_path: str) -> None:
    """
    Convierte un archivo JSON a CSV.
    
    Args:
        json_file_path (str): Ruta del archivo JSON de entrada
        csv_file_path (str): Ruta del archivo CSV de salida
    """
    try:
        # Leer el archivo JSON
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        if not data:
            print("Error: El archivo JSON está vacío")
            return
        
        # Obtener las cabeceras del CSV
        fieldnames = data[0].keys()
        
        # Escribir el archivo CSV
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Conversión exitosa: {json_file_path} -> {csv_file_path}")
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: El archivo {json_file_path} no es un JSON válido")
    except Exception as e:
        print(f"Error durante la conversión: {str(e)}")

def main():
    while True:
        print("\n=== Convertidor CSV <-> JSON ===")
        print("1. CSV a JSON")
        print("2. JSON a CSV")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == "1":
            csv_file = input("Ingrese la ruta del archivo CSV: ")
            json_file = input("Ingrese la ruta del archivo JSON de salida: ")
            csv_to_json(csv_file, json_file)
        
        elif opcion == "2":
            json_file = input("Ingrese la ruta del archivo JSON: ")
            csv_file = input("Ingrese la ruta del archivo CSV de salida: ")
            json_to_csv(json_file, csv_file)
        
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main() 