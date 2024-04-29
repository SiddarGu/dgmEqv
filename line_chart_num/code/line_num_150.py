
import matplotlib.pyplot as plt
import numpy as np

# Create data
Year = [2011, 2012, 2013, 2014, 2015]
Smartphone_sales = [100, 140, 120, 160, 200]
Tablet_sales = [20, 50, 60, 70, 90]
Computer_sales = [150, 110, 120, 90, 70]

# Create figure
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()

# Plot graph
plt.plot(Year, Smartphone_sales, label="Smartphone sales")
plt.plot(Year, Tablet_sales, label="Tablet sales")
plt.plot(Year, Computer_sales, label="Computer sales")

# Set x-axis
plt.xticks(Year, Year, rotation=45)

# Labeling the points
for i, txt in enumerate(Smartphone_sales):
    ax.annotate(txt, (Year[i], Smartphone_sales[i]))
for i, txt in enumerate(Tablet_sales):
    ax.annotate(txt, (Year[i], Tablet_sales[i]))
for i, txt in enumerate(Computer_sales):
    ax.annotate(txt, (Year[i], Computer_sales[i]))

# Set legend
plt.legend(loc='upper right')

# Set title
plt.title("Global Technology Device Sales from 2011 to 2015")

# Resize the image by tight_layout()
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/483.png")

# Clear figure
plt.clf()