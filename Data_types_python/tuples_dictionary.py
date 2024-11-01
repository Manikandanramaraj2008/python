# tuple collection of ordered and changeable data 
# allows duplicate members. single value inside 
# the variable # different data types , cannot add or remove 
# values after creation. it is immutable.

mytuple =tuple((2,4,6,8,True,"Hi"))
print(mytuple)

mytuple_1= (3,6,True,"bye")
print(type(mytuple_1))

# adding new values to tuple. convert the tuples to 
# list then add the value, later pass 
# the list in to tuple

new_list = list(mytuple)
new_list.append("krm")
new_tuple =tuple(new_list)
print(new_tuple)

(one,*two,Hi) = mytuple_1
print(one)  # return first element
print(two) # return the list of elements
print(Hi) # return last element

print(mytuple_1.count(6))

# Dictionaries_  collection ordered data, changeable,
# no duplicates # Key value pairs object / dictionaries

car = dict(car="tesla", year ="2011")
car_1 ={"car": "Nissan","year": "2011"}

print(car)
print(car_1)
print(type(car_1))
print(len(car))

#Access items
print(car.get("year"))
print(car_1["car"])

print(car.keys())  # list all keys
print(car.values()) # list all values
print(car_1.items())  # list of key values as tuples
# verify the key exists
print("model" in car)
print("year"in car_1 )
# change values
car.update({"price":"2L" })
print(car)
car["year"] = 2011
print(car)

print(car.pop("year")) # removing the item
print(car.popitem()) # returning the last item as tuple

del car["car"]  # delete particular item
print(car)

car_1.clear() # make empty
print(car_1)

# BAD COPY
car=dict(model = "2011", price="3L",make ="Nissan")
# car_1 = car
# print(car_1)
# print(car)

# car_1["EV"]= "No" 
# # bad caopy value added to variable car which was copied
# print(car)

car_1 =car.copy()
car_1["EV"]="yes"  # copy method of dictionaries
print(car_1)
print(car) #  good copy the value added only copied item
             # not to the initial variable car.

car_3 =dict(car) # good copy method of dictionaries
print(car_3)

# NESTED DICIONARIES

sabai_1 ={"vadalur": "sabai",
"mettukuppam": "sidhivalkam"}
sabai_2 ={"vadalur": "salai",
"mettukuppam": "dheenjuvai"}

# combining two dictionaries

vallalar ={"sabai_1": sabai_1,
"sabai_2": sabai_2}
print(vallalar)

# accessing the vaues

print(vallalar["sabai_1"]['vadalur'])
















