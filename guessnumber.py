import random

secretNumb=random.randint(0,10)

i=0

while(i<5):
   i=i+1

   myNumber=int(input("guess a number between 1 to 9"))

   if(myNumber == secretNumb):
       print("you guessed the correct number")
       break
    
     elif(myNumber<secretNumb):
        print("your guess was too low:guess a number higher than",myNumber)
    
     elif(myNumber>secretNumb):
        print("your guess was too high:guess a number lower than",myNumber)
    
     if(i == 4):
        print("sorry time out:the number was",secretNumb)
