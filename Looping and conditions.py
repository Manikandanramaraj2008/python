# looping
# while loop
i = 1
while i<6 :
       print(i)
       i+= 2 
# adding  2 to 1 meeting condition
# #printing 3.  again adding 2 printing 5
# again adding 2 becoming 7 not meeting the 
# conditions so that printing stopped after 5
print(" ")  # for output space

i=1
while i<10:
       i+=1 
       if i==8:
         break  # after 8 the loop break 
           # print up to 8
       print(i)
print(" ")

i=1
while i<10:
       i+=1
       if i==8: # continueing the loop
         continue
       print(i)

i=1
while i<10:
       i+=1
       if i==8: # continueing the loop
         continue
       print(i)
else:
       print("i is notlonger less than 10")

# for loop

fruits =["apple","orange","grapes"]
for x in fruits:
  print(x) 
for x in "share":
       print(x)
print(" ")

# breaking the loop

fruits =["apple","orange","grapes"]
for x in fruits:
  if x =="orange":
       break
  print(x) 
for x in "share":
       print(x)
print(" ")

# continuing the loop by if condition

fruits =["apple","orange","grapes"]
for x in fruits:
  if x =="orange":
       continue
  print(x) 
for x in "share":
       print(x)
# range in loops
for x in range(10): # print from 0 to 9
       print(x)
for x in range (4,9): # print upto 8 starts from 4
       print(x)
for x in range(10,51,5): # print up to 50 jumped by 5
       print(x)
else:
       print(" Great it is over")

#nested loops
names =["vallalr","ramalingam","chidambaram"]
actions =["sabai","salai","siddhi"]
for name in names:
      # print(name)
      for action in actions:
       print(name +(" ")+ action + ",")
print(" ")
#nested loops_2
names =["vallalr","ramalingam","chidambaram"]
actions =["sabai","salai","siddhi"]
for action in actions:
      # print(name)
      for name in names:
       print(name +(" ")+ action + ",")


















         



