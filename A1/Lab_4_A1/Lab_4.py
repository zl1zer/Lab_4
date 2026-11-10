
import random
import time

while True:
    try:
        N = int(input("Введите количество примеров: "))
        if N > 0:
            break
        print("Введите положительное целое число!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

correct_answers = 0
total_time = 0

for i in range(1, N + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    print(f"\nВопрос {i}/{N}")

    start_time = time.time()

    while True:
        try:
            answer = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    end_time = time.time()
    question_time = end_time - start_time

    total_time = total_time + question_time

    if answer == a * b:
        print(f"Верно! (Время: {question_time:.1f} сек)")
        correct_answers = correct_answers + 1
    else:
        print(f"Неверно! Правильно: {a * b} "
              f"(Время: {question_time:.1f} сек)")

average_time = total_time / N
percentage = (correct_answers / N) * 100

print("\n" + "=" * 45)
print("СТАТИСТИКА:")
print("=" * 45)

print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {average_time:.1f} сек")
print(f"Правильных ответов: {correct_answers}/{N}")
print(f"Процент правильных ответов: {percentage:.1f}%")

