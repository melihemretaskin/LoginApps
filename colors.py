import socket
import getpass


class color:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PROPE = '\033[0m' #Düz yazı
    BOLD = '\033[1m'  #Kalın yazı
    UNDERLINE = '\033[4m' #Altçizgili


class lang:
    class tr:
        unknown_command = "Bilinmeyen komut."


directory = "C:\\" #dizin
authorization = "$"  #yetki
if directory == "C:\\":
    displayed_directory = "~"
else:
    displayed_directory = directory
run = True

commands = ["exit"]