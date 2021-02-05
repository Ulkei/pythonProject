def capitalization(deposit, percent, period):
    i = 0
    if period == 1:
        return int(deposit + deposit * percent / (12 * 100))
    else:
        for i in range(period):
            deposit = deposit + deposit * percent / (12 * 100)
        i += 1
        return int(deposit)


money = capitalization(10000, 10, 1)
print(money)
