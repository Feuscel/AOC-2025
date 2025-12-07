total_joltage = 0
with open("input.txt") as f:
    while line := f.readline():
        bank = line.rstrip('\n')
        index = 0 
        joltage = ""
        for number_loop in reversed(range(12)):
            jolt = 0
            if number_loop != 0:
                jolt = max(bank[index:-number_loop])
            else :
                jolt = max(bank[index:])
            index = bank.find(jolt,index) + 1
            joltage += jolt
        total_joltage += int(joltage) 
print(total_joltage)
