## Calculate a users BMI 
# The formula for BMI is bmi = (weight / height^2) * 703
# 1. Ask for the users weight by using an input function that asks the question, "how much do you weigh?"
# 2. Convert user input to an integer with the proper variable
# Must convert users input into an integer so python doesn't treat it like a string
# 3. Ask the user their height in inches with an input function
# 4. Convert the users height to a integer with the proper variable
# Must convert users input into an integer so python doesn't treat it like a string
# 5. Use the BMI formula to calculate the output
# 6. Print the function

print("Welcome to the Body Mass Index Calculator!")
weight = input("Lets calculate your BMI, how much do you weigh? ")
weight = int(weight)

height = input("What is your height in inches? ")
height = int(height)

bmi = (weight / height**2) * 703
print("Your BMI is", bmi)