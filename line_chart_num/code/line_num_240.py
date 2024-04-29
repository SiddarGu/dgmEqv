
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()

# Set data
year = np.array([2001,2002,2003,2004,2005,2006,2007])
donations = np.array([200,150,180,220,190,210,220])
volunteers = np.array([500,400,450,500,420,480,510])

# Plot line chart
plt.plot(year, donations, color='b', linestyle='-', marker='o',label='Donations (million dollars)')
plt.plot(year, volunteers, color='r', linestyle='-', marker='o',label='Volunteers')

# Set title, legend, x/y ticks, labels
plt.title('Growth in charity donations and volunteers for non-profit organizations', fontsize=14)
plt.legend(loc='upper right', fontsize=11)
plt.xticks(year, fontsize=11, rotation=90)
plt.yticks(fontsize=11)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Amount', fontsize=12)

# Annotate value of each data point
for x, y1, y2 in zip(year, donations, volunteers):
    plt.annotate(f'{y1}m', xy=(x, y1), xytext=(x-0.2, y1+2), fontsize=10)
    plt.annotate(f'{y2}', xy=(x, y2), xytext=(x+0.2, y2+2), fontsize=10)

# Set background grids
plt.grid(linestyle = '-.')

# Adjust image by tight_layout()
plt.tight_layout()

# Save and close image
plt.savefig('line chart/png/203.png')
plt.clf()