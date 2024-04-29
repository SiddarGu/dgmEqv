
import matplotlib.pyplot as plt 
import numpy as np 

data = [['USA', 600, 350], 
        ['UK', 550, 400], 
        ['Germany', 700, 450], 
        ['France', 500, 420]] 

fig = plt.figure(figsize=(9, 5)) 
ax = fig.add_subplot() 

label = [i[0] for i in data] 
x = np.arange(len(label)) 
ax.bar(x - 0.2, [i[1] for i in data], width=0.4,
       label='Criminal Cases', color='r', align='center') 
ax.bar(x + 0.2, [i[2] for i in data], width=0.4,
       label='Civil Cases', color='b', align='center') 

ax.set_xticks(x) 
ax.set_xticklabels(label, rotation=0, wrap=True) 
ax.legend(frameon=False, bbox_to_anchor=(1.4, 0.9)) 
ax.set_title('Number of criminal and civil cases in four countries in 2021') 

plt.tight_layout() 
plt.savefig('bar chart/png/475.png') 
plt.clf()