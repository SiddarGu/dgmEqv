

import matplotlib.pyplot as plt
import numpy as np

# Set the title and labels
plt.title('Changes in Voter Participation and Satisfaction in the US from 2020-2023')
plt.xlabel('Year')
plt.ylabel('Percentages (%)')

# Set the data
data = np.array([[2020, 80, 82, 75, 20],
                 [2021, 82, 85, 77, 22],
                 [2022, 85, 87, 80, 25],
                 [2023, 88, 90, 83, 28]])

# Set the xticks
plt.xticks(data[:, 0])

# Plot the line chart
plt.plot(data[:, 0], data[:, 1], label='Voter Turnout')
plt.plot(data[:, 0], data[:, 2], label='Voter Registration')
plt.plot(data[:, 0], data[:, 3], label='Voter Satisfaction')
plt.plot(data[:, 0], data[:, 4], label='Voter Apathy')

# Set the legend
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 0.95))

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/360.png')

# Clear the current image state
plt.clf()