
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,8))
labels = ['Computer Science','Electrical Engineering','Materials Science','Mechanical Engineering','Civil Engineering','Chemical Engineering']
percentages = [25,20,15,20,10,10]
explode = np.full(len(labels), 0.05)
plt.pie(percentages, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90)
plt.title('Distribution of Science and Engineering Fields in Universities Worldwide, 2023')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/157.png')
plt.clf()