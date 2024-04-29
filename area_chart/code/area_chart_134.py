
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Department': ['HR', 'IT', 'Operations', 'Finance', 'Marketing', 'Research & Development', 'Sales', 'Customer Service', 'Accounting', 'Legal', 'Procurement', 'Management', 'Facilities', 'Training'],
    'Administration (Employees)': [200, 100, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120, 100],
    'Sales (Employees)': [150, 120, 180, 200, 180, 200, 150, 100, 130, 100, 200, 180, 150, 200],
    'IT (Employees)': [180, 150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 130, 200, 250],
    'HR (Employees)': [130, 100, 150, 180, 130, 250, 200, 180, 200, 180, 100, 200, 170, 150],
    'R&D (Employees)': [250, 200, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 130, 180]
}

df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(111)

max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 100) * 100
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']
transparent = 0.7

ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, colors=colors, alpha=transparent)

ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(yticks)
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

ax.grid(axis='y', linestyle=':', alpha=0.5)

ax.set_title('Employee Distribution by Department and Position')

plt.tight_layout()

plt.savefig('output/final/area_chart/png/20231228-140159_48.png', bbox_inches='tight')

plt.close(fig)