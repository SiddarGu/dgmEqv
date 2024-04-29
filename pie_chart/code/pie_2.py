
import matplotlib.pyplot as plt 
import numpy as np

labels = ['Individuals','Foundations','Corporations','Government Grants','Other']
sizes = [60,20,10,5,5]

fig, ax = plt.subplots(figsize=(12,8))
ax.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.title("Distribution of Donors to Charity and Nonprofit Organizations in 2021")
plt.tight_layout()
plt.savefig('pie chart/png/27.png')
plt.clf()