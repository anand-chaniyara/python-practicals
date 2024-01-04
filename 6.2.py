# Student Ages
student_ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Task 1
student_ages.sort()
min_age = min(student_ages)
max_age = max(student_ages)
student_ages.extend([min_age, max_age])

# Task 2
median_age = (student_ages[len(student_ages)//2 - 1] + student_ages[len(student_ages)//2]) / 2 if len(student_ages) % 2 == 0 else student_ages[len(student_ages)//2]
average_age = sum(student_ages) / len(student_ages)
age_range = max_age - min_age
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)

# Print results for Task 1
print("Sorted Ages: ", student_ages)
print("Min Age: ", min_age)
print("Max Age: ", max_age)

# Print results for Task 2
print("Median Age: ", median_age)
print("Average Age: ", average_age)
print("Age Range: ", age_range)
print("Abs(Min - Average): ", min_average_diff)
print("Abs(Max - Average): ",max_average_diff)

# Countries List
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Task 3
middle_countries = countries[len(countries)//2 - 1:len(countries)//2 + 1] if len(countries) % 2 == 0 else [countries[len(countries)//2]]

# Task 4
first_half = countries[:len(countries)//2 + len(countries) % 2]
second_half = countries[len(countries)//2 + len(countries) % 2:]

# Task 5
first_three, *scandic_countries = countries[:3], countries[3:]

# Print results for Task 3, 4, and 5
print("\nMiddle Country(ies): ", middle_countries)
print("First Half: ", first_half)
print("Second Half: ", second_half)
print("First Three Countries:", first_three)
print("Scandic Countries: ", scandic_countries)
