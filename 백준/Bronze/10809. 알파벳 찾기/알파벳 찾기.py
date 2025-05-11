import string
word = input()
seen = set()
result = ""
for ch in word :
    if ch in seen :
        result += "*"
    else :
        result += ch
        seen.add(ch)
alphabet = list(string.ascii_lowercase)
find_alphabet = [-1] * 26
find_count = 0
for i in result :
    count = 0
    for j in alphabet :
        if i == j :
            find_alphabet[count] = find_count
        count +=1
    find_count +=1
print(*find_alphabet)