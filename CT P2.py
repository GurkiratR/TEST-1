RED = "red"
BLUE = "blue"
YELLOW = "yellow"

color1 = input("Enter the first primary color: ")
color2 = input("Enter the second primary color: ")

if color1 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color1")
elif color2 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
    if (color1 == RED and color2 == BLUE) or (color1 == BLUE and color2 == RED):
        print("Purple")
    elif (color1 == RED and color2 == YELLOW) or (color1 == YELLOW and color2 == RED):
        print("Orange")
    elif (color1 == BLUE and color2 == YELLOW) or (color1 == YELLOW and color2 == BLUE):
        print("Green")
