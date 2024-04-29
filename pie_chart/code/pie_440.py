
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# set the figure size  
plt.figure(figsize=(7,7))

# define labels 
labels = ['0-17','18-25','26-35','36-50','51-65','65+']

# set data 
sizes = [25,20,25,15,13,2]

# set colors 
colors = ['#ffd1dc','#f9a7b0','#f77f88','#f45d5d','#ee3a36','#e81714']

# draw pie chart 
explode = (0.1,0,0,0,0,0) 
plt.pie(sizes, labels=labels, colors=colors, autopct='%.2f%%', pctdistance=0.9, explode=explode, shadow=True)

# adjust the position of the legend 
plt.legend(labels, bbox_to_anchor=(1,0.7), loc="center right", fontsize=12)

# set title 
plt.title('Age Distribution of the US Population in 2023')

# adjust the position of the title 
plt.subplots_adjust(top=0.85)

# adjust the characters to show correctly 
plt.tight_layout()

# xticks to prevent interpolation 
plt.xticks(rotation=90)

# save the figure 
plt.savefig('pie chart/png/154.png',bbox_inches = 'tight')

# clear the current state
plt.clf()