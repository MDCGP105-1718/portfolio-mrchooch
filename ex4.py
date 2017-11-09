my_name = 'Chris Janes'
my_age = 21 # maybe
my_height_inches = 67 # inches
my_weight_pounds = 160 # pounds
inches_to_cm = 2.54
pounds_to_kg = 0.453592
my_height_cm = my_height_inches*inches_to_cm # cm
my_weight_kg = my_weight_pounds*pounds_to_kg # kg

my_eyes = 'Green'
my_hair = 'Ginger'
is_heavy = my_weight_pounds > 3000
print(f"Let's talk about {my_name}.")
print(f"He is {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"It is {is_heavy} that he is overweight.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
total = my_age + my_height_inches + my_weight_pounds
print(f"If I add {my_age}, {my_height} and {my_weight} I get
{total}")
