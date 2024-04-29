
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Create data
year = np.array([2016,2017,2018,2019,2020])
gross_earnings = np.array([2.2,2.3,2.5,2.7,2.9])
tickets_sold = np.array([90,95,100,105,110])

# Plot the line chart
ax.plot(year, gross_earnings, color='blue', label='Gross Earnings')
ax.plot(year, tickets_sold, color='red', label='Tickets Sold')

# Set title and labels
ax.set_title('Growth of Box Office Gross and Ticket Sales for the NBA from 2016-2020')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sales (million dollars)', fontsize=12)

# Set limits
#ax.set_ylim(2.0, 3.0)

# Set xticks
ax.set_xticks(year)

# Add grid
ax.grid()

# Add legend
ax.legend(loc='upper right')

# Save the figure
plt.savefig('line_11.png', bbox_inches='tight')

# Clear the current image state
plt.clf()