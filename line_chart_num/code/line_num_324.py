
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
temp = [20,22,24,28,30,33,35,33,30,26,22,20]
rainfall = [100,120,150,200,180,170,150,160,140,110,90,100]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)  
ax.set_title("Average Temperature and Rainfall in Hawaii in 2023")
ax.set_xlabel('Month')
ax.set_ylabel('Temperature (degrees)/Rainfall (mm)')
ax.plot(month,temp,label='Temperature (degrees)',color='red',marker='o')
ax.plot(month,rainfall,label='Rainfall (mm)',color='blue',marker='o')
ax.legend(loc='upper right',bbox_to_anchor=(1.2,1))

# Add grids
ax.grid(axis='y', alpha=0.75)
ax.set_xticks(month)

# Add annotation
for i,j in zip(month,temp):
    ax.annotate(str(j),xy=(i,j),xytext=(0,10),textcoords='offset points')
for i,j in zip(month,rainfall):
    ax.annotate(str(j),xy=(i,j),xytext=(0,10),textcoords='offset points')

plt.tight_layout()
plt.savefig("line chart/png/279.png")
plt.clf()