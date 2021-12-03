increased = 0

filename = "sampleinput.txt"

with open(filename) as f:
    lines = f.read().splitlines()

lines_num = list(map(int, lines))

print(type(lines_num))
print("len of lines", len(lines_num))
print(lines_num)

for i in range(len(lines_num) - 3):
  a = i 
  b = i + 1
  c = i + 2

  val1 = lines_num[a] + lines_num[b] + lines_num[c]
  print("val 1 is", val1)
  val2 = lines_num[a + 1] + lines_num[b + 1] + lines_num[c + 1]
  print("val 2 is", val2)

  if val2 > val1:
    increased += 1

print("this is the inc", increased)