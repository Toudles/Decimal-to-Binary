"""
Assignment #4, Part 3
Andrew Park
"""

integer1 = int(input("Enter a number greater than or equal to 0: "))
integer = integer1
binary = ""
totalbinary = ""
valid = True


if integer1 < 0:
    valid = False
    while valid == False:
            print("Invalid, try again")
            print()
            integer1 = int(input("Enter a number greater than or equal to 0: "))
            
            if integer1 >= 0:
                valid = True
                integer = integer1
                while valid == True:
                    remainder = (integer%2)
                    if remainder == 1:
                        binary = str(remainder) + binary
                        print(integer, "% 2 =", (integer%2), "---", (binary))
                        print(integer, "/ 2 =", integer//2)
                        integer = (integer//2)
                    elif remainder == 0:
                        binary = str(remainder) + binary
                        print(integer, "% 2 =", (integer%2), "---", (binary))
                        print(integer, "/ 2 =", integer//2)
                        integer = (integer//2)
                    if integer <= 0:
                        print()
                        print(integer1, "in binary is", binary)
                        break

else:
    valid = True
    integer = integer1
    while valid == True:
        remainder = (integer%2)
        if remainder == 1:
            binary = str(remainder) + binary
            print(integer, "% 2 =", (integer%2), "---", (binary))
            print(integer, "/ 2 =", integer//2)
            integer = (integer//2)
        elif remainder == 0:
            binary = str(remainder) + binary
            print(integer, "% 2 =", (integer%2), "---", (binary))
            print(integer, "/ 2 =", integer//2)
            integer = (integer//2)
        if integer <= 0:
            print()
            print(integer1, "in binary is", binary)
            break
