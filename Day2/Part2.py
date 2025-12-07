sum = 0
with open("entrer.txt") as f:
    line = f.readline()
    ranges = line.split(',')
    for range_id in ranges:
      range_ = range_id.split('-')
      start_range = range_[0]
      end_range = range_[1]
      for id in range(int(start_range),int(end_range)+1,1):
        str_id = str(id)
        lenght_id = len(str_id)
        # print("-----------------")
        for index in range(1, (lenght_id//2)+1):
          # print("Id              : " + str_id)
          # print("index           : " + "-" + str(index))
          is_sub_valid = True
          if lenght_id % index == 0 :
            test_caracters = str_id[-index:]
            # print(" Test caractere : " + test_caracters)
            for i_sub_id in range(0, lenght_id+1-index, index):
              sub_id = str_id[i_sub_id:i_sub_id+index]
              # print(" index sub id   : "+ str(i_sub_id))
              # print(" sub id         : " + sub_id)
              if sub_id == test_caracters :
                is_sub_valid = True
              else :
                is_sub_valid = False
                break
          else :
            is_sub_valid = False
          if is_sub_valid == True :
              # print("Valid Id        : " + str_id )
              sum += id
              break
print(sum)

