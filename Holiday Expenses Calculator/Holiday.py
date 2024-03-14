print("Book your self a holiday to Zamunda, Wakanda or Kuvuki")
# Request holiday information from user
city_flight = input("Where are you flying to? : ").lower()
num_nights = int(input("How many nights will you be staying? :"))
rental_days = int(input("How many days will you be renting a car? :"))

#calculate the cost to stay a night.
def hotel_cost(num_nights):
    per_night_cost =  num_nights * 500
    return per_night_cost

# Calculate the cost of the flight
def plane_cost(city_flight):
    flight_cost = 0
    if city_flight == "zamunda":
        flight_cost = 500
        return flight_cost
    elif city_flight == "wakanda":
        flight_cost = 550
        return flight_cost
    elif city_flight == "kuvuki":
        flight_cost = 600
        return flight_cost
    else:
        flight_cost = 900
        return flight_cost

# calculate cost of car rental
def car_rental(rental_days):
    rental_cost = rental_days * 200
    return rental_cost

# Calculate total cost of the holiday
def holidays_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# Print total cost and break down of cost
print("\n**************************************************")
print(f"The total cost of the holiday is R{holidays_cost(city_flight, num_nights, rental_days)}")
print("**************************************************")
print(f"Flight to {city_flight} cost R{plane_cost(city_flight)}")
print(f"Car rental cost R{car_rental(rental_days)}")
print(f"Accomodation costs {hotel_cost(num_nights)}")
print("**************************************************\n")