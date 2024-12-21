# Flight-Reservation-system
MINI PROJECT 4 - REPORT: AIRLINE RESERVATION SYSTEM
Group 3
Members: Nguyen The An, Tran Anh Chuong, 
Do Thi Hai Binh, Dao Bach Nguyen, Tien Minh Hieu

Program Overview
1.1 Purpose
The program is a simplified airline reservation system that utilizes different concepts of Object-Oriented Programming in Python. It allows users to perform basic operations such as booking seats, canceling reservations, and viewing flight and passenger details.
1.2 Main features
Adding flights with flight number, destination, departure time, and total seats.
Booking and canceling seats on specific flights.
Support VIP reservations.
Displaying flight details including reserved and available seats.
Displaying passenger details on a flight.
Searching flights by destination.
Program Structure
2.1 Classes
2.1.1 Flight:
The class Flight stores details about a flight such as flight ID, destination, departure time, and the number of available seats.
2.1.2 Passenger
The Passenger class represents individual passengers with name, age, and passport number.
2.1.3 Reservation
The Reservation class manages reservations by enabling passengers to book or cancel flight seats, linking them with specific flights. 
2.1.4 AirlineSystem:
The AirlineSystem class is the central hub for managing flights, reservations, and passenger details, combining features from the Flight, Reservation, and Passenger classes into a unified workflow.
2.1.5 VIPPassenger
The VIPPassenger class inherits from Passenger class and adds a special_offers attribute.
2.2 Implemented Functions
2.2.1 Add a Flight
Feature: Add a new flight with details such as flight number, destination, departure time, and total seats.
Implementation:
Instantiate a new Flight instance with a private flight number (__flight_number) and a dictionary tracking seat availability.
The AirlineSystem.addflight() method adds the flight to flight_database, checking for duplicates.
Test case: Input for flight details: 123 Hanoi 12:00 20

2.2.2 Book a Seat (integrate with seat and VIP selection → Bonus)
Feature: Book available seats on a flight and provide VIP options.
Implementation:
The Reservation.bookFlight() method displays available seats, accepts passenger information, and assigns the seat to the passenger.
If a passenger chooses VIP upgrade, a VIPPassenger instance is created with additional special_offers.
The system updates seat availability and stores the reservation.
Test case: when user enters “2” in the main menu to book a seat

2.2.3 Cancel a Flight/ Reservation:
Feature: Cancel reservations by passport number.
Implementation:
The Reservation.cancelFlight() method checks the passenger’s passport number and seat assignment and cancels the seat.
After cancellation, the seat is marked as available, and the reservation is removed from the system.
Test case: when user chooses “3” to cancel a previous reservation

2.2.4 View Flight Details
Feature: Help passengers and administrators quickly check flight information and seat availability.
Implementation: The method AirlineSystem.viewFlightDetails() displays flight ID, destination, departure time, and status of all seats (occupied or available).
2.2.5 View Passenger Details
Feature: Displays all passengers on a specific flight.
Implementation: Check if the flight ID exists in flight_database, then retrieve all Passenger objects in the reservation database and print the formatted output using showAll() method.
2.2.6 Search flight by destination (Bonus)
Feature: Allow searching available flights by destination.
Implementation: The method searchByDestination(destination) checks through the flight database and displays the matched destination search.
2.3 Error handling

The above section is used to handle errors when user types string values and values out of range from 1 to 3. 

OOP Concepts
3.1 Classes and objects
5 classes have been created including Flight, Reservation, Passenger, VIPPassenger, AirlineSystem.
The main program will be run using: main_system = AirlineSystem() 
The Flight object is created when a user wants to add a new flight to the database.
3.2 Inheritance 
The VIPPassenger class inherits from the Passenger class. 
3.3 Encapsulation
Put the passport_num and flight_number as private attributes and require a getter method to access them

3.4 Polymorphism
The showAll() method in the VIPPassenger class overrides the showAll() method in the Passenger class where it will show the offer of the VIP passenger along with name and age. 
Challenges
During the development process, we faced several problems:
4.1 Database management 
We didn’t know where to put the flight database (which is a dictionary) in the program. At first, we all agreed that it should be located in the Flight class but then we realized that putting the database in the Flight class would result in conflicts and inconsistency after multiple manipulations such as booking or canceling reservations/seats. 
4.2 Building the overall logic of the whole program
We struggled to determine the mechanism of the program to work smoothly as required in the task. From figuring out a solution to keep user input as consistent as possible in the main menu, the conditions in methods of different classes, etc.
