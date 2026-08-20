
# First distance conversion
distance_in_km = float(input("Enter distance in kilometers: ")) # Asks for distance in km
conversion_factor = 0.621371
distance_in_miles = distance_in_km * conversion_factor # Defines the distance in miles as km * conversion factor
print("Distance in miles:", distance_in_miles)

# Check if user wants to convert a second distance
user_choice = input("Do you want to convert another distance? (yes/no): ")
if user_choice == "yes":
    second_distance_in_km = float(input("Enter distance in kilometers: "))
    second_distance_in_miles = second_distance_in_km * conversion_factor
    print("Distance in miles:", second_distance_in_miles)
else:
    print("Program ended.")

