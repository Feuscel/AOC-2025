with open("input.txt") as f:
    lines = []
    x = 0
    while line := f.readline():
        lines.append(line.rstrip('\n'))
    for i in range(len(lines)):
        for j in range(len(lines[i])) :
            if lines[i][j] == "@":
                number_of_adjacent = 0
                if (i-1) >= 0:
                    if lines[i-1][j] == "@" :
                        number_of_adjacent += 1 
                if (i+1) < len(lines):
                    if lines[i+1][j] == "@":
                        number_of_adjacent += 1 
                if (j-1) >= 0 :
                    if lines[i][j-1] == "@" and (j-1) >= 0 :
                        number_of_adjacent += 1 
                if (j+1) < len(lines[i]):
                    if lines[i][j+1] == "@" and (j+1) < len(lines[i]):
                        number_of_adjacent += 1 
                if (i-1) >= 0 and (j-1) >= 0:
                    if lines[i-1][j-1] == "@" :
                        number_of_adjacent += 1 
                if (i+1) < len(lines) and (j+1) < len(lines[i]):
                    if lines[i+1][j+1] == "@":
                        number_of_adjacent += 1
                if (i-1) >= 0 and (j+1) < len(lines[i]):
                    if lines[i-1][j+1] == "@" :
                        number_of_adjacent += 1 
                if (i+1) < len(lines) and (j-1) >= 0: 
                    if lines[i+1][j-1] == "@":
                        number_of_adjacent += 1
                if number_of_adjacent < 4 :
                    x += 1
print(x)