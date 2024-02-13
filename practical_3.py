# A)
str1="Anand"
str2="Chaniyara"
print("reversed string :",str1[::-1])
print("Replaced string :",str1.replace("and","end"))
print("Merge two string :",str1+str2)
print("Find character in string :","a" in str1)

st = "Hello, World!"
print("words", st.split())
print("characters",[char for char in st])

# B)
drct={
    "name":"Anand",
    "age":22 ,   
    "grade":"AB"
}

print("update  Dictionary Values:",drct.update({'grade':'AA'}))
print("Access Dictionary Values: ",drct.values())
print("Access Dictionary key: ",drct.keys())
print("Print the 'age': ",drct.get('age'))
print("pop : ",drct.pop('age'))
print("pop item :",drct.popitem())
print("clear :",drct.clear())
print("delete :")
del drct

dict1 = {'A': 1, 'B': 2}
dict2 = {'C': 3, 'D': 4}
dict3 = {'E': 5, 'F': 6}

merged_dict = dict1 | dict2 | dict3

print(merged_dict)