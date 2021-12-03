
horizontal_pos = 0
depth = 0
aim = 0

filenamenum = "nums.txt"
filenamewords = "words.txt"

with open(filenamenum) as f:
    num_list = f.read().splitlines()

with open(filenamewords) as f:
    word_list = f.read().splitlines()

num_list = list(map(int, num_list))

#print(num_list)
#print(word_list)

for i in range(len(word_list)):
  if word_list[i] == "up":
    aim = aim - num_list[i]

  if word_list[i] == "down":
    aim = aim + num_list[i]

  if word_list[i] == "forward":
    horizontal_pos += num_list[i]
    depth += num_list[i] * aim
    


print("horizontal position:", horizontal_pos)
print("depth position: ", depth)

print("final position is: ", horizontal_pos*depth)
