name = input("Name: ")
age = int(input("Age: "))
height = int(input("Height(cm): "))
weight = int(input("Weight(kg): "))
eye = input("Eye Colour: ")
hair = input("Hair Colour: ")

print("%s is %i years old." % (name,age))

if (age <= 10): print("%s is probably too young to be at uni right now." % (name))
elif (age > 10 and age <= 35): print("%s is young." % (name))
elif (age > 35 and age <= 80): print("%s is old." % (name))
else: print("%s is REALLY old." % (name))

if (height==weight): print("%s's height and weight are the same, that probably isnt healthy." % (name))
else: print("Im too lazy to insult %s's height or weight right now." % (name))

print("%s has %s eyes and %s hair." % (name,eye,hair))
