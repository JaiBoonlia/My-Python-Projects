# Predefined expense categories
categories = ["groceries", "transportation", "utilities", "entertainment"]
expenses = []  # List to store expense entries

file_name = "expenses.txt"

file_exists = False
try:
    file = open(file_name, "r")
    file_exists = True
    for line in file:
        entry = line.strip().split(",")
        if len(entry) == 3:  # Ensure there are exactly 3 parts
            amount = float(entry[0])
            description = entry[1]
            category = entry[2]
            expenses.append({
                "amount": amount,
                "description": description,
                "category": category
            })
    file.close()
except FileNotFoundError:
    file_exists = False

if not file_exists:
    print("No previous data found. Starting fresh.")

# User interface loop
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Add New Category")
    print("4. Exit")

    choice = input("Choose an option: ")
    
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        # Add Expense
        amount_input = input("Enter amount spent: ")
        if amount_input.replace('.', '', 1).isdigit() and float(amount_input) > 0:  # Check if it's a valid float
            amount = float(amount_input)
            description = input("Enter a brief description: ")
            print("Categories:", ", ".join(categories))
            category = input("Enter category: ")

            if category in categories:
                expenses.append({
                    "amount": amount,
                    "description": description,
                    "category": category
                })

                # Save to file
                file = open(file_name, "a")
                file.write(f"{amount},{description},{category}\n")
                file.close()

                print("Expense added successfully.")
            else:
                print("Invalid category. Please choose an existing category or add a new one.")
        else:
            print("Invalid input. Amount should be a number.")

    elif choice == 2:
        # View Summary
        if not expenses:
            print("No expenses recorded yet.")
        else:
            total = 0
            breakdown = {}

            for expense in expenses:
                total += expense["amount"]
                if expense["category"] in breakdown:
                    breakdown[expense["category"]] += expense["amount"]
                else:
                    breakdown[expense["category"]] = expense["amount"]

            print("\nExpense Summary:")
            print(f"Total Expenses: ${total}")
            print("Breakdown by Category:")
            for category, amount in breakdown.items():
                print(f"  {category}: ${amount}")

    elif choice == 3:
        # Add New Category
        new_category = input("Enter new category name: ").strip()
        if new_category in categories:
            print("Category already exists.")
        else:
            categories.append(new_category)
            print("New category added successfully.")

    elif choice == 4:
        # Exit
        print("Exiting the Expense Tracker...")
        break

    else:
        print("Invalid choice. Please choose a number between 1 and 4.")