
import matplotlib.pyplot as plt 
import numpy as np 

# create figure 
fig = plt.figure() 
ax = fig.add_subplot(1,1,1) 

# set figure size 
fig.set_figwidth(10) 
fig.set_figheight(6) 

# define data 
x_labels = ['0-17','18-35','36-50','51-65','65+'] 
hospital_visits = [50,120,90,80,60] 
gp_visits = [90,150,100,110,130] 

# plot bar chart 
bar_width = 0.45
ax.bar(x_labels, hospital_visits, bar_width, label='Hospital Visits', color='blue') 
ax.bar(x_labels, gp_visits, bar_width, label='GP Visits', color='red', bottom=hospital_visits) 

# set label name 
ax.set_xlabel('Age Group') 
ax.set_ylabel('Visits (million)') 
ax.set_title('Healthcare visits by age group in 2021') 
ax.set_xticks(np.arange(len(x_labels))) 
ax.set_xticklabels(x_labels, rotation=90) 

# annotate 
for i, v in enumerate(hospital_visits): 
    ax.text(i-bar_width/2, v + 5, str(v), color='blue', fontweight='bold') 
for i, v in enumerate(gp_visits): 
    ax.text(i+bar_width/2, hospital_visits[i] + v + 5, str(v), color='red', fontweight='bold') 

# set legend 
ax.legend(loc='upper left') 

# adjust the display 
fig.tight_layout() 

# save figure 
fig.savefig('Bar Chart/png/382.png') 

# clear the figure state 
plt.clf()