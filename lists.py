###### Replace ######
names = ["John", "David"]
names[0] = "Joy"
print ("replace index 0 - John with Joy", names)

###### find max number in list ######
numbers = [1, 2, 3, 6, 8, 10]
print("maximum value: ", max(numbers))

###### append ######
numbers = [1, 2, 3, 4]
numbers.append(20)
print("Append -> 20: ", numbers)

###### inset ######
b = [1, 2, 3, 4]
b.insert(0, 5)
print("insert 5 at zero index: ", b)

###### pop ######
c = [1, 2, 3, 4, 5, 6]
c.pop()
print("pop: ", c)

###### del ######
d = [1, 2, 3, 4, 5, 6]
del d[0]
print("delete 0 index: ", d)

###### check Index number ######
d = [1, 2, 3, 4, 5]
print("index: ", d.index(1))
# or
print("if object exists: ", 1 in d)

###### count ######
e = [10, 2, 3, 4, 5, 10]
print("count: ", e.count(10))

###### sort ######
f = [5, 2, 3, 4, 7]
f.sort()
print("sort", f)

###### reverse ######
f = [5, 2, 3, 4, 7]
f.reverse()
print("reverse: ", f)

###### copy ######
list_1 = [5, 2, 3, 4, 7]
list_2 = list_1.copy()
list_1.append(22)
print("append", list_1)
print("copy: ", list_2)

###### extend ######
# create a list
prime_numbers = [2, 3, 5]
# create another list
numbers = [1, 4]
# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)
print('List after extend():', numbers)

###### remove ######
# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]
# remove 9 from the list
prime_numbers.remove(9)
# Updated prime_numbers List
print('remove 9 from list: ', prime_numbers)