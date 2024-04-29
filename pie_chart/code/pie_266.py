
import matplotlib.pyplot as plt
import numpy as np 

labels = ['Education','Healthcare','Defense','Infrastructure','Social Services']
values = [30,25,20,15,10]

fig = plt.figure(figsize = (8,7))
ax = fig.add_subplot()
ax.pie(values, labels=labels, autopct='%.2f%%', shadow=True, startangle=90, rotatelabels=False, textprops={'fontsize': 10})
plt.title("Distribution of Public Funds for Government Services in the USA, 2023")
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/512.png')
plt.clf()