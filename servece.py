
tasks = {}
def add_todo():
    task_id = 1

    while True:
        task = input("Vazifa kiriting (chiqish uchun 'stop'): ")

        if task.lower() == "stop":
            break

        if task:
            tasks[task_id] = task
            print(f"Vazifa qo'shildi!")
            task_id += 1
        else:
            print("Iltimos vazifa kiriting!")

    return tasks


def view_tasks():
    if tasks:
        print("====== Sizning vazifalaringiz =======")
        for i, task in tasks.items():
            print(f"{i}. {task} ")
    else:
        print("Hozircha sizda vazida mavjud emas!")


def delete_task():
    view_tasks()
    number = int(input("O'chirmoqchi bolgan taskni raqamini kiriting: "))
    if number in tasks.keys():
        del  tasks[number]
        print("=== Vazifa o'chirildi ===")

    else:
        print("Ushbu nomerli vazifa topilmadi!")