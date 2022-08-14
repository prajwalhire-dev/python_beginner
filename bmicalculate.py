Height = float(input("Enter your height in centimeters : "))
Weight = float(input("Enter your weight in Kg : "))
Height = Height/100
BMI = Weight/(Height**2)
print("Your Body mass index is : ", BMI )
if (BMI > 0):
    if (BMI<=16):
        print("Your are severly under-weight")
    elif(BMI<=18.5):
        print("your are underweight")
    elif(BMI<=25):
        print("You are Healthy")
    elif(BMI<=30):
        print("you are overweight")
    else: print("you are severly overweight")
else: print("enter invalid details")