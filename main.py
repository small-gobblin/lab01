import numpy as np
import matplotlib.pyplot as plt
def fib(n):
    fib_mas = np.zeros(n)
    fib_mas[0] = 0
    if (n > 1):
        fib_mas[1] = 1
        for i in range(2, n):
            fib_mas[i] = fib_mas[i - 1] + fib_mas[i - 2]
    return fib_mas
N = int(input("Введите кол-во первых чисел Фибоначчи"))
fib_mas = fib(N)
plt.plot(range(N), fib_mas, marker = 'o')
plt.xlabel('Номер числа')
plt.ylabel('Значение числа Фибоначчи')
plt.grid()
plt.show()