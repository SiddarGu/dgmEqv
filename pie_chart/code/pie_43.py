
import matplotlib.pyplot as plt 
import numpy as np 

# Data to plot
labels = ['Individuals','Foundations','Corporations','Government','Events and Fundraisers']
sizes = [60, 15, 10, 5, 10]

# Plot
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, explode=(0.1, 0, 0, 0, 0))
ax.axis('equal')
ax.set_title('Breakdown of Donations to Nonprofit Organizations in 2021')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/257.png')
plt.clf()