total_joltage = 0
with open("input.txt") as f:
    while line := f.readline():
        bank = line.rstrip('\n')
        lenght_bank = len(bank)
        max_joltage_possible = 0
        for index_first_jolt in range(lenght_bank):
            for index_second_jolt in range(index_first_jolt+1,lenght_bank):
                first_jolt = bank[index_first_jolt]
                second_jolt = bank[index_second_jolt]
                sum_jolt = first_jolt + second_jolt
                #print(first_jolt, second_jolt, sum_jolt)
                if int(sum_jolt) > max_joltage_possible: 
                    max_joltage_possible = int(sum_jolt)
        total_joltage += max_joltage_possible
print(total_joltage)
