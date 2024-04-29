
import matplotlib.pyplot as plt
import numpy as np

labels = ['Facebook', 'Instagram', 'Twitter', 'YouTube', 'LinkedIn', 'Snapchat', 'Reddit', 'Other']
percentage = [35, 18, 14, 14, 9, 7, 3, 4]

fig = plt.figure(figsize = (10, 10), dpi=80)
ax = fig.add_subplot(111)
ax.set_title("Social Media Platform Usage in the USA, 2023", fontsize=20)
ax.pie(percentage, labels=labels, autopct='%.2f%%', textprops={'fontsize': 15}, 
       shadow=True, radius=1.2, startangle=90, rotatelabels=True, pctdistance=0.8, labeldistance=1.15)
plt.savefig('pie chart/png/458.png', bbox_inches='tight')
plt.tight_layout()
plt.xticks([])
plt.show()
plt.clf()