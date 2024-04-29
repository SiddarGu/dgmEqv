
import matplotlib.pyplot as plt
import numpy as np

#Data
age = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70']
weight = [20, 50, 65, 60, 65, 55, 50]
height = [110, 165, 170, 160, 170, 155, 150]
cholesterol = [100, 200, 150, 180, 220, 250, 280]

#Create figure
fig=plt.figure(figsize=(10,6))

#Plot
ax1=fig.add_subplot(111)
ax1.plot(age, weight, color='b',marker='o', linestyle='-', linewidth=2, label='Weight')
ax1.plot(age, height, color='r',marker='o', linestyle='-', linewidth=2, label='Height')
ax1.plot(age, cholesterol, color='g',marker='o', linestyle='-', linewidth=2, label='Cholesterol Level')
ax1.set_xticks(age)
ax1.set_xlabel('Age')
ax1.set_title('Average weight, height, and cholesterol level of different age groups in the US')
ax1.legend(bbox_to_anchor=(1.05, 1.2))

#Resize figure
plt.tight_layout()

#Save figure
plt.savefig('line chart/png/436.png', bbox_inches = 'tight')

#Clear figure
plt.clf()