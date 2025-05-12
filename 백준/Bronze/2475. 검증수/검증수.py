total = 0
a = list(map(int,input().split()))

for i in range(5):
    total += a[i]*a[i]
print(total%10)