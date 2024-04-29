
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot()
labels = np.array(['18-29','30-44','45-64','65+'])
turnout = np.array([25,30,40,5])
ax.pie(turnout, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal') 
ax.set_title("Voter Turnout by Age Group in the USA, 2023")
ax.legend(labels, loc="best", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/63.png')
plt.clf()