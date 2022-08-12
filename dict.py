customer = {
    "name": "Hammad Ali",
    "age": "25",
    "Married": False,
    "Company": "TRA"
}

print(customer["name"])

#sort on the basis of dict
this_dict = {
        '1': 'Class A',
        '2': 'Class B',
        '5': 'Class C',
        '4': 'Travel Trailer',
        '8': '5th Wheel'
    }

print('sort on the basis of dict:')
for key in sorted(this_dict):
    print (key, this_dict[key])


# match key with value
this_dict = {
        'classA': 'Class A',
        'classB': 'Class B',
        'classC': 'Class C',
        'travel_trailer': 'Travel Trailer',
        'fifth_wheel': '5th Wheel',
        'truck_camper': 'Truck Camper',
        'tent_camper': 'Tent Camper',
        'popup_trailer': 'Pop Up'
    }

selected_class = 'classB'

print('match key with value: ')
for key, value in this_dict.items():
    if selected_class == key:
        print(value)


#Convert List items as keys in dictionary with enumerated value
listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr) ) }



#Get values
values = customer.values()
list_customer = list(values)
print("customer_info", list_customer)

# will return None object that represent the absence of a value
print(customer.get("Name", '')) 


# digit mapping
# phone = input("Phone:")

phone = "2121212a"
diggit_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three"
}
output= ""
for d in phone:
    output += diggit_mapping.get(d, "!") + " "

print(output)
