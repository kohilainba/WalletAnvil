from ._anvil_designer import depositTemplate
from anvil import *
#import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class deposit(depositTemplate):

    def __init__(self, phone=None, **properties):
        # Initialize self.user as a dictionary
        self.user = {'phone': phone} if phone else {}
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Assuming you have a 'get_username' function in your server module
        username = anvil.server.call('get_username', self.user['phone'])
        self.label_1.text = f"Welcome to Green Gate Financial, {username}"
        user_account_numbers = anvil.server.call('get_user_account_numbers', self.user['phone'])
        self.drop_down_1.items = list(map(str, user_account_numbers)) if user_account_numbers is not None else []

        self.display()

    def button_1_click(self, **event_args):
        current_datetime = datetime.now()
        acc = self.drop_down_1.selected_value

        if self.user and 'phone' in self.user:
            entered_amount = ''.join(filter(str.isdigit, str(self.text_box_2.text)))
            money_value = float(entered_amount) if entered_amount else 0.0

            new_transaction = app_tables.wallet_users_transaction.add_row(
                phone=self.user['phone'],
                fund=money_value,
                date=current_datetime,
                transaction_type="Debit",
                transaction_status="Wallet-Topup",
                receiver_phone=""
            )
            
            balance = app_tables.wallet_users_balance.add_row(
                currency_type= INR,
                e_money = money_value,
                phone=self.user['phone']
            )

            self.label_2.text = "Money added successfully to the account."
        else:
            self.label_2.text = "Error: No matching accounts found for the user or invalid account number."

   

    def drop_down_1_change(self, **event_args):
        self.display()


         

# Assuming 'user_currency' is a dictionary containing user's currency information
# 'money_value' is the amount of money to be added
# 'selected_symbol' is the currency symbol selected by the user

    # def button_1_click(self, money_value, selected_symbol):
    #     if 'phone' in self.user:
    #         # Assuming 'user_currency' is a dictionary containing user's currency information
    #         user_currency = self.user['user_currency']
    
    #         # Update the user's e-wallet with the deposited amount
    #         if selected_symbol in user_currency:
    #             user_currency[selected_symbol] = str(float(user_currency[selected_symbol] or 0) + money_value)
    #         else:
    #             self.label_2.text = "Error: Invalid currency symbol selected."
    #             return
    
    #         user_currency.update()
    
    #         # Add a new transaction record
    #         new_transaction = app_tables.wallet_users_transactions.add_row(
    #             phone=self.user['phone'],
    #             fund=f"{selected_symbol}-{money_value}",
    #             date=current_datetime,
    #             transaction_type="Debit",
    #             transaction_status="Wallet-Topup",
    #             receiver_phone=money_value
    #         )
    
    #         self.label_2.text = "Money added successfully to the e-wallet."
    
    #     else:
    #         self.label_2.text = "Error: User information is not available"

# Example usage:
# Assuming 'self.user' is the user object and 'current_datetime' is the current date and time
# You may need to adapt this to your actual code structure
# Also, handle the case where 'app_tables.transactions' and 'app_tables.user_currency' are defined
# according to your application's backend structure.

# To use the function, call it like this:
# self.add_money_to_e_wallet(money_value, selected_symbol)

    def display(self, **event_args):
          acc=self.drop_down_1.selected_value
          # user_for_emoney = self.user['username']
          # fore_money = anvil.server.call('get_accounts_emoney',acc)
          # acc_validate = anvil.server.call('validate_acc_no_to_display_in_transfer',acc)
          # self.label_6.text = "$" + str(acc_validate['money_usd'])
          # self.label_10.text = "₹ " + str(acc_validate['money_inr'])
          # self.label_11.text = "€ " + str(acc_validate['money_euro'])
          # self.label_12.text = "₣ " + str(acc_validate['money_swis'])
          # e_money_value = str(fore_money['e_money'])
          # eb= self.drop_down_2.selected_value
          # if e_money_value and e_money_value != 'None' and e_money_value.replace('.', '', 1).isdigit() and eb == '$':
          #   try:
          #     e_money_value = float(e_money_value)
          #     dollar_to_rupee = e_money_value / 80.0  # Set a default value, adjust as needed
          #     self.label_14.text = str(dollar_to_rupee)
          #   except ValueError:
          #     pass 
          #   else:
          #       pass
          # if eb == 'Є':
          #   try:
          #     e_money_value = float(e_money_value)  
          #     euro_to_rupee = e_money_value / 90.0
          #     self.label_14.text = str(euro_to_rupee)  # Convert result to string before assigning to label
          #   except ValueError:
          #     pass
          # if eb == '₣':
          #   try:
          #     e_money_value = float(e_money_value)
          #     swis_to_rupee = (e_money_value)/95.0
          #     self.label_14.text = str(swis_to_rupee)
          #   except ValueError:
          #     pass   
          # if eb == '₹':
          #   self.label_14.text = (e_money_value)






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
