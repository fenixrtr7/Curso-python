numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []

for number in numbers:
    square = number**2
    squares.append(square)

print(squares)
#-----------------------------------------------------
numbers2 = [11, 12, 13, 14, 15, 16]

squares2 = [x**2 for x in numbers2]
print(squares2)