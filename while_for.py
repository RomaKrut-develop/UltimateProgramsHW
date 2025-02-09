import time

Energy_input = 2
Energy_needs = 0

while Energy_needs != 100: # 100 это значение, которое мы хотим получить
    time.sleep(0.03)
    Energy_needs += Energy_input
    print(f"Энергия - {Energy_needs}")

print('Достигнуто необходимое кол-во энергии, включаем устройство..')
print('Это был цикл while')
print('Для цикла for запустите файл while_for_for')