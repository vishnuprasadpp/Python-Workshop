mark= int(input("Enter the Mark "))
if mark >= 40:
  print("You have passed the exam")
  if mark >= 90:
    print("You have obtained A+ grade") 
  elif mark<90 and mark>=85:
    print("Your grade is A+") 
  elif mark<85 and mark>=80:
    print("Your grade is A")
  elif mark<80 and mark>=75:
    print("Your grade is B+")
  elif mark<75 and mark>=70:
    print("Your grade is B")
  elif mark<70 and mark>=65:
    print("Your grade is C+")
  else:
    print("You have Grade below C+")

else:
  print("You have Failed the exam. Better luck next time!")
