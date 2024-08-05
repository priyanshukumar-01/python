import os
from pathlib import Path

def deldir(directory: Path)->None:
  try:

    if os.path.exists(directory):
      os.rmdir(directory)
    else:
      print(f"No such dirctory name {directory} exists")
  except Exception as e:
    print(e)

if __name__ == "__main__":
  deldir(Path("./old_folder"))


  