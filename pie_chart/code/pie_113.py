
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,8))
plt.title('Distribution of Legal Professionals in the USA, 2023')
labels = ['Lawyers','Judges','Paralegals','Legal Assistants','Other']
sizes = [35,20,15,10,20]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize':14,'color':'black', 'wrap':True, 'rotation':0})
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/103.png')
plt.clf()