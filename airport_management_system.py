print('Hello, Welcome to Alpha Airport ')

print('Select your work as per the given system')
print("Functions\t\t\tCode\nAdd Flight\t\t\t1\n"\
    "View Flights\t\t\t2\n"\
        "Book Ticket\t\t\t3\n"\
            "View Bookings\t\t\t4")

flights = {}
booked_tickets={}
passenger_details={}
def add_flight():
    print("Add flight details")
    f_id = input('Flight Id: ')
    f_name = input('Flight name: ')
    f_source=input('Flight Source: ')
    f_destination=input('Flight Destination: ')
    f_seat=input('Flight Total Seat: ')
    f_price=input("Flight Ticket Price: ")
    # You can add more details like destination, seats, etc.
    flight_dict = { 
        "Name":f_name, 
        "Source":f_source, 
        "Destination":f_destination, 
        "Seat":f_seat,
        "Ticket Price":f_price}
    
    flights[f_id]=flight_dict
    print("                           ")
    print("Flight added successfully!")
    print("Current Flights:")
    for flight_ID, details in flights.items():
       print("--------------\n")
       print("Flight Id:",flight_ID)
       print("Flight Name:",details["Name"])
       print("Flight Source:",details["Source"])
       print("Flight Destination:",details["Destination"])
       print("Flight Total Seat:",details["Seat"])
       print("Flight Ticket Price:",details["Ticket Price"])
       print("--------------")
    
    return flights


def view_flights():
    if not flights:
        print("No flights available.")
    else:
        for flight_ID, details in flights.items():
            print("--------------\n")
            print("Flight Id:",flight_ID)
            print("Flight Name:",details["Name"])
            print("Flight Source:",details["Source"])
            print("Flight Destination:",details["Destination"])
            print("Flight Total Seat:",details["Seat"])
            print("Flight Ticket Price:",details["Ticket Price"])
            print("--------------")


def book_ticket():
    ticket_booking_client_name=input("Enter your name:")
    ticket_booking_client_ph_no=input("Enter Your mobile Number:")
    client_id='alphaair'+ticket_booking_client_name[:5]+ticket_booking_client_ph_no[-4:]
    no_of_tickets = int(input('Enter number of tickets: '))
    no_of_adults=int(input("Enter number of Adults: "))
    no_of_child=int(input("Enter Number of child:"))
    passenger_ticket_price=input("Pay the price of the ticket: ")
    flight_book_id=input("Select Flight id:  ")
    
    passenger_details_list=[]
    for i in range(1,no_of_tickets+1):
        passenger_name=input('Passenger Name: ')
        passenger_age=input('Passenger Age: ')
        passenger_gender=input('Enter Gender: ')
        passenger_details_list.append({"Passenger Name:":passenger_name,\
            "Passenger Age:":passenger_age,\
                "Passenger Gender:":passenger_gender})
        
        
    passenger_details[client_id]=passenger_details_list
    
    found=False
    print(flight_book_id)
    print(ticket_booking_client_name)
    print(ticket_booking_client_ph_no)
    print(client_id)
    print(no_of_tickets)
    print(no_of_adults)
    print(no_of_child)
    

    if no_of_tickets==no_of_child+no_of_adults:
        print("Kindly Proceede for Payment System")
            
    else:
        print("Invalid Passenger Details, Please Re-Enter Passenger details")
    for Flight_ID,details in flights.items():
        if flight_book_id == Flight_ID:
            available_seat=int(details["Seat"])
            if no_of_tickets<=available_seat:
                details["Seat"]=str(available_seat-no_of_tickets)
                ticket_payable_amount=int(details["Ticket Price"])*no_of_tickets
                print("Kindly Pay Rs",ticket_payable_amount+'/-')
                print(passenger_ticket_price)
                if passenger_ticket_price==str(int(details["Ticket Price"])*no_of_tickets):
                    print("----------------------------------------------")
                    print('Your ticket is booked for Flight',Flight_ID,\
                        '\nClient ID:\t\t\t',client_id,\
                        '\nClient Name:\t\t\t',ticket_booking_client_name,\
                            '\nClinet Phone Number\t\t\t',ticket_booking_client_ph_no,\
                                "\nFlight ID:\t\t\t",Flight_ID,\
                                    "\nFlight Ticket Payment Status","Rs",str(int(details["Ticket Price"])*no_of_tickets),"PAID",\
                                    "\nNumber of Tickets:",no_of_tickets,\
                                    "\Passenger Details:",passenger_details,\
                                    "\nAdults:",no_of_adults,\
                                    "\nChild:",no_of_child,\
                                    "\n Passenger Details",passenger_details_list,\
                                    "---------------------------")
                    booked_tickets_dict={
                            "Client ID":client_id,
                            "Client Name":ticket_booking_client_name,
                            "Client Contact":ticket_booking_client_ph_no,
                            "Boarding Passenger Details":passenger_details, 
                            "Source":details["Source"], 
                            "Destination":details["Destination"], 
                            "Seats":str(no_of_tickets),
                            "Passenger Details:":passenger_details_list}
                    if Flight_ID in booked_tickets:
                        booked_tickets[Flight_ID].append(booked_tickets_dict)
                    else:
                        booked_tickets[Flight_ID]=booked_tickets_dict
                else:
                    print("Kindly pay the required amount of the ticket")
            else:
                print("Not enough seat available")
            found=True
            break
           
    if not found:
        print('Invalid Flight Id, Please try again ')


def view_bookings():
    if not booked_tickets:
        print("No Flights Tickets Booked Yet.")
    else:
        for booked_ticket_id, details in booked_tickets.items():
            print("--------------\n")
            print("Flight Id:",booked_ticket_id)
            print("Flight Name:",details["Name"])
            print("Flight Source:",details["Source"])
            print("Flight Destination:",details["Destination"])
            print("Flight Seat Booked:",details["Seats"])
            print("Passenger Name:",details["Passenger Name"])
            print("Passenger Phone Number:",details["Passenger Phone Number"])
            print("--------------")
            
            
while True:
    operation=int(input("What you want to do: "))
    print(operation)
    
    if operation == 1:
        add_flight()
    
    
    elif operation == 2:
        view_flights()
    
    elif operation == 3:
        book_ticket()
            
    elif operation == 4:
        view_bookings()

    else: 
        print('Invalid Code, please try again')



            


    