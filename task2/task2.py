#second task
print("Решение второго задания")

time = int(input("Укажите время в секундах: "))
while time < 0:
    time = int(input("Нужно значение большее или равное 0! Укажите время в секундах: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
if hours < 10:
    hours_str = f"0{hours}"
else:
    hours_str = str(hours)
if minutes < 10:
    minutes_str = f"0{minutes}"
else:
    minutes_str = str(minutes)
if seconds < 10:
    seconds_str = f"0{seconds}"
else:
    seconds_str = str(seconds)
result = f"Время: {hours_str}:{minutes_str}:{seconds_str}"
print(result)