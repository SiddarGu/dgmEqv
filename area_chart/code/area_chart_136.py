
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Data in the form of a dictionary
data = {'Category':['IT', 'Marketing', 'Finance', 'Education', 'Healthcare', 'Science', 'Business', 'Government', 'E-commerce', 'Gaming', 'Mobile', 'Retail', 'Telecommunications', 'Automotive'],
        'Recruitment (Employees)':[150, 100, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120, 100],
        'Training (Employees)':[180, 120, 180, 200, 180, 200, 150, 100, 130, 100, 200, 180, 150, 200],
        'Compensation (Employees)':[200, 150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 130, 200, 250],
        'Performance (Employees)':[100, 100, 150, 180, 130, 250, 200, 180, 200, 180, 100, 200, 170, 150],
        'Benefits (Employees)':[120, 200, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 130, 180]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with an area chart
fig, ax = plt.subplots(figsize=(12,8))
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=['Recruitment', 'Training', 'Compensation', 'Performance', 'Benefits'], colors=['#FDB813', '#00A6E0', '#EF3E2E', '#8D6A9F', '#5CBDBD'], alpha=0.8)

# Set x ticks and tick labels
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Set y ticks and tick labels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10) * 10
y_ticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)

# Set grid lines
ax.grid(linestyle='dashed', color='#D3D3D3')

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Set title
plt.title('Employee Distribution by Department')

# Automatically resize the image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_5.png', bbox_inches='tight')

# Clear current image state
plt.clf()