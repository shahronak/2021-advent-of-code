## part 1
with open('day-2-input') as f:
    commands = [line.split() for line in f]
    commands = [(direction, int(delta)) for direction, delta in commands]

horizontal = 0
depth = 0

for x in range(0, len(commands)):
    if commands[x][0] == "forward":
        horizontal += commands[x][1]
    if commands[x][0] == "down":
        depth += commands[x][1]
    if commands[x][0] == "up":   
        depth -= commands[x][1]

print (horizontal)
print (depth)
print (horizontal*depth)

## part 2
horizontal = 0
depth = 0
aim = 0

for x in range(0, len(commands)):
    if commands[x][0] == "forward":
        horizontal += commands[x][1]
        depth += commands[x][1]*aim
    if commands[x][0] == "down":
        aim += commands[x][1]
    if commands[x][0] == "up":   
        aim -= commands[x][1]

print (horizontal)
print (depth)
print (horizontal*depth)
