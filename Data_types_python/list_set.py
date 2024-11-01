print("Hello Python")

#list _ collection of ordered and changeable data,
# allows duplicate members. heterogeneous data arranged in 
# sequences. Eeach value of list is called element.
# and its position referred by index. 
# values can be added or deleted by codes. 
# data types of valuse can be list,integer, float, bool,object 


sky_body =["star","sun","Moon","veli"]

print('star'in sky_body) 
# detecting the object star return  True Boolean value
print(sky_body[0])   # indexing return first position
print(sky_body[-1])  # return last position
print(sky_body[-3:-1])  
# return range of items by position before last index
print(sky_body[-2:-1])  # return range of items by position
print(sky_body[0:])  # return range of items by index position

print(sky_body.index("sun"))  # return index number of the item 
print(len(sky_body))  # length of the list

sky_body += ["para veli"] # adding one item at the end of the list
sky_body.append("peruveli")  # adding one more element at the end
print(sky_body)

sky_body.extend(["parambaraveli","paraparaveli"])
print(sky_body)  # adding itmes endof the list 

data =["mani","ram",42,True]
sky_body.extend(data) 
print(sky_body)  # adding items from another list

sky_body.insert(0,"Arul")  # first poition added new item
print(sky_body)

sky_body[2:2] = ["jeeva", "karunya"]  # list added to the list by index 
print(sky_body)

sky_body.remove("karunya") # remove the specific item
print(sky_body)

print(sky_body.pop()) # removing the last index item true

del sky_body[1]  # first index item star removed
print(sky_body)

data.clear()
print(sky_body)  # clear items in list data 

sky_body.remove(42)  # removing last item 42
sky_body.sort(key=str.lower) 
# the uppercase printed first priority to avoid convert lowercase then sort

#sky_body.sort()  # same data types sorted.and
print(sky_body)

nums_1 =[1,2,3,4,5]
nums_1.reverse()  # reverse the items
print(nums_1)
nums_1.remove(2) # remove the specific items
print(nums_1)

nums_1.sort() # sorting returns ascending order
print(nums_1)

sorted(nums_1,reverse=True) # after sorting keeping the original format
print(nums_1)  

copynums_1 = nums_1.copy()
print(copynums_1)

mynums=list(nums_1)
print(mynums)

print(type(nums_1))

# set collection of unordered and uchangeable unindexed,
#  no key values. can be updated by list,tuple
# and dictionary. duplicates not allowed.

num={1,2,3,4}
num_1=set((3,4,6,7))

print(num)
print(num_1)
print(len(num_1))  # find lenght of set
print(type(num))   #find type of set

nums={1,2,2,3,3,3,4,4} # duplicates will not printed in set
print(nums)

# True is duplicate of 1. False is duplicate of 0
# set will print the first number of true /false value

nums_1 = {True,1,2,False, 0,4}
print(nums_1) # duplicate values 0,1 not printed.

num_1.add(10)  # add any value to set
print(num_1)

# add values from another set duplicates eliminated
nums_1.update(num)
print(nums_1)
num={1,2,3,4}
num_1=set((3,4,6,7))

# merge two sets to create new set
mynewset= num.union(num_1)
print(mynewset)

#  intersection update printing duplicates
num.intersection_update(num_1)
print(num)
#  printing symmetric values
num.symmetric_difference_update(num_1)
print(num)




















