
tasks = []
def add_todo():
    while True:
        task = input("Vaziffa kiriting(chiqish uchun (stop)): ")
        if task == "stop":
            break
        if task:
            tasks.append(task)
            print("Vazifa qo'shildi!")
        else:
            print("Iltimos vazifa kiriting!")


def view_tasks():
    if tasks:
        print("====== Sizning vazifalaringiz =======")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task} ")
    else:
        print("Hozircha sizda vazida mavjud emas!")
