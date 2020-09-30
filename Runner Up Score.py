n = int(input())
arr = list(map(int, input().split()))
m1 = max(arr)
m2 = -9999999999
for i in range(n):
    if arr[i] != m1 and arr[i] > m2:
        m2 = arr[i]
print(m2)
