#  Posted from EduTools plugin
# put your python code here
days_spent = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

meals_cost = days_spent * food_cost
travel_cost = 2 * flight_cost
nights_cost = (days_spent - 1) * hotel_cost
total_cost = meals_cost + travel_cost + nights_cost

print(total_cost)
