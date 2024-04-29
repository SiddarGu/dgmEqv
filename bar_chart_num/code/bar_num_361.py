
import matplotlib.pyplot as plt 
import numpy as np 

#Data 
School= ['ABC School', 'XYZ School', 'KLM School', 'PQR School'] 
Students = [500, 450, 420, 480] 
Teachers = [25, 20, 22, 24] 

#Creating figure 
fig = plt.figure(figsize=(10,7)) 
ax = fig.add_subplot(111) 

#Plotting Bar Chart 
p1 = ax.bar(School, Students, color='#ff9999', label='Students') 
p2 = ax.bar(School, Teachers, bottom=Students, color='#9999ff', label='Teachers') 

#Setting labels and title 
ax.set_ylabel('Number of people') 
ax.set_title('Number of students and teachers in four schools in 2021') 
ax.set_xticks(School) 
ax.set_xticklabels(School, rotation=45, ha="right", wrap=True) 
ax.legend(loc='upper right') 

#adding values 
def autolabel(rects): 
    for rect in rects: 
        height = rect.get_height() 
        ax.annotate('{}'.format(height), 
                    xy=(rect.get_x() + rect.get_width()/2, height), 
                    xytext=(0,3), 
                    textcoords="offset points", 
                    ha='center', va='bottom') 

autolabel(p1) 
autolabel(p2) 

plt.tight_layout() 
plt.savefig('Bar Chart/png/360.png') 
plt.clf()