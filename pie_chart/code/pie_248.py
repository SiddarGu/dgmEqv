
import matplotlib.pyplot as plt
import numpy as np

labels = ['Individual Donors', 'Foundations', 'Corporate Partners', 'Government Grants', 
          'Social Impact Investing', 'Other']
sizes = [35,25,15,10,10,5]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','orange','red']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True, 
        explode = (0, 0.1, 0, 0, 0, 0))
plt.title('Distribution of Donations to Nonprofit Organizations in 2023', fontsize=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/12.png')
plt.clf()