
import matplotlib.pyplot as plt
import numpy as np

data = [['January', 60, 70, 10000], ['February', 65, 80, 15000], ['March', 68, 85, 16000],
        ['April', 70, 90, 17000], ['May', 75, 95, 18000], ['June', 80, 90, 20000],
        ['July', 85, 85, 22000], ['August', 80, 80, 25000], ['September', 70, 75, 28000],
        ['October', 65, 70, 30000], ['November', 60, 65, 32000], ['December', 55, 60, 35000]]

months=[]
hotel_occupancy=[]
restaurant_occupancy=[]
tourist_number=[]

for row in data:
    months.append(row[0])
    hotel_occupancy.append(row[1])
    restaurant_occupancy.append(row[2])
    tourist_number.append(row[3])

x = np.arange(len(months))

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)

ax.plot(x, hotel_occupancy, label="Hotel Occupancy Rate(%)")
ax.plot(x, restaurant_occupancy, label="Restaurant Occupancy Rate(%)")
ax.plot(x, tourist_number, label="Tourist Number")

plt.xticks(x, months)

plt.title('Tourist activities and occupancy rates in a tourist destination from January to December 2021')
plt.xlabel('Month')
plt.ylabel('Occupancy Rate/Tourist Number')
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/555.png')
plt.clf()