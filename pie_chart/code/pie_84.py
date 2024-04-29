
import matplotlib.pyplot as plt
import numpy as np

labels = ['Hospitals','Clinics','Ambulance Services','Home Healthcare','Nursing Homes']
data = [35,25,20,15,5]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, labels=labels, autopct='%.1f%%', shadow=True, startangle=90)
ax.legend(loc=2, bbox_to_anchor=(1.1, 0.8))
ax.set_title("Distribution of Healthcare Providers in the USA, 2023")
ax.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)

plt.savefig('pie chart/png/182.png')
plt.clf()