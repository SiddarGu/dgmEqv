
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5)) 
ax = fig.add_subplot(111) 

x = ["2020","2021","2022","2023"] 
y1 = [10,13,15,18]
y2 = [10,12,15,20]
y3 = [100,110,120,130]

ax.bar(x,y1,label="Space Exploration(hundred km)", bottom=0, color="green") 
ax.bar(x,y2,label="Engineering Advances(percentage)", bottom=y1, color="red") 
ax.bar(x,y3,label="Scientific Discoveries(count)", bottom= [i+j for i,j in zip(y1,y2)], color="blue") 

plt.title("Science and engineering progress from 2020 to 2023") 
ax.legend(loc='upper left', bbox_to_anchor=(1,1)) 
ax.set_xticks(x)
ax.set_xticklabels(x,rotation=45,wrap=True) 
plt.tight_layout() 
plt.savefig("bar_309.png") 
plt.clf()