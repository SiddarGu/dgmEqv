
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,7))
labels = ['High School','Associate\'s Degree','Bachelor\'s Degree','Master\'s Degree','Doctorate Degree']
sizes = [25,15,30,20,10]
colors = ['red','yellow','green','blue','purple']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=50)
plt.title('Proportion of Students at Different Levels of Education in the US, 2023', fontsize=20)
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/330.png')
plt.clf()