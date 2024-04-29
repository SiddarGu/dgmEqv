
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,7))
labels = ['Individuals','Foundations','Corporations','Religious Institutions','Government Grants']
sizes = [35,18,20,20,7]
explode = (0.1, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Source of Donations for Nonprofit Organizations in the USA, 2023')
plt.legend(labels, loc="best", bbox_to_anchor=(1, 0, 0.5, 1))
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=-45)
plt.savefig('pie chart/png/481.png')
plt.clf()