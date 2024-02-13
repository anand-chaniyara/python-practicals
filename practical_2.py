
#A)
your_list = [2, 6, 5, 3, 5, 4, 1, 5, 4, 6, 9 ]

your_list.append(5)
print("Append :",your_list)

your_list.extend([5, 8, 9])
print("extend :",your_list)

your_list.remove(5)
print("remove :",your_list)

your_list.reverse()
print("reverse :",your_list)

your_list.sort()
print("List in ascending order:", your_list)

your_list.sort(reverse=True)
print("List in descending order:", your_list)


#B)

your_list = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]

word1 = your_list[8][2]
print("Word 1:", word1)

word2 = your_list[4][0].capitalize()
print("Word 2:", word2)

new_list = [your_list] * 5
print("Repeated list:", new_list)



#C)

original_list = [99, 92, 39, 45, 55, 66, 57]

copied_list = original_list[:]

print("Original List:", original_list)
print("Copied List:", copied_list)


#D)
# Create a tuple
my_tuple = (15, 22, 73, 54, 25)

sum_tuple = sum(my_tuple)
print("Sum of Tuple:", sum_tuple)

max_tuple = max(my_tuple)
print("Maximum value in Tuple:", max_tuple)

min_tuple = min(my_tuple)
print("Minimum value in Tuple:", min_tuple)
