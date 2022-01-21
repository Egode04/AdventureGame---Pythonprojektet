def print_format_table():
    style = 0
    for fg in range(31,38):
        s1 = ''
        bg = 40
        format = ';'.join([str(style), str(fg), str(bg)])
        s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
        print(s1)
    print('\n')

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

def color(clr):
    if clr.lower() == "black":
        return CGREY
    elif clr.lower() == "red":
        return CRED2
    elif clr.lower() == "green":
        return CGREEN2
    elif clr.lower() == "yellow":
        return CYELLOW2
    elif clr.lower() == "blue":
        return CBLUE2
    elif clr.lower() == "pink":
        return CVIOLET2
    elif clr.lower() == "aqua":
        return CBEIGE2
    elif clr.lower() == "white":
        return CWHITE2
    elif clr.lower() == "none":
        return CEND
    elif clr.lower() == "light_red":
        return CRED
    elif clr.lower() == "light_green":
        return CGREEN
    elif clr.lower() == "light_aqua":
        return CBEIGE
    elif clr.lower() == "light_pink":
        return CVIOLET
    elif clr.lower() == "light_yellow":
        return CYELLOW
    elif clr.lower() == "light_blue":
        return CBLUE
    
black = color("black")
red = color("red")
green = color("green")
yellow = color("yellow")
blue = color("blue")
pink = color("pink")
aqua = color("aqua")
white = color("white")
end = color("none")

light_red = color("light_red")
light_green = color("light_green")
light_aqua = color("light_aqua")
light_pink = color("light_pink")
light_yellow = color("light_yellow")
light_blue = color("light_blue")

print(f"This is {red}Color Red{end} and This is {yellow}Color Yellow{end}!")