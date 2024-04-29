

import matplotlib.pyplot as plt
import numpy as np

# Create figure and set figure size
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

# Set x and y axis data
x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
y1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
y2 = [3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750]

# Plot line chart
plt.plot(x, y1, color="blue", linewidth=2, linestyle="-", label="Number of Employees")
plt.plot(x, y2, color="green", linewidth=2, linestyle="-", label="Average Salary(dollars)")

# Set x and y axis labels
plt.xlabel('Month')
plt.ylabel('Employee Growth')

# Set x-axis ticks
plt.xticks(np.arange(len(x)), x)

# Set title
plt.title("Employee Growth and Salary Trend in 2021")

# Display legend
plt.legend(loc="upper left", bbox_to_anchor=(1,1))

# Annotate x, y axis value
for a,b,c in zip(x, y1, y2): 
    plt.annotate(str(b),xy=(a,b), rotation=90, va='bottom')
    plt.annotate(str(c),xy=(a,c), rotation=90, va='top')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/319.png')

# Clear the current image state
plt.clf()