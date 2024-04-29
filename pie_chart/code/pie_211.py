

import matplotlib.pyplot as plt
import numpy as np

#create figure
plt.figure(figsize=(8,6))

#plot chart
labels = ['Mobile Apps', 'Social Media', 'Websites', 'E-commerce', 'Cloud Computing'] 
sizes = [30,25,20,15,10]
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Technology Usage in the US in 2023', fontsize=15, wrap=True)

#set legend
plt.legend(labels, bbox_to_anchor=(1.1, 0.9), loc="upper left")

#tight layout
plt.tight_layout()

#save figure
plt.savefig('pie chart/png/108.png')

#clear figure
plt.clf()