

import matplotlib.pyplot as plt
import numpy as np

# Set data
year = [2020, 2021, 2022, 2023]
attendance = [750, 850, 900, 1000]
tickets_sold = [500, 600, 700, 800]
revenue = [100, 120, 130, 150]

# Create figure
fig = plt.figure(figsize=(15, 5))

# Plot data
ax = fig.add_subplot(111)
ax.plot(year, attendance, c='r', marker='o', label='Attendance')
ax.plot(year, tickets_sold, c='g', marker='^', label='Tickets Sold')
ax.plot(year, revenue, c='b', marker='s', label='Revenue')

# Add grid
ax.grid(linestyle='--', linewidth=1.00, alpha=0.3)

# Add labels
ax.set_xticks(year)
ax.set_title('Attendance, tickets sales and revenue of a sports event from 2020 to 2023')
ax.set_xlabel('Year')
ax.set_ylabel('Data')
ax.legend(loc='upper right')

# Annotate data
for x, y1, y2, y3 in zip(year, attendance, tickets_sold, revenue):
    ax.annotate(f'{y1}\n{y2}\n{y3}', xy=(x, y1), xytext=(x - 0.2, y1 + 50))

# Fit figure
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/449.png')

# Clear figure
plt.clf()