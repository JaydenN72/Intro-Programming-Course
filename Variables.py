print("Please enter your first number")
first_number = int(input())
print("Please enter your second number")
second_number = int(input())
print("Please enter your sign (+, -, *, /, %, //)")
sign = input()
#this isnt "int(input) because the signs are a string, not a input per say
if sign == "+":
    answer = first_number + second_number
elif sign == "-":
    answer = first_number - second_number
elif sign == "*":
    answer = first_number * second_number
elif sign == "/":
    answer = first_number / second_number
elif sign == "%":
    answer = first_number % second_number
elif sign == "//":
    answer = first_number // second_number
else:
    answer = "unable to be outputed due to an Invalid Sign"

print("The answer to your query is {}\n".format(answer))
print("Jayden Narvaez")