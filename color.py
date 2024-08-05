
from colorama import Fore, Style, init

init(autoreset=True)
string = 'priyanshu'
for i in dir(Fore):
  try:
   print(getattr(Fore, i) + string)
  except:
    print(end='')
    break
    
