import os
from pathlib import Path
import shutil

print(os.listdir())

# creating a path object with the pathlib module
z_path = Path("C:\\Users\\Dell 7390\\OneDrive\\Desktop\\Pycharm files\\Zcodes")

# using methods from the os and pathlib module now with my object because it is a path

print(z_path.home()) # returns the home directories
print(z_path.parent) # returns the directory path up to the current folder
print(z_path.name)   # returns the name of the folder
print(z_path.stem)   # returns name without the extension
print(z_path.suffix) # returns the extension

home = z_path.home()           # create a variable with home directory
directory = z_path.parent      # create a variable of the path to the current directory of the path
folder_name = z_path.name      # create a variable with the name of the folder
no_extension = z_path.stem     # create a variable with no extension to name
extension = z_path.suffix      # create a variable of the extension of the path

new_path = z_path.joinpath("file study") # creates a new directory name by joining a string at the end

if new_path.exists(): # if the path that you created exist or doesn't exist do something
    print("this path exist")

if not new_path.exists():
    #new_path.mkdir()
    print("The not key word means this == False")

#new_f = z_path.joinpath("file.txt")   # create a new file name
#new_f.touch()                         # creates the file , THE TOUCH() METHOD CREATES A FILE
#new_f.write_text("hello world ")      # write text to the file , THIS METHOD CREATES A FILE
#new_f.unlink()                        # deletes the file, THIS METHOD DELETES A FILE

relative_path = Path('filestudy.py')
print(relative_path.resolve())        # resolve method finds the absolute path of a relative path

#for i in range(1, 6):                  # creating multiple files with a template
    #template = f"this is file {i}"
    #file = Path(f"file-{i}.txt")
    #file.write_text(template)

for file in os.listdir():       # iterate through files in a directory
    z = z_path.joinpath(file)   # made a path to specific files in the directory
    print(f"{z.stem:15} {z.suffix}")               # remove the extension on the file
    #print(z.suffix)            # prints the file type by itself


#shutil.move('pokemon.py', z_path)      # move the pokemon program into the zcodes directory                       #

for d , p, f in os.walk(os.getcwd()):   # os.walk returns a tuple with the (path, directory,file)
    print("current path:",  d)          # iterate and organize with the for loop
    print("Directories:", p)
    print("files: ", f)
    print()


