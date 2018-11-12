"""This is my test program."""
# -*- coding: utf-8 -*-

# file = open("test.txt", "w")
# file.write("This has been written to a file")
# file.close()

# file = open("test.txt", "r")
# print(file.read())
# file.close()
# file = open("test.txt", "r")
# print(file.readlines())
# file.close()


# squares = {1:1, 2:4, 3:"error", 4:16}
# squares[8] = 64
# squares[3] = 9
# print(squares.get(3, 1))
# print(squares)

# j = [i**3 for i in range(5)]
# print(j)

# name = input("Enter you name:")
# print("hello", name)

#nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(4, 5, 6)
print(msg)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
