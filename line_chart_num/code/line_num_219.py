
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Data
Month=['January', 'February', 'March', 'April']
Production_A = [10000, 11000, 8000, 13000]
Production_B = [8000, 9000, 10000, 12000]
Production_C = [15000, 14000, 13000, 14500]
Production_D = [20000, 18000, 19000, 16000]

# Plot line chart
ax.plot(Month, Production_A, label='Production A')
ax.plot(Month, Production_B, label='Production B')
ax.plot(Month, Production_C, label='Production C')
ax.plot(Month, Production_D, label='Production D')

# Set the x-axis and y-axis limits
ax.set_xlim(0, 4)
ax.set_ylim(0, 22000)

# Set title and legend
ax.set_title('Production output of four products in the first four months of 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          ncol=4, shadow=True, fontsize='x-large')

# Set the xticks
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(Month)

# Label the value of each data point directly on the figure
for a, b in zip(Month, Production_A):
    ax.annotate(str(b), xy=(a, b), xytext=(0, -10),
                textcoords='offset points', ha='center')
for a, b in zip(Month, Production_B):
    ax.annotate(str(b), xy=(a, b), xytext=(0, -10),
                textcoords='offset points', ha='center')
for a, b in zip(Month, Production_C):
    ax.annotate(str(b), xy=(a, b), xytext=(0, -10),
                textcoords='offset points', ha='center')
for a, b in zip(Month, Production_D):
    ax.annotate(str(b), xy=(a, b), xytext=(0, -10),
                textcoords='offset points', ha='center')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/80.png')

# Clear the current image state
plt.clf()