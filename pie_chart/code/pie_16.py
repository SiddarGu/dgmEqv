
import matplotlib.pyplot as plt
import numpy as np

ageGroup = ['18-25','26-35','36-45','46-55','56-65']
percentage = [20,30,25,15,10]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

ax.pie(percentage, labels=ageGroup, autopct='%.2f%%', startangle=90)
ax.set_title('Distribution of Employees by Age in the United States, 2023')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/164.png')
plt.gcf().clear()