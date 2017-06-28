test_case = [3, 4, 1, 2, 5]
def insertion_sort(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i-1
        while value > a[j] and j >= 0:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = value
    return a
print(insertion_sort(test_case))