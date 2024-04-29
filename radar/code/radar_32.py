

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Responsibility', 'Career Development', 'Work-Life Balance', 'Leadership', 'Communication']
data_susan = [6.93, 8.11, 5.45, 7.45, 7.14]
data_bob = [4.21, 4.04, 4.97, 4.93, 4.77]
data_symbol = [7.45, 9.63, 7.11, 8.54, 9.03]

# Create figure before plotting
fig = plt.figure(figsize=(9, 9))

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array and append the first element of that row to its end
data_susan = np.concatenate((data_susan, [data_susan[0]]))
data_bob = np.concatenate((data_bob, [data_bob[0]]))
data_symbol = np.concatenate((data_symbol, [data_symbol[0]]))

# Plot the axis label
ax = plt.subplot(111, polar=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)

# Adjust the radial limits to accommodate the maximum of data
ax.set_rlim(-0.5, 10.0)

# Plotting data
ax.plot(angles, data_susan, linewidth=2, linestyle='dashed', label='Susan')
ax.plot(angles, data_bob, linewidth=2, linestyle='dashed', label='Bob')
ax.plot(angles, data_symbol, linewidth=2, linestyle='solid', label='Symbol')

# Plotting legend
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Resize the image
plt.tight_layout()

# Set xticks to prevent interpolation
plt.xticks(angles[:-1], data_labels)

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/StructChart/simulated_data_corner_cases/radar/png/multi_col_80042.png', dpi=200)

# Clear the current image state
plt.clf()