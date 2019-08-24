hours_scheduled = input('How many hour have you been scheduled? ')
incentives = input('How much will you receive as incentives? ')
billable_hours = 145 * int(hours_scheduled)
taxable_income = billable_hours + int(incentives)
tax = taxable_income * 0.05
money_in_bank = taxable_income - tax
print("You'll be deducted " + str(tax) + ' as taxes')
print("You'll receive " + str(money_in_bank) + "in your account")
