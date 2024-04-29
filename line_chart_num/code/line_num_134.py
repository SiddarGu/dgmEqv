
import matplotlib.pyplot as plt

# Create figure and add subplot
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(111)

# Set x axis 
x = ['2020', '2021', '2022', '2023']

# Set y axis 
y_1 = [1000, 1200, 1300, 1400]
y_2 = [650, 800, 900, 700]
y_3 = [50, 55, 60, 65]

# Plot data
ax.plot(x, y_1, color='b', marker='o', linestyle='-', label='Domestic Tourism')
ax.plot(x, y_2, color='r', marker='*', linestyle='--', label='International Tourism')
ax.plot(x, y_3, color='g', marker='s', linestyle=':', label='Hotel Occupancy Rate')

# Set xticks
ax.set_xticks(x)

# Set x and y labels
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of People (million) / Occupancy Rate (%)', fontsize=14)

# Label the value of each data point directly on the figure
for i,j in zip(x, y_1):
    ax.annotate(j, xy=(i,j), fontsize=14)
for i,j in zip(x, y_2):
    ax.annotate(j, xy=(i,j), fontsize=14)
for i,j in zip(x, y_3):
    ax.annotate(j, xy=(i,j), fontsize=14)

# Set the title of the figure
plt.title('Global Tourism and Hotel Occupancy Rates from 2020 to 2023', fontsize=14)

# Set the position of the legend
ax.legend(loc='upper right', fontsize=14)

# Automatically resize the image by tight_layout
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/385.png')

# Clear the current image state
plt.clf()