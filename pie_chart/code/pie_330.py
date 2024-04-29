
import matplotlib.pyplot as plt
import numpy as np

labels=['Primary','Secondary','Tertiary','Post-secondary','Vocational']
sizes=[25,35,28,6,6]

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90,
        textprops={'fontsize':10,'color':'white','rotation':90,'wrap':True})
ax.axis('equal')
plt.title('Distribution of Education Levels in the USA, 2023')
plt.savefig('pie chart/png/495.png')
plt.tight_layout()
plt.xticks([])
plt.clf()