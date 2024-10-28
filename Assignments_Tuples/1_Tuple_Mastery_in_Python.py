# Create a Python function that takes a list of tuples as an argument.





#  Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`,
#  the output should be a string formatted as:
# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco
# Prompt the user for name, origin, and destination
# List to hold all itineraries
itineraries = []

while True:
    name = input("Enter traveler name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    
    # Append the traveler's itinerary to the list
    itineraries.append((name, origin, destination))

# Format and print each itinerary
for i, itinerary in enumerate(itineraries, start=1):
    print(f"Itinerary {i}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}")
