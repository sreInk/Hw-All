class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
    
        base_fare = super().fare()
        total_fare = base_fare + (0.10 * base_fare)
        return total_fare

# Example usage
bus = Bus("City Bus", 50)
print(f"Bus Name: {bus.name}")
print(f"Total Fare: {bus.fare()}")
