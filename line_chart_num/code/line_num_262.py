
import matplotlib.pyplot as plt
import numpy as np

# Set figure size & title
plt.figure(figsize=(14,7))
plt.title('Renewable Energy Growth in the US from 2016 to 2020')

# Plot the data
x = np.arange(2016, 2021)
plt.plot(x, [80, 90, 100, 130, 180], label='Solar Energy(GW)')
plt.plot(x, [100, 120, 140, 150, 200], label='Wind Energy(GW)')
plt.plot(x, [150, 170, 190, 210, 250], label='Hydro Energy(GW)')

# Set x-axis
plt.xticks(x, x)

# Add legend
plt.legend(loc='best', fontsize=14)

# Annotate the data
for a, b, c, d in zip(x, [80, 90, 100, 130, 180], [100, 120, 140, 150, 200], [150, 170, 190, 210, 250]):
    plt.text(a, b+2, '%s' % b, ha='center', va='bottom', fontsize=12)
    plt.text(a, c+2, '%s' % c, ha='center', va='bottom', fontsize=12)
    plt.text(a, d+2, '%s' % d, ha='center', va='bottom', fontsize=12)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/258.png')

# Clear the current image state
plt.clf()