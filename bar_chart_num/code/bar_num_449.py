
import matplotlib.pyplot as plt
import numpy as np

# Data
Country = ['USA', 'UK', 'Germany', 'France']
Hospitals = [3000, 4000, 3500, 4500]
Doctors = [20000, 25000, 22000, 27000]
Nurses = [30000, 40000, 35000, 45000]

# Create figure
fig = plt.figure()
ax = fig.add_subplot()

# Plot data
width = 0.3
ax.bar(Country, Hospitals, width, label='Hospitals', color='b')
ax.bar(Country, Doctors, width, bottom=Hospitals, label='Doctors', color='r')
ax.bar(Country, Nurses, width, bottom=[x + y for x, y in zip(Hospitals, Doctors)], label='Nurses', color='g')

# Legend
ax.legend(loc='upper left')

# Title
ax.set_title('Number of hospitals, doctors and nurses in four countries in 2021')

# Labels
def autolabel(rects):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(2, 2),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(ax.patches)

# Set x ticks
plt.xticks(Country, rotation=45, ha="right")

# Figure size
fig.set_size_inches(15, 10)

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/370.png')

# Clear current figure
plt.clf()