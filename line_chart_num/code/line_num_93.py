
import matplotlib.pyplot as plt
import numpy as np

# Set data
Month = np.array(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
Online_Sales = np.array([1000, 1100, 1300, 1200, 1500, 1400, 1300, 1200, 1100, 1400, 1200, 1500])
Offline_Sales = np.array([1200, 1400, 1600, 1800, 1700, 1600, 1500, 1400, 1600, 1800, 1700, 1600])

# Create a figure
plt.figure(figsize=(14, 7))

# Draw a line chart
plt.plot(Month, Online_Sales, label="Online Sales", linestyle="-.", marker="o")
plt.plot(Month, Offline_Sales, label="Offline Sales", linestyle="--", marker="x")

# Add a legend
plt.legend(loc="best")

# Add a title
plt.title("Annual Sales Trend in Retail and E-commerce Industry")

# Add x labels
plt.xlabel("Month")

# Add y labels
plt.ylabel("Sales (million dollars)")

# Add a grid
plt.grid(True)

# Label every point
for x, y1, y2 in zip(Month, Online_Sales, Offline_Sales):
    plt.annotate('%d\n%d' % (y1, y2), xy=(x, y1), xytext=(0, 5), textcoords="offset points", ha="center", va="bottom")

# Set x ticks
plt.xticks(Month, rotation=45)

# Automatically resize the image
plt.tight_layout()

# Save and show the figure
plt.savefig("line chart/png/71.png")
plt.show()

# Clear the current image state
plt.clf()