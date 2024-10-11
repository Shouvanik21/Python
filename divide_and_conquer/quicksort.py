def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

n = int(input("Enter the length of the array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element {}: ".format(i+1))))

print("Unsorted array: ", arr)

sorted_arr = quick_sort(arr)

print("Sorted array: ", sorted_arr)
