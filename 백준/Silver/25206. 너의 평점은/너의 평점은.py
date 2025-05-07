time = []
score = []

for i in range(20) :
    no_result,t,s = input().split()
    time.append(float(t))
    score.append(s)
total = 0
total_time = 0
for i in range(20) :

    if score[i] == 'A+' :
        total += 4.5 * time[i]
    elif score[i] == 'A0' :
        total += 4.0 * time[i]
    elif score[i] == 'B+' :
        total += 3.5 * time[i]
    elif score[i] == 'B0' :
        total += 3.0 * time[i]
    elif score[i] == 'C+' :
        total += 2.5 * time[i]
    elif score[i] == 'C0' :
        total += 2.0 * time[i]
    elif score[i] == 'D+' :
        total += 1.5 * time[i]
    elif score[i] == 'D0' :
        total += 1.0 * time[i]
    elif score[i] == 'P' :
        continue
    elif score[i] == 'F' :
        total += 0
    total_time += time[i]

print(f"{total / total_time:.6f}")