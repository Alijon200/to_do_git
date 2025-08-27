from servece import add_todo, view_tasks


while True:
    tanlov = int(input("1–Vazifa qo‘shish\n2–Ro‘yxatni ko‘rish\n3–Vazifani o‘chirish\n0–Chiqish\nTanlov: "))
    if tanlov == 1:
        add_todo()

    elif tanlov == 2:
        view_tasks()

