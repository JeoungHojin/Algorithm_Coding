total = 1
for i in range(3) :
    n = int(input())
    total *= n

total_list = [0] * 10
for val in str(total) :
    for i in range(10) :
        if int(val) == i :
            total_list[i] += 1

for i in range(10) :
    print(total_list[i])