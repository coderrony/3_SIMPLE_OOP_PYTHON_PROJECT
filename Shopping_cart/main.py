
# Shopping Cart Design

class User:
    user_list = []

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class Item:
    def __init__(self, itemID, price, description, quantity) -> None:
        self.itemID = itemID
        self.price = price
        self.description = description
        self.quantity = quantity


class ShoppingBasket:
    user_lst = []
    user_order_data = {}  # {"username": [{1,2,3},{6,5,7}]}
    itemsDB = []  # [{1,3,4,5},{6,'rony',3,55}]

    def get_usersLst(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter you username: ")

        isNameExit = False
        for user in self.user_lst:
            if user['username'] == name:
                print("you have already Exits")
                isNameExit = True
                break
        if isNameExit == False:
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Account create successfully")

    def addItemToDataBase(self):
        itemID = input("enter itemId: ")
        description = input("enter description: ")
        price = float(input("enter item price: "))
        quantity = int(input("enter quantity: "))
        self.new_item = Item(itemID, price, description, quantity)
        self.itemsDB.append(vars(self.new_item))

    def addItemToCart(self, username):

        itemId = input("enter item id: ")
        quantity = int(input("enter item quantity: "))
        flag = 0
        for i in self.itemsDB:
            if i['itemID'] == itemId and i['quantity'] > quantity:
                print("Items available")
                flag = 1
                break
        if not flag:
            print("Items not available")
        else:
            if username in self.user_order_data.keys():
                self.user_order_data[username].append(
                    {"itemID": itemId, "quantity": quantity})
            else:
                self.user_order_data[username] = [
                    {'itemID': itemId, 'quantity': quantity}]

    def updateProductCart(self, username):

        itemId = input('enter item id: ')
        quantity = int(input("enter update quantity number: "))
        for i in self.user_order_data[username]:
            if i['itemID'] == itemId:
                print(i['quantity'])
                if quantity > i['quantity']:
                    i['quantity'] = quantity
                else:
                    print("quantity out of stack")
                    break

    def deleteItemProduct(self, username, itemId):
        flag = 0
        for i in self.itemsDB:
            if i['itemID'] == itemId:
                flag = 1
                break
        if flag:
            for i in self.user_order_data[username]:
                if i['itemID'] == itemId:
                    self.user_order_data[username].remove(i)

    def showData(self):
        print(self.itemsDB)
        print(self.user_order_data)
        print(self.user_lst)


basket = ShoppingBasket()
basket.addItemToDataBase()
basket.addItemToDataBase()
basket.showData()
while True:
    print("1. create account\n2. Login to your account\n3. Exit")
    user_choice = int(input("enter you choice : "))
    if user_choice == 3:
        break
    elif user_choice == 1:
        basket.create_account()
    elif user_choice == 2:
        isNameExits = False
        name = input("enter you username: ")
        password = input('enter your password: ')
        for user in basket.user_lst:
            if user['username'] == name and user['password'] == password:
                isNameExits = True

        if isNameExits:
            while True:
                print(
                    "1. add to you cart\n2. update you cart\n3. delete cart\n4. show you cart\n5. exit")
                choice = int(input("enter you choice: "))
                if choice == 1:
                    basket.addItemToCart(name)
                elif choice == 2:
                    basket.updateProductCart(name)
                elif choice == 3:
                    itemId = input("enter item id: ")
                    basket.deleteItemProduct(name, itemId)
                elif choice == 4:
                    basket.showData()
                else:
                    break
        else:
            print("invalid user")
