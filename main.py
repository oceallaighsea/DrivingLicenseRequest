# Page 187        DrivingLicince.py
# Determine if user is eligible to get a driving licence

age = int(input("Please enter your age: "))
hasProvisional = input("Do you have a provisional (y/n)")
if age >= 17:
    if hasProvisional == "y":
        print("You can apply for a Licence.")
    else:
        print("You can not apply, get a provisional")
else:
    print("you cant apply for a provisional - you are too young")
