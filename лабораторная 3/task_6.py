list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
m = 0
for i in range(0,len(list_numbers)-1):
    if list_numbers[i]>m:
        m = list_numbers[i]
        k = i
n = list_numbers[-1]
list_numbers[k] = n
list_numbers[-1] = m
print(list_numbers)
