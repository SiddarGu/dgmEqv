
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

#Data
countries = ["USA", "UK", "Germany", "France"]
hotel_bookings = [2.5, 3.5, 2.3, 2.8]
restaurant_visits = [4.5, 5.5, 4.4, 4.7]

#Plot
ax.bar(countries, hotel_bookings, width=0.4, bottom=0, label="Hotel Bookings")
ax.bar(countries, restaurant_visits, width=0.4, bottom=hotel_bookings, label="Restaurant Visits")

#Label each bar
for i in range(len(countries)):
    ax.annotate(str(hotel_bookings[i]) + "M", xy=(i-0.1, hotel_bookings[i]/2))
    ax.annotate(str(restaurant_visits[i]) + "M", xy=(i-0.1, hotel_bookings[i] + restaurant_visits[i]/2))

#X-axis
plt.xticks(np.arange(len(countries)), countries)

#Title
plt.title('Number of hotel bookings and restaurant visits in four countries in 2021')

#Legend
plt.legend(loc='upper left')

#Adjustment
plt.tight_layout()

#Save
plt.savefig('Bar Chart/png/319.png')

#Clear
plt.clf()