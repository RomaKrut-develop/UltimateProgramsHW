cube_l = lambda x: x**3

source = [1, 2, 3, 4, 5]
list = list(map(cube_l, source))

print(f"Исходный список: {source}")
print(f"Список кубов: {list}")
