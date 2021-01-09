cars = ['audi','ford','hyundai','volkswagen','skoda']

for car in cars:
	print(f"\t-{car.title()}")
print(f"These are all nice cars.")

my_car = (cars[1])
print(my_car)

pizzas = ['pepperoni','margherita','hawaian', 'calzone']

for pizza in pizzas:
	print(f"My favourite type of pizza is {pizza.title()}")
msg = f"I really like pizza.\nOn a Monday I like {pizzas[0]}"
print(msg)

canine_family = ['beagle','alsation','jack russel','pug']

for canine in canine_family:
	print(f"A {canine} would be a brilliant pet.")
print("All of these dogs are great company.")

for value in range(1,11):
	print(value)

for value in range(1,21):
	if value % 2 == 0:
		print(f"{value} is an even number!")
	else:
		print(f"{value} is an odd number!")
 
 
squares = [] 
 
for value in range(1,101):
	square = value ** 2
	squares.append(square)
print(squares)


digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

##fav_num_list = []
##prompt = "\nPick your favourite number:"
##fav_num = input(prompt)
##int(fav_num)
##print(fav_num)
##fav_num_list.append(fav_num)
##print(fav_num_list)

"""Counting to 20"""
big_num = []
for value in range(1,1000001):
	big_num.append(value)
print(big_num)


print(sum(big_num))

numbers = []

for value in range(1,1000001):
	numbers.append(value)
print(min(numbers)) #Has to be outside the loop to min/max
print(max(numbers))
print(sum(numbers))

for value in range(18,94):
	if value % 2 == 1:
		print(value)
	else:
		print(f"{value} is an even number")

for value in range(3,31):
	if value % 3 == 0:
		print(value)

for value in range(1,11):
	print(value**3)

num_list = [value**3 for value in range(1,11)]
print(num_list)#Make a list from a range!!!!

for value in range(1,1000001):
	if value %2 == 1:
		print(value)