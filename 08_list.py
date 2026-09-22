departure_queue = [
    "LOT123", # Flight number for LOT Polish Airlines   
    "AF456", # Flight number for Air France
    "BA789", # Flight number for British Airways
    "LH012", # Flight number for Lufthansa
    "DL345", # Flight number for Delta Airlines
    "SAS678", # Flight number for Scandinavian Airlines
]

# Check first value in the list
print(f"First flight in the departure queue: {departure_queue[0]}")

#Change Value in the list
departure_queue[0] = "KLM987" # Change the first flight to KLM
print(f"Updated first flight in the departure queue: {departure_queue[0]}")

#check third flight in the list
print(f"Third flight in the departure queue: {departure_queue[2]}")


#Move a delayed flight to the end of the queue
delayed_flight = departure_queue.pop(1) # Remove the second flight (AF456) from the queue
departure_queue.append(delayed_flight) # Add it to the end of the queue
print(f"Updated departure queue after moving delayed flight: {departure_queue}")


#Remove the first flight because it has taken off
departed_flight = departure_queue.pop(0) # Remove the first flight (KLM987) from the queue
print(f"Flight {departed_flight} has taken off. Updated departure queue: {departure_queue}")

#Find the index of a specific flight in the queue
flight_to_find = "DL345"
if flight_to_find in departure_queue:
    flight_index = departure_queue.index(flight_to_find)
    print(f"Flight {flight_to_find} is at index {flight_index} in the departure queue.")
    