
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(9, 5))
ax = fig.add_subplot()

# Data
year = np.array([2010, 2011, 2012, 2013])
physics_patents = np.array([10, 15, 20, 25])
chemistry_patents = np.array([20, 25, 30, 35])
engineering_patents = np.array([30, 35, 40, 45])

# Plotting
ax.bar(year, physics_patents, label='Physics Patents', bottom=chemistry_patents+engineering_patents)
ax.bar(year, chemistry_patents, label='Chemistry Patents', bottom=engineering_patents)
ax.bar(year, engineering_patents, label='Engineering Patents')

# Axis
ax.set_xticks(year)
ax.set_ylabel('Percentage of Patents')
ax.set_title('Percentage of Patents in Physics, Chemistry and Engineering from 2010 to 2013')

# Legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=3)

# Save figure
plt.tight_layout()
plt.savefig('bar chart/png/111.png')
plt.clf()