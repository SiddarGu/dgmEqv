
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
type=['Traditional Retail','Online Shopping','Mobile Shopping','Social Commerce']
percentage=[45,35,15,5]

plt.pie(percentage,labels=type,autopct='%1.1f%%',explode=(0.1,0,0,0),pctdistance=0.8,textprops={'fontsize': 14, 'ha': 'center'}, startangle=45,radius=1)
plt.title('Distribution of Retail Methods in the USA, 2023',fontsize=14, wrap=True)
plt.axis('equal')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/428.png')
plt.clf()