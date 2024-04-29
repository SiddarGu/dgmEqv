
import matplotlib.pyplot as plt
import numpy as np

data = {'Country': ['USA', 'UK', 'Germany', 'France'],
        'Manufacturing Output(million)': [1000, 1500, 1200, 1300],
        'Agriculture Output(million)': [200, 250, 300, 350]}

# Create figure
fig = plt.figure(figsize=(10, 5))

# Create bar plot
ax = fig.add_subplot(111)
ax.bar(data['Country'], data['Manufacturing Output(million)'], width=0.3, color='b', label='Manufacturing Output')
ax.bar(data['Country'], data['Agriculture Output(million)'], width=0.3, bottom=data['Manufacturing Output(million)'], color='g', label='Agriculture Output')

# Set axis labels, title and legend
ax.set_xlabel('Country')
ax.set_ylabel('Output(million)')
ax.set_title('Manufacturing and Agriculture Output in four countries in 2021')
ax.legend(loc='best')

# Set gridlines
ax.grid(linestyle='--')

# Set xticks
ax.set_xticks(np.arange(len(data['Country'])) + 0.3/2)
ax.set_xticklabels(data['Country'], rotation=90)

# Automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/204.png')

# Clear current image
plt.clf()