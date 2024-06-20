from datetime import datetime

def generate_task_id(tasks):
    """
    Genera un identificador único para una nueva tarea.
    El identificador es 1 más que el máximo identificador actual.
    """
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def create_task(tasks):
    """
    Crea una nueva tarea con los detalles proporcionados por el usuario.
    """
    description = input("Descripción de la tarea: ")
    deadline = input("Fecha límite (YYYY-MM-DD): ")
    priority = input("Prioridad (baja, media, alta): ")
    category = input("Categoría: ")
    status = 'pendiente'
    
    new_task = {
        'id': generate_task_id(tasks),
        'description': description,
        'deadline': deadline,
        'priority': priority,
        'category': category,
        'status': status
    }
    
    tasks.append(new_task)
    print("Tarea creada con éxito.")

def read_tasks(tasks):
    """
    Muestra todas las tareas existentes con sus detalles.
    """
    if not tasks:
        print("No hay tareas registradas.")
        return

    for task in tasks:
        print(f"ID: {task['id']}, Descripción: {task['description']}, Fecha Límite: {task['deadline']}, Prioridad: {task['priority']}, Categoría: {task['category']}, Estado: {task['status']}")

def update_task(tasks):
    """
    Permite al usuario actualizar los detalles de una tarea existente.
    """
    task_id = int(input("ID de la tarea a actualizar: "))
    task = next((task for task in tasks if task['id'] == task_id), None)

    if not task:
        print("Tarea no encontrada.")
        return

    task['description'] = input(f"Descripción ({task['description']}): ") or task['description']
    task['deadline'] = input(f"Fecha límite ({task['deadline']}): ") or task['deadline']
    task['priority'] = input(f"Prioridad ({task['priority']}): ") or task['priority']
    task['category'] = input(f"Categoría ({task['category']}): ") or task['category']
    task['status'] = input(f"Estado ({task['status']}): ") or task['status']

    print("Tarea actualizada con éxito.")

def delete_task(tasks):
    """
    Elimina una tarea específica identificada por su ID.
    """
    task_id = int(input("ID de la tarea a eliminar: "))
    task = next((task for task in tasks if task['id'] == task_id), None)

    if not task:
        print("Tarea no encontrada.")
        return

    tasks.remove(task)
    print("Tarea eliminada con éxito.")
