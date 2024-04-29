
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
hotel_bookings = [200, 220, 210, 250, 210, 220, 240, 210, 200, 220, 195, 215]
restaurant_bookings = [150, 220, 225, 215, 220, 230, 235, 240, 205, 210, 215, 220]
tourist_bookings = [50, 55, 60, 70, 75, 80, 85, 90, 95, 100, 105, 110]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

plt.title('Bookings of tourism and hospitality sector in the USA, 2021')
plt.plot(months, hotel_bookings, color='blue', label='Hotel Bookings (thousands)')
plt.plot(months, restaurant_bookings, color='red', label='Restaurant Bookings (thousands)')
plt.plot(months, tourist_bookings, color='green', label='Tourist Attractions Bookings (thousands)')

plt.grid()

ax.xaxis.set_ticks(np.arange(len(months)))
ax.xaxis.set_ticklabels(months, rotation=90, fontsize=10)

plt.legend(loc='lower right', fontsize=10)
plt.xticks(rotation=90)

for a,b,c in zip(months, hotel_bookings, restaurant_bookings): 
    plt.annotate(str(b)+','+str(c), xy=(a, b), xytext=(-2, 15), textcoords='offset points')

plt.tight_layout()
plt.savefig('line chart/png/357.png')
plt.clf()