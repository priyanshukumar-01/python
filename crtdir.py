import os
from pathlib import Path



def crtdir(directory: Path)->None:
  try:
    if not os.path.exists(directory) : 
      os.mkdir(directory)
    else:
      print( "directory already exists")
  except Exception as e:
    print(e)

dir_name = input("Enter the path: ")

crtdir(dir_name)