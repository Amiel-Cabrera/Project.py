from task_io import load_tasks, save_tasks
from task_operations import create_task, read_tasks, update_task, delete_task

def menu():
    """
    Proporciona un menú interactivo para la gestión de tareas.
    Permite al usuario crear, leer, actualizar y eliminar tareas.
    """
    tasks = load_tasks()
    while True:
        print("\nSistema de Gestión de Tareas")
        print()
        print("1. Crear Tarea")
        print("2. Leer Tareas")
        print("3. Actualizar Tarea")
        print("4. Eliminar Tarea")
        print("5. Salir")
        print()
        choice = input("Seleccione una opción: ")

        if choice == '1':
            create_task(tasks)
            save_tasks(tasks)
        elif choice == '2':
            read_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
