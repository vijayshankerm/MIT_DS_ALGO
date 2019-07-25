
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        wall = i
        for j in range(wall):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr)


a = input("enter a list ")
arra = []
for ai in a:
    if ai != " ":
        arra.append(int(ai))
print(arra)
insertion_sort(arra)











