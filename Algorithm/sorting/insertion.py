arr = [21,34,23,45,67,37,43,89,67,12]
print(arr)

for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1],arr[j]
            
print(arr)
