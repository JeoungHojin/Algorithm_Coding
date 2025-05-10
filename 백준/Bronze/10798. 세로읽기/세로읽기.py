matrix = [input() for _ in range(5)]

max_len = max(len(row) for row in matrix)

for col in range(max_len):
    for row in matrix:
        if col < len(row):
            print(row[col], end='')