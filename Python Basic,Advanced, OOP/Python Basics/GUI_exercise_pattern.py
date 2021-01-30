# GUI example exercise

#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# SOLUTION (STEPS)
# the list above is a 2d list (2d array)
# 1 iterate over picture
# if 1, print '*'
# if 0, print ''

star = '*'
empty = ' '
for row in picture: # rows of the picture
    for col in row: # each row, has several columns
        if col == 1:
            print(star,end="") # string append after last value- side by side
        else:
            print(empty,end="")
    print() # after each row, print a new line









