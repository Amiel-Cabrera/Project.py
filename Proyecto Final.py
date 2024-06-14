# Importamos las bibliotecas necesarias
import json
import os

# Definimos el archivo de almacenamiento de datos
DATA_FILE = 'tasks.json'

# Cargamos las tareas desde el archivo si existe, sino inicializamos una lista vacía
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Guardamos las tareas en el archivo
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Generamos un identificador único para cada tarea
def generate_task_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

# Función para crear una tarea nueva
def create_task(tasks):
    task = {}
    task['id'] = generate_task_id(tasks)
    task['description'] = input("Descripción de la tarea: ")
    task['deadline'] = input("Fecha límite (YYYY-MM-DD): ")
    task['priority'] = input("Prioridad (alta, media, baja): ")
    task['category'] = input("Categoría: ")
    task['status'] = 'pendiente'
    tasks.append(task)
    save_tasks(tasks)
    print("Tarea creada exitosamente!")

# Función para leer y mostrar las tareas
def read_tasks(tasks):
    if not tasks:
        print("No hay tareas registradas.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Descripción: {task['description']}, Fecha límite: {task['deadline']}, "
              f"Prioridad: {task['priority']}, Categoría: {task['category']}, Estado: {task['status']}")

# Función para actualizar una tarea existente
def update_task(tasks):
    task_id = int(input("Ingrese el ID de la tarea a actualizar: "))
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        print("Tarea no encontrada.")
        return
    task['description'] = input(f"Descripción ({task['description']}): ") or task['description']
    task['deadline'] = input(f"Fecha límite ({task['deadline']}): ") or task['deadline']
    task['priority'] = input(f"Prioridad ({task['priority']}): ") or task['priority']
    task['category'] = input(f"Categoría ({task['category']}): ") or task['category']
    task['status'] = input(f"Estado ({task['status']}): ") or task['status']
    save_tasks(tasks)
    print("Tarea actualizada exitosamente!")

# Función para eliminar una tarea por su ID
def delete_task(tasks):
    task_id = int(input("Ingrese el ID de la tarea a eliminar: "))
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print("Tarea eliminada exitosamente!")

# Función para filtrar tareas por estado
def filter_tasks_by_status(tasks):
    status = input("Ingrese el estado a filtrar (pendiente, en progreso, completada): ")
    filtered_tasks = [task for task in tasks if task['status'] == status]
    read_tasks(filtered_tasks)

# Función para filtrar tareas por categoría
def filter_tasks_by_category(tasks):
    category = input("Ingrese la categoría a filtrar: ")
    filtered_tasks = [task for task in tasks if task['category'] == category]
    read_tasks(filtered_tasks)

# Función para ordenar las tareas por fecha límite
def sort_tasks_by_deadline(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x['deadline'])
    read_tasks(sorted_tasks)

# Función para ordenar las tareas por prioridad
def sort_tasks_by_priority(tasks):
    priority_order = {'alta': 1, 'media': 2, 'baja': 3}
    sorted_tasks = sorted(tasks, key=lambda x: priority_order[x['priority']])
    read_tasks(sorted_tasks)

# Función para mostrar el menú principal
def main_menu():
    tasks = load_tasks()
    while True:
        print("\nSistema de Gestión de Tareas")
        print("1. Crear Tarea")
        print("2. Leer Tareas")
        print("3. Actualizar Tarea")
        print("4. Eliminar Tarea")
        print("5. Filtrar Tareas por Estado")
        print("6. Filtrar Tareas por Categoría")
        print("7. Ordenar Tareas por Fecha Límite")
        print("8. Ordenar Tareas por Prioridad")
        print("9. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            create_task(tasks)
        elif choice == '2':
            read_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            filter_tasks_by_status(tasks)
        elif choice == '6':
            filter_tasks_by_category(tasks)
        elif choice == '7':
            sort_tasks_by_deadline(tasks)
        elif choice == '8':
            sort_tasks_by_priority(tasks)
        elif choice == '9':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Llamamos al menú principal para iniciar el programa
main_menu()

"""
Explicación Detallada
Carga y Guardado de Tareas:

load_tasks(): Carga las tareas desde un archivo JSON.
save_tasks(tasks): Guarda las tareas en un archivo JSON.
Funciones de Gestión de Tareas:

generate_task_id(tasks): Genera un ID único para cada tarea.
create_task(tasks): Permite al usuario crear una nueva tarea.
read_tasks(tasks): Muestra todas las tareas.
update_task(tasks): Permite al usuario actualizar una tarea existente.
delete_task(tasks): Permite al usuario eliminar una tarea por su ID.
Clasificación y Visualización:

filter_tasks_by_status(tasks): Filtra tareas por su estado.
filter_tasks_by_category(tasks): Filtra tareas por categoría.
sort_tasks_by_deadline(tasks): Ordena las tareas por fecha límite.
sort_tasks_by_priority(tasks): Ordena las tareas por prioridad.
Menú Interactivo:

main_menu(): Muestra el menú principal y maneja la interacción del usuario.
"""