Phy = float(input("Enter your marks scored in Physics: "))
Chem = float(input("Enter your marks scored in Chemistry: "))
Math = float(input("Enter your marks scored in Maths: "))

marks = {"Physics":Phy, "Chemistry":Chem, "Mathematics":Math}
highest_marks = max(marks, key = marks.get)
lowest_marks = min(marks, key = marks.get)
print(f"Highest marks in: {highest_marks}")
print(f"Lowest marks in: {lowest_marks}")

total = Phy + Chem + Math
percentage = round(((total / 300) * 100), 2)
print(percentage)


if percentage < 40:
    print("You Failed")
elif 40 <= percentage < 60:
    print("You Passed")
elif 60 <= percentage < 75:
    print("You Passed with 1st class")
else:
    print("You passed with distinction")
