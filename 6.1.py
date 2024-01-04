
# 1. Declare an empty list
empy_lst = []

# 2. Declare a list with more than 5 items
list_with_five_item = [1, 2, 3, 4, 5, 6, 7]

# 3. Find the length of your list
length_of_list = len(list_with_five_item)

# 4. Get the first item, the middle item, and the last item of the list
first_item = list_with_five_item[0]
middle_item = list_with_five_item[length_of_list // 2]
last_item = list_with_five_item[-1]

# 5. Declare a list called mixed_data_types
mixed_data = ["Your Name", 25, 1.75, "Married", "Your Address"]

# 6. Declare a list variable named good_it_companies
good_it_companies = ["GoldmanSachs", "Atlasian", "Wipro", "Infosys", "IBM", "Oracle", "Odoo"]

# 7. Print the list using print()
print(good_it_companies)

# 8. Print the number of companies in the list
print("Number of companies:", len(good_it_companies))

# 9. Print the first, middle, and last company
print("First company:", good_it_companies[0])
print("Middle company:", good_it_companies[len(good_it_companies) // 2])
print("Last company:", good_it_companies[-1])

# 10. Print the list after modifying one of the companies
good_it_companies[2] = "Updated Company"
print(good_it_companies)

# 11. Add an IT company to good_it_companies
good_it_companies.append("New Company")

# 12. Insert an IT company in the middle of the companies list
good_it_companies.insert(len(good_it_companies) // 2, "Middle Company")

# 13. Change one of the good_it_companies names to uppercase (IBM excluded!)
good_it_companies[4] = good_it_companies[4].upper()

# 14. Join the good_it_companies with a string '#;&nbsp; '
joined_companies = '#;&nbsp; '.join(good_it_companies)
print(joined_companies)

# 15. Check if a certain company exists in the good_it_companies list
company_to_check = "Google"
print(company_to_check in good_it_companies)

# 16. Sort the list using sort() method
good_it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
good_it_companies.reverse()

# 18. Slice out the first 3 companies from the list
first_three_companies = good_it_companies[:3]

# 19. Slice out the last 3 companies from the list
last_three_companies = good_it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
middle_companies = good_it_companies[1:-1]

# 21. Remove the first IT company from the list
good_it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
good_it_companies.pop(len(good_it_companies) // 2)

# 23. Remove the last IT company from the list
good_it_companies.pop()

# 24. Remove all IT companies from the list
good_it_companies.clear()

# 25. Destroy the IT companies list
del good_it_companies

# 26. Join the following lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
joined_lists = list1 + list2
print(joined_lists)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
full_stack = joined_lists.copy()

# Then insert Python and SQL after Redux.
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")

print(full_stack)