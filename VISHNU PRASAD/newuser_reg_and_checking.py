user={}
index=1

for add in range(3):
  username= input("Enter the username {} for signup : ".format(index))
  password= input("Enter the password here: ")
  user[username]=password
  index+=1

print("You are successfully signedup! click OK for login") 
yesno=input("")
if yesno=="ok":
  user_name= input("Enter the username here: ")
  if user_name in user:
    password_for_checking= input("Enter your PASSWORD: ")
    if password_for_checking== user[user_name]:
      print("You are Logged in!")
    else:
      print("Incorrect Password! Please enter the correct password")
  else:
    print("Incorrect Username! Please enter the correct username oncemore ")
else:
  print("Thankyou for registering")






