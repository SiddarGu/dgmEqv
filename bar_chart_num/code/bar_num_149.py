
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Set figure properties
labels = ['Road', 'Air', 'Sea']
costs = [300, 500, 400]
times = [10, 4, 20]

x = np.arange(len(labels))
width = 0.25

ax.bar(x-width, costs, width=width, color='#EE3224', label='Cost')
ax.bar(x, times, width=width, color='#F78F1E', label='Time')

ax.set_title('Cost and time for transportation by road, air and sea in 2021')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='upper center')

# Annotate the value of data points
for i, v in enumerate(costs):
    ax.text(i - width/2, v + 10, str(v), fontsize=9)
for i, v in enumerate(times):
    ax.text(i + width/2, v + 10, str(v), fontsize=9)

fig.tight_layout()
plt.savefig('Bar Chart/png/311.png')
plt.clf()