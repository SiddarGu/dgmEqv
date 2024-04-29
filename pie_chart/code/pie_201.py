
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
labels = ['Facebook','YouTube','Twitter','Instagram','Reddit','Snapchat','Pinterest','Other']
sizes = [30,20,10,15,10,10,5,10]
explode = [0, 0, 0, 0, 0, 0, 0, 0] 
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=30, shadow=True)
plt.title("Social Media Platform Distribution in the USA, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/335.png', format='png')
plt.clf()