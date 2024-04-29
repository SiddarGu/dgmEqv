
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(14,8))
ax = plt.subplot()

# Set the data
year = [2017,2018,2019,2020,2021]
satellites = [20,25,30,35,40]
rockets = [10,15,20,25,30]

# Plot the line chart
ax.plot(year, satellites, color = '#6BD6F2', label = 'Number of Satellites', marker = 'o')
ax.plot(year, rockets, color = '#F0F2F7', label = 'Number of Rockets', marker = 'o')

# Add the legend
ax.legend(loc = 'upper left')

# Add the title
ax.set_title('Increase in the number of satellites and rockets launched in the past five years')

# Set the x-axis and y-axis
ax.set_xticks(year)
ax.set_ylim(0,45)

# Add the label for each data point
for i, txt in enumerate(satellites):
    ax.annotate(txt, (year[i], satellites[i]), fontsize=12, rotation=45, ha='right')
for i, txt in enumerate(rockets):
    ax.annotate(txt, (year[i], rockets[i]), fontsize=12, rotation=45, ha='right')

# Automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/21.png')

# Clear the current image state
plt.clf()