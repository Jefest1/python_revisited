names = ['Big fish', 'me', 6,"emmanuel",67,67,67,67,89,"francis"]
just=["come","go","eat",34,45,112,43,45,67,98,90,44,"francis",6,6,6,6]
# creating a loop to iterate over name and it five times
#for name in range(len(names)):
    #print(names[name])
common = []

for i in range(len(names)):
   if names[i] in just:
      common.append(names[i])
print(common) 

