
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 10))

# Plot data
labels = ['Hospitals', 'Clinics', 'Outpatient Centers', 'Nursing Homes', 'Home Health Care']
sizes = [30,25,20,15,10]
explode=[0.1,0,0,0,0]

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 14, "wrap": True})
plt.title('Healthcare Services Distribution in the USA, 2023', fontsize=20)
plt.axis('equal')

plt.savefig('pie chart/png/122.png')
plt.tight_layout()
plt.xticks([])
plt.clf()