portion_deposit = 0.2
current_savings = 0
months = 0

total_cost = float(input("Total cost of house: "))
annual_salary = float(input("Annual Salary: "))
portion_saved = float(input("% saved per month (as a float): "))
semi_annual_raise = float(input("Semi Annual raise % (as a float): "))

while current_savings < (total_cost*portion_deposit):
	months += 1
	if (months % 6 == 0):
		annual_salary += semi_annual_raise
		
	current_savings += ((current_savings * 0.04) / 12) + ((annual_salary / 12) * portion_saved)




print(months)