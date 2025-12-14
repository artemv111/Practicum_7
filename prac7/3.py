while True:
    n = int(input("Введите число: "))
    for k in range(1, int(n**0.5)+1):
        if k * k == n:
            print(n,'является полным квадратом')
            break
    else:
        print(f"Нет, {n} не является полным квадратом")
