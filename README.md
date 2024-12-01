# Expense-Tracker
Build a simple expense tracker to manage your finances.
Expense Tracker CLI
Overview
The Expense Tracker CLI is a command-line interface (CLI) tool for managing and tracking expenses. You can use this tool to add, update, delete, view, and summarize your expenses. All data is stored in a CSV file (data.csv), and the tool provides features for maintaining and analyzing your expenses.
Features
• Add Expenses: Add new expenses with a description and amount.
• Update Expenses: Modify existing expense details (description and/or amount).
• Delete Expenses: Remove expenses by their ID.
• Show Expenses: View a list of all recorded expenses.
• Summarize Expenses: Get total expenses, with an optional filter by month.
Installation
1. Make sure you have Python 3.6+ installed.
2. Install the `click` module by running:

   pip install click

3. Clone or download the project files and navigate to the folder where `expenseTracker.py` is located.
Usage
The main executable is `expenseTracker.py`. Use the following commands to interact with the tool:
Add an Expense
Command:
python expenseTracker.py add --description <description> --amount <amount>

Example:
python expenseTracker.py add --description "Lunch" --amount 15

Output:
Expense added successfully (ID: 1)

Update an Expense
Command:
python expenseTracker.py update --id <id> [--new-description <new_description>] [--new-amount <new_amount>]

Example:
python expenseTracker.py update --id 1 --new-description "Dinner" --new-amount 20

Output:
ID 1 was updated successfully

Delete an Expense
Command:
python expenseTracker.py delete --id <id>

Example:
python expenseTracker.py delete --id 1

Output:
ID 1 was deleted.

Show All Expenses
Command:
python expenseTracker.py show

Example Output:
ID    Date                 Description     Amount    
--------------------------------------------------
1     2024-12-01 12:34:56 Lunch           15
2     2024-12-01 18:45:20 Groceries       30

Summarize Expenses
Command:
python expenseTracker.py summary [--month <month>]

Example:
python expenseTracker.py summary --month 12

Output:
Total expenses for December: $45

File Structure
- `expenseTracker.py`: Main script for CLI functionality.
- `data.csv`: CSV file used to store all expense records. It is automatically created if it does not exist.
Notes
• Date Format: Dates are recorded in the format `YYYY-MM-DD HH:MM:SS`.
• CSV File: Ensure the `data.csv` file is not edited manually to prevent corruption of data.
• Error Handling: The tool provides meaningful error messages for invalid inputs (e.g., invalid IDs or options).
Example Workflow
1. Add two expenses:
   python expenseTracker.py add --description "Lunch" --amount 15
   python expenseTracker.py add --description "Groceries" --amount 30

2. View all expenses:
   python expenseTracker.py show

3. Update the first expense:
   python expenseTracker.py update --id 1 --new-description "Dinner"

4. Delete the second expense:
   python expenseTracker.py delete --id 2

5. Summarize expenses for December:
   python expenseTracker.py summary --month 12
License
This project is free to use and modify for personal or educational purposes.
URL project: https://roadmap.sh/projects/expense-tracker
