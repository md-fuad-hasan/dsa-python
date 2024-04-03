arr = [21,34,23,45,67,37,43,89,67,12]
print(arr)
for i in range(len(arr)):
    idx = i
    for j in range(i+1,len(arr)):
        if arr[idx]>arr[j]:
            idx = j
    arr[i], arr[idx] = arr[idx], arr[i]
print(arr)
