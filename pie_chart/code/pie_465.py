
import matplotlib.pyplot as plt
import pandas as pd

data = [['Football',30], ['Basketball',20], ['Baseball',15], ['Hockey',10], ['Golf',10], ['Motorsports',7], ['Tennis',5], ['Soccer',3]]  
df = pd.DataFrame(data, columns = ['Sports', 'Percentage']) 

plt.figure(figsize=(8, 8), dpi=80)

labels = df['Sports'].tolist()
sizes = df['Percentage'].tolist()
explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)

plt.pie(sizes, labels=labels, explode=explode, autopct='%1.2f%%', shadow=True, startangle=90, textprops={'wrap':True, 'rotation':0})
plt.title('Popular Sports in the USA in 2023', fontweight="bold")
plt.tight_layout()
plt.savefig('pie chart/png/140.png')
plt.show()
plt.clf()