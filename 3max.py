def max3(arr):
    arr = sorted(arr, reverse=True)
    return arr[:3]

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
max_number= max3(numbers_list)
for num in max_number:
    print(num)