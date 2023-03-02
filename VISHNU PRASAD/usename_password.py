user={"user1": "123", "user2": "456","user3": "789"}

user_name= input("Enter the username here: ")
if user_name in user:
  password= input("Enter your PASSWORD: ")
  if password== user[user_name]:
    print("You are Logged in!")
  else:
    print("Incorrect Password! Please enter the correct password")
else:
  print("Incorrect Username! Please enter the correct username oncemore ")
