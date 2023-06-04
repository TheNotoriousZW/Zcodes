from colorama import Fore, Style, Back

x = "A"
print(ord(x))                   # ord() function converts the specified character into integer
print(chr(ord(x)))              # chr() function converts the specified integer value into character

x = "0"

try:
    print(ord(x))               # returns integer
    print(chr(x))
except TypeError:
    print("the chr() function only accepts integers")

try:
    print("chr: ", chr(90))
    print(ord(5))
except TypeError:
    print("The ord() function only accepts string characters")

print(f"{Fore.RED}chr: {chr(90)}  ord: {ord(chr(90))}")

# the chr function takes a integer and returns the character of that integer
# the ord function takes a chr and returns the integer of the character

string = "python"
chr_list = []
for ch in string:
    chr_list.append(ord(ch))
    print(f"{Fore.CYAN} {ord(ch)} {Style.RESET_ALL}")
for ord in chr_list:
    print(f"{Fore.MAGENTA}{chr(ord)}{Style.RESET_ALL}", end=" * ")


