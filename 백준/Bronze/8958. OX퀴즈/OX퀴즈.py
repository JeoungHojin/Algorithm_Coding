n = int(input())
num = [0] * n
for i in range(n) :
    ox = input()
    ox = ox +"a"
    count = 0
    for idx,value in enumerate(ox) :
        if value == 'O' :
            count += 1
        else :
            num[i] += (count+1) * count / 2
            count = 0
for i in range(n) :
    print(int(num[i]))