import json
import os

# Nombre del archivo donde se almacenarán las tareas
TASK_FILE = 'tasks.json'

def load_tasks():
    """
    Carga las tareas desde un archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """
    Guarda las tareas en un archivo JSON.
    """
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
