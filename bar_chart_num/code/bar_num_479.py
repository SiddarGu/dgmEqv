
import matplotlib.pyplot as plt
import numpy as np

# Setting the figsize
plt.figure(figsize=(10, 7))

# Define data
labels = ['January', 'February', 'March', 'April']
machinesUsed = [100, 110, 120, 130]
prodA = [1000, 900, 1100, 800]
prodB = [1200, 1300, 1400, 1500]
prodC = [800, 1100, 1200, 1400]

# Create a bar plot with each data
x = np.arange(len(labels))  # the label locations
width = 0.2  # width of the bars

# Plot each data
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, machinesUsed, width, label='Machines used')
rects2 = ax.bar(x, prodA, width, label='Production A')
rects3 = ax.bar(x + width, prodB, width, label='Production B')
rects4 = ax.bar(x + 2*width, prodC, width, label='Production C')

# Set labels
ax.set_ylabel('Quantity')
ax.set_title('Machine usage and production output from January to April 2021')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='upper left')

# Automatically resize the image
fig.tight_layout()

# Annotate value of each data point
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

# Save the figure
plt.savefig('Bar Chart/png/567.png')

# Clear the current image state
plt.clf()