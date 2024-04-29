
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,5))

# Get the data
data = np.array([[2.5,1.8],[2.1,1.4],[1.9,1.2],[2.3,1.6]])
countries = np.array(['USA','UK','Germany', 'France'])

# Plot the bar chart
ax = fig.add_subplot(111)
width = 0.3
ind = np.arange(data.shape[0])
ax.bar(ind, data[:,0], width, color='b', label='Cases registered')
ax.bar(ind + width, data[:,1], width, color='r', label='Cases closed')
ax.set_title('Cases registered and closed in four countries in 2021')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(countries, fontsize=8)
ax.legend(loc='best')

# Label each bar
for i in range(len(ind)):
    ax.annotate('{:.1f}'.format(data[i,0]), (ind[i], data[i,0]), xytext=(0,5), textcoords='offset points', ha='center', va='bottom', fontsize=8)
    ax.annotate('{:.1f}'.format(data[i,1]), (ind[i]+width, data[i,1]), xytext=(0,5), textcoords='offset points', ha='center', va='bottom', fontsize=8)

# Adjust the figure
fig.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/373.png')

# Clear the current image state
plt.clf()