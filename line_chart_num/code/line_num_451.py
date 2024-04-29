
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))

# Set X,Y axis
x= np.arange(2017, 2022)
y1 = [200, 250, 280, 300, 320]
y2 = [40, 60, 80, 100, 110]
y3 = [240, 310, 360, 400, 430]

# plot
plt.plot(x, y1, label='Offline Store Revenue', marker='o', color='#2A91F2')
plt.plot(x, y2, label='Online Store Revenue', marker='o', color='#FF8C00')
plt.plot(x, y3, label='Total Revenue', marker='o', color='#5A99F3')

# Set X,Y axis label and title
plt.xlabel('Year', fontsize=13)
plt.ylabel('Revenue (million dollars)', fontsize=13)
plt.title("Revenue growth of online and offline stores in the retail industry", fontsize=15)

# Set xticks
plt.xticks(x, x, rotation=45)

# Set legend
plt.legend(loc=2, bbox_to_anchor=(1.05, 1), borderaxespad=0)

# Set grid
plt.grid(linestyle='--', color='#e0e0e0')

# Set annotation
plt.annotate('320', xy=(2021, 320), xytext=(2021.2, 325), fontsize=12, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))
plt.annotate('40', xy=(2017, 40), xytext=(2016.8, 45), fontsize=12, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))
plt.annotate('430', xy=(2021, 430), xytext=(2021.2, 435), fontsize=12, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))

# Adjust the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/308.png')
plt.show()

# Clear the current image state
plt.clf()