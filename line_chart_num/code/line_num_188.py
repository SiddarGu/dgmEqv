
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(12, 8))

# Add subplot
ax = fig.add_subplot(111)

# Data
Year = [2000, 2001, 2002, 2003, 2004]
Wheat_Yield = [5000, 6000, 7000, 8000, 9000]
Corn_Yield = [4000, 5000, 6000, 7000, 8000]
Rice_Yield = [2000, 3000, 4000, 5000, 6000]

# Plot line chart
p1, = ax.plot(Year, Wheat_Yield, label="Wheat Yield (Metric Tons)")
p2, = ax.plot(Year, Corn_Yield, label="Corn Yield (Metric Tons)")
p3, = ax.plot(Year, Rice_Yield, label="Rice Yield (Metric Tons)")

# Annotate for each data point
for x, y in zip(Year, Wheat_Yield):
    ax.annotate(y, xy=(x,y), xytext=(-10, 10), textcoords='offset points')
for x, y in zip(Year, Corn_Yield):
    ax.annotate(y, xy=(x,y), xytext=(-10, 10), textcoords='offset points')
for x, y in zip(Year, Rice_Yield):
    ax.annotate(y, xy=(x,y), xytext=(-10, 10), textcoords='offset points')

# Draw background grids
ax.grid(True, linewidth=1, color='#aaaaaa', linestyle='--')

# Set legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1), framealpha=0.3)

# Set x ticks
ax.set_xticks(Year)

# Set title
ax.set_title("Crop Yield of Major Grains in the US from 2000 to 2004")

# Resize image
plt.tight_layout()

# Save image
fig.savefig('line chart/png/83.png')

# Clear current image state
plt.clf()