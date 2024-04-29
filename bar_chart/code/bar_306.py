
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
ax = plt.subplot()
ax.bar(['USA','UK','Germany','France'],[450,320,380,420],label='Charitable Donations(million)',bottom=0,color='#FFC0CB')
ax.bar(['USA','UK','Germany','France'],[2500,2300,2100,2000],label='Nonprofit Organizations',bottom=0,color='#FFA07A')
ax.set_title('Charitable donations and nonprofit organizations in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Amount')
plt.xticks(rotation=45, ha='right')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/115.png')
plt.clf()