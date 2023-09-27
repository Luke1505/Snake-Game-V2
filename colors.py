# Defining colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
blurple = (114, 137, 218)
cyan = (0, 255, 255)
purple = (128, 0, 255)
yellow = (255, 255, 0)
brown = (153, 51, 0)
pink = (255, 0, 255)
orange = (255, 69, 0)
gray = (128, 128, 128)
standard = (240, 240, 237)
baby_blue = (173, 216, 230)
dark_green = (34, 139, 34)
peach = (255, 218, 185)
voilet = (199, 21, 133)
sienna = (160, 82, 45)
Seagreen = (60, 179, 113)
orchid = (153, 50, 204)
slate_blue = (106, 90, 205)
light_pink = (255, 182, 193)
aqua = (127, 255, 212)
dark_red = (139, 0, 0)
dark_sea_green = (143, 188, 143)
dark_magenta = (139, 0, 139)
sandy_brown = (244, 164, 96)
light_green = (144, 238, 144)
lavender = (230, 230, 250)
Deep_Sky_blue = (0, 191, 255)
Deep_Pink = (255, 20, 147)
old_lace = (253, 245, 230)
Rosy_brown = (188, 143, 143)
light_steel_blue = (176, 196, 222)
Alice_blue = (240, 248, 255)
Ghost_white = (248, 248, 255)
Tan = (210, 180, 140)
Teal = (0, 128, 128)
pink2 = (255, 192, 203)
Dark_gray = (169, 169, 169)
orange2 = (255, 165, 0)
saddle_brown = (139, 69, 19)
Firebrick = (178, 34, 34)
Tomato = (255, 99, 71)
Green2 = (0, 128, 0)
Indian_red = (205, 92, 92)
Chocolate = (210, 105, 30)
Plum = (221, 160, 221)
Light_blue = (173, 216, 230)
Light_gray = (211, 211, 211)
Light_salmon = (255, 160, 122)
Light_coral = (240, 128, 128)
Light_cyan = (224, 255, 255)
Light_goldenrod_yellow = (250, 250, 210)
Light_yellow = (255, 255, 224)
colors = [blue, blurple, green, cyan, purple, yellow, brown, pink, purple, orange, gray, baby_blue,
          dark_green, peach, voilet, sienna, Seagreen, orchid, slate_blue, light_pink, aqua, dark_red,
          dark_sea_green, dark_magenta, sandy_brown, light_green, lavender, Deep_Sky_blue, Deep_Pink,
          old_lace, Rosy_brown, light_steel_blue, Alice_blue, Ghost_white, Tan, Teal, pink2, Dark_gray,
          orange2, saddle_brown, Firebrick, Tomato, Green2, Indian_red, Chocolate, Plum, Light_blue,
          Light_gray, Light_salmon, Light_coral, Light_cyan, Light_goldenrod_yellow, Light_yellow]
color = green
color2 = cyan

# Converting rgb to hex


def from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'