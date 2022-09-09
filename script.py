age = int(input("How old are you?"))

if age > 100 or age <= 0:
    raise ValueError("Тебе не может быть столько лет")

print(f"Тебе {age} лет!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.