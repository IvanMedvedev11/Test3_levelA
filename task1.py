def summ(numbers):
    summ = 0
    for elem in numbers:
        if elem % 2 != 0:
            summ += elem
    return summ
list_ = list(map(int, input("Введите список: ").split()))
sum_ = summ(list_)
for i in range(len(list_)):
    if list_[i] % 2 != 0:
        list_[i] = sum_
print(list_)
