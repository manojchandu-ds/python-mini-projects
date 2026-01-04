print("*******Welcome to Percentage Calculator*******")
print("Made with love❤️")

a = int(input("Enter your maths subject marks: "))
b = int(input("Enter your chemistry subject marks: "))
c = int(input("Enter your physics subject marks: "))
d = int(input("Enter your english subject marks: "))
e = int(input("Enter your Samskrit subject marks: "))

total = a + b + c + d + e 
percentage = (total / 500) * 100
print("Your total is ", total)
if percentage >= 90:
    print("Your percentage is ",percentage, "You nailed it ⚡")
elif 90 <= percentage < 75:
    print("Your percentage is ",percentage, "Keep it up 👀")
elif 75 <= percentage < 55:
    print("Your percentage is",percentage, "Yep you studied soo hard 👍")
elif 55 <= percentage < 35:
    print("Your percentage is",percentage, "You just cameup for enjoyment 😵‍💫")
else:
    print("Your percentage is",percentage, "You nailed it keep going on to next year 😵") 



      