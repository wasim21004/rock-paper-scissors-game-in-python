

import random


l=["rock","paper","scissors"]

while True:
 user=input("Enter any one rock ,paper ,scissors\n you choice ")
 com=random.choice(l)
 print(" computer choice ",com)
 if user in l:
  if user==com:
    print("tie")
  elif com=="rock" and user=="paper":
      print("win")
  elif com=="paper" and user=="scissors":
      print("win")
  elif com=="scissors" and user=="rock":
      print("win")      
  else:
      print("loss")
 else:
      print("try again")

