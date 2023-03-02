list=[]
a=0
index=1

for add in range(5):
    value= int(input("Enter the number of index position {} :".format(index)))
    list.append(value)
    index+=1
print("The set according to the input is ",list)

for num in list:
  a=a+num
print("The sum of elements in list equal to",a)
  
