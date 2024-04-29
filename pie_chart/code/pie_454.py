
import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
labels = ['Facebook','YouTube','Twitter','Instagram','Snapchat','LinkedIn','Reddit','Other']
sizes = [36,20,7,7,4,4,4,23]
explode = (0.1,0,0,0,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
plt.title('Distribution of Social Media Platforms Usage in the USA, 2023')
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=-45)
plt.savefig('pie chart/png/527.png')
plt.clf()