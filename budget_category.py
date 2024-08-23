'''

Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.

- Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

- Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.

Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.
'''

class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__remaining_budget = budget

# Implement Getters and Setters
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_budget(self):
        return self.__budget
    
    def set_bidget(self, budget):
        if budget > 0:
            self.__budget = budget
            self.__remaining_budget = budget
        else:
            print("Budget should be a positive number.")
# Add Budget Functionality
    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
            else: 
                print("Insufficient budget for this expense.")
        else:
            print("Expense should be a positive number.")
# Display Budget Details
    def display_category_summary(self):
        print(f"Category: {self.__name}")
        print(f"Allocated Budget: {self.__budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")

    
# Instance of BudgetCategory
        food_category = BudgetCategory("Food", 1000)

# An expense to the categroy
        food_category.add_expense(500)

# display the budget category details
        food_category.display_category_summary()  
        