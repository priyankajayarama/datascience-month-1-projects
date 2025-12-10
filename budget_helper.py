def print_line():
    print("-" * 40)

print("Budget Maker")
print_line()

# Get budget
while True:
    try:
        budget = float(input("Enter your total budget: $"))
        break
    except ValueError:
        print("Please enter a valid number.")

expenses = []

print("\nEnter your expenses (name + amount).")
print("Type 'q' at any time to finish.")
print_line()

# Expense input loop
while True:
    name = input("Expense name (or q to quit): ").strip()
    if name.lower() == "q" or name == "":
        break

    # get amount
    try:
        amount = float(input("Amount: $"))
    except ValueError:
        print("Invalid amount. Try again.")
        continue

    expenses.append((name, amount))
    print(f"Added: {name} — ${amount:.2f}")
    print_line()

# Calculate results
total_expenses = sum(x[1] for x in expenses)
remaining = budget - total_expenses

# Output summary
print("\n📊 Budget Summary")
print_line()
print(f"Total Budget:        ${budget:.2f}")
print(f"Total Expenses:      ${total_expenses:.2f}")
print(f"Remaining Balance:   ${remaining:.2f}")

# overspending warning
if remaining < 0:
    print("\n⚠️  You are over budget!")
else:
    print("\n👍 You are within your budget.")

print_line()

# Show detailed expenses
print("📁 Expense Breakdown:")
for name, amount in expenses:
    print(f" - {name}: ${amount:.2f}")
print_line()
print("Done!")
