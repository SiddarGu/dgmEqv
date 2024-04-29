
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
ax = plt.subplot()

year = np.array([2018, 2019, 2020, 2021])
hotel_occupancy_rate = np.array([70, 75, 65, 80])
airline_passenger_volume = np.array([50, 55, 60, 50])
tourist_attraction_visitors = np.array([40, 45, 50, 55])

ax.plot(year, hotel_occupancy_rate, label="Hotel Occupancy Rate", linewidth=2)
ax.plot(year, airline_passenger_volume, label="Airline Passenger Volume", linewidth=2)
ax.plot(year, tourist_attraction_visitors, label="Tourist Attraction Visitors", linewidth=2)

ax.legend(loc="best", fontsize=10, framealpha=0.5)
ax.set_xticks(year)
plt.title("Yearly travel trends in the tourism industry")
plt.tight_layout()
plt.savefig("line chart/png/258.png")
plt.clf()