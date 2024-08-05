import os
from colorama import Fore,Style,init
init(autoreset=True)
def tree()->None:
    try:
        path = input(Fore.GREEN +"Enter the path: ")
        if os.path.exists(path):
            listing = os.walk(path)

            for root_path , directoires,files in listing:
                print(f"{Fore.LIGHTMAGENTA_EX }root_path =  {root_path}")
                print(f"{Fore.LIGHTBLUE_EX }directories =  {directoires}")
                print(f"{Fore.LIGHTCYAN_EX }files =  {files}")
        else:
            print(Fore.RED +"Path does not exist")
    except:
        print(f'{path},it is not a valid input')
tree()