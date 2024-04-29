
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(['East','West','North','South'],[250,200,350,300], width=0.3,label='Crops', bottom=0)
ax.bar(['East','West','North','South'],[100,120,130,150], width=0.3,label='Livestock', bottom=[250,200,350,300])
plt.xticks(['East','West','North','South'])
plt.title('Crop and livestock production in four regions in 2021')
plt.legend(loc='upper left')
for i, v in enumerate(['250/100','200/120','350/130','300/150']):
    ax.text(i-0.15, int(v.split('/')[0])+int(v.split('/')[1])/2, v, fontsize=12, fontweight='bold', rotation=90)
fig.tight_layout()
plt.savefig('bar_426.png', dpi=400)
plt.clf()