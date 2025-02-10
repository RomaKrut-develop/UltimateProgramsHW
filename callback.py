import time

def callback_1(): # Мы назначаем первую коллбэк-функцию
    time.sleep(0.9)
    print("Я начало эстафеты, передаю свою функцию второму каллбэку!")

def callback_2(): # Затем вторую
    time.sleep(1.2)
    print("Я второй коллбэк, я принимаю функцию первого каллбэка и передаю его третьему!")

def callback_3(): # И последнюю
    time.sleep(1)
    print("Третий коллбэк принимает функцию, эстафета завершается")

callbacks = [callback_1, callback_2, callback_3] # После этого в переменной мы передаём эти функции как параметры

for callback in callbacks:
    callback()