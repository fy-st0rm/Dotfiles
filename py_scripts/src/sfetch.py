#-- Imports
import platform
import os
import random

# Colors for terminal
class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#-- Settings
border = colors.CYAN
info_name = colors.BLUE
info = colors.YELLOW
logo_color = random.choice([colors.PURPLE, colors.BLUE, colors.CYAN, colors.GREEN, colors.RED, colors.YELLOW, colors.DEFAULT])

#-- Info holders
infos = {}

#logo = [
#"░██████╗░█████╗░░██████╗",
#"██╔════╝██╔══██╗██╔════╝",
#"╚█████╗░██║░░██║╚█████╗░",
#"░╚═══██╗██║░░██║░╚═══██╗",
#"██████╔╝╚█████╔╝██████╔╝",
#"╚═════╝░░╚════╝░╚═════╝░"
#]

logo = [
"╋╋╋┏━━━┓   ",
"╋╋╋┃┏━┓┃   ",
"┏━━┫┃┃┃┣━━┓",
"┃━━┫┃┃┃┃━━┫",
"┣━━┃┗━┛┣━━┃",
"┗━━┻━━━┻━━┛"
]

#-- Collecting system information
infos.update({"User": platform.node()})
infos.update({"Os": platform.system()})
infos.update({"Kernel": platform.release()})
infos.update({"Machine": platform.machine()})
infos.update({"DE": os.environ.get("DESKTOP_SESSION")})
infos.update({"Term": os.environ.get("TERM")})
infos.update({"Uptime": os.popen("uptime -p").read()[:-1]})

#-- Generating the length of the box
longest_name = len("machine")
longest_info = len(infos["User"])
longest_line = len(" ") + longest_name + len(": ") + len(infos["User"]) + len(" ")

for i in infos:
    new_line = len(" ") + longest_name + len(": ") + len(infos[i]) + len(" ")
    new_info = len(infos[i])

    if new_line > longest_line: longest_line = new_line
    if new_info > longest_info: longest_info = new_info

#-- Creating the horizontal line of the box
top    = border + "╭" + "─" * longest_line + "╮" + colors.DEFAULT
bottom = border + "╰" + "─" * longest_line + "╯" + colors.DEFAULT

#-- Printing the final info
offset = 0
logo_gap = len(infos) + 2 - len(logo)

print(" " * len(logo[0]) + " " + top)

for line, i in enumerate(infos):
    format = info_name + i + colors.DEFAULT + " " * (longest_name - len(i)) + ": " + info + infos[i] + colors.DEFAULT + " " * (longest_info - len(infos[i]))
    
    #-- Printing logo
    if line + 1 >= logo_gap:
        print(logo_color + logo[offset] + " " + colors.DEFAULT, end="")
        offset += 1

        print(border + "│" + colors.DEFAULT, format, border + "│" + colors.DEFAULT)
    else:
        print(" " * len(logo[0]) + " " + border + "│" + colors.DEFAULT, format, border + "│" + colors.DEFAULT)

print(logo_color + logo[-1] + colors.DEFAULT + " " + bottom)


