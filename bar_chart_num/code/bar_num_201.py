
import matplotlib.pyplot as plt
import numpy as np

# Set up the data
Year = np.array(['2018', '2019', '2020', '2021'])
Revenue = np.array([1000, 1100, 1300, 1500])
Profit = np.array([200, 300, 400, 500])

# Generate the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot the data
ax.bar(Year, Revenue, label='Revenue', bottom=0)
ax.bar(Year, Profit, label='Profit', bottom=Revenue)

# Set title and axis labels
ax.set_title('Financial performance of a business from 2018 to 2021')
ax.set_xlabel('Year')
ax.set_ylabel('$ (million)')

# Annotate the data
for x, y1, y2 in zip(Year, Revenue, Profit):
    ax.text(x, y1/2, '{:.0f}'.format(y1), ha='center', va='center', fontsize=12)
    ax.text(x, y1+y2/2, '{:.0f}'.format(y2), ha='center', va='center', fontsize=12)

# Set the xticks
plt.xticks(Year, Year)

# Adjust the legend position
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# Adjust the display
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/288.png')

# Clear the current figure
plt.clf()