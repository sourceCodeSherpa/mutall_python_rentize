#
# Import classes
from rentize import Client, Service, Water, Charges, Rent
#
# Date Variables
month = 2
year = 2024
#
# Instantiate Client class
client = Client(month, year)
#
# Instantiate Service class
service = Service(client)
#
# List active clients
clients_df = service.client.get_active_clients()
#
# Instantiate Charges class
charges = Charges(client)
#
# Show subscribed charges for each client
subs_df = charges.get_subscribed_charges()
#
# Show automatic charges for each client
auto_charges_df = charges.get_auto_charges()
#
# Get current water readings based on the variable date at the top
curr_water_rds = Water(client).get_current_readings()
#
# Get previous water readings based on the variable date at the top
prev_water_rds = Water(client).get_previous_readings()
#
# Instantiate Rent class
rent = Rent(client)
rent_p = rent.get_rental_charges()

print('finished')
