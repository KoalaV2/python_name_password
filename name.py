#Enter a name in "<name>"
#And a password in "<password>"
import getpass
name = input("What is your name? \n :")
password_not = getpass-getpass("Enter your pin \n :")
while not password_not.isdigit():
  password_not = input("Please enter a number \n :")
password = int(password_not)
if name.lower() == ("name") and password_not == ("<password>"):
  print ("Acces granted")
else:
  print ("Acces denied")
