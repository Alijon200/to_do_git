
def add_todo():
    try:
        with open("malumot.txt", "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

            if lines:
                last_line = lines[-1]
                last_id = int(last_line.split(".")[0])
                task_id = last_id + 1
            else:
                task_id = 1
    except FileNotFoundError:
        task_id = 1

    while True:
        task = input("Vazifa kiriting (chiqish uchun 'stop'): ")

        if task.lower() == "stop":
            break

        if task:
            with open("malumot.txt", "a") as file:
                file.write(f"{task_id}. {task}\n")
            print(f"Vazifa qo'shildi! ID: {task_id}")
            task_id += 1
        else:
            print("Iltimos vazifa kiriting!")




def view_tasks():
    try:
        with open("malumot.txt", "r") as file:
            content = file.read().strip()
            if content:
                print("====== Sizning vazifalaringiz =======")
                print(content)
            else:
                print("Hozircha sizda vazifa mavjud emas!")
    except FileNotFoundError:
        print("Hali 'malumot.txt' fayli yaratilmagan!")


def delete_task():
    view_tasks()
    task_id = input("Qaysi vazifani o‘chirmoqchisiz (raqam kiriting): ")

    try:
        with open("malumot.txt", "r") as file:
            lines = file.readlines()

        found = False
        new_lines = []

        for line in lines:
            if not line.startswith(f"{task_id}."):
                new_lines.append(line)
            else:
                found = True

        with open("malumot.txt", "w") as file:
            file.writelines(new_lines)

        if found:
            print(f"{task_id}-raqamli vazifa o‘chirildi!")
        else:
            print("Bunday raqamli vazifa topilmadi.")

    except FileNotFoundError:
        print("Hali 'malumot.txt' fayli yaratilmagan!")


