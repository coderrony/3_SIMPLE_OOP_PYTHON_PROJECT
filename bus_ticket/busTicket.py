

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]


class PhitronCompany:
    total_bus = 5
    total_bus_lst = []  # dummy database

    def install(self):
        bus_no = int(input("Enter the bus no: "))
        flag = 1
        for bus in self.total_bus_lst:  # checking bus already install
            if bus['coach'] == bus_no:
                print("Bus already install")
                flag = 0
                break
        if flag:
            bus_driver = input("Enter bus driver Name: ")
            bus_arrival = input("Enter bus Arrival time: ")
            bus_departure = input("Enter Bus Departure Time: ")
            bus_from = input("Enter bus start from: ")
            bus_to = input("Enter bus Destination: ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival,
                               bus_departure, bus_from, bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print("\n Bus install Successfully\n")


class BusCounter(PhitronCompany):
    user_lst = []  # user database
    bus_seat = 20

    def reservation(self):

        bus_no = int(input("Enter bus number: "))
        flag = 1
        for bus in self.total_bus_lst:
            if bus['coach'] == bus_no:
                flag = 0
                passenger = input("Enter your name: ")
                seat_no = int(input("Enter Your Seat Number: "))
                if seat_no-1 > self.bus_seat:
                    print("Only 20 seat available")
                elif bus['seat'][seat_no-1] != 'Empty':
                    print("Seat already Booked")
                else:
                    bus["seat"][seat_no-1] = passenger

        if flag == 0:
            print("no bus available")

    def showBusInfo(self):

        bus_no = int(input("Enter Bus No: "))
        for bus in self.total_bus_lst:
            if bus['coach'] == bus_no:
                print("*"*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no}      \t Driver: {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']}\t\t Departure : {bus['departure']}")
                print(f"From: {bus['from_des']} \t\t To: {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                        print("\t", end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()

    def get_users(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter your name: ")

        flag = 0
        for user in self.user_lst:
            if user.username == name:
                flag = 1
                print("Username already exits")
                break

        if flag == 0:
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Account Create successfully")

    def available_bus(self):
        if len(self.total_bus_lst) == 0:
            print("No Bus Available")
        else:
            for bus in self.total_bus_lst:
                print("*"*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(
                    f"Bus Number : {bus['coach']}      \t Driver: {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']}\t\t Departure : {bus['departure']}")
                print(f"From: {bus['from_des']} \t\t To: {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                        print("\t", end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()


while True:
    counter = BusCounter()
    print("1.create an account")
    print("2.Login To your Account")
    print("3. Exit")
    user_input = int(input("Enter your choice: "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter you name: ")
        password = input("Enter your password: ")
        isAdmin = False
        flag = 0
        if name == 'admin' and password == '123':
            isAdmin = True
        if isAdmin == False:
            for user in counter.get_users():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(
                        "1. Available Buses \n2. Show Bus info\n3. Reservation \n4. Exit")
                    a = int(input("Enter our choice: "))
                    if a == 4:
                        break
                    elif a == 1:
                        counter.available_bus()
                    elif a == 2:
                        counter.showBusInfo()
                    elif a == 3:
                        counter.reservation()
            else:
                print("Unavailable to log in")
        else:
            while True:
                print("Hello Admin, welcome back")
                print(
                    f"1. install bus \n2. Available Buses \n3. Show Bus \n4. Show User list \n5. Exit")
                a = int(input("Enter you choice: "))
                if a == 5:
                    break
                elif a == 1:
                    counter.install()
                elif a == 2:
                    counter.available_bus()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    print(counter.get_users())
