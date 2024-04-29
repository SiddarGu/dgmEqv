
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Data
organization = np.array(['Red Cross', 'UNICEF', 'World Food Programme', 'Oxfam'])
donations = np.array([1200, 1100, 1000, 900])
volunteers = np.array([300, 400, 250, 200])

# Bar plot
ax.bar(organization, donations, label='Donations (thousand)', color='#539caf')
ax.bar(organization, volunteers, bottom=donations, label='Volunteers', color='#7663b0')

# Set title and labels
ax.set_title('Contributions and volunteers to four major charities in 2021', fontsize=14, fontweight='bold')
ax.set_xlabel('Organization', fontsize=11, fontweight='bold')
ax.set_ylabel('Amount', fontsize=11, fontweight='bold')

# Set ticks
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
ax.yaxis.set_tick_params(labelsize=10)

# Set legend
ax.legend(loc='upper right', fontsize='x-large')

# Adjust gap
plt.tight_layout()

# Save graph
plt.savefig('bar chart/png/387.png')

# Clear current figure
plt.clf()