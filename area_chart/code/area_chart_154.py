
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Convert data to dictionary
data_dict = {
    'Category': ['Theoretical', 'Experimental', 'Applied', 'Environmental', 'Materials', 'Robotics', 'Genetics', 'Nanotechnology', 'Aerospace', 'Biotechnology', 'Nuclear', 'Chemical', 'Marine', 'Electrical'],
    'Physics': [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340],
    'Chemistry': [60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320],
    'Biology': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750],
    'Geology': [40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],
    'Computer Science': [120, 100, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
}

# Create dataframe and convert first column to string type
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value and set ylimit and yticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10)*10
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(linestyle='dashed', color='gray', alpha=0.5)

# Plot data as stackplot
ax.stackplot(df['Category'], df['Physics'], df['Chemistry'], df['Biology'], df['Geology'], df['Computer Science'], labels=['Physics', 'Chemistry', 'Biology', 'Geology', 'Computer Science'])
plt.xticks(rotation=90, ha='right', rotation_mode='anchor')
# Set legend position and title
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
ax.set_title('Science and Engineering Categories and Applications')

# Automatically resize image before savefig()
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-140159_71.png', bbox_inches='tight')

# Clear current image state
plt.clf()