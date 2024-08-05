import time
import sys
a = 10.1234
f'{a:.2f}'


questions: list[str] = ["what is the capital of INDIA? ","what is the capital of GERMANY? ","what is the capital of FRANCE? ","what is the capital of USA? "]

answer:list[str] = ["NEW DELHI","BERLIN","PARIS","WASHINGTON DC"]

def quizagame()->str:
  playing = input("do you want to play (yes or not)? ")
  if playing.lower() == "yes":
    initial_Time = time.time()
    print("******* welcome to my quiz game *******")
    print()
    write_Answer:int = 0
    wrong_Answer:int = 0
    try:
      for i in range(len(questions)):
      
          print(f"{questions[i]}")
          userAnswer = input("Enter your Answer or enter 'q' to quit: ")
          assert userAnswer,'Enter the Answer'
          if (userAnswer.upper() == "Q"):
            break
          
          
          if (userAnswer.upper() == answer[i] ):
            write_Answer+=1
            print("WRITE ANSWER")
            print()
          else:
            wrong_Answer+=1
            print("wrong")
            print()
            print(F"the correct answer is '{answer[i]}'")
      final_time = time.time()
      print(f"Number of correct answer you did {write_Answer} out of {len(questions)}")
      print(f"Number of wrong answer you did {wrong_Answer} out of {len(questions)}")
      print(f"Total time taken {-1*(initial_Time - final_time):.2f} seconds")
    except Exception as e:
      print(e)
      print("Enter a valid input")
          
  else:
    sys.exit("hope you will play")
  

if __name__ == "__main__":
  quizagame()
    
    
