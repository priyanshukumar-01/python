
import random


pass_items_number:list[str] = ["1","2","3","4","5","6","7","8","9","0"]
pass_items_specialchar:list[str] = ["!","@","#","$","%","&","*","(",")","+","-",";",":","|",".",",","?",">","<","~","=","{","}","[","]"]
pass_items_alphabet:list[str] = ["A","B","C","d","E","F","G","H","I","J","k","l","M"]
pass_mainlist:list[str] = pass_items_alphabet+pass_items_number+pass_items_specialchar
def pass_generaotr(pass_lenght:int)->str:

  password:str = ""
  
  for i in range(pass_lenght):
    password+=random.choice(pass_mainlist)
  random.shuffle(list(password))
  return str(password)

if __name__ == "__main__":
  print(pass_generaotr(3))
