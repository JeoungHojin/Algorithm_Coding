matrix = [list(map(int,input().split())) for _ in range(9)]
max_ = -1
total_elements = 0
col_count = 0
for i in matrix:
    col_count += 1
    total_elements += len(i)
    row_count =0
    for j in i :
        row_count +=1
        if j > max_ :
            max_ = j
            m,n = row_count, col_count
print(max_)
print(n,m)