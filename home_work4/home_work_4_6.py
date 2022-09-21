# Finding the value of the desired element in the Febonacci set

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Введите номер искомого элемента:"))
print("Искомый элемент равен: ")
#for i in range(n):
    #result = list(range(n))
print(fibonacci(n))
