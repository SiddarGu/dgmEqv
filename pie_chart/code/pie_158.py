
import matplotlib.pyplot as plt
import numpy as np

causes = ['Humanitarian & Disaster Relief', 'Education & Literacy', 'Poverty', 'Health', 'Animals', 'Environment & Sustainability', 'Arts, Culture & Humanities', 'Religion', 'Other']
percentage = [25,20,15,12,10,10,8,5,5]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()
ax.pie(percentage, labels=causes, autopct='%1.1f%%', rotatelabels=True, textprops={'fontsize':8}, wedgeprops={'linewidth':3, 'edgecolor':'black'})
ax.axis('equal')
ax.set_title('Distribution of Charitable Causes in the USA, 2023')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/250.png')
plt.clf()