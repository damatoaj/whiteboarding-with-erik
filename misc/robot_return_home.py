# Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. 
# The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively. 

# L = -1 x
# R = +1 x
# D = -1 y
# U = +1 y

def return_home(directions):
  x = 0
  y = 0
  for direction in directions:
    if direction == "R":
      x += 1
    elif direction == "L":
      x -= 1
    elif direction == "U":
      y += 1
    elif direction == "D":
      y -= 1
  # print("X:", x, "Y:", y)
  return x == 0 and y == 0

print(return_home("LRUDRLDU"))
# -> True
print(return_home("LRUDRLD"))
# -> False
print(return_home("LRULLRRDDRUDLLLURRLRULLRRDDRUDLLLURR"))