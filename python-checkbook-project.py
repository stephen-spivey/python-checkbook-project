import os
import subprocess


cur_bal = 0
welcome_pg = input("Welcome to your terminal checkbook!\n\n"\
"What would you like to do?\n"\
"1) view current balance\n"\
"2) record a debit (withdraw)\n"\
"3) record a credit (deposit)\n"\
"4) exit\n\n"\
"Your answer: ")
welcome_pg = int(welcome_pg)
print(welcome_pg)
if welcome_pg == 1:
    print("Current balance is: $", new_bal)              
elif welcome_pg == 2:                                                 
    debit_amt = input("You are withdrawing funds\n"\
"How much would you like to withdraw?\n"\
"Enter amount here: $")
    debit_amt = int(debit_amt)
    new_bal = cur_bal - debit_amt
    print('Your new balance is: $', new_bal)
elif welcome_pg == 3:
    dep_amt = input("You are depositing funds\n"\
"How much would you like to deposit?\n"\
"Enter amount here: $")
    dep_amt = int(dep_amt)
    new_bal = cur_bal + dep_amt
    print('Your new balance is: $', new_bal)
elif welcome_pg == 4:
    print("Thank you for using terminal checkbook!")
elif welcome_pg != 1 or 2 or 3 or 4:             
    print("This is not a valid selection\n"\
    "Please make another selection: ")