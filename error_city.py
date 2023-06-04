from colorama import Fore, Back, Style

# error handling
try:                                                # Try block
    f = open('filer.txt')                           # try to run this code
except:                                             # except block
    print(Fore.RED + "something went wrong do this", Style.RESET_ALL)    # if the code throws a error do this


# be specific with except blocks
try:
    f = open('fil.txt')
except FileNotFoundError as e:
    print(f"{Fore.RED }we expect this went wrong {e} {Style.RESET_ALL}")
else:                                               # if the try block ran smooth do this
    pass
finally:                                            # finally branch always execute
    print("i will always execute")

val = [1, 4, 'Hello', 5, 0, 3, 'z', 2]

#for value in val:                                   # error handling in a loop
    #try:
        #print(f" {10 / value}" , end="")

    #except:
        #print("something went wrong here", end="")

for value in val:
    try:
        print(f"{10 / value}", end=" : ")           # the end="" method is a seperator

    except (ValueError, ZeroDivisionError):         # you can tuple an exception block
        pass
    except Exception as e:
        print(Fore.RED + "no good", Style.RESET_ALL, end=" : ")

#class wrong_number(ValueError, ZeroDivisionError, TypeError):    # you can create your own error class
    #pass

#def phone(number):
    #if len(str(number)) > 7:
        #return number
    #else:
        #raise wrong_number('invalid number')                    # more defined name to the error

#phone(413231)


info = {
    "Firstname": "Zaphon",
    "lastname": "wray"
}

try:                            # try block for a dictionary
    print(info["country"])
except Exception as e:
    print()
    print(Fore.RED + "Invalid Key")                          # make Exception specific   # Colorrama method to show red
    print(f"key: {e}" + Style.RESET_ALL )                    # returns the keyError exception as the key("country")
                        # Style method to reset the color





