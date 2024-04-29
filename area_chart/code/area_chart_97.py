
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent data using dictionary
data = {'Category': ['Technology', 'Internet', 'Mobile', 'Cloud Computing', 'E-commerce', 'Artificial Intelligence', 'Internet of Things', 'Big Data', 'Social Networking', 'Cybersecurity', 'Digital Marketing', 'Virtual Reality', 'Augmented Reality', 'Blockchain'], 'Web Development (Users)': [250, 200, 180, 150, 130, 100, 200, 150, 180, 120, 100, 150, 130, 200], 'Data Science (Users)': [180, 150, 200, 180, 100, 200, 180, 200, 150, 100, 200, 180, 100, 180], 'Cybersecurity (Users)': [200, 180, 150, 130, 150, 250, 150, 100, 100, 200, 250, 130, 150, 150], 'Artificial Intelligence (Users)': [150, 130, 100, 200, 180, 150, 130, 250, 200, 180, 250, 200, 150, 130], 'Social Media (Users)': [300, 250, 250, 170, 200, 180, 100, 120, 170, 150, 180, 170, 200, 100]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10,5))

# Use ax.stackplot()
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Web Development', 'Data Science', 'Cybersecurity', 'Artificial Intelligence', 'Social Media'], colors=['#FFA500', '#FFD700', '#FFA07A', '#87CEEB', '#FFC0CB'], alpha=0.8)

# Set x and y axis ticks and ticklabels
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Number of Users')

# Set title
ax.set_title('User Distribution in Technology and the Internet Industry')

# Set background grid lines
ax.grid(color='grey', linestyle='--', linewidth=0.5)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-131755_87.png', bbox_inches='tight')

# Clear current image state
plt.clf()