def sum(a,b):
  c=a+b
  return c
def difference(a,b):
  c=a-b
  return c

n1=int(input("Enter a number: "))
n2= int(input("Enter the second number: "))
operator=input("Enter 'sum' for addition and 'difference' for difference: ")

if operator=="sum":
  print(sum(n1,n2))
else:
  print(difference(n1,n2)) 

