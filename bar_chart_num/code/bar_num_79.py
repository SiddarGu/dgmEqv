
import matplotlib.pyplot as plt
import numpy as np

# Generate data
data = np.array([[20000,40000,5000], [15000,30000,8000], [17000,25000,6000], [19000,35000,9000]])
x = np.arange(4)

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Plot the data
ax.bar(x, data[:,0], label='Restaurants', width=0.3, bottom=data[:,1]+data[:,2])
ax.bar(x, data[:,1], label='Cafes', width=0.3, bottom=data[:,2])
ax.bar(x, data[:,2], label='Bars', width=0.3)

# Set labels and title
ax.set_xticks(x)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'])
ax.set_ylabel('Number of restaurants, cafes, and bars')
ax.set_title('Number of restaurants, cafes, and bars in four countries in 2021')
ax.legend(loc='upper left')

# Place the value of each data point on the figure
for i, v in enumerate(data):
    ax.text(i-0.1, v[2]/2, str(v[2]), color='white', fontweight='bold')
    ax.text(i-0.1, v[2]+v[1]/2, str(v[1]), color='white', fontweight='bold')
    ax.text(i-0.1, v[2]+v[1]+v[0]/2, str(v[0]), color='white', fontweight='bold')

# Automatically resize the image
fig.tight_layout()

# Save image
plt.savefig('Bar Chart/png/506.png')

# Clear the current image state
plt.clf()