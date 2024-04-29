

import matplotlib.pyplot as plt
import numpy as np

# Generate data
country = np.array(['USA', 'UK', 'Germany', 'France'])
theater = np.array([200, 180, 160, 180])
dance = np.array([150, 130, 120, 140])
concert = np.array([250, 220, 200, 240])

# Generate figure
plt.figure(figsize=(8, 6), dpi=80)

# Generate plot
ax = plt.subplot()
ax.bar(country, theater, bottom=dance+concert, width=0.4, label='Theater')
ax.bar(country, dance, bottom=concert, width=0.4, label='Dance')
ax.bar(country, concert, width=0.4, label='Concerts')

# Add labels
for x, y in zip(country, theater):
    ax.text(x, y + 5, '%d' % y, ha='center', va='bottom')
for x, y in zip(country, dance):
    ax.text(x, y + 5, '%d' % y, ha='center', va='bottom')
for x, y in zip(country, concert):
    ax.text(x, y + 5, '%d' % y, ha='center', va='bottom')

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title
ax.set_title("Number of performances in theater, dance, and concerts in four countries in 2021")

# Set x ticks
plt.xticks(country)

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/25.png')

# Clear the figure
plt.clf()