myFile= open("numbers.txt","r")

display= myFile.readline()
print(display)
display=display.split(",")
print(display)

file_to_write= open("even_numbers","w")
                    
for element in display:
  if int(element)%2==0:
      file_to_write.write(element)
      file_to_write.write("\n")
      print(element)

myFile.close()

