
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
plt.bar(['East Coast','West Coast','Midwest','South'], [500000,600000,450000,400000], color='green',width=0.4,label='Average Home Value')
plt.bar(['East Coast','West Coast','Midwest','South'], [3000,3500,2500,2200], bottom=[500000,600000,450000,400000],color='blue',width=0.4,label='Average Rent')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.title('Average home values and rental rates in four regions in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/293.png')
plt.clf()