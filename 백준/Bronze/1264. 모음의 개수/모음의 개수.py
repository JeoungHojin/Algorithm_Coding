while True:
    sentence = input()
    if sentence == '#':
        break

    sentence = sentence.lower()  
    count = 0  

    for ch in sentence:
        if ch in 'aeiou':
            count += 1
    print(count)
