import csv
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk, messagebox

class Flight:
    def __init__(self, flight_id, departure, arrival, date, time, seats_available):
        self.flight_id = flight_id
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.time = time
        self.seats_available = int(seats_available)

    def to_csv_row(self):
        return [self.flight_id, self.departure, self.arrival, self.date, self.time, self.seats_available]


class Passenger:
    def __init__(self, passenger_id, name, contact_details, booked_flights):
        self.passenger_id = passenger_id
        self.name = name
        self.contact_details = contact_details
        self.booked_flights = booked_flights.split(';') if booked_flights else []

    def add_flight(self, flight_id):
        if flight_id not in self.booked_flights:
            self.booked_flights.append(flight_id)

    def remove_flight(self, flight_id):
        if flight_id in self.booked_flights:
            self.booked_flights.remove(flight_id)

    def to_csv_row(self):
        return [self.passenger_id, self.name, self.contact_details, ';'.join(self.booked_flights)]


class BookingManager:
    def __init__(self):
        self.flights = []
        self.passengers = []
        self.bookings_log = []

    def load_data(self):
        self.load_flights()
        self.load_passengers()
        self.load_bookings()

    def load_flights(self):
        try:
            with open('flights.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                self.flights = [Flight(*row) for row in reader]
        except FileNotFoundError:
            print("flights.csv not found. Creating an empty dataset.")

    def load_passengers(self):
        try:
            with open('passengers.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                self.passengers = [Passenger(*row) for row in reader]
        except FileNotFoundError:
            print("passengers.csv not found. Creating an empty dataset.")

    def load_bookings(self):
        try:
            with open('bookings.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                self.bookings_log = [row for row in reader]
        except FileNotFoundError:
            print("bookings.csv not found. Creating an empty dataset.")

    def save_data(self):
        self.save_flights()
        self.save_passengers()
        self.save_bookings()

    def save_flights(self):
        with open('flights.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Flight ID', 'Departure', 'Arrival', 'Date', 'Time', 'Seats Available'])
            for flight in self.flights:
                writer.writerow(flight.to_csv_row())

    def save_passengers(self):
        with open('passengers.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Passenger ID', 'Name', 'Contact Details', 'Booked Flights'])
            for passenger in self.passengers:
                writer.writerow(passenger.to_csv_row())

    def save_bookings(self):
        with open('bookings.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Transaction Type', 'Flight ID', 'Passenger ID', 'Date'])
            writer.writerows(self.bookings_log)

    def search_flight(self, query):
        return [f for f in self.flights if query.lower() in f.departure.lower() or query.lower() in f.arrival.lower()]

    def search_passenger(self, query):
        return [p for p in self.passengers if query.lower() in p.name.lower() or query == p.passenger_id]

    def book_flight(self, flight_id, passenger_id):
        flight = next((f for f in self.flights if f.flight_id == flight_id), None)
        passenger = next((p for p in self.passengers if p.passenger_id == passenger_id), None)

        if not flight:
            return "Flight not found."
        if not passenger:
            return "Passenger not found."
        if flight.seats_available <= 0:
            return "No seats available."

        passenger.add_flight(flight_id)
        flight.seats_available -= 1
        self.bookings_log.append(['Booking', flight_id, passenger_id, datetime.now().strftime('%Y-%m-%d')])
        self.save_data()
        return "Booking confirmed."

    def cancel_booking(self, flight_id, passenger_id):
        flight = next((f for f in self.flights if f.flight_id == flight_id), None)
        passenger = next((p for p in self.passengers if p.passenger_id == passenger_id), None)

        if not flight or not passenger:
            return "Invalid cancellation request."

        if flight_id not in passenger.booked_flights:
            return "Passenger has not booked this flight."

        # Calculate refund
        cancellation_date = datetime.now().strftime('%Y-%m-%d')
        refund_percentage = self.calculate_refund(flight_id, cancellation_date)

        # Perform cancellation
        passenger.remove_flight(flight_id)
        flight.seats_available += 1
        self.bookings_log.append(['Cancellation', flight_id, passenger_id, cancellation_date])
        self.save_data()

        # Return cancellation status with refund value
        return f"Booking cancelled. Refund: {refund_percentage}%."

    def calculate_refund(self, flight_id, cancellation_date):
        flight = next((f for f in self.flights if f.flight_id == flight_id), None)
        if not flight:
            return 0

        flight_date = datetime.strptime(flight.date, '%Y-%m-%d')
        cancellation_date = datetime.strptime(cancellation_date, '%Y-%m-%d')
        delta = (flight_date - cancellation_date).days

        if delta >= 2:
            return 50
        elif 1 <= delta < 2:
            return 80
        return 0

class FlightBookingGUI:
    def __init__(self):
        self.manager = BookingManager()
        self.manager.load_data()
        self.window = tk.Tk()
        self.window.title("Flight Booking System")

        # Flight Management Section
        self.flight_search_label = ttk.Label(self.window, text="Search Flights:")
        self.flight_search_label.pack()
        self.flight_search_entry = ttk.Entry(self.window)
        self.flight_search_entry.pack()
        self.flight_search_button = ttk.Button(self.window, text="Search", command=self.search_flights)
        self.flight_search_button.pack()

        self.flight_results = tk.Text(self.window, height=10, width=50)
        self.flight_results.pack()

        # Passenger Management Section
        self.passenger_search_label = ttk.Label(self.window, text="Search Passengers:")
        self.passenger_search_label.pack()
        self.passenger_search_entry = ttk.Entry(self.window)
        self.passenger_search_entry.pack()
        self.passenger_search_button = ttk.Button(self.window, text="Search", command=self.search_passengers)
        self.passenger_search_button.pack()

        self.passenger_results = tk.Text(self.window, height=10, width=50)
        self.passenger_results.pack()

        # Booking Section
        self.flight_id_label = ttk.Label(self.window, text="Flight ID:")
        self.flight_id_label.pack()
        self.flight_id_entry = ttk.Entry(self.window)
        self.flight_id_entry.pack()
        self.passenger_id_label = ttk.Label(self.window, text="Passenger ID:")
        self.passenger_id_label.pack()
        self.passenger_id_entry = ttk.Entry(self.window)
        self.passenger_id_entry.pack()
        self.book_button = ttk.Button(self.window, text="Book Flight", command=self.book_flight)
        self.book_button.pack()
        self.cancel_button = ttk.Button(self.window, text="Cancel Booking", command=self.cancel_booking)
        self.cancel_button.pack()

    def search_flights(self):
        query = self.flight_search_entry.get()
        results = self.manager.search_flight(query)
        self.flight_results.delete('1.0', tk.END)
        for flight in results:
            self.flight_results.insert(tk.END, f"{flight.flight_id} - {flight.departure} to {flight.arrival} on {flight.date} at {flight.time} ({flight.seats_available} seats available)\n")

    def search_passengers(self):
        query = self.passenger_search_entry.get()
        results = self.manager.search_passenger(query)
        self.passenger_results.delete('1.0', tk.END)
        for passenger in results:
            self.passenger_results.insert(tk.END, f"{passenger.passenger_id} - {passenger.name}, {passenger.contact_details}, Flights: {', '.join(passenger.booked_flights)}\n")

    def book_flight(self):
        flight_id = self.flight_id_entry.get()
        passenger_id = self.passenger_id_entry.get()
        result = self.manager.book_flight(flight_id, passenger_id)
        messagebox.showinfo("Booking Status", result)

    def cancel_booking(self):
        flight_id = self.flight_id_entry.get()
        passenger_id = self.passenger_id_entry.get()
        result = self.manager.cancel_booking(flight_id, passenger_id)
        messagebox.showinfo("Cancellation Status", result)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = FlightBookingGUI()
    gui.run()
