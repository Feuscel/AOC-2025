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
        elif even_len_id and not left_side_id == right_side_id :
          if len(str(id)) % 5 == 0:
            lenght = len(str(id)) // 5
            left_side_id = (str(id)[0:lenght])
            midle_side_id = (str(id)[lenght:lenght+lenght])
            right_side_id = (str(id)[-(lenght) :])
          else:
            lenght = len(str(id)) // 2
            left_side_id = (str(id)[0:lenght-1])
            midle_side_id = (str(id)[lenght-1:(lenght-1)+(lenght-1)])
            right_side_id = (str(id)[-(lenght-1):])
          if left_side_id == midle_side_id and left_side_id == right_side_id and midle_side_id == right_side_id :
            sum += id
        elif not even_len_id :
          lenght = 0
          if len(str(id)) % 7 == 0:
            lenght = len(str(id)) // 7
          elif len(str(id)) % 5 == 0:
            lenght = len(str(id)) // 5
          elif len(str(id)) % 3 == 0:
            lenght = len(str(id)) // 3
          left_side_id = (str(id)[0:lenght])
          midle_side_id = (str(id)[lenght:lenght+lenght])
          right_side_id = (str(id)[-(lenght) :])
          if left_side_id == midle_side_id and left_side_id == right_side_id and midle_side_id == right_side_id :
            sum += id
print(sum)

