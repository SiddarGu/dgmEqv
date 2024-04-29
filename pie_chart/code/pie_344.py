
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,8))
ax = plt.subplot()
taxes = ['Income Tax','Property Tax','Sales Tax','Excise Tax','Other']
percentage = [45,25,15,10,5]
colors=['pink','purple','red','orange','green']
plt.pie(percentage,labels=taxes,colors=colors,autopct='%.2f%%',textprops={'fontsize': 10},startangle=90)
plt.title('Distribution of Tax Revenue in the USA, 2023',fontsize=15)
plt.tight_layout()
plt.savefig('pie chart/png/424.png')
plt.clf()