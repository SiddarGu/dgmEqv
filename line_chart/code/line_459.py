
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create figure
fig = plt.figure(figsize=(10, 5))

# Plot the data
ax = fig.add_subplot(1,1,1)
ax.plot(['April','May','June','July','August','September','October'], [100,150,200,250,300,350,400], label='Hotel A', marker='o')
ax.plot(['April','May','June','July','August','September','October'], [150,200,250,300,350,400,450], label='Hotel B', marker='o')
ax.plot(['April','May','June','July','August','September','October'], [200,250,300,350,400,450,500], label='Hotel C', marker='o')

# Set x-axis ticks
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

# Add labels
ax.set_xlabel('Month')
ax.set_ylabel('Bookings')
ax.set_title('Hotel bookings in three locations in 2021')

# Add legend
plt.legend(loc='best')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/143.png')

# Clear the image state
plt.cla()