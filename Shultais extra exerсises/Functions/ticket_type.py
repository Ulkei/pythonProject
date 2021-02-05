def ticket_type(tickets):
    numbers = []
    for char in tickets:
        numbers.append(int(char))
    summa1 = 0
    summa2 = 0
    summa1 = numbers[0] + numbers[1] + numbers[2]
    summa2 = numbers[3] + numbers[4] + numbers[5]
    if summa1 == summa2:
        return "счастливый"
    elif summa1 + 1 == summa2 or summa1 == summa2 + 1:
        return "встречный"
    elif summa1 + 2 == summa2 or summa1 == summa2 + 2:
        return "пьяный"
    else:
        return "обычный"
result = ticket_type("123456")
print(result)