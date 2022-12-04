

class Car:
    def __init__(self, license, modal, color):
        self.license = license
        self.modal = modal
        self.color = color

    def __repr__(self) -> str:
        return f"{self.license} {self.modal} {self.color}"


class Garage:
    def __init__(self) -> None:
        self.car_add = []
        self.sport = 10
        self.car_info = {"Tickets": [],
                         "License": [], 'Model': [], 'Color': []}
        self.bill = 0
        self.ticket = []

    def sport_available(self):
        return f"Total Spot Available {self.sport}"

    def add_car_to_garage(self, car):

        self.sport_name = ['A1', 'B1', 'C1', 'D1',
                           'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
        if self.sport > 0:
            user_date = str(car).split(" ")

            self.sport -= 1
            self.car_add.append(user_date)
            # self.car_info = {"Tickets": [],
            #                  "License": [], 'Model': [], 'Color': []}
            ticket = ""

            for i, val in enumerate(self.car_add):
                ticket = self.sport_name[i] + user_date[0]

            self.car_info['Tickets'].append(ticket)
            self.car_info['License'].append(val[0])
            self.car_info['Model'].append(val[1])
            self.car_info['Color'].append(val[2])
            print(f"successfully Park your ticket {ticket}")
        else:
            print("NO SPOTS AVAILABLE")

    def unPark(self, ticket, hours):
        past_spot_len = len(self.car_info['Tickets'])

        if ticket not in self.car_info['Tickets']:
            print("NO CAR FOUND!!")
        else:
            for i, val in enumerate(self.car_info['Tickets']):
                if val == ticket:
                    print(f"Your License Is {self.car_info['License'][i]}")
                    print(f"Your Model Is {self.car_info['Model'][i]}")
                    print(f"Your Color Is {self.car_info['Color'][i]}")

                    # self.car_add.pop(i)
                    remove_car = i

                    self.car_info["License"].pop(i)
                    self.car_info["Model"].pop(i)
                    self.car_info["Color"].pop(i)
                    self.car_info["Tickets"].pop(i)
                    self.sport += 1
        if hours > 30:
            print(f"Total Bil = ${hours*5 + 100} ")
        else:
            print(f"Total Bil = ${hours*5} ")
        print()

    def total_Car_n_garage(self):
        for i in self.car_info.items():
            print(i)


# my_garage = Garage()
# user_car_1 = Car('1234mn', 'Ferrari', 'Red')
# user_car_2 = Car('56EB', 'Toyota', 'green')
# user_car_3 = Car('70KH', 'marute', 'blue')
# my_garage.add_car_to_garage(user_car_1)
# my_garage.add_car_to_garage(user_car_2)
# my_garage.add_car_to_garage(user_car_3)

# my_garage.unPark("A11234mn", 10)
# my_garage.unPark("B156EB", 20)
# print(my_garage.car_add)

# my_garage.total_Car_n_garage()
# my_garage.unPark("A11234mn", 10)
# my_garage.total_Car_n_garage()


my_garage = Garage()
print("*******************WELCOME TO OUR PARKING SYSTEM****************")

while True:
    print("What do you want? ")
    print("1. Park Your Car")
    print("2. Check Available Space")
    print("3. Remove un park Your Car")
    print("4. Total Car in Garage")
    user_choice = (int(input("Enter Your Choice: ")))
    if user_choice == 1:
        car_license = input("Enter your car License: ")
        car_model = input("Enter your car model: ")
        car_color = input("Enter your car color: ")
        user_car = Car(car_license, car_model, car_color)
        my_garage.add_car_to_garage(user_car)

    elif user_choice == 2:
        print(my_garage.sport_available())
    elif user_choice == 3:
        ticket = input("Enter your Ticket Number: ")
        hours = int(input("Enter Hours: "))
        print()
        my_garage.unPark(ticket, hours)
    else:
        break
    print()
