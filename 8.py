# Exercise: Day 8

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
student = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210"
    }
}

# 4. Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# 5. Get the value of skills and check the data type, it should be a list
skills_value = student["skills"]
print("Skills:", skills_value)
print("Data type of skills:", type(skills_value))

# 6. Modify the skills values by adding one or two skills
student["skills"].extend(["HTML", "CSS"])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
print("Dictionary values:", values_list)

# 9. Change the dictionary to a list of tuples using items() method
student_tuples = list(student.items())
print("List of tuples:", student_tuples)

# 10. Delete one of the items in the dictionary
student.pop('is_marred')

# 11. Delete one of the dictionaries
del dog

# Printing the modified dictionaries
print("Modified student dictionary:", student)
