def max_heapify(arr, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest,n)


arr = [7,4,5,-6,8,-9,1,1,2,3,2,-5,6]
n = len(arr)
x = int(n/2)

# build max heap
for i in range(n, -1, -1):
    max_heapify(arr, i,n)

sorted_arr = list()
for i in range(n-1, 0, -1):
    arr[0],arr[i] = arr[i],arr[0]
    max_heapify(arr,0,i)


print(arr)
