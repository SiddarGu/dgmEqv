
import matplotlib.pyplot as plt 
fig,ax = plt.subplots(figsize=(8,6))
x = ["North America","South America","Europe","Asia"] 
laws = [20,25,22,27] 
regulations = [30,35,32,37] 
procedures = [40,45,42,47] 
width = 0.2 
ax.bar(x, laws, width, label = 'Laws') 
ax.bar(x, regulations, width, bottom = laws, label = 'Regulations') 
ax.bar(x, procedures, width, bottom = [x+y for x,y in zip(laws, regulations)], label = 'Procedures') 
ax.set_title("Number of Laws, Regulations and Procedures in four regions in 2021") 
ax.set_xticklabels(x, rotation = 15, wrap=True) 
ax.legend() 
plt.tight_layout() 
plt.savefig('bar chart/png/294.png')
plt.clf()