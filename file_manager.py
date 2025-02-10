filename = "messages.txt" # Имя файла
message = "Hello, world! \nI love hamsters \nEveryone loves them" # Само сообщение которое хотим передать/записать в файл

def write(): # Обозначем функцию которая будет записывать message в файл
    with open(filename, "a") as file: # Предзнаменуем работу с файлом и о завршенни работы в последней строчке блока:
        file.write(message) # Тоесть здесь

def read(): # Обозначем функцию которая будет считывать текст файла
    with open(filename, "r") as file:  # Предзнаменуем работу с файлом и о завршенни работы в последней строчке блока
        for message in file: # Здесь, начало считывания сообщения в файле
            print(message, end="") # Тут выводим в консоль
    print() # Здесь конец

write() # Вызываем функции
read() # Вызываем функции