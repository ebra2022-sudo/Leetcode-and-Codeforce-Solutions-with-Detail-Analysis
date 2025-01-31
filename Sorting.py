from collections import  deque
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# design teh sate of the  current value of the state
def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        min_in = i
        for j in range(i + 1, l):
            if arr[j] < arr[min_in]:
                min_in = j

        arr[i], arr[min_in] = arr[min_in], arr[i]
    return arr


def merge_sort(arr):
    l = len(arr)
    if l <= 1:
        return arr
    left_arr = arr[:l // 2]
    right_arr = arr[l // 2:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))


def merge(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)
    merged_arr = []
    ind1 = 0
    ind2 = 0

    while ind1 < l1 and ind2 < l2:
        e1, e2 = arr1[ind1], arr2[ind2]
        if e1 < e2:
            merged_arr.append(e1)
            ind1 += 1
        else:
            merged_arr.append(e2)
            ind2 += 1
    if ind1 == l1:
        merged_arr.extend(arr2[ind2:])
    else:
        merged_arr.extend(arr1[ind1:])

    return merged_arr


def counting_sort(arr):
    if not arr:
        return arr  # Return empty array if input is empty

    # Find the range of the input
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    # Create and initialize the count array
    count = [0] * range_val

    # Count the occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Cumulative count
    for i in range(1, range_val):
        count[i] += count[i - 1]

    # Build the sorted array
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        sorted_arr[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    return sorted_arr










print(f"original array: {[1, 2, 1, 1, 0, 1]}")
print(f"sorted array by insertion sorting algorithm: {insertion_sort([1, 2, 1, 1, 0, 1])}")
print(f"sorted array by selection sorting algorithm: {selection_sort([1, 2, 1, 1, 0, 1])}")
print(f"sorted array by merge sorting algorithm: {merge_sort([1, 2, 1, 1, 0, 1])}")
print(f"sorted array by count sorting algorithm: {merge_sort([1, 2, 1, 1, 0, 1])}")

stack_collection = [0,1, 3, 1, 3,3,3,1,0]
freq_l = list(map(lambda x: stack_collection.count(x), set(stack_collection)))
print(stack_collection.count(0))
print(stack_collection)
print(freq_l)