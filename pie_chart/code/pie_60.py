
import matplotlib.pyplot as plt
import numpy as np

taxation = ['Income Tax','Sales Tax','Property Tax','Excise Tax','Other']
percent = [35,20,15,15,15]

plt.figure(figsize=(9,7))
ax = plt.subplot(111)
wedges, texts, autotexts = ax.pie(percent, labels=taxation, autopct='%1.1f%%',startangle=90)
ax.axis('equal')
ax.set_title('Taxation Distribution in the USA, 2023')
plt.tight_layout()
ax.legend(wedges, taxation,title="Taxation", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

for tx in texts:
    tx.set_rotation(90)
for at in autotexts:
    at.set_rotation(90)

plt.savefig('pie chart/png/87.png')
plt.clf()