COLOUR_NAMES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "azure": "f0ffff",
    "bisque": "#ffe4c4",
    "chartreuse": "#7fff00",
    "coral": "ff7f50",
    "crimson": "#dc143c",
    "darkcyan": "#008b8b",
    "deepskyblue": "#00bfff"
}

print(COLOUR_NAMES)

colour_code = input("Enter colour name: ").lower()
while colour_code != "":
    try:
        print(f"{colour_code} is {COLOUR_NAMES[colour_code]}")
    except KeyError:
        print("Invalid colour name")

    colour_code = input("Enter colour name: ").lower()

print("Thank you!")
