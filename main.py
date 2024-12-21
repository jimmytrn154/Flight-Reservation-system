
class Flight:

    def __init__(self, flight_number, destination, departure_time, available_seats):
        self.__flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.available_seats = {x: False for x in range(1, available_seats+1)} #Initially the available seat after creating a flight is 100% and the they're set to False for each seat available
    
    #Assume flight number is secured
    def getFlightNum(self):
        return self.__flight_number #--> Encapsulation with private attributes and getter method

class Reservation:
    '''
    Manage reservation (Book and cancel), linking passengers with specific flights
    '''

    def __init__(self):
        self.reservation = {} #Main database to store users in corresponding flight
    
    def bookFlight(self, flight):
        flight_id = flight["ID"]
        if flight_id not in self.reservation:
            self.reservation[flight_id] = {} #Create a new user database for a flight
        
        #Show available seats on the flight
        available_seats = [str(seat) for seat in flight["Total seats"] if not flight["Total seats"][seat]]
        print(f"These are available seats for the flight {flight_id}: {', '.join(available_seats)}")
        
        seatNum = int(input("Enter your targeted seat number: "))

        if str(seatNum) in available_seats:
            flight["Total seats"][seatNum] = True #Seat selection
            user_prompt = list(map(str, input("Enter you information including name, age and passport number in order: ").split()))

            vipChecker = input("Would you like to upgrade your ticket to VIP? type yes or no: ")
            if vipChecker.lower() == "yes":
                print("Here are the offers for VIP ticket, choose one by typing the number represent each:\n 1. Buffet\n 2. Drinks on plane\n 3. Exclusive teddy bears")
                try:
                    vipOffer = int(input("Enter your choice: "))
                    if vipOffer == 1:
                        choice = "Buffet"
                    elif vipOffer == 2:
                        choice = "Drinks on plane"
                    elif vipOffer == 3:
                        choice = "Teddy bears"
                except ValueError:
                    raise f"Invalid value chosen, retry"
                passenger = VIPPassenger(
                    user_prompt[0],
                    user_prompt[1],
                    user_prompt[2],
                    choice
                )
                self.reservation[flight['ID']][seatNum] = passenger #Store passenger/user information in the reservation database as a dictionary with the format {seat_number -> string: user object}
                print(f"Seat number {seatNum} on the flight {flight['ID']} is booked successfully!")
                print("Current seats:", flight["Total seats"])
            elif vipChecker.lower() == "no":
                passenger = Passenger(
                    user_prompt[0],
                    user_prompt[1],
                    user_prompt[2],
                )
                self.reservation[flight['ID']][seatNum] = passenger #Store passenger/user information in the reservation database as a dictionary with the format {seat_number -> string: user object}
                print(f"Seat number {seatNum} on the flight {flight['ID']} is booked successfully!")
                print("Current seats:", flight["Total seats"])
            else:
                flight["Total seats"][seatNum] = False #Handle invalid error
                print("Invalid value, retry to book ticket.")
            
        else:
            print(f"Seat number {seatNum} is booked. Seek for another one please.")
    
    def cancelFlight(self, passport_num, flight): #User can only cancel their booking by asking passport number at first 
        flight_id = flight["ID"]
        for booked_seat in self.reservation[flight_id]: 
            print(f"Checking seat {booked_seat}, Passenger Passport: {self.reservation[flight_id][booked_seat].getPassportNum()}")
            if passport_num == self.reservation[flight_id][booked_seat].getPassportNum():
                verification = input((f"You have booked the seat {booked_seat}. You will cancel this seat soon. Are you sure you want to cancel? "))
                if verification.lower() == "yes":
                    flight["Total seats"][booked_seat] = False
                    self.reservation[flight_id].pop(booked_seat)
                    print(f'You have successfully canceled the seat {booked_seat} on the flight {flight_id}')
                    break
                else: #No or any other option
                    print("Choose another option in the menu please.")
                    break
        else:
            print("You have not reserved a seat on this flight.")

class Passenger:
    def __init__(self, name, age, passport_num): #The passport_num parameter is consider unique among passengers
        self.name = name
        self.age = age
        self.__passport_num = passport_num
    
    def getPassportNum(self):
        return self.__passport_num
    
    def showAll(self):
        return f"Name: {self.name}\n Age: {self.age}\n"

class VIPPassenger(Passenger): #Simple inheritance from Passenger class
    def __init__(self, name, age, passport_num, special_offers):
        super().__init__(name, age, passport_num)
        self.special_offers = special_offers
    def showAll(self): #Method overriding of Passenger class
        inherit = super().showAll()
        return f"{inherit} Offer: {self.special_offers}"

#Bach Nguyen
class AirlineSystem:
    def __init__(self):
        self.flight_database = {} #Main database to store flights
        self.reservationManager = Reservation() #Instancing/ Initializing Reservation class
    
    def addflight(self, flight):
        if flight.getFlightNum() in self.flight_database:
            print(f"The flight {flight.getFlightNum()} already exist. Choose another num/flight ID please.")
        else:
            self.flight_database[flight.getFlightNum()] = {
                "ID": flight.getFlightNum(),
                "Destination": flight.destination,
                "Departure time": flight.departure_time,
                "Total seats": flight.available_seats
            }
            print(f"The flight {flight.getFlightNum()} has been created.")
    
    def book_seat(self, flight_num):
        if flight_num in self.flight_database:
            self.reservationManager.bookFlight(self.flight_database[flight_num])
        else:
            print(f"Flight {flight_num} does not exist.")

    #Search flights based on destinations
    def searchByDestination(self, destination):
        flightByDes = [self.flight_database[num]["ID"] for num in self.flight_database if self.flight_database[num]["Destination"] == destination]
        if flightByDes: #If the list is not empty
            print(f"These are the flight to {destination}: ")
            for singleFlight in flightByDes:
                print(singleFlight)
        else:
            print(f"There is no flight to {destination} in current schedule.")

    #Invoke cancelFlight method from Reservation class
    def cancel_seat(self, passport_num, flight_num):
        if flight_num in self.flight_database:
            self.reservationManager.cancelFlight(passport_num, self.flight_database[flight_num])
        else:
            print(f"Flight {flight_num} does not exist.")
    
    def viewFlightDetails(self, flight_num):
        if flight_num not in self.flight_database:
            print(f"Flight {flight_num} does not exist.")
        else:
            print(f'''
                    Flight: {flight_num},\n
                    Destination: {self.flight_database[flight_num]["Destination"]},\n
                    Departure time: {self.flight_database[flight_num]["Departure time"]},\n 
                    Total seats: {len([count_total for count_total in range(len(self.flight_database[flight_num]["Total seats"]))])},\n
                    Available seats: {len([count_available for count_available in self.flight_database[flight_num]["Total seats"] if not self.flight_database[flight_num]["Total seats"][count_available]])}
                    ''')
    
    def viewPassengerDetails(self, flight_num):
        if flight_num not in self.flight_database:
            print(f"Flight {flight_num} does not exist.")
        else:
          for seat in self.reservationManager.reservation[flight_num]:
            # print(f'Name: {self.reservationManager.reservation[flight_num][seat].name}\n Age: {self.reservationManager.reservation[flight_num][seat].age}')
            print(f"{self.reservationManager.reservation[flight_num][seat].showAll()}")

menu_content = ["Welcome to VinUni airline! Choose your service:", "1. Add Flight", "2. Book a seat", "3. Cancel reservation", "4. View details", "5. Search flight by destination"]

main_system = AirlineSystem() #Invoke the main class to operate the programme

while True: #Loop for the user interface to run continuously after choices making
    print()
    for i in menu_content: #Display the menu content
        print(i)
    
    print("Type exit or quit to exit the app.")

    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        add_a_flight = list(map(str, input("Enter your flight number, destination, departure time and total seats in order and seperated by single spaces: ").split()))
        newSingleFlight = Flight(
            add_a_flight[0],
            add_a_flight[1],
            add_a_flight[2],
            int(add_a_flight[3])
        )
        main_system.addflight(newSingleFlight)
        # print(main_system.flight_database)

    elif user_input == "2": #If user want to book a seat
        
        checkForFlight = input("Enter your flight number: ")
        # free_seat = []
        main_system.book_seat(checkForFlight)
        print(main_system.reservationManager.reservation)
    
    elif user_input == "3":
        checkForUser = input("Enter your passport number that you used to book the flight: ")
        checkForFlight1 = input("Enter your flight ID: ")    
        main_system.cancel_seat(checkForUser, checkForFlight1)
        print(main_system.reservationManager.reservation)
        
    elif user_input == "4": #If user want to use view functionality
        flight_num = input("Enter you flight number: ")
        print("Enter your choice to view:\n 1. Flight\n 2. Passenger\n")
        typeOfView = input("Enter your choice of view: ")
        if typeOfView.lower() == "flight":
            main_system.viewFlightDetails(flight_num)
        elif typeOfView.lower() == "passenger":
            main_system.viewPassengerDetails(flight_num)
        else:
            print("Invalid value. Retry to enter your choice please.")

    elif user_input == "5":
        destination_inp = input("Enter your destination\n (Capitalize first letter, example: Hanoi, Tokyo, etc): ")
        main_system.searchByDestination(destination_inp)

    elif user_input.lower() == "quit" or user_input.lower() == "exit":
        print("See you later!")
        break

    else:
        print("Invalid choice, retry please.")
        