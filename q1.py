def pangkat(num,pow):
  number = 1
  for x in range(pow):
    number=number*num
  return number

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))


