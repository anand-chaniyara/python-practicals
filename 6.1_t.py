# 1. Create an empty tuple
emty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers
sisters = ('Alice', 'Bobette', 'Cathy')
brothers = ('David', 'Edward', 'Frank')
siblings = brothers + sisters

# 4. How many siblings do you have?
num_siblings = len(siblings)

# 5. Modify the siblings tuple and add the name of your father and mother
family_members = ('Father', 'Mother') + siblings

# 1. Unpack siblings and parents from family_members
father, mother, *other_family_members = family_members

# 2. Create fruits, vegetables, and animal products tuples. Join the three tuples.
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Spinach', 'Broccoli')
animal_products = ('Chicken', 'Beef', 'Eggs')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index] if len(food_stuff_lt) % 2 != 0 else food_stuff_lt[middle_index-1:middle_index+1]

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
estonia_nordic = 'Estonia' in nordic_countries

# Check if 'Iceland' is a nordic country
iceland_nordic = 'Iceland' in nordic_countries

