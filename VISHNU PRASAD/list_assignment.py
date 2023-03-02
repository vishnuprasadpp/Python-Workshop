common_set=[]
even_set=[]

index=1
for add in range(5):
    value= int(input("Enter the number of index position {} :".format(index)))
    common_set.append(value)
    index+=1
print("The set according to the input is ",common_set)


for element in common_set:
    if element%2==0:
      even_set.append(element)
print("The EVEN numbers among the input numbers are ",even_set)
