import random
print("********** Number Guessing Game **********")
print("""This is a number guessing game.
You will keep a number in your mind between 0 and 100 and the computer will try to guess the number you have in mind.

If the computer's prediction is greater than the number you have in mind, Please press "-" key to command the computer to estimate a smaller number.

If the computer's prediction is smaller than the number you have in mind, Please press "+" key to command the computer to estimate a bigger number.

If the computer finds the number you have in mind, Please, press "ENTER"
""")
positive=[]
negative=[]
pc_guess=random.randint(0,100)
while True:
    message=input("The game begins.\nYou keep a number in your mind between 0 and 100.\nIf you keep a number in your mind, Please press 'ENTER'\nPlease press 'q' to quit\n")
    if message.lower()=="q":
        print("The program is terminated.")
        quit()
    if not message:
        print("The number you keep in mind is: ",pc_guess,"\n")
        break
    else:
        print("You made an incorrect entry. Please check and read instructions!!!\n")
        continue
while True:
 try:
    data=input("""For smaller number, Please press '-',\nFor bigger number, Please press '+',\nFor accurate estimation, Please enter 'ENTER'\n""")
    if (data=="-" and pc_guess==0) or (data=="+" and pc_guess==100):
        print("The number you keep in mind should be between 0 and 100.\nYou made an incorrect entry. Please check and read instructions!!!\n")
        continue
    elif data=="-":
         negative.append(pc_guess)
         if positive!=[] and negative!=[]:
             negative.sort()
             positive.sort(reverse=True)
             pc_guess=random.randint(positive[0]+1,negative[0]-1)
         else:
             pc_guess=random.randint(0,pc_guess)
         print("The number you keep in mind is: ",pc_guess,"\n")
         continue
    elif data=="+":
         positive.append(pc_guess)
         if positive!=[] and negative!=[]:
             negative.sort()
             positive.sort(reverse=True)
             pc_guess=random.randint(positive[0]+1,negative[0]-1)
         else:
             pc_guess=random.randint(pc_guess+1,100)
         print("The number you keep in mind is: ",pc_guess,"\n")
         continue
    elif not data:
         print("The number you keep in mind is: ",pc_guess,"\n")
         break
    else:
         print("You made an incorrect entry. Please check and read instructions!!!\n")
 except ValueError:
      print("You made an incorrect entry. Please check and read instructions!!!\n")

    

