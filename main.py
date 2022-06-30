print("Note 1:\nIf 10 (binary) =  2 (decimal), then\n  -10 (binary) = -2 (decimal)\n\nNote 2:\nTo avoid incorrect answers DON'T use other numbers except 0 and 1")
num = input("\nEnter the binary number: ")


def decimal1():
  num_ok1 = num[::-1]
  decimal1 =  []
  sum1 = 0
  for i in range(len(num)):
    conv1 = int(num_ok1[i])*2**i
    decimal1.append(conv1)
    sum1 += decimal1[i]
  print(sum1)


def decimal2():
  dec_point = num.find(".")
  num_ahead_dec_point = (num[:dec_point:1])
  num_ok2 = num_ahead_dec_point[::-1]
  decimal_a = []
  sum_a = 0
  for i in range(len(num[:dec_point])):
    conv_a = int(num_ok2[i])*2**i
    decimal_a.append(conv_a)
    sum_a += decimal_a[i]
 
  num_after_dec_point = (num[dec_point + 1::1])
  decimal_b = []
  sum_b = 0
  for i in range(len(num[dec_point + 1::1])):
      conv_b = int(num_after_dec_point[i])*2**-(i+1)
      decimal_b.append(conv_b)
      sum_b += decimal_b[i]
  
  sum2 = sum_a + sum_b
  print(sum2)


pt = num.count(".")
if num.find(".") == -1:
  decimal1()
elif pt > 1:
  print("Wrong Input!")
else:
  decimal2()