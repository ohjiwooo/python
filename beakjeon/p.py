arr=[[]for i in range(5)]

arr[0].append((5,1))
arr[0].append((4,1))
arr[0].append((3,1))

arr[0].sort()

print(arr[0])