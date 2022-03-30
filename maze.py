import csv


with open("map_maze/rect_01.map", "r") as map:
    lines = map.read().split('\n')
matrix = []

pt_start = (0, 0)
pt_finish = (0, 0)
x = 0

position_x = 0
position_y = 0
finish_x = 0
finish_y = 0

for line in lines:
    y = 0
    if x == 0 or x > len(matrix) - 1:
        matrix.append([])
    for value in line:
        if value == '1':
            position_x = x
            position_y = y

        if value == '2':
            finish_x = x
            finish_y = y

        matrix[x].append(value)
        y += 1

    x += 1

for i in range(0, 12):
    print(matrix[i])

pt_start = (position_x, position_y)
print(pt_start)
