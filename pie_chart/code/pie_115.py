
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
sports = ['Basketball','Football','Baseball','Hockey','Soccer']
percentage = [25,30,20,15,10]

plt.title('Popular Sports in the USA, 2023')
plt.pie(percentage,labels=sports,autopct='%1.1f%%',textprops={'fontsize': 14},shadow=True,startangle=90)
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/494.png')
plt.clf()