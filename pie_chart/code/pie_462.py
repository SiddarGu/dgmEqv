
import matplotlib.pyplot as plt
import numpy as np

labels = ['High School','Associate Degree','Bachelor Degree','Master Degree','Doctoral Degree']
data = [20,25,30,20,5]

fig = plt.figure(figsize=(6,6))
plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, explode=(0,0,0.1,0,0))
plt.title('Educational Attainment in the USA, 2023')
plt.legend(labels, 
           bbox_to_anchor=(1,0.7), 
           loc="lower right", 
           fontsize=11, 
           bbox_transform=fig.transFigure)
plt.tight_layout()
plt.savefig('pie chart/png/365.png')
plt.clf()