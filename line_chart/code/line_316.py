
import matplotlib.pyplot as plt
import numpy as np

# Set data 
year = np.array([2001, 2002, 2003, 2004])
music_album_sales = np.array([10, 15, 20, 25])
book_sales = np.array([20, 25, 30, 35])
painting_sales = np.array([15, 20, 25, 30])

# Create figure
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot()

# Plot data
ax.plot(year, music_album_sales, color='b', linestyle='--', label='Music Albums')
ax.plot(year, book_sales, color='g', linestyle='-.', label='Books')
ax.plot(year, painting_sales, color='r', linestyle=':', label='Paintings')

# Set x ticks
ax.set_xticks(year)

# Add legend
ax.legend(loc='upper left')

# Set title
plt.title("Annual Artwork Sales in USA from 2001 to 2004")

# Set tight_layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/388.png')

# Clear current figure
plt.clf()