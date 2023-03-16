# Define the username and password
username = 'Deema'
password = '1234'

# Define the items dictionary
items = {
    'chocolate': [
        {'name': 'Kitkat', 'quantity': 9},
        {'name': 'Galaxy', 'quantity': 5},
        {'name': 'Cadbury', 'quantity': 3},
    ],
    'chips': [
        {'name': 'Lays', 'quantity': 7},
        {'name': 'Doritos', 'quantity': 4},
        {'name': 'Pringles', 'quantity': 6},
    ],
    'drinks': [
        {'name': 'Pepsi', 'quantity': 2},
        {'name': 'Coca-Cola', 'quantity': 4},
        {'name': 'Sprite', 'quantity': 3},
    ]
}

# Define a function to show all items
def show_items():
    print('Items:')
    print('{:<15} {:<15} {:<15}'.format('Type', 'Name', 'Quantity'))
    for item_type, item_list in items.items():
        for item in item_list:
            print('{:<15} {:<15} {:<15}'.format(item_type, item['name'], item['quantity']))

# Define a function to edit an item
def edit_item():
    name = input('Enter the name of the item you want to edit: ')
    for item_type, item_list in items.items():
        for item in item_list:
            if item['name'] == name:
                print('1. Edit name')
                print('2. Edit type')
                print('3. Edit quantity')
                choice = int(input('Please select an option: '))
                if choice == 1:
                    new_name = input('Enter the new name: ')
                    item['name'] = new_name
                elif choice == 2:
                    new_type = input('Enter the new type: ')
                    items[new_type].append(item)
                    item_list.remove(item)
                elif choice == 3:
                    new_quantity = int(input('Enter the new quantity: '))
                    item['quantity'] = new_quantity
                print('Item edited successfully!')
                return
    print('Item not found!')

# Define a function to delete an item
def delete_item():
    name = input('Enter the name of the item you want to delete: ')
    for item_type, item_list in items.items():
        for item in item_list:
            if item['name'] == name:
                item_list.remove(item)
                print('Item deleted successfully!')
                return
    print('Item not found!')

# Ask the user for the username and password
while True:
    user = input('Enter your username: ')
    pwd = input('Enter your password: ')
    if user == username and pwd == password:
        print('Welcome to the store!')
        break
    else:
        print('Invalid username or password, please try again.')

# Show the options to the user
while True:
    print('')
    print('1. Show all items')
    print('2. Edit an item')
    print('3. Delete an item')
    print('4. Exit')
    choice = int(input('Please select an option: '))
    if choice == 1:
        show_items()
    elif choice == 2:
        edit_item()
    elif choice == 3:
        delete_item()
    elif choice == 4:
        print('Thank you for shopping with us!')
        break
    else:
        print('Invalid choice, please try again.')

print('----Thanks for using our store!----')