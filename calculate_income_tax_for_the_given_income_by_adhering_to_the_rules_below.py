# Exercise 12: Calculate income tax for the given income by adhering to the rules below
# Taxable Income	  Rate (in %)
# First $10,000	      0
# Next $10,000	      10
# The remaining	      20

# Expected Output:
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.


taxable_income = int(input("\033[1;32;40mEnter a taxable income: "))
print("taxable income is:", taxable_income)

if taxable_income < 20000:
   

elif taxable_income == 20000:
    income_tax = 10000/10
    

else: 
    income_tax = ((taxable_income - 20000)/5)+1000
  