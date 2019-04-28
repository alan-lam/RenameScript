#! python3
# rename.py - renames files by replacing spaces with periods

import os

for foldername, subfolder, filenames in os.walk(os.getcwd()):
   for filename in filenames:
      listy = filename.split(' ')
      new_name = '.'.join(listy)
      os.rename(filename, new_name)
