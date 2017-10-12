portion_deposit = 0.25
total_cost = 1000000
target = total_cost*portion_deposit
epsilon = 100
semi_annual_raise = 0.07
invest_return_rate = 0.04
total_saved = 0
months = 36
saving_rate = 0.5

annual_salary = float(input("Annual Salary: "))

for i in range(months):
	if (i % 6 == 0):
		annual_salary += semi_annual_raise
		
	total_saved += ((total_saved *invest_return_rate) / 12) + ((annual_salary / 12))

iterations = 0
while total_saved*saving_rate > target+epsilon or total_saved*saving_rate < target-epsilon:
	if total_saved*saving_rate > target+epsilon:
		saving_rate = saving_rate/2
	else:
		saving_rate += saving_rate/2
		
	print(total_saved*saving_rate)
