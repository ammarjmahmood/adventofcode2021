with open("sample.txt") as f:
  nums = [x for x in f.read().split()]

gamma = ""
epsilon = ""

for i in range(0, len(nums[0])):
  zero = 0
  one = 0
  for j in range(0, len(nums)):
    if nums[j][i] == "0":
      zero += 1
    else:
      one += 1

  if zero > one :
    gamma += "0"
    epsilon += "1"
  else:
    gamma += "1"
    epsilon += "0"

g = int(gamma, 2)
e = int(epsilon, 2)
print("THE READING IS", g * e)