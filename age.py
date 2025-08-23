#Age check with categories
age = int(input("enter your age: "))
if (age<=10):
    print("You are a kid fella.")
elif( age>=11 and age<20):
    print("You are in your teens ENJOY!")
elif( age>=20 and age<40):
    print("Work hard fella coz you are an ADULT")
elif( age>=40 and age<60): 
    print("Just few years more friend, U almost retired.")
elif( age>=60 and age<=90):
    print("You have retired fella.")
elif ( age>90):
    print("Should I carbon date u fella?, Die already")
