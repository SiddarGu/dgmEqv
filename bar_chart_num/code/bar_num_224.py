

import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
x_data=['North','South','East','West']
y1_data=[100,110,115,120]
y2_data=[200,220,230,240]

ax=plt.subplot()
ax.bar(x_data,y1_data,label='Doctors(thousand)',bottom=y2_data)
ax.bar(x_data,y2_data,label='Nurses(thousand)')

for a,b in zip(x_data,y1_data):
    ax.text(a,b-20,'%d' %b,ha='center',va='bottom',fontsize=10)
for a,b in zip(x_data,y2_data):
    ax.text(a,b+20,'%d' %b,ha='center',va='bottom',fontsize=10)

plt.title('Number of doctors and nurses in four regions in 2021')
ax.legend()
plt.xticks(x_data)
plt.tight_layout()
plt.savefig('Bar Chart/png/1.png')
plt.clf()