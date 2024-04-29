

import numpy as np
import matplotlib.pyplot as plt

x = ["January", "February", "March", "April", "May"]
hotel_bookings = [20000, 25000, 30000, 35000, 40000]
restaurant_reservations = [45000, 50000, 55000, 60000, 65000]
tourist_visits = [80000, 85000, 90000, 95000, 100000]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()
ax.plot(x, hotel_bookings, label="Hotel Bookings")
ax.plot(x, restaurant_reservations, label="Restaurant Reservations")
ax.plot(x, tourist_visits, label="Tourist Visits")
ax.set_title("Changes in travel industry services in 2021")
ax.set_xlabel("Month")
ax.set_ylabel("Number")
ax.legend(loc="upper left")
ax.grid(True)
plt.xticks(x, rotation=40)
plt.tight_layout()
plt.savefig("line chart/png/325.png")
plt.clf()