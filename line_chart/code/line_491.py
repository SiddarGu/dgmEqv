
import matplotlib.pyplot as plt
import numpy as np

# Setting up figure size
plt.figure(figsize=(12, 8))

# Setting up subplot
ax = plt.subplot(111)

# Setting x-axis values
x = np.arange(2010, 2014)

# Setting y-axis values
y1 = np.array([100000, 150000, 130000, 200000])
y2 = np.array([200000, 250000, 180000, 300000])
y3 = np.array([300000, 400000, 250000, 400000])

# Plotting line charts
plt.plot(x, y1, label='Donations A', linestyle='--', marker='o', color='b')
plt.plot(x, y2, label='Donations B', linestyle='--', marker='s', color='g')
plt.plot(x, y3, label='Donations C', linestyle='--', marker='^', color='r')

# Setting up the title and labels
plt.title('Annual Donations to Charity Organizations in the US')
plt.xlabel('Year')
plt.ylabel('Donations (in USD)')

# Setting up xticks
plt.xticks(x)

# Setting up legend position
plt.legend(loc='upper left')

# Automatically resize image by tight_layout()
plt.tight_layout()

# Save figure as line chart/png/30.png
plt.savefig('line chart/png/30.png')

# Clear current image state
plt.clf()