
import matplotlib.pyplot as plt
import numpy as np

#Create data
Country=['USA','UK','Germany','France']
Students=[35,25,20,15]
Schools=[10000,7000,8000,6000]

#Create figure
fig, ax=plt.subplots(figsize=(10,6))

#Create bar chart
ax.bar(Country, Students, label='Students(million)', bottom=Schools)
ax.bar(Country, Schools, label='Schools')

#Label the value of each data point
for y, x in enumerate(Country):
    ax.annotate(str(Students[y]), xy=(y, Students[y]+Schools[y]), rotation=90, ha='center', va='bottom')
    ax.annotate(str(Schools[y]), xy=(y, Schools[y]), rotation=90, ha='center', va='bottom')

#Add title
plt.title('Number of students and schools in four countries in 2021')

#Add legend
plt.legend(loc='upper left', frameon=False)

#Prevent interpolation
plt.xticks(Country)

#Adjust image, compress content
plt.tight_layout()

#Save figure
plt.savefig('Bar Chart/png/183.png')

#Clear current image state
plt.clf()