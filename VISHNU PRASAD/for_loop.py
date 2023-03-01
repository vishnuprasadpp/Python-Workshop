x=0
word=input("Enter a word ")
for char in word: 
  if char.isupper():
    x=x+1
if x>0:
  print("The word you entered contain capital letters")
else:
  print("The word you entered is purely lowercase", word)
  

