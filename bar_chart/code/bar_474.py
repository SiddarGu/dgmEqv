
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(['Air','Rail','Sea','Road'],[2000,4000,6000,8000],bottom=[0,2000,4000,6000],width=0.3,align='center')
ax.bar(['Air','Rail','Sea','Road'],[6,12,24,48],bottom=[2000,4000,6000,8000],width=0.3,align='center',color='r')
ax.set_title('Travel distance and time of four transportation modes in 2021')
ax.set_xlabel('Mode')
ax.set_ylabel('Distance(km)/Time(h)')
ax.legend(['Distance','Time'],loc='upper left')
ax.set_xticks(['Air','Rail','Sea','Road'])
plt.tight_layout()
plt.savefig('bar chart/png/138.png')
plt.clf()