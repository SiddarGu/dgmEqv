
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

months = ["January","February","March","April","May","June"]
hotel_room_occupancy_rate = [90,85,80,75,70,80]
restaurant_occupancy_rate = [80,75,65,60,75,80]
tourist_attraction_visits = [500000,450000,400000,350000,300000,350000]

plt.plot(months,hotel_room_occupancy_rate,label="Hotel Room Occupancy Rate(%)",color="red")
plt.plot(months,restaurant_occupancy_rate,label="Restaurant Occupancy Rate(%)",color="green")
plt.plot(months,tourist_attraction_visits,label="Tourist Attraction Visits",color="blue")

plt.xticks(np.arange(len(months)),months,rotation=45)
plt.title("Tourism and Hospitality Occupancy Rates in Spring of 2021")
plt.legend(loc="best")
plt.tight_layout()

plt.savefig("line chart/png/551.png")
plt.clf()