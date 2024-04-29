
import matplotlib.pyplot as plt
import numpy as np

# Data
Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
Air_Travelers = np.array([25, 30, 35, 40, 45, 50, 55])
Rail_Travelers = np.array([20, 25, 30, 35, 40, 45, 50])

# Create figure
fig = plt.figure(figsize=(8,5))

# Plot line chart
ax = fig.add_subplot()
ax.plot(Month, Air_Travelers, '-o', color='red', label='Air Travelers (millions)')
ax.plot(Month, Rail_Travelers, '-o', color='blue', label='Rail Travelers (millions)')

# Set xticks
plt.xticks(Month, rotation=45)

# Set title
ax.set_title('Comparing Air and Rail Travelers in the US during 2020')

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/385.png')

# Clear figure
plt.clf()