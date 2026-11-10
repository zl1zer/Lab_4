def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end="")
        print()

def draw_triangle(rows, ch):
    for i in range(1, rows + 1):
        for j in range(i):
            print(ch, end="")
        print()


def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()


n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))

ch = "#"

print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
draw_rectangle(n, m, ch)

print("\nПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК:")
draw_triangle(n, ch)

print(f"\nРАМКА {n}x{m}:")
draw_frame(n, m, ch)
