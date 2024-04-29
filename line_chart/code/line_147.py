
import matplotlib.pyplot as plt

year = [2000, 2001, 2002, 2003, 2004]
temp = [14.5, 14.7, 14.8, 14.9, 15.0]
gas = [7100, 7200, 7300, 7400, 7500]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.plot(year, temp, label='Average Global Temperature (degrees Celsius)', color='r')
ax.plot(year, gas, label='Carbon Emissions (million tons)', color='b')
ax.set_xticks(year)
ax.set_title('Average Global Temperature and Carbon Emissions from 2000 to 2004')
ax.legend(loc='upper left', bbox_to_anchor=(-0.1, -0.2), ncol=2, frameon=False)
plt.tight_layout()
plt.savefig('line chart/png/311.png')
plt.clf()