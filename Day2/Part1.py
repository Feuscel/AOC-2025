sum = 0
with open("entrer.txt") as f:
    line = f.readline()
    ranges = line.split(',')
    for range_id in ranges:
      range_ = range_id.split('-')
      start_range = range_[0]
      end_range = range_[1]
      for id in range(int(start_range),int(end_range)+1,1):
        even_len_id = (len(str(id)) % 2) == 0
        left_side_id = (str(id)[0:len(str(id)) // 2])
        right_side_id = (str(id)[len(str(id)) // 2:])
        if even_len_id and left_side_id == right_side_id :
          sum += id
print(sum)
