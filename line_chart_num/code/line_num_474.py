
import matplotlib.pyplot as plt
import numpy as np

# Create figure and subplot, and set figsize
fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(1,1,1)

# Create data
data = np.array([[2001, 100, 200, 300, 400],
                 [2002, 120, 220, 320, 420],
                 [2003, 110, 210, 310, 410],
                 [2004, 130, 230, 330, 430]])

# Plot data
ax1.plot(data[:,0], data[:,1], 'r-', label = 'Production A(units)')
ax1.plot(data[:,0], data[:,2], 'b-', label = 'Production B(units)')
ax1.plot(data[:,0], data[:,3], 'g-', label = 'Production C(units)')
ax1.plot(data[:,0], data[:,4], 'y-', label = 'Production D(units)')

# Add annotation
for i in range(len(data[:,0])):
    ax1.annotate(str(data[i,1]), xy=(data[i,0], data[i,1]), xytext=(data[i,0], data[i,1]))
    ax1.annotate(str(data[i,2]), xy=(data[i,0], data[i,2]), xytext=(data[i,0], data[i,2]))
    ax1.annotate(str(data[i,3]), xy=(data[i,0], data[i,3]), xytext=(data[i,0], data[i,3]))
    ax1.annotate(str(data[i,4]), xy=(data[i,0], data[i,4]), xytext=(data[i,0], data[i,4]))

# Draw grid and legend
ax1.grid(True)
ax1.legend()

# Set xticks
plt.xticks(data[:,0])

# Set title
plt.title('Production of four items in a manufacturing plant')

# Adjust image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/79.png')

# Clear current image
plt.clf()