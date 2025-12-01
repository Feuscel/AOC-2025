dial = 50
count = 0
with open("input.txt") as f:
    while line := f.readline():
        content = line.rstrip('\n')
        rotation = content[0]
        number = int(content[1:])
        if rotation == 'L':
            dial -= number
        if rotation == 'R':
            dial += number
        while dial > 99 :
            dial -= 100
        while dial < 0 :
            dial +=  100
        if dial == 0 :
            count += 1
print(count)