def counting_sort(arr, exp):
    n = len(arr)
    output = [0 for i in range(n)]
    count = [0 for i in range(10)]
    exp = pow(10, exp)

    for i in arr:
        index = int(i / exp)
        count[index % 10] = count[index % 10] + 1

    for i in range(1, 10):
        count[i] = count[i] + count[i - 1]

    for i in range(len(arr)-1, -1, -1):
        index = int(arr[i] / exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] = count[index % 10] - 1

    for j in range(len(output)):
        arr[j] = output[j]


# Method to do Radix Sort
def radix_sort(arr):

    max1 = max(arr)
    exp = 0
    while int(max1 / pow(10, exp)) > 0:
        counting_sort(arr, exp)
        exp += 1

    return arr


def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_arr = radix_sort(arr)
    print(sorted_arr)


if __name__ == "__main__":
    main()
