n1= int(input("Enter the first number for operation "))
n2= int(input("Enter the second number for operation "))
operant= input("Enter the operant ")
if operant== "+":
    sum1= n1+n2
    print("The sum of two number is", sum1)
elif operant== "-":
    difference= n1-n2
    print("The difference of two number is", difference)
elif operant== "*":
    product= n1*n2
    print("The product of two number is ", product)
elif operant== "/":
    if n2==0:
        print("A number cannot be divided by zero!")
    else:
        division= n1/n2
        print("The division of two number is ", division)
else:
    print("You entered a wrong operand!")
