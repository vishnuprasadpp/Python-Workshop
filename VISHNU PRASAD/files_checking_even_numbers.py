myFile= open("numbers.txt","r")

display= myFile.readline()
print(display)
display=display.split(",")
print(display)

for element in display:
  if int(element)%2==0:
      print(element)

myFile.close()

