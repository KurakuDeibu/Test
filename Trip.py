class Trip:
    def __init__(self, origin, destination, distance):
        self.origin = origin
        self.destination = destination
        self.distance = distance

    def display_details(self):
        print(f"{self.origin} to {self.destination}, {self.distance} km")
    

class BusTrip(Trip):
    def __init__(self, origin, destination, distance, base_fare):
        super().__init__(origin, destination, distance)
        self.base_fare = base_fare

    def compute_cost(self):
        return self.base_fare * self.distance

    def display_details(self):
        print(f"Bus Constructor")
        print(f"Bus Trip: {self.origin} to {self.destination}, {self.distance} km, P{self.base_fare} base fare")

class BoatTrip(Trip):
    def __init__(self, origin, destination, distance, base_fare):
        super().__init__(origin, destination, distance)
        self.base_fare = base_fare

    def compute_cost(self):
        return self.base_fare

    def display_details(self):
        print(f"Boat Constructor")
        print(f"Boat Trip: {self.origin} to {self.destination}, {self.distance} km, P{self.base_fare} base fare")
        

class PlaneTrip(Trip):
    def __init__(self, origin, destination, distance, base_fare):
        super().__init__(origin, destination, distance)
        self.base_fare = base_fare

    def compute_cost(self):
        return self.base_fare * (1 + 0.1)

    def display_details(self):
        print(f"Plane Constructor")
        print(f"Plane Trip: {self.origin} to {self.destination}, {self.distance} km, P{self.base_fare} base fare")

trips = [
    BusTrip("Zamboanga", "Cagayan", 494, 5),
    BusTrip("Tagbilaran", "Panglao", 20, 10),
    BoatTrip("Cebu", "Tagbilaran", 90, 800),
    PlaneTrip("Manila", "Davao", 1500, 4500),
    PlaneTrip("Clark", "Iloilo", 751, 2300)
]

total_cost = 0
for trip in trips:
    print(f"Trip Constructor")
    trip.display_details()
    total_cost += trip.compute_cost()

print(f"Total Cost of trips: {total_cost}")
