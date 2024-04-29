
import matplotlib.pyplot as plt

x=['Sales','Marketing','Operations','Human Resources']
y=[2,4,3,1]

fig,ax=plt.subplots(figsize=(10,6))
ax.bar(x,y,width=0.5,color='g',align='center')
ax.set_title('Employee absenteeism rate in four departments in 2021')
ax.set_xlabel('Department')
ax.set_ylabel('Absenteeism(%)')
plt.xticks(x,rotation=45,ha='right')
plt.grid(color='gray', linestyle='-.', linewidth=0.5)
plt.tight_layout()
plt.savefig('bar chart/png/537.png',dpi=300)
plt.clf()