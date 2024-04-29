
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
plt.title('Media Platform Distribution in the Sports and Entertainment Industry, 2023')
labels = ['Television','Social Media','Streaming Services','Radio','Print','Digital Advertising']
sizes = [35,25,18,10,7,5]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,textprops={'fontsize': 14},rotatelabels=True)
plt.legend(labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=14, 
           bbox_transform=plt.gcf().transFigure)
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/16.png')
plt.clf()