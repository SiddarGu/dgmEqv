
import matplotlib.pyplot as plt
import numpy as np

# Set up the data
year = np.array(['2001', '2002', '2003', '2004'])
criminal_cases = np.array([20000, 19000, 18000, 17000])
civil_cases = np.array([15000, 16000, 17000, 18000])
family_cases = np.array([2500, 3000, 3500, 4000])

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot the data
ax.plot(year, criminal_cases, '-o', label='Criminal Cases')
ax.plot(year, civil_cases, '-o', label='Civil Cases')
ax.plot(year, family_cases, '-o', label='Family Cases')

# Add xticks
plt.xticks(year)

# Add labels to data points
for x, y in zip(year, criminal_cases):
    ax.annotate(y, xy=(x, y), xytext=(0, 5), textcoords='offset points')
for x, y in zip(year, civil_cases):
    ax.annotate(y, xy=(x, y), xytext=(0, 5), textcoords='offset points')
for x, y in zip(year, family_cases):
    ax.annotate(y, xy=(x, y), xytext=(0, 5), textcoords='offset points')

# Add legend
plt.legend(loc='best')

# Add title
plt.title('Number of cases filed in US Courts annually from 2001 to 2004')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/545.png')

# Clear the current image state
plt.clf()