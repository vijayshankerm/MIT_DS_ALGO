def counting_sort(arr):
    out = [0 for i in range(10)]

    count = [0 for i in range(10)]

    for i in arr:
        count[i] = count[i] + 1

    print(count)

    for i in range(1, len(count)):
        count[i] = count[i] + count[i - 1]

    for i in range(len(arr)):
        out[count[arr[i]]-1] = arr[i]
        count[arr[i]] = count[arr[i]] - 1
    
    return out


def main():
    arr = [1, 4, 1, 2, 7, 5, 2]
    print(counting_sort(arr))


if __name__ == "__main__":
    main()
