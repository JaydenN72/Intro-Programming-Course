# Function Assignment - Python Program

# 1. Circle Function
def circleArea(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

# 2. Taxes Function
def calculateTaxes(money, tax_rate):
    total_due = money + (money * tax_rate)
    return total_due

# 3. Temperature Function
def fahrenhiteToCelsius(fahrenhite):
    celsius = (fahrenhite - 32) * (5 / 9)
    return celsius

print("Circle Area Calculation ")
user_radius = float(input("Circle Radius: "))
circle_result = circleArea(user_radius)
print(f"Output: {circle_result:.2f}")


print("Taxes Calculation")
user_money = float(input("Enter money amount: "))
# Accepts decimal representation (e.g., 0.06 for 6%)
user_tax_rate = float(input("Enter tax rate as a decimal): "))
tax_result = calculateTaxes(user_money, user_tax_rate)
print(f"Output: {tax_result:.2f}")


print("Temperature Conversion")
user_fahrenhite = float(input("Fahrenhite temperature: "))
temp_result = fahrenhiteToCelsius(user_fahrenhite)
print(f"Output: {temp_result}")