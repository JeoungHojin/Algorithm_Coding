music = [n for n in range(1,9)]
reverse_music = music[::-1]
n = list(map(int,input().split()))
if n == music :
    print("ascending")
elif n == reverse_music :
    print("descending")
else :
    print("mixed")
