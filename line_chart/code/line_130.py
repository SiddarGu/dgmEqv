
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))

# Set data
month = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
online_shopping = np.array([250,280,310,320,340,360,380,400,420,440,460,480])
in_store_shopping = np.array([320,340,370,400,420,440,460,480,500,520,540,560])

# Plot the data and set the position of the legend
ax = fig.add_subplot(111)
plt.plot(month,online_shopping,color='blue',label='Online Shopping',marker='o')
plt.plot(month,in_store_shopping,color='red',label='In-Store Shopping',marker='o')
ax.legend(loc='upper left')

# Set x ticks to avoid interpolation
xticks = np.arange(0,12,1)
plt.xticks(xticks, month, rotation='vertical')

# Set title of the figure
plt.title("Comparison of online and in-store shopping in 2020")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/541.png')

# Clear the current image state
plt.clf()