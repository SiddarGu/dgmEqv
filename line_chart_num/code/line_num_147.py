
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(20, 8))
ax1 = fig.add_subplot(1, 1, 1)

# Set data
x = np.array([2015, 2016, 2017, 2018])
y1 = np.array([20, 15, 17, 21])
y2 = np.array([18, 22, 19, 21])
y3 = np.array([25, 20, 22, 25])
y4 = np.array([30, 35, 30, 26])

# Plot data
ax1.plot(x, y1, color="blue", linewidth=2.5, linestyle="-", label="Donation A")
ax1.plot(x, y2, color="red", linewidth=2.5, linestyle="-", label="Donation B")
ax1.plot(x, y3, color="green", linewidth=2.5, linestyle="-", label="Donation C")
ax1.plot(x, y4, color="orange", linewidth=2.5, linestyle="-", label="Donation D")

# Set ticks
plt.xticks(x, fontsize=14)

# Set labels
ax1.set_xlabel('Year', fontsize=16)
ax1.set_ylabel('Donation (million dollars)', fontsize=16)

# Set title
ax1.set_title('Donations to four charities in the past four years', fontsize=20)

# Set grids
ax1.grid(linestyle='-.')

# Set legend
ax1.legend(loc='upper center', fontsize=16)

# Annotate
for a, b, c in zip(x, y1, y1):
    ax1.text(a, b + 0.1, '{:.1f}'.format(c), ha='center', va='bottom', fontsize=14)
for a, b, c in zip(x, y2, y2):
    ax1.text(a, b + 0.1, '{:.1f}'.format(c), ha='center', va='bottom', fontsize=14)
for a, b, c in zip(x, y3, y3):
    ax1.text(a, b + 0.1, '{:.1f}'.format(c), ha='center', va='bottom', fontsize=14)
for a, b, c in zip(x, y4, y4):
    ax1.text(a, b + 0.1, '{:.1f}'.format(c), ha='center', va='bottom', fontsize=14)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/420.png')

# Clear the current image state
plt.clf()