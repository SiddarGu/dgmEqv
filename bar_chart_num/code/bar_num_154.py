

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(10,8))

# Data
countries = ['USA', 'UK', 'Germany', 'France']
roads = [45000, 43000, 41000, 39000]
railways = [30000, 31000, 32000, 33000]
airports = [1000, 1200, 1100, 1300]

# Bar chart
x = np.arange(len(countries))  # the label locations
width = 0.2 # width of the bars

ax.bar(x - width, roads, width, label='Roads (km)')
ax.bar(x, railways, width, label='Railways (km)')
ax.bar(x + width, airports, width, label='Airports')

# Labels
ax.set_ylabel('Number of km')
ax.set_title('Transportation Infrastructure in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.legend()

# Show value
for i in range(len(countries)):
    ax.annotate('%s' % roads[i], xy=(x[i] - width, roads[i]+500), xytext=(0, -20), 
                textcoords="offset points", ha='center', va='bottom', rotation=90)
    ax.annotate('%s' % railways[i], xy=(x[i], railways[i]+500), xytext=(0, -20), 
                textcoords="offset points", ha='center', va='bottom', rotation=90)
    ax.annotate('%s' % airports[i], xy=(x[i] + width, airports[i] + 500), xytext=(0, -20), 
                textcoords="offset points", ha='center', va='bottom', rotation=90)

# Adjust padding
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/415.png')

# Clear current state
plt.clf()