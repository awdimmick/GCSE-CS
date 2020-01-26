import set_colour as sc

# Store the 0s and 1s that make up our bitmap in a string
bitmap_data = "01010101 10101010 01010101 10101010 01010101 10101010 01010101 10101010 "

# Split bitmap_data at each space - i.e. into the chunks that will make up each row
bitmap_rows = bitmap_data.split()

sc.set_colour("RED")

# Loop through each row
for row in bitmap_rows:
    # Loop through each 0 or 1 (value) within each row
    for value in row:
        if value == "0":
            print(" ", end="") # end = "" is a special argument that we can pass to print() to stop it from printing a
                               # newline
        elif value == "1":
            print("*", end="") # try replacing * with \u2588 - this is a Unicode 'block' character - you can find other unicode characters to use here: https://unicode-table.com/en/#2588
    print()

# Task 1 - Replace the 0s and 1s in bitmap_data with the values for your own design

# Task 2 - Adapt your program so that it can handle multiple colours by using two bits for each pixel. For example,
# 00 = black, 01 = white, 10 = blue and 11 = red.

# To do this, you will need to find a way to look at every two characters instead of every 1 character within each row.
# You might want to slice your rows every 2 characters (think back to your Manipulating Strings assignments).
#
# You can use the set_colour() procedure to change the colour of the output generated by print(), for
# example, the following code will print "Hello!" in red and then reset the output back to normal:
#
# set_colour("RED")  # set to red
# print("Hello!")  # print message
# set_colour("RESET")  # reset output
#
# You can see which colours you can use by looking inside the set_colour() procedure's code at the start of the program.

