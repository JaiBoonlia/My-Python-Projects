# 1. Agricultural Production Data Analysis
# Overview
This project performs comprehensive data analysis on agricultural production to extract key insights and support better decision-making. The analysis involves handling real-world agricultural data and leveraging Python to answer critical agricultural metrics and trends.

# Features
The project is designed to solve the following problems:<br>

Calculate the Total Yield by Crop Type.<br>
Determine the Average Price by Crop Type.<br>
Identify High-Yield Crops by Region.<br>
Compute the Total Revenue by Region.<br>
Find the Most Profitable Crop in Each Region.<br>
Pinpoint the Region with the Highest Total Yield.<br>
Summarize Yearly Production for a Crop.<br>
Sort Regions by Average Price.<br>
Add New Crop Data.<br>
Identify the Highest and Lowest Prices for a Crop.<br>
Classify Underperforming Crops.<br>
# Dataset
The dataset (agri.csv) includes agricultural data such as:<br>
Date of entry<br>
Crop type<br>
Region of production<br>
Production yield (in metric units)<br>
Price per unit of the crop<br>
# Core Techniques:
Data structures: Lists, sets, and dictionaries<br>
Python operators, loops, and conditionals<br>
Modular functions for specific tasks<br>
Libraries:
(Optional) For extended functionality, libraries like Pandas and NumPy can be used.

# Each subproblem provides:
Summarized insights like total yield or average prices.<br>
Rankings or filtered data by yield, region, or profit.<br>
Easy addition and verification of new data entries.<br>

# 2. Expense Tracker
# Overview
The Expense Tracker is a simple and efficient Python program to record, categorize, and summarize daily expenses. It provides a user-friendly way to keep track of spending and manage budgets effectively.

# Features
Add Expenses: Record an expense with a description, amount, and category.<br>
View Expense Summary:<br>
Total amount spent.<br>
Breakdown of expenses by category.<br>
Add New Categories: Expand the predefined categories with custom options.<br>
Persistent Storage: Stores expenses in a file (expenses.txt) for future reference.<br>
Easy to Use: Simple text-based interface.<br>
# Predefined Categories
Groceries<br>
Transportation<br>
Utilities<br>
Entertainment<br>
# How to Use
Run the Script:<br>
Select from the following options in the menu:<br>

1. Add Expense:<br>
Enter the expense amount.<br>
Provide a brief description.<br>
Choose from available categories or add new ones.<br>
2. View Summary:<br>
Displays the total spending and categorized breakdown of expenses.<br>
3. Add New Category:<br>
Add a custom category for organizing expenses.<br>
4. Exit: Quit the application.<br>
All recorded expenses are saved automatically in expenses.txt and loaded when the program restarts.<br>
# File Details
expenses.txt: Stores expense data in CSV format: amount,description,category
