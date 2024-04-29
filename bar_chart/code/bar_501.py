
import matplotlib.pyplot as plt
import numpy as np

#Set data
Month = ['January','February','March','April']
Factory_A = [1000,900,1100,800]
Factory_B = [1200,1300,1400,1500]
Factory_C = [800,1100,1200,1400]

#Create figure and axis
fig, ax = plt.subplots(figsize=(12,6))

#Plot the data
ax.bar(Month, Factory_A, bottom=np.zeros(len(Month)), label='Factory A', width=0.25, align='edge')
ax.bar(Month, Factory_B, bottom=Factory_A, label='Factory B', width=0.25, align='edge')
ax.bar(Month, Factory_C, bottom=np.array(Factory_A)+np.array(Factory_B), label='Factory C', width=0.25, align='edge')

#Set x,y axis labels
plt.xlabel('Month')
plt.ylabel('Units')

#Set x ticks
plt.xticks(Month, rotation=45, ha='right',wrap=True)

#Set title
plt.title('Manufacturing output of three factories from January to April 2021')

#Set legend
plt.legend(loc='upper left')

#Adjust the figure
plt.tight_layout()

#Save figure
plt.savefig('bar chart/png/334.png')

#Clear current state
plt.clf()