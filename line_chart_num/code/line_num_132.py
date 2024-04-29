
import matplotlib.pyplot as plt
import numpy as np

# create figure before plotting
fig = plt.figure(figsize=(10, 6))

# store data
data = [[2020, 1000, 4000], 
        [2021, 1200, 4500],
        [2022, 1500, 3000],
        [2023, 1700, 3500]]

data_array = np.array(data)

# plot data
plt.plot(data_array[:, 0], data_array[:, 1], '-r', label='Organic Food Sales')
plt.plot(data_array[:, 0], data_array[:, 2], '-b', label='Fast Food Sales')

# set axis label
plt.xlabel('Year')
plt.ylabel('Sales (million dollars)')

# set x-axis values
plt.xticks(data_array[:, 0])

# add grid
plt.grid(alpha=0.3)

# add legend
plt.legend(loc='best')

# add title
plt.title('Growth of Organic Food and Fast Food Sales in the U.S. from 2020 to 2023')

# display the value of each data point directly on the figure
for x, y1, y2 in data_array:
    plt.annotate(f'{y1:.1f}', xy=(x, y1), xytext=(x - 0.1, y1 + 50))
    plt.annotate(f'{y2:.1f}', xy=(x, y2), xytext=(x + 0.1, y2 + 50))

# adjust the figure layout
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/36.png')

# clear the current image state
plt.clf()