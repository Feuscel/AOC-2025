dial = 50
count = 0
with open("input.txt") as f:
    while line := f.readline():
        content = line.rstrip('\n')
        rotation = content[0]
        number = int(content[1:])
        if rotation == 'L':
        # Edge case in left 
            if dial == 0 :
                count = count + (number // 100)
            elif number >= dial :
                count = count + (1 + ((number - dial) // 100))
            dial = ((dial - number) % 100+ 100) % 100    
        if rotation == 'R':
            count += (dial + number) // 100
            dial = (dial + number) % 100
print(count)
