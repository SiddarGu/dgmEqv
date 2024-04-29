
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

labels = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Antarctica']
sizes = [40, 30, 15, 7, 5, 3]

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
ax.set_title('Global Tourism Distribution in 2023', fontsize=14)
ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90, wedgeprops={'linewidth': 10}, 
       textprops={'fontsize': 14, 'wrap': True, 'rotation': -90},
       colors=['#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'])
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/403.png', bbox_inches='tight')
# Clear the current figure 
plt.clf()