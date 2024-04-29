

import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(15,10))

# Plotting the data
plt.plot([2017, 2018, 2019, 2020], [1000, 1100, 1500, 1300], label='Emissions(kg/year)')
plt.plot([2017, 2018, 2019, 2020], [5000, 6000, 8000, 7000], label='Energy Consumption(kWh/year)')
plt.plot([2017, 2018, 2019, 2020], [300, 400, 500, 600], label='Recycled Materials(kg/year)')

# Adding label
plt.xlabel('Year')
plt.ylabel('Units')

# Setting legend
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, -0.2, 1.2, 0))

# Title
plt.title('Global Environmental Impact in the last four years')

# Setting ticks
plt.xticks(rotation=45)

# Setting grid
plt.grid(True, linestyle='-.')

# Setting layout
plt.tight_layout()

# Saving the figure
plt.savefig('line chart/png/304.png')

# Clear the current image state
plt.clf()