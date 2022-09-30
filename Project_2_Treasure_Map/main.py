# horizontal map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the tressure? ")

# get the horizontal & vertical position you want
horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

# put insert X vertical map 
map[vertical][horizontal] = "X"

# print new position
print(f"{row1}\n{row2}\n{row3}")
