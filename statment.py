# Conditional Statement

age = int(input("Please enter you age:"))
 
if age >= 18 :
    print ("You are an adult and now you can vote")
elif age < 18 and age > 11 :
    print("You are a teenager")
else :
    print("You are a child")