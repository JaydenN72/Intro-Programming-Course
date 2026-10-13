
kw_hours = int(input("Enter the KW hours used: "))

if kw_hours <= 1000:
    total_cents = kw_hours * 7.633
else:
    first_thousand = 1000 * 7.633
    extra_hours = kw_hours - 1000
    extra_cost = extra_hours * 9.259
    total_cents = first_thousand + extra_cost

total_dollars = total_cents / 100

print(f"Amount owed is ${total_dollars}")