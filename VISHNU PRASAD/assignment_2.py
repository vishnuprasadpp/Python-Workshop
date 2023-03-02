common_set=[]
even_set=[]

index=1
for add in range(5):
    value= int(input("Enter the number of index position {} ".format(index)))
    common_set.append(value)
    index+=1
print("The set according to input is ",common_set)


for num in common_set:
    if num%2==0:
      even_set.append(num)
print("The Even numbers among the input numbers are ",even_set)
    
          
