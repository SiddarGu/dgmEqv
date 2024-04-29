
import matplotlib.pyplot as plt
import numpy as np

# Data
Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Wheat_Production = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
Rice_Production = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850]
Corn_Production = [400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]

# Plot
fig = plt.figure(figsize=(10,7))
plt.plot(Month, Wheat_Production, color='green', linestyle='solid', marker='o', label='Wheat Production')
plt.plot(Month, Rice_Production, color='red', linestyle='solid', marker='o', label='Rice Production')
plt.plot(Month, Corn_Production, color='blue', linestyle='solid', marker='o', label='Corn Production')

# Title
plt.title('Crop Production in 2020 in the US')

# Grid
plt.grid(True, color='k', linestyle='-.', linewidth=0.5)

# Annotate
for x,y in zip(Month, Wheat_Production):
    plt.annotate(y,xy=(x,y))
for x,y in zip(Month, Rice_Production):
    plt.annotate(y,xy=(x,y))
for x,y in zip(Month, Corn_Production):
    plt.annotate(y,xy=(x,y))

# X Ticks
plt.xticks(Month, rotation=45, wrap=True)

# Legend
plt.legend(loc='upper left')

# Tight Layout
plt.tight_layout()

# Save
plt.savefig('line chart/png/98.png')

# Clear
plt.clf()