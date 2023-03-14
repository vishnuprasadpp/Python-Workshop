with open("numbers.txt","r") as myFile:
    display= myFile.readline()
    print(display)
    display=display.split(",")

 with open("even_numbers","w") as file_to_write:
     for element in display:
         if int(element)%2==0:
             file_to_write.write(element)
             file_to_write.write("\n")

 with open("even_numbers", "r") as even:
     file=even.read()
     print(file)

