while True:
    packets = input("Введите последовательность пакетов: ")

    if len(packets) < 5:
        print("Ошибка! Длина строки должна быть не менее 5 символов.")
    elif not all(char in "01" for char in packets):
        print("Ошибка! Используйте только символы 0 и 1.")
    else:
        break

total_packets = len(packets)

lost_packets = packets.count('0')

current_zeros = 0
max_zeros = 0

for packet in packets:
    if packet == '0':
        current_zeros = current_zeros + 1

        if current_zeros > max_zeros:
            max_zeros = current_zeros
    else:
        current_zeros = 0

loss_percent = (lost_packets / total_packets) * 100

if loss_percent <= 1:
    quality = "отличное"
elif loss_percent <= 5:
    quality = "хорошее"
elif loss_percent <= 10:
    quality = "удовлетворительное"
elif loss_percent <= 20:
    quality = "плохое"
else:
    quality = "критическое состояние сети"

print("\nВЫВОД:")
print("Общее количество пакетов:", total_packets)
print("Количество потерянных пакетов:", lost_packets)
print("Длина самой длинной последовательности потерянных пакетов:", max_zeros)
print(f"Процент потерь: {loss_percent:.1f}%")
print("Качество связи:", quality)
