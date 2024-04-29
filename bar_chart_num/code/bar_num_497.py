
import matplotlib.pyplot as plt
import numpy as np

# create data
year = np.array([2015, 2016, 2017, 2018])
CO2_emissions = np.array([5500, 5350, 5200, 5150])
Renewable_Energy = np.array([7, 8, 9, 10])
Electric_Vehicles = np.array([2, 3, 5, 7])

# set figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# plot data
bar1 = ax.bar(year, CO2_emissions, color='#fb0303', label='CO2 Emissions(kg)')
bar2 = ax.bar(year, Renewable_Energy, bottom=CO2_emissions, color='#3bbd2f', label='Renewable Energy(%)')
bar3 = ax.bar(year, Electric_Vehicles, bottom=CO2_emissions+Renewable_Energy, color='#2f31bd', label='Electric Vehicles(%)')

# label value of each bar
for bar in bar1+bar2+bar3:
    x_pos = bar.get_x() + bar.get_width()/2
    y_pos = bar.get_height() - bar.get_height()/10
    ax.text(x_pos, y_pos, '%.2f' % bar.get_height(), ha='center', va='center', fontsize=12, color='#000000')

# set ticks
ax.set_xticks(year)
ax.set_xticklabels(year)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.set_ylabel('Units', fontsize=15)

# set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fontsize=15, frameon=True, ncol=3)

# set title
plt.title('CO2 emissions, renewable energy usage and electric vehicles in four years', fontsize=15)

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/290.png')

# clear current image state
plt.clf()