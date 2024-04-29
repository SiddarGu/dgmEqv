
import matplotlib.pyplot as plt
import numpy as np

#data
data = np.array([[2015, 500000, 3000000], 
                 [2016, 550000, 3200000],
                 [2017, 600000, 3500000],
                 [2018, 650000, 3700000],
                 [2019, 700000, 4000000]])

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Plot data
ax.plot(data[:, 0], data[:, 1], label='Number of Criminal Cases')
ax.plot(data[:, 0], data[:, 2], label='Number of Civil Cases')

# Set ticks
ax.set_xticks(data[:, 0])

# Other settings
ax.set_title("Trend of Criminal and Civil Cases in the US Courts from 2015 to 2019")
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('line chart/png/476.png')
plt.clf()