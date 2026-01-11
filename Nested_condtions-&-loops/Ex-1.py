a = (input())
b = int(input())
if a == "admin":
  if b == int("1234"):
    print("Login success")
  else:
    print("Wrong password")
else:
  print("Invalid username")
