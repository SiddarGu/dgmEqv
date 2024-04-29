
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6,6))
labels=['Civil Law','Criminal Law','International Law','Constitutional Law','Administrative Law']
sizes=[37,27,16,10,10]
explode=(0.1,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=45,pctdistance=0.6,labeldistance=1.1)
plt.title('Types of Law Practiced in the US, 2023')
plt.axis('equal')
plt.tight_layout()
plt.xticks([]) 
plt.savefig('pie chart/png/183.png')
plt.clf()