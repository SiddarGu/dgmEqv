
import matplotlib.pyplot as plt

#Create figure 
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

#Define data
Country = ['USA','UK','Germany','France']
Facebook_Users = [190,30,80,50]
Twitter_Users = [80,20,10,17]
Instagram_Users = [150,25,30,35]

#Plot chart
ax.bar(Country,Facebook_Users, bottom=Twitter_Users,label="Facebook Users",align='center',width=0.4)
ax.bar(Country,Twitter_Users, bottom=Instagram_Users,label="Twitter Users",align='center',width=0.4)
ax.bar(Country,Instagram_Users,label="Instagram Users",align='center',width=0.4)

#Set xticks to prevent interpolation
plt.xticks(Country)

#Add title
plt.title("Number of Social Media users in four countries in 2021")

#Add legend 
ax.legend(loc="lower left", bbox_to_anchor=(0,1))

#Automatically resize the image by tight_layout()
plt.tight_layout()

#Save the figure
plt.savefig('bar chart/png/27.png')

#Clear the current image state
plt.clf()