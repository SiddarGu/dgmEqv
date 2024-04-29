
import matplotlib.pyplot as plt
import numpy as np

#Data
modes=['Roadways','Railways','Airways','Waterways','Other']
percentage=[45,25,20,5,5]

#Draw Pie
fig,ax=plt.subplots(figsize=(8,8))
ax.pie(percentage, labels=modes, autopct='%1.1f%%',textprops={'wrap': True,'fontsize': 14}, startangle=90, pctdistance=0.85,labeldistance=1.05)
ax.axis('equal')
ax.set_title('Distribution of Transportation Modes in the USA, 2023', fontsize=16)
plt.tight_layout()
plt.savefig('pie chart/png/126.png')
plt.cla()