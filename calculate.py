# Function to calculate swimming statistics
def calculate_swimming_stats(distance_meters, time_hours):
    # Calculate swimming speed in meters per hour
    speed = distance_meters / time_hours
    
    return {
        'distance': distance_meters,
        'hours': time_hours,
        'speed': speed,
        'kall' : kall,
    }

# Example usage
distance = int(input("Enter distance swam in meters: "))
hours = int(input("Enter time spent swimming in hours: "))
kall = int(input("Enter kall swam in meters: "))

stats = calculate_swimming_stats(distance, hours)

print(f"\nSwimming Statistics:")
print(f"Distance: {stats['distance']} meters")
print(f"Time: {stats['hours']} hours") 
print(f"Average speed: {stats['speed']:.2f} meters/hour")
print(f"Kall: {stats['kall']} meters")
