def avg(lst):
  return sum(lst) / len(lst)


def letter(avg):
  if avg >= 90:
    return "A"
  if avg >= 80:
    return "B"
  if avg >= 70:
    return "C"
  if avg >= 60:
    return "D"
  return "F"


# Get user input
name = input("Enter the student name: ")
lst = []

for i in range(5):
  score = float(input(f"Grade {i + 1}: "))
  lst.append(score)

# Calculate results
avg = avg(lst)
letter = letter(avg)

# Print output
print("Final Grade")
print(name)
print(f"Average: {avg:.1f}")
print(f"Letter Grade: {letter}")