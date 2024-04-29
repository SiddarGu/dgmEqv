
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(12,8)) 
ax = fig.add_subplot() 
ax.bar(['USA','UK','Germany','France'],[5.8,4.7,3.9,3.6],bottom=0,label='Retail Sales')
ax.bar(['USA','UK','Germany','France'],[3.5,2.8,2.2,2.0],bottom=[5.8,4.7,3.9,3.6],label='Online Sales')
plt.title("Retail and Online Sales in four countries in 2021") 
plt.xticks(rotation=45, wrap=True)
plt.legend(loc='upper right')
plt.tight_layout() 
plt.savefig('bar chart/png/236.png') 
plt.clf()