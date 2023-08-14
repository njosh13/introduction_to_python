# Let's assume you are planning to use your Python skills to build a social networking service.
# You decide to host your application on servers running in the cloud. You pick a hosting provider
# that charges $0.51 per hour. You will launch your service using one server and want to know
# how much it will cost to operate per day and per month.
# Write a Python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per month?

cost_per_hour = 0.51
currency = '$'
day_in_hours = 24
month_in_hours = day_in_hours * 30

# Question 1
cost_per_day = cost_per_hour * day_in_hours
print('cost per day: {1}{0:.2f}' .format(cost_per_day, currency))

# Question 2
cost_per_month = cost_per_hour * month_in_hours
print('cost per month: {1}{0:.2f}' .format(cost_per_month, currency))

# Building on the previous example, let's also assume that you have saved $918 to fund your new
# adventure. You wonder how many days you can keep one server running before your money
# runs out. Of course, you hope your social network becomes popular and requires 20 servers to
# keep up with the demand. How much will it cost to operate at that point?
# Write a Python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per month?
# How much does it cost to operate twenty servers per day?
# How much does it cost to operate twenty servers per month?
# How many days can I operate one server with $918?

saved_amount = 918
servers = 20

# Question 3
twenty_servers_per_day = servers * cost_per_day
print('twenty servers per day {0}{1:.2f}' .format(
    currency, twenty_servers_per_day))

# Question 4
twenty_servers_per_month = servers * cost_per_month
print('twenty servers per month {0}{1:.2f}' .format(
    currency, twenty_servers_per_month))

# Question 5
days = saved_amount / cost_per_day
full_days = int(days)
print('$918 can buy: {} days' .format(full_days))
