import os
from pathlib import Path
import shutil
# import needed packages


downloads = Path(r"C:\Users\Dell 7390\Downloads")   # create a file object for the downloads directory
os.chdir(downloads)                                 # change your current directory to the downloads path
print(os.listdir())                                 # list files in your directory for reference

for files in os.listdir():                          # iterate through files in your directory
    file = downloads.joinpath(files)                # create object for the file
    folder = file.suffix                            # creates a folder for each file type using the suffix method
    if not downloads.joinpath(folder).exists():     # if folder doesn't exist create one
        os.mkdir(downloads.joinpath(folder))
        if files.endswith(folder):
            shutil.move(files, downloads.joinpath(folder))  # otherwise file joins the folder with the matching suffix
    else:
        shutil.move(files, downloads.joinpath(folder))


print(os.listdir())   # look at your organized downloads

