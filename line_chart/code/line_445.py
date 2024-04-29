
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)

Year = [2000, 2001, 2002, 2003, 2004]
Air_Travel = [100, 120, 140, 160, 180]
Rail_Travel = [50, 60, 70, 80, 90]
Road_Travel = [200, 230, 250, 270, 290]
Sea_Travel = [30, 40, 50, 60, 70]

ax.plot(Year, Air_Travel, color='blue', linestyle='-', marker='o', label='Air Travel')
ax.plot(Year, Rail_Travel, color='red', linestyle='-', marker='o', label='Rail Travel')
ax.plot(Year, Road_Travel, color='green', linestyle='-', marker='o', label='Road Travel')
ax.plot(Year, Sea_Travel, color='yellow', linestyle='-', marker='o', label='Sea Travel')

plt.title('Global Passenger Travel Trends from 2000 to 2004')
plt.xlabel('Year')
plt.ylabel('Passengers (million)')
plt.xticks(Year)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig('line chart/png/373.png')
plt.clf()