
import matplotlib.pyplot as plt
import numpy as np

# Set the figure size
plt.figure(figsize=(9, 6))

# Set up the data
year = [2020, 2021, 2022, 2023]
donations = [1000, 1200, 1500, 1800]
hours = [20000, 25000, 30000, 35000]
projects = [100, 120, 150, 200]

# Plot the Donation Line Chart
ax1 = plt.subplot()
ax1.plot(year, donations, color='b', label='Donations(million dollars)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Donations(million dollars)')

# Plot the Hours Line Chart
ax2 = ax1.twinx()
ax2.plot(year, hours, color='g', label='Volunteer Hours')
ax2.set_ylabel('Volunteer Hours')

# Plot the Projects Line Chart
ax3 = ax1.twinx()
ax3.plot(year, projects, color='r', label='Number of Projects')
ax3.set_ylabel('Number of Projects')

# Annotate the data points
for i, txt in enumerate(donations):
    ax1.annotate(txt, (year[i], donations[i]), rotation=15, fontsize=14)
for i, txt in enumerate(hours):
    ax2.annotate(txt, (year[i], hours[i]), rotation=15, fontsize=14)
for i, txt in enumerate(projects):
    ax3.annotate(txt, (year[i], projects[i]), rotation=15, fontsize=14)

# Add legend
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Add title
plt.title('Nonprofit Organization Contributions and Activities in the US from 2020 to 2023', fontsize=18)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/19.png')

# Clear the current image state
plt.clf()