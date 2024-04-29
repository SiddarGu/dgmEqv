
import matplotlib.pyplot as plt 

#create figure
plt.figure(figsize=(8,8))

# set label
labels = ['Automation','Robotics','Machinery','3D Printing','Human Labor']
production = [30,20,25,10,15]

# plot pie chart
plt.pie(production, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# title
plt.title("Production Distribution in the Manufacturing Industry, 2023")

#resize
plt.tight_layout()

#save
plt.savefig('pie chart/png/275.png',bbox_inches='tight')

#clear
plt.clf()