lucky_numbers =[0,7,9,3,6,4]
friends = ["Ian","Gift","Ham","Felisha"]

#list functions
friends.extend(lucky_numbers)
friends.append("Husein") #adds an item at the end of the list
friends.insert(1,"Kerry") #insertls the element to the index indicated which in this case is 1
friends.sort() #arranges the list in ascending order
friends.remove("Felisha")
friends.pop()#removes the last element in the list
friends2 =friends.copy()

print(friends2)