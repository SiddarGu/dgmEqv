
import matplotlib.pyplot as plt
import numpy as np

labels = ['Operating Systems','Programming Languages','Database Management','Networking','Artificial Intelligence','Graphics','Animation', 'Simulation'] 
percentage = [25, 15, 15, 15, 15, 10, 5, 5]

plt.figure(figsize=(12, 8))
plt.title('Software Distribution in the Science and Engineering Industry, 2023')
plt.pie(percentage, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12, 'rotation': 90, 'wrap':True})
plt.axis('equal')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/191.png')
plt.clf()