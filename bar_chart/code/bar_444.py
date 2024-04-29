
import matplotlib.pyplot as plt
import numpy as np

# Create data
Year = np.array([2016, 2017, 2018, 2019])
Engineering_Graduates = np.array([90, 100, 110, 120])
Science_Graduates = np.array([70, 80, 90, 100])

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Plotting data
ax.bar(Year-0.2, Engineering_Graduates, width=0.4, label='Engineering Graduates')
ax.bar(Year+0.2, Science_Graduates, width=0.4, label='Science Graduates', bottom=Engineering_Graduates)

# Set title
ax.set_title('Number of Engineering and Science Graduates in four consecutive years')

# Set legend
ax.legend()

# Set labels
ax.set_xlabel('Year')
ax.set_ylabel('Number (thousand)')

# Set yticks
ax.set_yticks([20, 40, 60, 80, 100, 120])

# Set xticks
ax.set_xticks(Year)

# Make sure the plot is shown correctly
plt.tight_layout()

# Save as png
plt.savefig('bar chart/png/373.png')

# Clear current state
plt.clf()