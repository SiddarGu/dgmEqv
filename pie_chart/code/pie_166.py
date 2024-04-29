

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
labels = ['Automotive','Food and Beverage','Consumer Products','Chemical Products','Machinery','Electronics','Textiles']
sizes = [25,15,20,10,10,15,5]
explode = (0.1,0,0,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90,textprops={'fontsize': 10,'wrap':True,'rotation':45})
plt.title('Distribution of Manufacturing Types in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/248.png')
plt.xticks([])
plt.clf()