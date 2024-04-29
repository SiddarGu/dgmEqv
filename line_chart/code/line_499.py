

import matplotlib.pyplot as plt
import pandas as pd

# Set figure size
plt.figure(figsize=(10,5))

# Read data
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Online Sales(billion dollars)': [500, 550, 600, 650, 700, 720, 750, 800, 850, 900, 950, 1000],
    'In-store Sales(billion dollars)': [1000, 1100, 900, 800, 1200, 1100, 1000, 900, 800, 1100, 1000, 1100]}

# Create dataframe
df = pd.DataFrame(data)

# Plot
ax = plt.subplot()
ax.plot(df['Month'], df['Online Sales(billion dollars)'], label = 'Online Sales')
ax.plot(df['Month'], df['In-store Sales(billion dollars)'], label = 'In-store Sales')

# Set xticks and rotate them
plt.xticks(rotation=45)

# Set title, legend and grid
plt.title('Comparison of Online and In-store Sales in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
    fancybox=True, shadow=True, ncol=2)
ax.grid(True)

# Set padding
plt.tight_layout()

# Save image
plt.savefig('line chart/png/556.png')

# Clear figure
plt.clf()