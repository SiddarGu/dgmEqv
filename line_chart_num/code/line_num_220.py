

import matplotlib.pyplot as plt
import numpy as np

# Data
Year = np.array([2010,2011,2012,2013,2014])
Crimes_Reported = np.array([1000,1200,1300,1400,1300])
Crimes_Proven = np.array([800,900,900,1000,1200])
Crimes_Unproven = np.array([200,300,400,400,100])

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the data
ax.plot(Year, Crimes_Reported, marker='o', linestyle='--', label='Crimes Reported')
ax.plot(Year, Crimes_Proven, marker='o', linestyle='--', label='Crimes Proven')
ax.plot(Year, Crimes_Unproven, marker='o', linestyle='--', label='Crimes Unproven')

# Set xlabel and ylabel
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Crimes', fontsize=14)

# Set xticks
ax.set_xticks(Year)
ax.set_xticklabels(Year, rotation=90, fontsize=12, wrap=True)

# Set title
ax.set_title('Comparison of Reported and Proven Crimes in the US from 2010-2014', fontsize=14)

# Set legend
ax.legend(loc="upper right", fontsize=12)

# Annotate each point
for x, y in zip(Year, Crimes_Reported):
    ax.annotate('{:.0f}'.format(y), xy=(x, y), xytext=(0, 4),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)
for x, y in zip(Year, Crimes_Proven):
    ax.annotate('{:.0f}'.format(y), xy=(x, y), xytext=(0, 4),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)
for x, y in zip(Year, Crimes_Unproven):
    ax.annotate('{:.0f}'.format(y), xy=(x, y), xytext=(0, 4),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/170.png')

# Clear current image state
plt.clf()