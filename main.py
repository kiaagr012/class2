#create a dictionary
dict = {'color':'red', 'name':'Kian Agrawal', 'age':11}
print(dict)

#accessing values
print(dict['name'])

#get the list of keys and values
print(dict.keys())
print(dict.values())

#create a list
list = ['red','Kian Agrawal',11 ]
print(list)
print(list[2])

# for loop for dict(same for values and keys)
for key in dict.keys():
    print(key,dict[key])

#checking key in dictionary
if "country"in dict:
    print(dict["country"])
else:
    print('Key does not exist')

if "age"in dict:
    print(dict["age"])
else:
    print('Key does not exist')

#appending a new key to dict
dict["country"] = "U.S.A"
print(dict)

#delete a key value
del(dict['country'])
print(dict)

#store a list as a value in dict
dict['marks'] = [10,9,8,7,6,5,4,3,2,1]
print(dict)

#creating a nested dict
classroom ={
    "Kian Agrawal":{
        "age":11,'marks':[2,3,4,5,6,7]
    }, 
    'Max':{'age':20,'marks':[2,3,4,5]}
}

print(classroom.keys())
print(classroom.values())
classroom['Kian Agrawal']['age'] = 12
print(classroom)