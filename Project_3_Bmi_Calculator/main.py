# get height and weight
height = float(input("enter you height ini m: ")) 
weight = int(input("enter you weigh ni kg: ")) 

# calculate bmi function
def calBmi(height,weight):
    bmi = 0
    bmi = weight / height ** 2
    return round(bmi)

if calBmi(height, weight) < 18.5:
    print(f"Your BMI is {calBmi(height,weight)}, you are underweight.")
elif calBmi(height, weight) < 25:
    print(f"Your BMI is {calBmi(height,weight)}, you are normal weight.")
elif calBmi(height, weight) < 30:
    print(f"Your BMI is {calBmi(height,weight)}, you are slightly overweight.")
elif calBmi(height, weight) < 35:
    print(f"Your BMI is {calBmi(height,weight)}, you are obese.")
else:
    print(f"Your BMI is {calBmi(height,weight)}, you are clinically obese.")
