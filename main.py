from typing import Union, Optional

from fastapi import FastAPI

class AirportSystem:
    __admin_list = []
    __reservation_list = []	
    __flight_list = []
    __flight_instance_list = []
    __service_list = []
    __aircraft_list = []

    def reservation_list():
        return AirportSystem.__reservation_list

    def check_in(booking_reference, lastname):
        return AirportSystem.create_boarding_pass(AirportSystem.check_reservation(booking_reference), AirportSystem.check_passenger(booking_reference, lastname))
    
    def create_reservation(reservation):
        return AirportSystem.__reservation_list.append(reservation)
    
    def check_reservation(booking_reference):
        for i in AirportSystem.__reservation_list:
            if i.booking_reference == booking_reference:
                return i
            
    def check_passenger(booking_reference, lastname):
        for i in AirportSystem.check_reservation(booking_reference).passengers:
            if i.lastname == lastname:
                return i

    def create_boarding_pass(reservation, passenger, returnl = False):
        reservation.boarding_pass = BoardingPass(reservation, passenger, returnl)
        return BoardingPass(reservation, passenger)
    
    def create_flight(flight):
        return AirportSystem.__flight_instance_list.append(flight)
    
    def check_flight(froml, to, date_depart, date_return = None):
        a = []
        for i in AirportSystem.__flight_instance_list:
            if i.froml.upper() == froml.upper() and i.to.upper() == to.upper() and i.date == date_depart:
                a.append(i)
        if date_return != None:
            for i in AirportSystem.__flight_instance_list:
                if i.froml.upper() == to.upper() and i.to.upper() == froml.upper() and i.date == date_return:
                    a.append(i)
        return a
    
    def choose_flight(flight, depart_time, arrive_time):
        for i in flight:
            if i.time_departure == depart_time and i.time_arrival == arrive_time:
                return i
    
    def create_passenger(title, firstname, middlename, lastname, birthday, phone_number, email):
        n = User()
        n.passenger = Passenger(title, firstname, middlename, lastname, birthday, phone_number, email)
        return n
    
    def check_seat(flight):
        return flight.flight_seats
    
    def choose_seat(passenger, flight, seat):
        for i in flight.flight_seats:
            if i == seat:
                passenger.seat = seat
        return passenger

class Reservation:
    def __init__(self, booking_reference):
        self.__flight_instances = []
        self.__passengers = []
        self.__booking_reference = booking_reference
        self.__extra_service = None
        self.__total_cost = 0
        self.__boarding_pass = None

    @property
    def booking_reference(self):
        return self.__booking_reference

    @property
    def passengers(self):
        return self.__passengers
    
    @passengers.setter
    def passengers(self, passenger):
        self.__passengers.append(passenger)
    
    @property
    def boarding_pass(self):
        return self.__boarding_pass

    @boarding_pass.setter
    def boarding_pass(self, boarding_pass):
        self.__boarding_pass = boarding_pass

    @property
    def flight_instances(self):
        return self.__flight_instances
    
    @flight_instances.setter
    def flight_instances(self, flight):
        self.__flight_instances.append(flight)

class Admin:
    pass

class User:
    def __init__(self):
        self.__passenger = None

    @property
    def passenger(self):
        return self.__passenger

    @passenger.setter
    def passenger(self, passenger):
        self.__passenger = passenger

class Passenger:
    def __init__(self, title, firstname, middlename, lastname, birthday, phone_number, email):
        self.__title = title
        self.__firstname = firstname
        self.__middlename = middlename
        self.__lastname = lastname
        self.__birthday = birthday
        self.__phone_number = phone_number
        self.__email = email
        self.__seat = None

    @property
    def lastname(self):
        return self.__lastname
    
    @property
    def seat(self):
        return self.__seat
    
    @seat.setter
    def seat(self, seat):
        self.__seat = seat

    @property
    def title(self):
        return self.__title
    
    @property
    def name(self):
        return self.__firstname + " " + self.__middlename + " " + self.__lastname

    
class BoardingPass:
    def __init__(self, reservation, passenger, returnl = False):
        self.__flight_seat_number = passenger.seat
        self.__flight_number = reservation.flight_instances[returnl]
        self.__passenger_title = passenger.title
        self.__passenger_name = passenger.name
        self.__aircraft_number = reservation.flight_instances[returnl].aircraft.aircraft_number
        self.__booking_reference = reservation.booking_reference
        self.__departure_date = reservation.flight_instances[returnl].date
        self.__boarding_time = reservation.flight_instances[returnl].boarding_time
        self.__from = reservation.flight_instances[returnl].froml
        self.__to = reservation.flight_instances[returnl].to
    
class Flight:
    def __init__(self, froml, to, flight_number):
        self.__from = froml
        self.__to = to
        self.__flight_number = flight_number

    @property
    def froml(self):
        return self.__from
    
    @property
    def to(self):
        return self.__to

class FlightInstance(Flight):
    def __init__(self, froml, to, time_departure, time_arrival, aircraft, date):
        super().__init__(froml, to, aircraft.aircraft_number)
        self.__flight_seats = aircraft.seats
        self.__time_departure = time_departure
        self.__time_arrival = time_arrival
        self.__aircraft = aircraft
        self.__date = date

    @property
    def date(self):
        return self.__date
    
    @property
    def boarding_time(self):
        return self.__time_arrival + " " + self.__time_departure
    
    @property
    def aircraft(self):
        return self.__aircraft
    
    @property
    def time_departure(self):
        return self.__time_departure
    
    @property
    def time_arrival(self):
        return self.__time_arrival
    
    @property
    def flight_seats(self):
        return self.__flight_seats
    
class Aircraft:
    def __init__(self, seats, aircraft_number):
        self.__seats = seats
        self.__aircraft_number = aircraft_number

    @property
    def aircraft_number(self):
        return self.__aircraft_number
    
    @property
    def seats(self):
        return self.__seats
    
class Seats:
    def __init__(self, seat_number, seat_category):
        self.__seat_number = seat_number
        self.__seat_category = seat_category

class Category:
    def __init__(self, price):
        self.__price = price

class SeatFlight:
    def __init__(self, seat, occupied) -> None:
        super().__init__(seat, occupied)

class Payment:
    def __init__(self, create_on, amount, status):
        self.__create_on = create_on
        self.__amount = amount
        self.__status = status

class CreditCard(Payment):
    pass

class Qr(Payment):
    pass

class Service:
    def __init__(self, price):
        self.__price = price

class Insurance(Service):
    pass

class MoreBaggage(Service):
    def __init__(self, price, weight):
        super().__init__(price)
        self.__weight = weight

n = User()
n.passenger = Passenger("Mr","Rachchanon", "","Klaisuban", "3-5-2005","0621419954","nphisu@gmail.com")
AirportSystem.create_flight(FlightInstance("Thai", "Indo",  "8.00", "10.00", Aircraft([Seats("A1", "N"), Seats("A2", "N")], "ABC"), "22-2-2020"))
AirportSystem.create_flight(FlightInstance("Thai", "Indo", "12.00", "14.00", Aircraft([Seats("A1", "N"), Seats("A2", "N")], "ABC"), "22-2-2020"))
AirportSystem.create_flight(FlightInstance("Thai", "Indo", "16.00", "18.00", Aircraft([Seats("A1", "N"), Seats("A2", "N")], "ABC"), "22-2-2020"))
AirportSystem.create_flight(FlightInstance("Indo", "Indo", "20.00", "22.00", Aircraft([Seats("A1", "N"), Seats("A2", "N")], "ABC"), "22-2-2020"))
AirportSystem.create_flight(FlightInstance("Indo", "Thai", "8.00", "10.00", Aircraft([Seats("A1", "N"), Seats("A2", "N")], "ABC"), "22-2-2020"))
AirportSystem.create_flight(FlightInstance("Indo", "Thai", "12.00", "14.00", Aircraft([Seats("A1", "N"), Seats("A2", "N")], "ABC"), "22-2-2020"))
AirportSystem.create_flight(FlightInstance("Indo", "Thai", "16.00", "18.00", Aircraft([Seats("A1", "N"), Seats("A2", "N")], "ABC"), "22-2-2020"))
AirportSystem.create_flight(FlightInstance("Indo", "Thai", "20.00", "22.00", Aircraft([Seats("A1", "N"), Seats("A2", "N")], "ABC"), "22-2-2020"))
AirportSystem.create_reservation(Reservation(0))
AirportSystem.check_reservation(0).flight_instances = AirportSystem.choose_flight(AirportSystem.check_flight("Thai", "Indo", "22-2-2020"), "8.00", "10.00")
AirportSystem.check_reservation(0).passengers = n.passenger
print(AirportSystem.check_in(0, "Klaisuban"))

app = FastAPI()

@app.get("/all_reservation")
def all_reservation():
    return AirportSystem.reservation_list()

@app.post("/reservation")
def new_reservation(booking_reference : str):
    return AirportSystem.create_reservation(Reservation(booking_reference))

@app.get("/see_flight")
def see_flight(froml : str, to : str, date_depart : str, return_depart : Optional[str] = None):
    return AirportSystem.check_flight(froml, to, date_depart, return_depart)

@app.post("/select_flight")
def select_flight(booking_reference : str, froml : str, to : str, date : str, depart_time : str, arrive_time : str):
    AirportSystem.check_reservation(booking_reference).flight_instances = AirportSystem.choose_flight(AirportSystem.check_flight(froml, to, date) , depart_time, arrive_time)
    return AirportSystem.check_reservation(booking_reference)

@app.post("/passenger")
def new_passenger(booking_reference : str, title : str, firstname : str, lastname : str, birthday : str, phone_number : str, email : str, middlename : Optional[str] = None):
    AirportSystem.check_reservation(booking_reference).passengers = AirportSystem.create_passenger(title, firstname, middlename, lastname, birthday, phone_number, email)
    return AirportSystem.check_reservation(booking_reference)

@app.get("/see_seat")
def see_seat(depart : str, arrive : str, date : str, depart_time : str, arrive_time : str):
    return AirportSystem.check_seat(AirportSystem.choose_flight(AirportSystem.check_flight(depart, arrive, date) , depart_time, arrive_time))

@app.post("/select_seat")
def select_seat(booking_reference : str, lastname : str, returnl : bool, seat : str):
    return AirportSystem.choose_seat(AirportSystem.check_passenger(booking_reference, lastname), AirportSystem.check_reservation(booking_reference).flight_instances[returnl], seat)

@app.get("/boarding_pass")
def board_pass(booking_reference : int, lastname : str):
    return AirportSystem.check_in(booking_reference, lastname)