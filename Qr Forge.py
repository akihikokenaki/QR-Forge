import qrcode
from qrcode.console_scripts import error_correction

colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
    "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet",
    "brown", "burlywood", "cadetblue", "chartreuse", "chocolate",
    "coral", "cornflowerblue", "cornsilk", "crimson", "cyan",
    "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen",
    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
    "darkorchid", "darkred", "darksalmon", "darkseagreen",
    "darkslateblue", "darkslategray", "darkturquoise", "darkviolet",
    "deeppink", "deepskyblue", "dimgray", "dodgerblue", "firebrick",
    "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite",
    "gold", "goldenrod", "gray", "green", "greenyellow", "honeydew",
    "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender",
    "lavenderblush", "lawngreen", "lemonchiffon", "lightblue",
    "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen",
    "lightgray", "lightpink", "lightsalmon", "lightseagreen",
    "lightskyblue", "lightslategray", "lightsteelblue", "lightyellow",
    "lime", "limegreen", "linen", "magenta", "maroon",
    "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple",
    "mediumseagreen", "mediumslateblue", "mediumspringgreen",
    "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream",
    "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive",
    "olivedrab", "orange", "orangered", "orchid", "palegoldenrod",
    "palegreen", "paleturquoise", "palevioletred", "papayawhip",
    "peachpuff", "peru", "pink", "plum", "powderblue", "purple",
    "rebeccapurple", "red", "rosybrown", "royalblue", "saddlebrown",
    "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver",
    "skyblue", "slateblue", "slategray", "snow", "springgreen",
    "steelblue", "tan", "teal", "thistle", "tomato", "turquoise",
    "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"
]

data = input("Your text or link: ")

while True:
    version = input("QR Size (1-40): ")
    if any(char.isalpha() for char in version):
        print("Please enter only number")

    elif version.strip() == "":
        version = 1
        break

    else:
        try:
            version = int(version)
            if 1 <= version <= 40:
                break

            else:
                print("please enter a number between 1 to 40: ")

        except ValueError:
            print("Invalid Input: please enter a number")


while True:
    box_size = input("Square size (1–10): ")

    if any(char.isalpha() for char in box_size):
        print("Please enter only number")

    elif box_size.strip() == "":
        box_size = 1
        break

    else:
        try:
            box_size = int(box_size)
            if 1 <= box_size <= 40:
                break

            else:
                print("please enter a number between 1 to 10: ")

        except ValueError:
            print("Invalid Input: please enter a number")

while True:
    border = input("Border size (1–10): ")

    if any(char.isalpha() for char in border):
        print("Please enter only number")

    elif border.strip() == "":
        border = 1
        break

    else:
        try:
            border = int(border)
            if 1 <= border <= 40:
                break

            else:
                print("please enter a number between 1 to 10: ")

        except ValueError:
            print("Invalid Input: please enter a number")

qr = qrcode.QRCode(
    version=version,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=box_size,
    border=border,
)

qr.add_data(data)
qr.make(fit=True)

while True:
    fill_color = input("Square color (leave empty for black): ")
    if fill_color in colors:
        break

    elif fill_color.strip() == "":
        fill_color = "black"
        break

    else:
        print("Enter a valid color")

while True:
    back_color = input("Background color (leave empty for white): ")
    if back_color in colors:
        break

    elif back_color.strip() == "":
        back_color = "white"
        break

    else:
        print("Enter a valid color")

img = qr.make_image(fill_color=fill_color, back_color=back_color)

while True:
    img_name = input("Enter image name (leave empty for default 'QR.png' and no .png or .jpg): ")

    if img_name.lower().endswith((".png", ".jpg")):
        print("Do not include .png or .jpg")

    elif img_name == "":
        img_name = "Qr"
        break

    else:
        break

img.save(img_name + ".png")
print(f"Your QR '{img_name}.png' has been created successfully!")
