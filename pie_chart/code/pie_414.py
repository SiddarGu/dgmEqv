
import matplotlib.pyplot as plt
import numpy as np

# set figure
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(111)

# data
labels = ['First-Generation Students','Graduates','Undergraduates','Non-Traditional Students','International Students']
sizes = [20,30,30,10,10]
explode = [0,0,0,0,0]

# plot
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)

# legend
plt.legend(labels,loc="lower right")

# title
plt.title('Student Population Distribution in US Colleges and Universities, 2023')

# adjust
plt.tight_layout()
plt.xticks(rotation=45)

# save
plt.savefig('pie chart/png/97.png',dpi=300)

# clear
plt.clf()