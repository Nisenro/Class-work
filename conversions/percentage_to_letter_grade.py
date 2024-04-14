# Your script, called percentage_to_letter_grade.py, will implement this table using a chained conditional statement (i.e. using if, elif and else) to print out the correct letter grade given a percentage as input. For bonus points: use a string function to check whether the given input is a digit and in the range of 0 to 100 and exit gracefully if invalid input is given.

valid_input = input("Please give your grade in percentages (0-100): ")

if valid_input.isdigit():
    grade = int(valid_input)
    if 0 <= grade <= 100: 
        if grade >= 70:
            print("Your letter grade is A.")
        elif grade >= 60:
            print("Your letter grade is B.")
        elif grade >= 50:
            print("Your letter grade is C.")
        elif grade >= 40:
            print("Your letter grade is D.")
        elif grade >= 30:
            print("Your letter grade is E.")
        else:
            print("Your letter grade is F.")
    else:
        print("Please input a digit between 0 and 100.")
else:
    print("Please input a digit between 0 and 100.")
   