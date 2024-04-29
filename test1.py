import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
ax.barh(['North','South','East','West'],[80,90,85,100],height=0.4,label="Hospitals",alpha=0.8)
ax.barh(['North','South','East','West'],[500,550,600,550],height=0.4,label="Doctors",bottom=[80,90,85,100],alpha=0.8)
ax.barh(['North','South','East','West'],[2500,2700,3000,2800],height=0.4,label="Nurses",bottom=[580,640,685,650],alpha=0.8)
ax.set_ylabel('Region')
ax.set_xlabel('Quantity')
ax.set_title('Healthcare facilities and personnel in four regions in 2021')
ax.legend(loc='upper left')
ax.set_yticks(['North','South','East','West'])
plt.gca().invert_xaxis()

plt.savefig('bar chart/png/341.png')
plt.clf()


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
ax.bar(['North','South','East','West'],[80,90,85,100],width=0.4,label=\"Hospitals\",alpha=0.8)
ax.bar(['North','South','East','West'],[500,550,600,550],width=0.4,label=\"Doctors\",bottom=[80,90,85,100],alpha=0.8)
ax.bar(['North','South','East','West'],[2500,2700,3000,2800],width=0.4,label=\"Nurses\",bottom=[580,640,685,650],alpha=0.8)
ax.set_xlabel('Region')
ax.set_ylabel('Quantity')
ax.set_title('Healthcare facilities and personnel in four regions in 2021')
ax.legend(loc='upper left')
ax.set_xticks(['North','South','East','West'])
plt.savefig('bar chart/png/341.png')