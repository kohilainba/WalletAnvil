from ._anvil_designer import depositTemplate
from anvil import *
#import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class deposit(depositTemplate):
    def __init__(self, user=None, **properties):
        # Set Form properties and Data Bindings.
        self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
        print(f"User parameter in deposit form: {user}")
        self.user = user
        self.init_components(**properties)

  
#     def button_1_click(self, **event_args):
#         current_datetime = datetime.now()

#         if self.user is not None:
#             wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

#             if wallet3 is None:
#                 self.label_2.text = "Error: Wallet is empty"
#                 return

#             money3_numeric = ''.join(filter(str.isdigit, str(self.text_box_3.text)))
#             money_value = float(money3_numeric) if money3_numeric else 0.0

#             selected_symbol = self.drop_down_1.selected_value

#             entered_account_number = self.text_box_2.text

#             user_currencies = anvil.server.call('get_currency_data', entered_account_number)

#             if len(str(entered_account_number)) < 10 or not str(entered_account_number).isdigit():
#                 self.label_2.text = "Error: Invalid account number. Please enter at least 10 digits."
#                 return

#             if user_currencies is not None:
#                 user_currency = user_currencies

#                 if selected_symbol == '€':
#                     user_currency['money_euro'] = str((float(user_currency['money_euro'] or 0)) + money_value)
#                 elif selected_symbol == '$':
#                     user_currency['money_usd'] = str((float(user_currency['money_usd'] or 0)) + money_value)
#                 elif selected_symbol == '₣':
#                     user_currency['money_swis'] = str((float(user_currency['money_swis'] or 0)) + money_value)
#                 elif selected_symbol == '₹':
#                     user_currency['money_inr'] = str((float(user_currency['money_inr'] or 0)) + money_value)
#                 else:
#                     self.label_2.text = "Error: Invalid currency symbol selected."
#                     return

#                 user_currency.update()

#                 # #Convert deposited amount to INR
#                 # inr_value = money_value
#                 # if selected_symbol != '₹':
#                 #     # Define exchange rates
#                 #     exchange_rates = {'$': 74.5, '€': 88.2, '₣': 80.0}  # Example rates
#                 #     if selected_symbol in exchange_rates:
#                 #         inr_value = money_value * exchange_rates[selected_symbol]
#                 #     else:
#                 #         self.label_2.text = "Error: Invalid currency symbol selected."
#                 #         return

#                 # # Update the user's limit in INR
#                 # remaining_limit = int(self.user['limit'] or 0) - inr_value
#                 # if remaining_limit < 0:
#                 #     alert("Limit exceeded. Cannot deposit more than the limit.")
#                 #     return  # Return to prevent storing negative value in 'limit' column and further execution

#                 # self.user['limit'] = remaining_limit
#                 # self.user.update()

#                 new_transaction = app_tables.transactions.add_row(
#                     user=self.user['username'],
#                     casa=int(entered_account_number),
#                     e_wallet=wallet3,
#                     money=f"{selected_symbol}-{money_value}",
#                     date=current_datetime,
#                     transaction_type="Deposit",
#                     proof="success"
#                 )

#                 self.label_2.text = "Money added successfully to the account." #Remaining limit: {}".format(remaining_limit)
#             else:
#                 self.label_2.text = "Error: No matching accounts found for the user or invalid account number."
#         else:
#             self.label_2.text = "Error: User information is not available"

# Assuming 'user_currency' is a dictionary containing user's currency information
# 'money_value' is the amount of money to be added
# 'selected_symbol' is the currency symbol selected by the user

    def button_1_click(self, money_value, selected_symbol):
        if 'phone' in self.user:
            # Assuming 'user_currency' is a dictionary containing user's currency information
            user_currency = self.user['user_currency']
    
            # Update the user's e-wallet with the deposited amount
            if selected_symbol in user_currency:
                user_currency[selected_symbol] = str(float(user_currency[selected_symbol] or 0) + money_value)
            else:
                self.label_2.text = "Error: Invalid currency symbol selected."
                return
    
            user_currency.update()
    
            # Add a new transaction record
            new_transaction = app_tables.wallet_users_transactions.add_row(
                phone=self.user['phone'],
                fund=f"{selected_symbol}-{money_value}",
                date=current_datetime,
                transaction_type="Debit",
                transaction_status="Wallet-Topup",
                receiver_phone=money_value
            )
    
            self.label_2.text = "Money added successfully to the e-wallet."
    
        else:
            self.label_2.text = "Error: User information is not available"

# Example usage:
# Assuming 'self.user' is the user object and 'current_datetime' is the current date and time
# You may need to adapt this to your actual code structure
# Also, handle the case where 'app_tables.transactions' and 'app_tables.user_currency' are defined
# according to your application's backend structure.

# To use the function, call it like this:
# self.add_money_to_e_wallet(money_value, selected_symbol)






    def link_2_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("deposit",user=self.user)

    def link_3_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("transfer",user=self.user)

    def link_4_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("withdraw",user=self.user)

    def link_7_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)

    def link_1_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("customer",user=self.user)

    def link_13_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("Home")

    def link_8_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)




# from ._anvil_designer import depositTemplate
# from anvil import *
# import anvil.server

# class deposit(depositTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.
