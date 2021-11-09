row_number = ['0','1','2','3']
row1 = ['1',"🌫","🌫","🌫"]
row2 = ['2',"🌫","🌫","🌫"]
row3 = ['3',"🌫","🌫","🌫"]

map = [row1, row2, row3]
print(f'{row_number}\n{row1}\n{row2}\n{row3}')
position = input("Where do you want to hide the treasure? ")

#they will input a value like 23
#take first value = column
# second value = row1
# list[[number of list], [number of value in list]]
column = int(position[0]) - 1

row = int(position[1])

map[column][row] = "X"
print(f'{row_number}\n{row1}\n{row2}\n{row3}')
