
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(16, 8), dpi=80)

# Create data
year = np.array([2001, 2002, 2003, 2004, 2005])
violent_crime_rate = np.array([550, 530, 580, 560, 590])
property_crime_rate = np.array([3120, 2970, 3180, 3200, 3100])

# Create line chart
ax = fig.add_subplot()
ax.set_xlabel('Year')
ax.set_ylabel('Rate (per 100,000 people)')
ax.set_xticks(year)
ax.plot(year, violent_crime_rate, label='Violent Crime Rate', color='red', marker='o', linestyle='--', linewidth=2)
ax.plot(year, property_crime_rate, label='Property Crime Rate', color='blue', marker='o', linestyle='--', linewidth=2)
ax.legend(loc='best')
ax.set_title('Change in Crime Rates in the US from 2001-2005')
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/467.png', bbox_inches="tight")

# Clear the current image state
plt.clf()