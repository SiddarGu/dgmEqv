
import matplotlib.pyplot as plt
import numpy as np

data = [[18, 90, 50, 80], [21, 80, 60, 90], [26, 70, 65, 75], [31, 60, 70, 80], [36, 50, 75, 85]]

# Create figure
fig = plt.figure(figsize=(14, 8))

# Add subplot
ax = fig.add_subplot(111)

# Set Title
ax.set_title('Interest in Arts among different age groups')

# Set labels
ax.set_xlabel('Age')
ax.set_ylabel('Interest in Arts')

# Set data
x_data = np.array([i[0] for i in data])
y1_data = np.array([i[1] for i in data])
y2_data = np.array([i[2] for i in data])
y3_data = np.array([i[3] for i in data])

# Plot data
ax.plot(x_data, y1_data, label='Interest in Music')
ax.plot(x_data, y2_data, label='Interest in Theater')
ax.plot(x_data, y3_data, label='Interest in Movies')

# Set ticks
ax.set_xticks(x_data)

# Set legend
ax.legend()

# Resize image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/16.png')

# Clear current image state
plt.clf()