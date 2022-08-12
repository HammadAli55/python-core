for item in ['Hammad', 'Ali', 'Shah']:
    print(item)

for items in range(4,7):
    print(items)

# move two steps forward
for items in range(4, 10, 2):
    print("move forward", items)


total = 0
prices = [10, 20, 30]
for price in prices:
    total += price
print(total)


# first inner loop completes with x = 0 and y = 2, then go to outerloop and the value of x get incremented 
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5,2,5,2,2]
for number in numbers:
    print(number * '*')

numbers = [1, 2, 2, 4, 5, 6, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

