Core Structure:


The application creates a GUI window with two main sections: left and right panels
Left panel: Shows the account balance and a pie chart of spending by category
Right panel: Contains input fields for transactions and a transaction history table


Main Features:


Add transactions with amount, category, and date
View all transactions in a table format
Delete selected transactions
Automatic balance updating
Visual representation of spending via pie chart
Input validation for transaction entries


Key Functions:


add_transaction(): Validates and adds new transactions to the system
update_balance(): Recalculates and displays the current account balance
update_pie_chart(): Creates/updates a visual breakdown of spending by category
delete_transaction(): Removes selected transactions from the list
update_transaction_list(): Refreshes the transaction history display


User Interface:


Clean, white background with a professional layout
Input fields for amount, category, and date
Add and Delete buttons with distinct colors (green and red)
Tree view component to display transaction history
Dynamic pie chart showing spending distribution
