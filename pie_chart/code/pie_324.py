
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,8))
labels = ['Individual Donations', 'Corporate Donations', 'Government Grants', 'Foundations', 'Events']
sizes = [50, 25, 15, 7, 3]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal') 
plt.title('Distribution of Donations for Nonprofit Organizations in 2023', fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/276.png')
plt.clf()