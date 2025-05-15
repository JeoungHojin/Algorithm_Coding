tri_right = []
while True :
    a,b,c = map(int,input().split())
    if a == 0 and b==0 and c==0:
        break
    if b > a : #a가 크게 해줌 a>b
        b ,a = a, b
    if a > c :
        c ,a = a ,c
    if a ** 2 + b ** 2 == c**2 :
        tri_right.append("right")
    else :
        tri_right.append("wrong")
    

for i in tri_right :
    print(i)
