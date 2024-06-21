from task_io import load_tasks, save_tasks
from task_operations import create_task, read_tasks, update_task, delete_task, filter_tasks_by_status, filter_tasks_by_category, sort_tasks_by_deadline, sort_tasks_by_priority

# Llamamos al menú principal para iniciar el programa
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
            
main_menu()
