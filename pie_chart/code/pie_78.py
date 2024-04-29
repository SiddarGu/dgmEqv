
import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 8))

# Pie Chart 
labels = ['18-29','30-44','45-59','60-74']
sizes = [28,45,20,7]
explode = (0, 0.2, 0.1, 0.1)
colors = ['#50E3C2', '#F5A623', '#EC4561', '#35A7FF']

pie = plt.pie(sizes,explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', pctdistance=0.75, startangle=80, shadow=True)

# Legend setting
plt.legend(pie[0], labels, loc="best", bbox_to_anchor=(-0.125, 1.0))

# Text Setting
plt.title("Employee Age Distribution in the United States, 2023", fontsize=20)
plt.xticks(fontsize=12)
plt.tight_layout()

# Save and clear
plt.savefig('pie chart/png/344.png')
plt.clf()