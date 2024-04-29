
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize = (12, 8))

# Plot line chart
plt.plot(np.arange(2020, 2025, 1), [100, 200, 300, 400, 500], label='Laser Power(Watts)')
plt.plot(np.arange(2020, 2025, 1), [30, 45, 60, 75, 90], label='Experiment Duration(minutes)')

# Add legend
plt.legend()

# Set title
plt.title('Evolution of laser power used in scientific experiments from 2020 to 2024')

# Prevent interpolation
plt.xticks(np.arange(2020, 2025, 1))

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/293.png')

# Clear the current image state
plt.clf()