def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1

        while j >= len(right) and i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right) and i >= len(left):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":
    array_str = input("Enter an array for sorting")
    array = list()
    for i in array_str:
        if i != ' ':
            array.append(int(i))
    print(array)
    sorted_array = merge_sort(array)
    print(sorted_array)
