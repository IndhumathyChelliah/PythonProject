import random

number=random.randrange(1,4)

Player=input("enter stone,paper,scissor: ")

computer=0

if number==1:
  Computer="stone"
elif number==2:
  Computer="paper"
else:
  Computer="scissor"

while True:
  if Player=="stone":
    if Computer=="stone":
      print ("match draw")
    elif Computer=="Scissor":
      print ("match won")
    else: 
      print ("match loss")
    break

  elif Player=="scissor":
    if Computer=="stone":
      print ("match loss")
    elif Computer=="Scissor":
      print ("match draw") 
    else: 
      print ("match won")
    break
   

  elif Player=="paper":
    if Computer=="stone":
      print ("match loss")
    elif Computer=="Scissor":
      print ("match won")
    else: 
      print ("match draw")
    break



 


    
