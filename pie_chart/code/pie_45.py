

import matplotlib.pyplot as plt 
import pandas as pd 

data = {'Types of Scientists':['Physicists','Biologists','Astronomers','Chemists','Computer Scientists','Environmental Scientists','Geologists','Other'], 
        'Percentage':[20,20,15,15,15,10,5,10]} 

df = pd.DataFrame(data,index = data['Types of Scientists']) 

plt.figure(figsize=(10,10)) 
pie = plt.pie(df['Percentage'],labels = df.index,autopct='%1.1f%%') 
plt.title('Distribution of Scientists in the World, 2023') 
plt.legend(pie[0], df.index, bbox_to_anchor=(1.3,0.5),loc="center right") 
plt.xticks(rotation=90, horizontalalignment='center') 
plt.tight_layout() 
plt.savefig('pie chart/png/413.png') 
plt.clf()