города = ("Москва", "Санкт-Петербург", "Казань")
print(f"Кортеж городов: {города}")

try:
    города[0] = "Новосибирск"
except TypeError as e:
    print(f"\nОшибка при попытке изменить элемент кортежа: {e}")
    print("Кортежи являются неизменяемыми (immutable) типами данных в Python.")
    print("После создания кортежа, вы не можете изменять его элементы.")