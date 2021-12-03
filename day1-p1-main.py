increased = 0

filename = "sampleinput.txt"

with open(filename) as f:
    lines = f.read().splitlines()

lines_num = list(map(int, lines))

print(type(lines_num))
print("len of lines", len(lines_num))
print(lines_num)

for i in range(len(lines_num) - 1):
  val1 = i 
  print("val 1 is", val1)
  val2 = i + 1
  print("val 2 is", val2)

  if val2 > val1:
    increased += 1

print("this is the inc", increased)