arr = [21,34,23,45,67,37,43,89,67,12]
print(arr)
for i in range(len(arr)):
    sp = False
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            sp = True
    if sp == False:
        break
print(arr)