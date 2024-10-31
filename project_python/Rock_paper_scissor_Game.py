# Rock_Scissor_Paper_Game


import random # choice of random numbers
import sys  # system control open / exit
from enum import Enum # help to assign the unique value

# chose variable name as class RPS(Rock, paper ,scissor) 
# for assign unique values. UPPER CASE stands for constant.
class RPS(Enum):
       ROCK =1 
       SCISSOR =2
       PAPER = 3
# print(RPS(3))
# print(RPS.ROCK.value)
# print(RPS["SCISSOR"])


print(" ")

playerchoice = input("Enter...\n1 for Rock\n2 for Scissor\n3 for Paper:\n\n")

# printing 1,2,3 and choices Rock,Scissor,paper                                                 
# print(playerchoice)  # choice 1 printed
# print(type(playerchoice)) # type is string, but we need integer

player = int(playerchoice) # datatype converted into string to integer

if player < 1 or player > 3: # if player choice lessthan 1 or more then 3 
# the lofic error ask system to exit from the programme with error message
   sys.exit("😨 you must enter 1, 2, or 3.")


computerchoice =random.choice("123") 
# computer choicing randomly 123 as string
computer =int(computerchoice) #datatype converted into integer from string

# Hold the below printing method for include RPS value alternate method
# print("you chose" + " " + playerchoice + " .")
# print("python chose"+ " "+ computerchoice + ".")

# instead of value sending the variable as value passing in RPS
# to convert the datatype from enum to string use constructor str
# use method replace for remove printing RPS in result

print("you chose" + " " + str(RPS(player)).replace("RPS.", " ")+ " .") 
print("python chose"+ " "+ str(RPS(computer)).replace("RPS.", " ") + ".")


if player==1 and computer ==3:
       print("🎉 you win")
elif player ==2 and computer == 1:
       print("🎯 you win")
elif player ==3 and computer == 2:
       print("😎 you win")
elif player == computer:
       print("🦋 Tie Game")
else:
       print("🏆 python win...!!!")







