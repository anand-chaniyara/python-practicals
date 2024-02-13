s1="anand"
print("reversed string :",s1[::-1])
print("Replaced string :",s1.replace("NaN","nan"))
print("Find character in string :","a" in s1)

tuple=('A','B','C','D','E')
str1=str(tuple)
print("tuple :",type(str1))

list2=['S','T','U','V','W']
str2=str(list2)
print("list :",type(str2),str2)

set1={'N','M','O','P','Q'}
str3=str(set1)
print("set1 :",type(str3),str3)

print("uppercase :",s1.upper())
print("lowercase :",s1.lower())

print("Split :",s1.split("r"))


tuple=(1,23,45,5,6)
print("Max :",max(tuple))
print("Min :",min(tuple))
print("Length :",len(tuple))
print("sum",sum(tuple))



list1=[12,22,44,53,66]
print("Max :",max(list1))
print("Min :",min(list1))
print("Length :",len(list1))
print("sum",sum(list1))


l1=['a','b','c','d','e']
list3=list(l1)
print("Coping list :",list3,type(list3))

dr={
    "name":"Anand",
    "age":22 ,   
    "grade":"AB"
}
print("Access Dictionary Values: ",dr.values())
print("Print the 'age': ",dr.get('age'))
dr['age']=20
print("Modify Modify Dictionary Values:",dr)

dr.update({'grade':'AA'})
print("update  Dictionary Values:",dr)

print("Check if the key 'gender' is present in the student dictionary :",'gender' in dr)

set1={11,22,33}
set2={33,44,55}

print("union",set1.union(set2))
print("union",set1 | set2)

print("intersection :",set1.intersection(set2))

print("Difference : ",set1.difference(set2))

print("Subset : ",set1.issubset(set2))

subject={}
subject['maths']={"Parv","Rohan","Anand"}
subject ['science']={"Abdul" , "Homi" , "Jagdish" }
print(subject)

subject['maths'].add("Chintu")
print("Add :",subject)

subject['maths'].remove("Chintu")
print("remove :",subject)


print("intersection :",subject["maths"].intersection(subject ["science"]))

country = {'USA': {'New York': 86230, 'Los Angeles': 3990, 'Chicago': 2700},
                    'China': {'Shanghai': 241800, 'Beijing': 21700, 'Guangzhou': 140400},
                    'India': {'Mumbai': 18400, 'Delhi': 16090, 'Bangalore': 11800}}

print("Nested Distionary :",country)



elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_indices = elements[::2]
odd_indices = elements[1::2]
print("even :",even_indices)  
print("odd :",odd_indices) 


a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)


test= [1, 2, 3, 2, 1]
print("palindrome :",test == test[::-1])

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = sum((tuple1, tuple2),())
print("concatenated_tuple: ",tuple3) 