
import numpy as np
import matplotlib.pyplot as plt

# Create figure before plotting
fig = plt.figure(figsize=(10,10))

# Data
data_labels = ['Excellence', 'Language Fluency', 'Financial Support', 'Resillience', 'Friendliness']
data_susan = [6.92, 7.45, 5.92, 6.12, 4.76]
data_bob = [4.20, 3.89, 3.21, 4.37, 4.18]
data_symbol = [5.56, 7.43, 8.25, 9.87, 9.52]
data = np.array([data_susan, data_bob, data_symbol])
# Set angles as np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array and append the first element of that row to its end
data_susan = np.concatenate((data_susan, [data_susan[0]]))
data_bob = np.concatenate((data_bob, [data_bob[0]]))
data_symbol = np.concatenate((data_symbol, [data_symbol[0]]))

# Plot
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data_susan, 'o-', label="Susan")
ax.plot(angles, data_bob, 'o-', label="Bob")
ax.plot(angles, data_symbol, 'o-', label="Symbol")

# Plot axis label by using set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust the radial limits to accommodate the maximum of data
ax.set_rlim(0, 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Draw the line legend
ax.legend(loc='upper right', bbox_to_anchor=(1, 1))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Prevent interpolation
plt.xticks(angles[:-1], data_labels, fontsize=20)

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/9813.png')

# Clear the current image state
plt.clf()