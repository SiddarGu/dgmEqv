
import matplotlib.pyplot as plt 
plt.figure(figsize=(10,5)) 
labels = ['Full-Time Employees','Part-Time Employees','Contractors','Interns'] 
sizes = [60,25,10,5] 
explode = [0.1,0,0,0]
colors = ['lightskyblue','lightcoral','gold','yellowgreen'] 
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90) 
plt.title('Employee Distribution in a Company, 2023',fontsize=16) 
plt.axis('equal') 
plt.tight_layout()
plt.xticks(rotation=45) 
plt.savefig('pie chart/png/320.png', bbox_inches='tight') 
plt.clf()