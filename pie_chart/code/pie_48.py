
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(6, 6))

# Plot data
labels = ['Theme Parks', 'Cultural Sites', 'Natural Landmarks', 'Zoos and Aquariums', 'Historical Places']
values = [25, 20, 30, 15, 10]
plt.pie(values, labels=labels, autopct='%1.1f%%', 
        pctdistance=0.7, labeldistance=1.2,
        rotatelabels=True,
        textprops={'fontsize': 10, 'color':'black'},
        wedgeprops={'linewidth': 2, 'edgecolor':'black'},
        startangle=90)

# Title
plt.title('Popular Tourist Destinations in the USA in 2023', fontsize=20)

# Adjust the figure
plt.tight_layout()

# Save and clear
plt.savefig('pie chart/png/476.png')
plt.clf()